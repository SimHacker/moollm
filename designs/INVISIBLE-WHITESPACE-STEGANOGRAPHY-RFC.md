# Invisible Whitespace Steganography and Its Practical Applications and Extensions

**RFC IWS-2026-04**  
**Date:** 2026-04-01  
**Status:** Informational  
**Author:** Don Hopkins, Transparent Steganography Working Group
​‌​​​​​‌​‌‌‌​​​​​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌​​​​‌​​​​​​‌​​​‌‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌​​​‌‌‌​​‌‌​​‌​​​​‌
---

## Status of This Memo

This memo provides information for the Internet community. It does not specify an Internet standard of any kind. Distribution of this memo is unlimited. Reproduction if desired may be handled locally.

## Note on Participation

The Transparent Steganography Working Group seems to consist of whoever is reading this document and anyone they have told about it. Membership is not closed.

Notes are encouraged to be timely rather than polished. Philosophical positions without examples, specific suggestions without introductory explication, and explicit questions without any attempted answers are all acceptable. The minimum length for a contribution is one octet (eight whitespace characters).

---

## Abstract

This document specifies a technique for encoding information in text using characters that are invisible to human perception and semantically neutral to conventional parsers. The primary encoding represents binary data as sequences of TAB and SPACE (or their zero-width Unicode equivalents), embedded at end of line. The two motivating applications are backwards-compatible comments in JSON and watermarking of LLM output. The core encoding uses only 7-bit ASCII characters (TAB and SPACE) and is compatible with any transport that preserves horizontal whitespace. An optional Unicode parallel encoding uses zero-width space and zero-width non-joiner for environments where horizontal scrollbars would reveal the payload. Extensions cover rendering of decoded control characters (BEL, ANSI SGR) by user agents. Compliance with this RFC requires only the core encoding; all extensions are optional.

---

## 1. Introduction

JSON has no comments, no trailing commas, and no way to attach out-of-band metadata without breaking standard parsers. LLM output has no standard mechanism for provenance watermarking that survives in the visible text. This RFC addresses both problems with one encoding: **arbitrary octets represented as sequences of TAB (U+0009) and SPACE (U+0020)**, embedded as trailing whitespace at end of line.

These characters are preserved by virtually all text editors, version-control systems, and transport protocols. The encoding requires only 7-bit ASCII, as does UTF-8 for these code points. Mixing tabs and spaces in the same document is widely considered poor style; the Working Group adopts this mixture deliberately and notes that antagonizing both indentation camps simultaneously is a feature, not a bug.

Previous steganographic techniques relied on zero-width Unicode characters, homoglyphs, or control characters that are stripped or normalized by many pipelines. TSB is more robust: TAB and SPACE survive almost everywhere. For environments where long trailing whitespace would be conspicuous (e.g. horizontal scrollbars in an editor), Section 3.1 defines a zero-width Unicode parallel encoding that can be freely mixed with the ASCII form.

---

## 2. Terminology

- **IWS**: Invisible Whitespace Steganography (this RFC).
- **TSB**: Tab-Space Binary encoding (Section 3).
- **Payload**: The octet sequence to be embedded.
- **Carrier**: The visible text or structure that contains the TSB encoding.
- **Channel**: The medium (e.g. source code, JSON, terminal output, LLM response) carrying the steganographic data.

---

## 3. Tab-Space Binary Encoding (TSB)

### 3.1 Encoding Rules

Each bit of the payload is represented by one character. Two equivalent character pairs are defined:

| Bit | ASCII (core) | Unicode (parallel) |
|-----|-------------|-------------------|
| 0 | Space U+0020 | Zero-width space U+200B |
| 1 | Tab U+0009 | Zero-width non-joiner U+200C |
| UTF-8 bytes per bit | 1 | 3 |
| UTF-8 bytes per payload byte | 8 | 24 |

The ASCII and Unicode forms may be freely mixed within a single payload. A decoder treats all four characters equivalently: space and ZWSP are 0; tab and ZWNJ are 1.

**Encoding:**
- Octets are encoded in big-endian bit order (MSB first).
- The resulting character sequence is appended at end of line (Section 3.2).
- No inter-octet separator is required; decoding consumes 8 characters per octet.

**7-bit ASCII compatibility.** The core encoding (tab + space) uses only 7-bit ASCII code points. UTF-8 encodes these identically. The expansion ratio is 1:8 — each payload byte becomes 8 carrier bytes (one tab or space per bit, each one byte in ASCII/UTF-8). The zero-width parallel encoding requires Unicode and is less efficient: U+200B and U+200C are 3 bytes each in UTF-8, so the expansion ratio is 1:24 — each payload byte becomes 24 carrier bytes. The tradeoff is invisibility: zero-width characters consume no horizontal space in rendering, avoiding scrollbars that might reveal a long whitespace tail. Implementations that must stay within 7-bit ASCII use only tab and space.

