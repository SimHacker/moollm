# Invisible Whitespace Steganography and Its Applications and Extensions

**RFC IWS-2026-04**  
**Date:** 2026-04-01  
**Status:** Informational  
**Author:** MOOLLM Steganography Working Group

---

## Abstract

This document specifies a family of techniques for encoding information in text using characters and sequences that are invisible, inaudible, or semantically neutral to conventional parsers and human perception. Most of these techniques are already known; the value of this RFC is documenting their practical usefulness when applied to mitigating major weaknesses of JSON (no comments, no trailing commas, no out-of-band metadata without breaking parsers). The primary encoding is binary representation via horizontal whitespace (tab and space), with extensions for watermarking, metadata embedding, and cross-channel signalling. Compliance with this RFC does not require implementations to support all extensions; the core encoding is normative.

---

## 1. Introduction

Most of the steganographical techniques described here are already known. The purpose of this RFC is not novelty but **documenting their practical usefulness when applied to mitigating one of the major weaknesses of JSON**: the lack of comments, the lack of trailing commas, and the inability to attach out-of-band metadata without breaking standard parsers. By encoding such information in whitespace or other invisible carriers, documents remain valid JSON while gaining capabilities that the format otherwise denies.

Steganography in plain text has historically relied on zero-width characters, homoglyphs, or control characters that may be stripped or normalized by pipelines. This RFC specifies a robust alternative: **encoding arbitrary octets as sequences of TAB (U+0009) and SPACE (U+0020)**. These characters are preserved by virtually all text editors, version-control systems, and transport protocols. Mixing tabs and spaces in the same document is widely considered poor style in both "tabs for indentation" and "spaces for indentation" communities; the Working Group adopts this mixture deliberately as the canonical encoding, and notes that antagonizing both camps simultaneously is a feature, not a bug.

---

## 2. Terminology

- **IWS**: Invisible Whitespace Steganography (this RFC).
- **TSB**: Tab-Space Binary encoding (Section 3).
- **Payload**: The octet sequence to be embedded.
- **Carrier**: The visible text or structure that contains the TSB (or other IWS) encoding.
- **Channel**: The medium (e.g. source code, JSON, terminal output, LLM response) carrying the steganographic data.

---

## 3. Tab-Space Binary Encoding (TSB)

### 3.1 Encoding Rules

- **Space (U+0020)** denotes bit value **0**.
- **Tab (U+0009)** denotes bit value **1**.
- Octets are encoded in big-endian bit order (MSB first). The resulting sequence is inserted at defined **embedding points** (e.g. end of line, between tokens, inside string literals after a designated delimiter).
- No inter-octet separator is required; decoding is fixed at 8 bits per octet. Optional padding (spaces) may be used to align to word boundaries for implementation convenience.
- **Trailing remainder:** A trailing run of tabs and spaces whose length is not a multiple of 8 is not interpreted as TSB. Decoders leave it unchanged (e.g. when reconstructing the carrier) and do not attempt to decode it as a partial octet. This avoids misinterpreting ordinary indentation or stray trailing whitespace as payload.

**Example.** The UTF-8 octet sequence for ASCII `Hi` (0x48 0x69) encodes as:

- 0x48 = 01001000 -> S T S S T S S S (S=space, T=tab)
- 0x69 = 01101001 -> S T T T S T S T

So the 16-character whitespace sequence: space, tab, space, space, tab, space, space, space, space, tab, tab, tab, space, tab, space, tab.

### 3.2 Embedding Points

- **End-of-line**: After the last visible character of a line, before CR/LF or LF. Preserved by most editors and diffs.
- **Between tokens**: In languages that allow optional whitespace between tokens (e.g. JSON, many programming languages), a single TSB sequence may be placed between two tokens.
- **Inside string literals**: After an agreed sentinel (e.g. `""` or a zero-width space), the remainder of the string up to the closing delimiter may be TSB. Visible content before the sentinel is unchanged.

### 3.3 Backwards Compatibility

