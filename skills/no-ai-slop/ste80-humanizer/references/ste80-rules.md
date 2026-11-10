# STE80 rules in detail

More examples for Pass 2 of SKILL.md. Read this file when you rewrite a long text, when an S-rule is unclear, or before strict mode.

These rules paraphrase and simplify ASD-STE100 Issue 9. They are not the official text.

The long-form numbers here (1 to 23) are finer than the S-rules in SKILL.md. They map like this:

| SKILL.md | This file |
|---|---|
| S1 One idea per sentence | 1 |
| S2 Short sentences | 2 |
| S3 Condition first | 3 |
| S4 Do not drop words | 4 |
| S5 Lists | 5, 6 |
| S6 Active voice | 7 |
| S7 Simple tenses | 8 |
| S8 Verbs, not nouns, no "-ing" chains | 9, 10 |
| S9 Honest modals | 11 |
| S10 Plain words, one meaning each | 12, 13, 15 |
| S11 One term per thing | 14, 17 |
| S12 No noun stacks | 16 |
| S13 One topic per paragraph | 18, 19 |
| S14 Procedure apart, warnings first | 20, 21 |
| S15 Simple punctuation | 22, 23 |

## A. Sentences

### 1. One idea per sentence

**Rule:** A sentence carries one subject and one main statement. A procedure step carries one action, unless two actions happen at the same time.

**Before:**
> The configuration file, which is loaded at startup and can be overridden by environment variables, controls the cache size as well as the timeout, and should be kept in version control.

**After:**
> The configuration file controls the cache size and the timeout. The application reads this file when it starts. Environment variables can override the values in the file. Keep the file in version control.

### 2. Keep sentences short

**Rule:** Instructions: 20 words or fewer. Descriptions: 25 words or fewer. Aim for an average of about 15. A number with its unit, a code identifier, a name or a quoted string counts as one word.

In 80% mode, a sentence may go a few words over the limit when splitting it would separate a condition from its result. Never go over in strict mode.

### 3. Put the condition first

**Rule:** If the reader must know a condition before they act, write the condition first, then a comma, then the command.

**Before:**
> Restart the service if the health check fails after the deploy.

**After:**
> If the health check fails after the deploy, restart the service.

### 4. Do not drop words

**Rule:** Keep articles (a, an, the), "that", and the verb. Telegraphic text is short but hard to parse.

**Before:**
> Run script, check output, fix errors found.

**After:**
> Run the script. Examine the output. Correct the errors that you find.

In 80% mode, terse fragments are acceptable in tables, headings and short UI labels.

### 5. Use lists for complex text

**Rule:** When a sentence holds a sequence, a set of options or more than two conditions, make it a vertical list. Number the items when order matters.

### 6. Link related sentences

**Rule:** Short sentences need clear joints. Use simple connectors: "but", "because", "thus", "as a result", "then", "after", "before", "if", "when". Do not use "however", "furthermore", "moreover", "additionally".

## B. Verbs

### 7. Use the active voice

**Rule:** Name who does the action. Use the passive only in descriptions where the actor is unknown or not important.

**Before:**
> The token is validated by the gateway before the request is forwarded.

**After:**
> The gateway validates the token. Then it sends the request to the server.

### 8. Use simple tenses only

**Rule:** Use the simple present, the simple past, the simple future ("will") and the imperative. Do not use perfect or progressive forms ("has been", "is being", "will have", "is running").

**Before:**
> We have been seeing failures that are being caused by a race condition that has existed since 2.3.

**After:**
> In version 2.3 and later versions, a race condition causes failures.

### 9. Use verbs, not nouns made from verbs

**Rule:** Put the action in the verb. "Make a decision" becomes "decide". "Perform an installation of" becomes "install". "Carry out a test of" becomes "test".

### 10. Avoid "-ing" verb forms

**Rule:** Do not use "-ing" forms as verbs. Use them only as a fixed noun ("logging", "caching", "load balancing").

**Before:**
> By enabling the flag, ensuring the cache is warm, and monitoring latency, you can avoid timeouts.

**After:**
> To prevent timeouts, do these steps:
> 1. Set the flag.
> 2. Make sure that the cache is warm.
> 3. Monitor the latency.