**Payloads MUST be 8-character chunks.** Every octet is exactly 8 characters of whitespace. A valid payload is always a multiple of 8 characters. There are no start bits, stop bits, or parity bits; these are known to cause interoperability problems.

**Trailing remainder.** A trailing run of whitespace whose length is not a multiple of 8 is not a payload. It is ordinary whitespace. Decoders discard trailing 1-7 characters and do not attempt to decode a partial octet. A line with 5 trailing spaces has no TSB payload — that's just whitespace.

**Recognition regex.** To extract the payload from trailing whitespace on a line:

```
([\t \u200B\u200C]{8})+$
```

This matches one or more complete 8-character groups anchored at end of line. Trailing whitespace shorter than 8 characters does not match. A trailing remainder of 1-7 characters after the last complete group is not captured. ASCII-only variant: `([\t ]{8})+$`.

**Example.** ASCII `Hi` (0x48 0x69) encodes as two 8-character groups (16 characters total):

- 0x48 = 01001000 → `S T S S T S S S`  (S=space, T=tab)
- 0x69 = 01101001 → `S T T S T S S T`

A line `{"key": "value"}` followed by these 16 whitespace characters is valid JSON with an invisible 2-byte TSB comment. A line with only 4 trailing spaces has no payload — 4 < 8, so the decoder ignores it entirely.

### 3.2 Embedding Point: End of Line Only

TSB is embedded only after the last visible character of a line, before the line terminator (CR/LF or LF). No other embedding points are defined. Whitespace between tokens within a line is not used for TSB; decoders ignore it.

**Whitespace is the delimiter.** The run of payload characters at end of line is self-delimiting. There are no comment delimiters (`//`, `/*`, `*/`, or otherwise). The boundary between visible content and payload is the transition from the last non-whitespace character to the first whitespace character at end of line. On a line that contains only whitespace (no visible characters), the entire line content is potential payload.

**Trailing whitespace in visible content.** If a line's visible content legitimately ends with whitespace, this is unambiguous as long as the trailing whitespace is shorter than 8 characters — decoders ignore runs of 1-7 characters. Lines carrying TSB payloads MUST NOT have visible content that ends with 8 or more whitespace characters, as a decoder would misinterpret them as payload. The only format known to use meaningful trailing whitespace is Markdown, which uses exactly two trailing spaces for a line break (`<br>`). Two is well under the 8-character minimum for a TSB octet. No other Markdown construct uses trailing whitespace of any length. In practice, no legitimate text format requires 8+ trailing spaces on a line, so this constraint costs nothing. The Whitespace programming language (Brady and Morris, 2003) — in which the only significant characters are space, tab, and line feed — is explicitly incompatible with TSB. Trailing whitespace in a Whitespace program is executable code, not a comment channel. The Working Group considers this an acceptable loss.

### 3.3 Backwards Compatibility

- Parsers that treat horizontal whitespace as equivalent (e.g. "one or more spaces or tabs") see no difference; document semantics are unchanged.
- Editors or pipelines that normalize tabs to spaces (or vice versa) destroy the payload. Implementations MUST document this.
- Editors that strip trailing whitespace destroy the payload. Implementations MUST document this.

---

## 4. Applications

### 4.1 Backwards-Compatible JSON Comments

**Purpose.** Allow human-readable comments in JSON without breaking standard JSON parsers.

**Method.** TSB-encoded UTF-8 text is appended as trailing whitespace on any line of the JSON document. Standard JSON parsers treat all whitespace as insignificant; the document remains valid JSON. IWS-aware tools decode the trailing whitespace and display it as a comment.

Per-line comments are supported: each line of JSON may carry its own TSB payload. A line with a JSON key-value pair followed by a TSB-encoded explanation is the JSON equivalent of an inline comment.

**Invisible trailing commas.** JSON does not allow trailing commas. However, TSB can encode the *representation* of a trailing comma. An IWS-aware editor may render this as a visible trailing comma after the last element of an array or object, for visual comfort during editing, while the on-disk document contains no actual comma. Standard JSON parsers see valid JSON; only the visual rendering is optional.

### 4.2 Watermarking LLM Output

**Purpose.** Attach a stable, extractable watermark to model-generated text for provenance tracking without altering the visible content.