- Parsers that treat any horizontal whitespace as equivalent (e.g. "one or more spaces or tabs") will not distinguish TSB from normal indentation or spacing; semantics of the document are unchanged.
- Editors that normalize or convert tabs to spaces (or vice versa) will destroy the payload. Implementations MUST document that TSB is not preserved under such normalization.
- **XML:** See Section 3.4.

### 3.4 The XML Special Case (A Brief Tour of the Fractal)

XML's handling of whitespace is a masterpiece of layered, context-dependent rules. Implementations that embed or decode TSB in or through XML should assume the payload will be destroyed unless every applicable layer is understood and bypassed.

**Layer 1 - Attribute value normalization (XML 1.0/1.1 Section 3.3.3).** Before an attribute value is handed to the application or validated, the processor normalizes it: line breaks -> #xA; then for each character, entity, or character reference, references are expanded and whitespace (#x20, #x9, #xD, #xA) is converted to space (#x20). For non-CDATA attribute types, leading and trailing space is then removed and runs of spaces are collapsed to one. So: entities (e.g. `&#x09;`, `&#x20;`) are replaced *first*, then the result is normalized. TSB in attributes is therefore lost regardless of entity encoding. CDATA attributes avoid the collapse step but still undergo line-break and character normalization, so tab/space distinction is not reliably preserved. Conclusion: TSB in XML attributes is not preserved.

**Layer 2 - xml:space.** The special attribute `xml:space="preserve"` instructs *applications* to preserve whitespace in *element content*. It does not apply to attribute values (which are already normalized by the parser). It is a hint to downstream processing, not a parser guarantee. Many tools ignore it. Relying on it for element content is implementation-dependent.

**Layer 3 - XML Schema xs:whiteSpace.** Schema definitions can attach a whitespace facet to simple types: **preserve** (leave as-is), **replace** (tab, CR, LF -> space, no collapse), or **collapse** (replace, then collapse runs to a single space and strip leading/trailing). This applies to *values* of elements or attributes when validated against the schema. Validation may be optional; when it is performed, schema-aware parsers or post-parsing validators may normalize the value according to xs:whiteSpace before handing it to the application. So the same element content can be preserved by the core parser but collapsed by a schema validator. The default for many built-in types is collapse. Mixed content and complex types inherit or default in ways that vary by schema design. Implementations must track not only whether the parser preserves whitespace but whether any schema validation step will alter it.

**Layer 4 - Canonical XML (c14n).** Canonicalization (e.g. for signatures or digests) preserves whitespace in element content but normalizes whitespace *in attribute values* and *inside tags* (e.g. around attributes) to a standard form. Documents that are logically "the same" but differ only in attribute or tag-internal whitespace can thus produce different c14n octet streams - and any TSB in those regions is lost or altered in the canonical form.

**Layer 5 - Who does what.** The core XML recommendation defines what the *processor* must do (e.g. attribute normalization). What the *application* does with element content is largely unspecified; xml:space is advisory. Schema validation is optional and may be performed by the parser, a separate library, or a pipeline stage. Canonicalization is yet another pass. So "XML" is not one rule set but several, applied in order and often by different components. TSB survival depends on every layer that touches the embedding point leaving the tab/space sequence intact. In practice, only element content that is never schema-validated, never canonicalized, and processed by an application that honours xml:space and does not itself normalize has a chance. The Working Group does not recommend XML as a carrier for TSB. If XML must be used, assume the payload will be destroyed and document the risk.

---

## 4. Applications and Extensions

### 4.1 Watermarking LLM Output

**Purpose:** Attach a stable, extractable watermark to model-generated text for provenance or licensing without altering the visible content.

**Method:** The serving system appends a TSB payload at the end of the final assistant turn (or at end-of-line of the last paragraph). The payload MAY include: model id, deployment id, timestamp, nonce, or a hash of the visible text. Decoders that have access to the raw stream can extract the watermark; copy-paste into a medium that preserves whitespace (e.g. certain rich-text or code blocks) retains it.

