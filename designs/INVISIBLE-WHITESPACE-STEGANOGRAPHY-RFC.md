# Invisible Whitespace Steganography and Its Applications and Extensions

**RFC IWS-2026-04**  
**Date:** 2026-04-01  
**Status:** Informational  
**Author:** MOOLLM Steganography Working Group

---

## Abstract

This document specifies a family of techniques for encoding information in text using characters and sequences that are invisible, inaudible, or semantically neutral to conventional parsers and human perception. The primary encoding is binary representation via horizontal whitespace (tab and space), with extensions for watermarking, metadata embedding, and cross-channel signalling. Compliance with this RFC does not require implementations to support all extensions; the core encoding is normative.

---

## 1. Introduction

Steganography in plain text has historically relied on zero-width characters, homoglyphs, or control characters that may be stripped or normalized by pipelines. This RFC defines a robust alternative: **encoding arbitrary octets as sequences of TAB (U+0009) and SPACE (U+0020)**. These characters are preserved by virtually all text editors, version-control systems, and transport protocols. Mixing tabs and spaces in the same document is widely considered poor style in both "tabs for indentation" and "spaces for indentation" communities; the Working Group adopts this mixture deliberately as the canonical encoding, and notes that antagonizing both camps simultaneously is a feature, not a bug.

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

- 0x48 = 01001000 → S T S S T S S S (S=space, T=tab)
- 0x69 = 01101001 → S T T T S T S T

So the 16-character whitespace sequence: space, tab, space, space, tab, space, space, space, space, tab, tab, tab, space, tab, space, tab.

### 3.2 Embedding Points

- **End-of-line**: After the last visible character of a line, before CR/LF or LF. Preserved by most editors and diffs.
- **Between tokens**: In languages that allow optional whitespace between tokens (e.g. JSON, many programming languages), a single TSB sequence may be placed between two tokens.
- **Inside string literals**: After an agreed sentinel (e.g. `""` or a zero-width space), the remainder of the string up to the closing delimiter may be TSB. Visible content before the sentinel is unchanged.

### 3.3 Backwards Compatibility

- Parsers that treat any horizontal whitespace as equivalent (e.g. "one or more spaces or tabs") will not distinguish TSB from normal indentation or spacing; semantics of the document are unchanged.
- Editors that normalize or convert tabs to spaces (or vice versa) will destroy the payload. Implementations MUST document that TSB is not preserved under such normalization.

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

### 4.3 ANSI Escape Sequences: RGBA with Alpha Zero

**Purpose:** Encode data in terminal output using SGR (Select Graphic Rendition) sequences that set foreground or background to an RGBA color with alpha=0, or that use blink/slow blink in a prescribed pattern.

**Method:**

- **RGBA( r, g, b, 0 ):** Terminals that support 24-bit color and ignore alpha, or that treat alpha=0 as "transparent", render the following text or background as invisible. The sequence of (r,g,b) triples can encode payload (e.g. one octet per color channel, or packed). Example pattern: `\033[38;2;r;g;b;48;2;r;g;b m` with alpha implied or passed where supported. Receivers that capture raw escape sequences can decode; human viewers see no visible change.
- **Blink:** SGR codes 5 (blink) and 6 (rapid blink) can be used in a temporal encoding (e.g. blink = 1, no blink = 0) for terminals that support blinking. Less reliable than RGBA due to terminal and accessibility variability.

**Considerations:** Not all terminals support 24-bit color or preserve escape sequences in copy-paste. This extension is best used in controlled or scripted environments where the full stream is available.

### 4.4 Inaudible BEL (^G)

**Purpose:** Embed a channel in audio or in terminal sessions that produce sound.

**Method:** The ASCII BEL character (U+0007, control-G) is inaudible in many contexts or may be filtered by terminal emulators. When sent over TTY or included in text-to-speech pipelines that strip or ignore BEL, the character can be used as a framing or signalling token. A sequence of BEL and non-BEL characters can encode binary (e.g. BEL = 1, no BEL = 0) in a stream that is later processed by a decoder with access to the raw octets. In purely textual storage, BEL can mark embedding points or act as a sentinel for TSB that follows.

**Considerations:** Some systems beep on BEL; use only where the channel is known to suppress or discard it.

### 4.5 Zero-Width and Format Characters

**Purpose:** Additional carriers for short payloads where TSB would be conspicuous (e.g. inline in prose).

**Method:** Zero-width space (U+200B), zero-width non-joiner (U+200C), zero-width joiner (U+200D), and word joiner (U+2060) can be used in a fixed mapping (e.g. 2 bits per character) to encode a small number of bits. This is complementary to TSB; zero-width characters are more likely to be stripped by normalization (e.g. NFC/NFD, or paste into social media). TSB is preferred for robustness where embedding points allow.

### 4.6 Homoglyphs and RTL Override

**Purpose:** Encode bits by choosing between visually identical glyphs or by inserting RTL/LTR override characters that do not change the displayed text order in a way visible to casual inspection.

**Method:** Pairs of lookalike characters (e.g. Latin "a" vs. Cyrillic "а") can represent 0 and 1. RTL mark (U+200F) and LTR mark (U+200E) can be inserted in positions that have no visual effect in the prevailing direction. These methods are fragile under normalization and font changes; they are documented for completeness but are not recommended for normative implementations.

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