**Method.** The serving system appends a TSB payload at the end of one or more lines of the assistant response. The payload may include: model identifier, deployment identifier, timestamp, nonce, or a cryptographic hash of the visible text. Decoders with access to the raw text can extract the watermark.

**Robustness.** Embedding at fixed intervals (e.g. every N lines) improves survival when text is truncated or partially copied. Copy-paste into media that preserve whitespace (e.g. code blocks, preformatted text) retains the watermark. UIs or APIs that strip trailing whitespace will remove it.

### 4.3 Control Characters and Escape Sequences in Payloads

TSB can encode any octet sequence, including control characters and escape sequences. A control character or ESC byte in the payload is just an octet; it encodes as 8 whitespace characters like any other byte. No literal control characters or escape bytes appear in the carrier.

**No ambiguity with line terminators.** A newline (0x0A) in the payload encodes as `SSSSTSTS` (00001010) — 8 whitespace characters within the trailing whitespace run. The literal newline that terminates the carrier line is separate; it is outside the TSB payload (it ends the embedding point, not part of it). A decoder recovers 0x0A from the whitespace and hands it to the application. There is no need to escape or replace newlines in the payload; they round-trip cleanly. The same applies to CR (0x0D), NUL (0x00), and every other control character.

**Multi-line comments.** Because whitespace is the delimiter (not `//` or `/*`), TSB has its own syntax and is not constrained by end-of-line comment conventions. A single TSB payload on one carrier line can contain encoded newlines, representing a multi-line comment. An IWS-aware IDE or user agent may render each decoded line as a separate `//`-prefixed comment, indented to align with the first `//`. The on-disk carrier line remains a single line with trailing whitespace; only the rendered view shows multiple comment lines.

**User agent rendering.** What a user agent does with decoded control characters is implementation-defined. The subsections below give practical recommendations for specific cases.

**BEL (U+0007).** A single octet (0x07 = 00000111), encoded as 8 whitespace characters: `S S S S S T T T`. No literal ^G appears in the carrier. A user agent that decodes this payload may:

- **Emit an audible beep** if the output channel is a terminal that supports BEL.
- **Display a visible glyph** (e.g. ^G or a bell symbol) in a control-character-aware renderer.
- **Do nothing.** This is the most common outcome and is the recommended default. BEL is already inaudible on most modern terminals and invisible in most renderers; encoding it in an invisible carrier means both layers typically produce nothing.

**ANSI SGR (color, blink, transparency).** SGR sequences (e.g. `ESC[38;2;r;g;bm` for 24-bit foreground color) can be encoded as TSB: the literal bytes of the escape sequence are the payload octets, represented as whitespace. No ESC or parameter bytes appear in the carrier. A user agent that decodes and interprets SGR payloads may:

- **Set text color to transparent** (RGBA with alpha=0) — rendering the subsequent text invisible even when decoded. The irony: the payload is invisible (it's whitespace), and the decoded instruction makes the *next visible text* invisible too.
- **Enable blink** (SGR 5 or 6) — text that is invisible half the time.
- **Ignore unrecognized SGR.** User agents that do not support 24-bit color or blink SHOULD silently discard the sequence.

**Terminal graphics protocols.** The same principle extends to graphics protocols that are escape-sequence-based. Their commands are byte sequences; TSB encodes them without modification.

- **Tektronix 4010/4014** — vector graphics. Drawing commands (move, draw line, point) are escape sequences supported by xterm and other terminal emulators (`ESC[?38h` enters Tek mode). An entire vector drawing can be encoded as trailing whitespace on a single carrier line. A Tek-aware user agent could decode the TSB and render the drawing. The default rendering is, of course, nothing.
- **Sixel** (DEC) — raster graphics. Pixel data is encoded in escape sequences (`DCS P1;P2;P3 q [sixel data] ST`). Supported by xterm, mlterm, foot, and several modern terminals. A raster image — encoded as Sixel, encoded as TSB — is a picture made of whitespace. The Working Group acknowledges this is absurd and sees no reason not to support it.
- **ReGIS** (DEC Remote Graphic Instruction Set) — structured 2D graphics. Commands specify coordinates, arcs, fills. Also escape-sequence-based, also encodable as TSB.

The Working Group notes that encoding graphics instructions inside an already-invisible encoding is a deliberate layering: neither layer produces anything perceptible by default. The practical value is that controlled environments (e.g. a rendering pipeline that understands IWS) can use these payloads for out-of-band signalling — or invisible art — without any visible artifact in unaware viewers.

**Recommendation.** User agents SHOULD NOT inject decoded control characters, escape sequences, or graphics commands into output streams unless the user has explicitly opted in. The default behavior for any decoded payload that is not UTF-8 text SHOULD be to expose it only through an API, not to emit it to a terminal.

### 4.4 Soft Hyphens and Other Conditionally Visible Characters

**Purpose.** Characters that are visible only in certain rendering contexts (e.g. soft hyphen U+00AD at a line break) can carry a small amount of information (presence/absence at a given position).

**Method.** This is a minor technique: a soft hyphen either appears or does not at a candidate position, encoding one bit. Many pipelines strip soft hyphens. This extension is documented for completeness and is not recommended for use where TSB is available.

---

## 5. Security Considerations

- **Denial of service.** Long TSB sequences can bloat file size. Implementations SHOULD impose reasonable limits on payload length.
- **Covert channels.** Any steganographic method can exfiltrate data or hide malicious payloads. Implementations that decode IWS in security-sensitive contexts SHOULD document the risk and consider stripping or logging embedded data.
- **Integrity.** This RFC does not define integrity or authentication. Applications that require tamper detection SHOULD include a signature or MAC within the payload.
- **Trailing whitespace stripping.** Many editors, linters, and CI pipelines strip trailing whitespace by default. This destroys TSB payloads silently. Implementations MUST document this risk. Toolchains that use IWS SHOULD configure their editors and pipelines to preserve trailing whitespace in carrier files.

---

## 6. IANA Considerations

This document does not request any IANA actions.

---

## 7. References

- **Snow** (Matthew Kwan, 1996) — steganography tool that encodes data in trailing whitespace using tabs and spaces. The most direct prior art for TSB; this RFC documents the same core technique and specifies applications. http://www.darkside.com.au/snow/
- **RFC 20** (ASCII, 1969) — defines TAB (0x09) and SPACE (0x20), the two core encoding characters.
- **RFC 3629** (UTF-8, 2003) — UTF-8 encodes TAB and SPACE as single bytes identical to ASCII; the basis for the 7-bit compatibility claim.
- **RFC 4648** (Base Encodings, 2006) — Base16, Base32, Base64. TSB is structurally a base-2 encoding with a whitespace alphabet ({SPACE, TAB} instead of {0, 1}).
- **RFC 8259** (JSON, 2017) — the JSON specification. Insignificant whitespace (including tabs and spaces between tokens and at end of line) is explicitly permitted and ignored by conforming parsers; this is the property that makes TSB-in-JSON work.
- **ECMA-404** (JSON, 2017) — the ECMA JSON standard, equivalent to RFC 8259.
- **JSON5** (2018) / **JSONC** (VS Code) — JSON supersets that add visible comments. These are the "visible" alternatives to what this RFC does invisibly. TSB has the advantage of not requiring a non-standard parser; the tradeoff is that the comments are invisible without tooling.
- **W3C XML 1.0 Fifth Edition** (2008) — Section 2.10 (whitespace handling), Section 3.3.3 (attribute-value normalization). The basis for Section 3.4 of this RFC.
- **Unicode Standard** — for U+0009 (TAB), U+0020 (SPACE), U+0007 (BEL), U+200B (zero-width space), U+200C (zero-width non-joiner), U+00AD (soft hyphen).
- **ECMA-48 / ISO 6429** (ANSI escape sequences) — SGR (Select Graphic Rendition) sequences referenced in Section 4.3.

---

## 8. Summary

The core of this RFC is **Tab-Space Binary (TSB)**: space = 0, tab = 1, octets in big-endian order, embedded as trailing whitespace at end of line. A zero-width Unicode parallel (ZWSP = 0, ZWNJ = 1) can be freely mixed with the ASCII form for environments where horizontal scrollbars would reveal the payload. The two primary applications are **backwards-compatible JSON comments** (invisible to standard parsers) and **LLM output watermarking** (invisible to human readers). Rendering of decoded control characters (BEL, ANSI SGR) is user-agent-defined; the recommended default is to do nothing, which is ironically the most practical outcome for an encoding whose entire purpose is invisibility.

---

## Appendix A. Why Not XML (and Why Definitely Not SGML)

If you are considering XML as a carrier for TSB, read this appendix first. If you are considering SGML, read it twice.

### A.1 XML

XML's handling of whitespace is a stack of independently specified, independently implemented, and mutually unaware normalization passes. TSB survival depends on every layer leaving the tab/space sequence intact. In practice, most do not, and the ones that claim to are lying by omission.

**Attribute values.** The processor normalizes attribute values before your code sees them (XML 1.0 Section 3.3.3): tabs, CRs, and LFs become spaces; for non-CDATA types, runs collapse to one space and leading/trailing spaces are stripped. Not optional, not configurable. Even `&#x09;` is expanded first, then normalized. Expat — James Clark's C parser; Clark was the technical lead of the W3C XML Working Group — implements this faithfully. Its `XML_SetStartElementHandler` delivers pre-normalized values with no flag or callback to obtain raw whitespace. If the spec's author did not provide an escape hatch, there is not one to be found.

**Element content.** The processor passes element content with whitespace intact. In theory. `xml:space="preserve"` is advisory (SHOULD, not MUST); serializers, pretty-printers, XSLT processors, and DOM round-trips routinely ignore it. XML Schema `xs:whiteSpace` facets default to collapse for most built-in types, destroying tab/space distinction during validation without warning.

**CDATA sections.** `<![CDATA[` ... `]]>` content passes through the parser literally. This is the most viable embedding point, but CDATA is a parser-level construct: once parsed it becomes ordinary character data, subject to schema validation, XSLT, serialization, and DOM round-trips. Verify empirically, not by reading specs.

**Canonical XML (c14n).** Preserves element-content whitespace but normalizes attribute values and intra-tag whitespace.

The Working Group does not recommend XML as a carrier for TSB. If XML must be used, embed only within CDATA sections, verify your entire toolchain empirically, and assume the payload will be destroyed the moment anyone adds a schema, an XSLT transform, a pretty-printer, or a second opinion.

### A.2 SGML

XML's whitespace handling was a simplification of SGML's. Let that sink in.

If you know HTML but not SGML: HTML was originally defined as an SGML application. SGML (ISO 8879:1986) is the meta-language that HTML's DTD was written in. The angle brackets, the ampersand entities, the DOCTYPE — all SGML. XML was created in 1998 as a simplified subset of SGML that removed features the XML Working Group considered too complex for the web. Whitespace handling was one of the things they simplified. What follows is what they simplified it from.

**Record Start and Record End.** SGML does not operate on characters the way you expect. It has abstract Record Start (RS) and Record End (RE) characters — typically mapping to LF and CR respectively — with rules for when they are ignored, preserved, or collapsed. The "RE delenda est" convention: RE immediately after a start tag is ignored; RE immediately before an end tag is ignored; all other REs become a single space. This sounds simple. It was never implemented consistently across parsers. The spec's language was ambiguous enough that two conforming parsers could produce different output from the same document — and did, routinely, for years.

**SHORTREF.** SGML has a feature called short reference maps that allows whitespace sequences to be bound to entity references. A tab character can trigger macro expansion. A blank line can become a `<p>` element. Two consecutive newlines can expand to an entity that closes one element and opens another. Your TSB payload, if it contained a tab, could be silently interpreted as markup. This feature was used in production SGML systems (for example, to support "natural" authoring where a blank line means a new paragraph). It was removed entirely from XML.

**SEPCHAR.** The SGML declaration — a document that precedes the DTD and declares the concrete syntax — defines which characters are separator characters. Separator characters are consumed by the parser as syntax and are not passed to the application. Tab (0x09) is a SEPCHAR in the reference concrete syntax. A tab in your document may never reach your application code. It was eaten by the parser as punctuation.

**Content model dependency.** Whether whitespace in element content is significant depends on the content model declared in the DTD. In element content (where only child elements are allowed, no text), all whitespace is insignificant and discarded. In mixed content (elements and text), whitespace is preserved. The DTD is mandatory in SGML, so your whitespace's fate is determined by a DTD you may not have written, may not have read, and may not be able to find. If someone changes the content model of an element from mixed to element-only, all whitespace in instances of that element silently vanishes. No warning, no error, no diagnostic.

James Clark wrote SP (the reference SGML parser, and the most conformant implementation ever built) and then wrote expat for XML, simplifying SGML's whitespace rules into the merely terrible system described in Section A.1. The Working Group does not recommend SGML as a carrier for anything.

For further study of the CDATA experience, see Hopkins, D., ["I Wanna Be `<![CDATA[`"](https://donhopkins.medium.com/i-wanna-be-cdata-3406e14d4f21), 2021. Sung to the tune of "I Wanna Be Sedated," with apologies to The Ramones.

---

## Authors' Address

Don Hopkins  
EMail: don@DonHopkins.com

## Full Copyright Statement

This document and the information contained herein is provided on an "AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY AND THE INTERNET ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

*This RFC is informational and intended for implementation in environments where invisible steganography is explicitly desired.*