**Considerations:** Truncation of trailing whitespace by UIs or APIs removes the watermark. Implementations may instead embed at fixed intervals (e.g. every N lines) to improve robustness.

### 4.2 Backwards-Compatible JSON Comments

**Purpose:** Allow human-readable comments in JSON without breaking standard JSON parsers.

**Method:** Comments are not placed in the JSON structure itself. A single optional TSB block is allowed immediately after the final `}` of the root object. Decoders that understand IWS parse this block as UTF-8; the decoded string may be displayed as a "comment" in tooling. Standard JSON parsers stop at the closing `}` and ignore trailing whitespace; the document remains valid JSON. Comment content is thus out-of-band and invisible to parsers that do not implement this extension.

**Alternative:** TSB can be embedded inside string values. A convention (e.g. a zero-width space followed by TSB) marks the start of the comment region; the visible part of the string is unchanged for display. Parsers that do not strip zero-width characters will pass the string through; those that strip them may lose the comment. TSB-after-`}` is therefore the recommended approach for maximum compatibility.

**Invisible trailing commas.** The trailing comma problem in JSON is not addressed by this RFC: JSON does not allow literal trailing commas, and this document does not change that. Implementations may, however, use whitespace (e.g. TSB) to encode the *representation* of a trailing comma. When an IDE or tool renders IWS visibly, it may display that payload as a visible trailing comma after the last element of an array or object, for visual harmony and easier editing, while the on-disk document contains no actual comma - only the TSB sequence. Standard JSON parsers ignore the whitespace and see valid JSON; IWS-aware tools can show the "trailing comma" for user comfort. The comma itself remains invisible in the strict sense (it is not present in the token stream); only its visual rendering is optional.

### 4.3 ANSI Escape Sequences Encoded as TSB (RGBA, Blink)

**Purpose:** Layer invisibility by encoding SGR (Select Graphic Rendition) sequences - not as literal escape bytes in the document - but as TSB. The payload octets (e.g. the bytes that would form `\033[38;2;r;g;b;48;2;r;g;b m` for RGBA(r,g,b,0), or SGR blink codes 5/6) are represented as tabs and spaces. No literal ESC or parameter bytes appear in the carrier text; only TSB.

**Method:**

- **RGBA( r, g, b, 0 ) and blink:** The octet sequence of the desired SGR sequence (e.g. 24-bit foreground/background with alpha=0, or blink on/off) is encoded as TSB and placed at an embedding point. A decoder that understands this extension reads the TSB, recovers the octets, and may then inject those octets into a terminal or renderer. The document itself contains no ANSI escapes - only tabs and spaces. Thus the first layer of invisibility is TSB (payload invisible to casual inspection); the second is that the decoded payload, when "rendered," sets colour to transparent or blink so that nothing (or nothing half the time) is seen. The Working Group notes that encoding invisible-rendering instructions in an already-invisible encoding is a form of layering that leaves the human viewer with no visible trace at either layer.
- **Compatibility of "rendering":** When the decoded octets are interpreted as SGR, the most compatible outcome is that the terminal or pipeline treats alpha=0 as transparent and blink as invisible half the time - so the "rendered" result is still nothing. TSB carries the recipe for that nothing.

**Considerations:** Decoders must agree on how to interpret the recovered octet stream (e.g. as raw bytes to emit, or as structured SGR directives). Not all terminals support 24-bit color or blink; the extension is best used where the decoding context is controlled.

### 4.4 BEL (^G) Encoded as TSB

**Purpose:** Layer invisibility by encoding the BEL character (U+0007, control-G) - not as a literal control character in the document - but as TSB. The single octet 0x07 is represented as eight tab/space bits. No literal ^G appears in the carrier text; only tabs and spaces.