### 11. Avoid modal hedging

**Rule:** STE uses "can" for possibility and ability, "must" for obligation, and "will" for the future. Replace "may", "might", "could", "should", "shall" and "would" with one of these, with the same strength of meaning.

Be careful here. If the source is uncertain, keep the uncertainty. "This might fail" becomes "This can fail" or "Possibly, this fails", not "This fails".

### 12. No phrasal verbs

**Rule:** Replace two-word verbs with one exact verb. "Set up" becomes "configure" or "install". "Find out" becomes "find" or "learn". "Carry out" becomes "do". "Look into" becomes "examine". "Fill in" becomes "complete" or "write".

## C. Words

### 13. One word, one meaning

**Rule:** Use each word in one meaning and as one part of speech. In STE, "check" is a noun only ("do a check"), and "test" is a noun only ("do a test"). In 80% mode, follow this only where the double meaning causes confusion.

### 14. One term per thing

**Rule:** Name each object, concept or role with one term and keep it. Do not switch between "server", "host", "machine" and "node" for the same thing. Do not cycle synonyms for variety. Readers think a new word means a new thing.

### 15. Use the plain word

**Rule:** Pick the short, common word. Common swaps:

| Instead of | Write |
|---|---|
| utilize, leverage | use |
| perform, conduct, accomplish, carry out | do |
| ensure, verify | make sure |
| commence, initiate, begin | start |
| terminate | stop |
| facilitate, enable, allow, permit | let, help |
| provide | give |
| indicate | show |
| obtain, acquire, achieve | get |
| prior to | before |
| due to | because of |
| in order to | to |
| however | but |
| therefore | thus, as a result |
| additional, further | more |
| approximately | about (80% mode) / approximately (strict) |

`word-swaps.md` (in this folder) has a longer list, grouped by topic. Read it when you rewrite a long text or work in strict mode.

### 16. No noun stacks

**Rule:** Use at most three nouns in a row. Break longer stacks with "of", "for" or a relative clause. Hyphenate pairs that act as one unit.

**Before:**
> the user session token refresh retry limit

**After:**
> the retry limit for the refresh of the session token

### 17. Define technical names once

**Rule:** Technical names (product names, field names, tool names, domain terms) are allowed. Use the name the reader knows. If a term is long, write it in full once, then use one short form.

## D. Paragraphs and structure

### 18. One topic per paragraph

**Rule:** Each paragraph covers one topic. Six sentences at most. Start with the sentence that tells the reader the topic.

### 19. Give information in steps

**Rule:** Go from general to specific. Say what something is before you say how it works. Say what the reader must do before you say why.

### 20. Separate procedure from description

**Rule:** Instructions use the imperative ("Open the file."). Descriptions use statements ("The file contains the keys."). Do not mix the two in one paragraph. Put background in a note, after or before the steps, not inside them.

### 21. Warnings first

**Rule:** A warning (risk to people) or caution (risk to data, money or equipment) comes before the step it applies to. Start with the command, then give the risk.

**Before:**
> Running the migration will drop the users table, so make a backup first.

**After:**
> **CAUTION:** Make a backup of the database before you run the migration. The migration deletes the users table.

## E. Punctuation

### 22. No semicolons

**Rule:** Write two sentences, or use a list. In 80% mode, this is a strong preference.

### 23. Simple punctuation

**Rule:** Use periods, commas, colons (before lists) and parentheses for short explanations or abbreviations. Avoid em dashes used as sentence glue. Use a period or a colon instead.

## F. What 80% mode relaxes

80% mode keeps the reader benefits and drops the parts that make normal prose sound odd:

- **Vocabulary.** Use plain common words, but you do not need the official STE dictionary. Keep words like "need", "important", "however" if a swap would sound strange. Never swap a technical term for a vague one.
- **Contractions.** Allowed in casual text (emails, chat answers). Not in documentation.
- **"Check" and "test" as verbs.** Allowed when the meaning is clear.
- **Length limits.** A small overrun is fine if the split would hurt meaning.
- **Tone.** Warmth is allowed. A short greeting in an email or a "thanks" stays.

80% mode never relaxes these: one idea per sentence, active voice, simple tenses, no filler, one term per thing, all facts kept.