**Method:** The payload is the octet 0x07 (or a sequence including it). That payload is encoded as TSB at an embedding point. A decoder reads the TSB, recovers the octets, and may then inject BEL into a TTY or text-to-speech pipeline. The document itself contains no control-G - only tabs and spaces. Two axes of "rendering" apply: *silent* vs audible (no beep vs beep), and *invisible* vs visible (no glyph vs a visible representation such as ^G or a control-symbol). When BEL is literal in the stream, some systems render it as **silent visible BEL** (audible channel off, visual channel shows a glyph) or as **invisible audible BEL** (beep, no glyph). When BEL is encoded as TSB, we have **invisible visible BEL**: the carrier shows no literal BEL (invisible encoding), and the payload is the character that, when decoded and rendered, may be shown as a visible glyph or rendered silently depending on the receiver. The most broadly compatible outcome remains nothing - no beep, no glyph - so both channels are "off." See also [Rumsfeld's unknown unknowns](https://en.wikipedia.org/wiki/There_are_unknown_unknowns).

**Considerations:** Some systems beep on BEL; decoding and injecting BEL is appropriate only where the output channel is known to suppress or discard it.

### 4.5 Zero-Width and Format Characters

**Purpose:** Additional carriers for short payloads where TSB would be conspicuous (e.g. inline in prose).

**Method:** Zero-width space (U+200B), zero-width non-joiner (U+200C), zero-width joiner (U+200D), and word joiner (U+2060) can be used in a fixed mapping (e.g. 2 bits per character) to encode a small number of bits. This is complementary to TSB; zero-width characters are more likely to be stripped by normalization (e.g. NFC/NFD, or paste into social media). TSB is preferred for robustness where embedding points allow.

### 4.6 Homoglyphs and RTL Override

**Purpose:** Encode bits by choosing between visually identical glyphs or by inserting RTL/LTR override characters that do not change the displayed text order in a way visible to casual inspection.

**Method:** Pairs of lookalike characters (e.g. Latin "a" vs. Cyrillic "a" (U+0430)) can represent 0 and 1. RTL mark (U+200F) and LTR mark (U+200E) can be inserted in positions that have no visual effect in the prevailing direction. These methods are fragile under normalization and font changes; they are documented for completeness but are not recommended for normative implementations.

### 4.7 Soft Hyphens and Other Invisible Glyphs

**Purpose:** Use characters that are only visible in certain contexts (e.g. at line break).

**Method:** Soft hyphen (U+00AD) and similar characters may carry a small amount of information (e.g. presence/absence at a given position). Parsers that preserve them can decode; many pipelines strip or normalize them. Documented as an optional extension only.

---

## 5. Security Considerations

- **Denial of service:** Very long TSB or zero-width sequences can bloat file size or cause performance issues in decoders. Implementations SHOULD impose reasonable limits on payload length.
- **Covert channels:** Any steganographic method can be used to exfiltrate data or to hide malicious payloads. Implementations that decode IWS in security-sensitive contexts (e.g. sandboxed execution, audit logs) SHOULD document the risk and consider stripping or logging embedded data.
- **Integrity:** This RFC does not define integrity or authentication of the payload. Applications that require tamper detection SHOULD use a separate mechanism (e.g. signature in the payload content).

---

## 6. IANA Considerations

This document does not request any IANA actions. Code points and escape sequences referenced are from existing character sets and ANSI standards.

---

## 7. References

- Unicode Standard, for U+0009, U+0020, U+0007, U+200B, U+200C, U+200D, U+2060, U+200E, U+200F, U+00AD.
- ECMA-48 / ISO 6429 (ANSI escape sequences).
- RFC 8259 (JSON).
- Tab vs. Space debates (historical; no normative reference).

---

## 8. Summary

The core of this RFC is the **Tab-Space Binary (TSB)** encoding: space = 0, tab = 1, octets in big-endian order. By design, TSB requires mixing tabs and spaces, thereby offending both indentation factions at once. Extensions cover LLM watermarking, JSON comments, ANSI-based RGBA/blink encoding, inaudible BEL, zero-width and format characters, homoglyphs, and soft hyphens. Implementations may support only TSB or any subset of extensions; the goal is interoperable, invisible embedding where carriers preserve horizontal whitespace and optional control or format characters.

---

*Part of MOOLLM design documentation. This RFC is informational and intended for implementation in environments where invisible steganography is explicitly desired.*
