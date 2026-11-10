# Pass 1: AI tells in full

## A. Staging instead of stating

These are the strongest and most frequent tells. Act on one sighting.

### §1. Not X but Y

**Watch for:** not X but Y; not just, not only, not merely X, but Y; it's not X, it's Y; X rather than Y; the same contrast across two sentences ("This doesn't mean X. It means Y."); a clipped negative tail ("..., no guessing"). Every language has this formula. Treat it the same way.
**Problem:** The negative half names something nobody claimed, so the positive half sounds bigger. It adds weight but no claim. State the point. Keep a contrast only if the reader really believes the X half, or if both halves carry information.
**Before:**
> It's not just a faster build tool, it's a new way to think about your pipeline.
**After:**
> The build tool caches each step, so a rebuild after a small change takes seconds.
**Before (split across sentences):**
> This doesn't mean tests are optional. It means the linter catches the easy errors first.
**After:**
> The linter catches the easy errors before the tests run.
**Before (clipped tail):**
> The form fills in your address from the postcode, no typing.
**After:**
> The form fills in your address from the postcode, so you do not have to type it.

### §2. One-line closers and dramatic fragments

**Watch for:** a one-sentence paragraph that repeats the paragraph before it; "That's the real win."; "That distinction matters."; "Let that sink in."; "Read that again."; the same closer after several sections; a sentence that names what an example just showed ("This shows the importance of..."); a row of fragments ("No setup. No config. No waiting."); one word in ALL CAPS or with periods (every. single. day.).
**Problem:** The line asks the reader to pause on a claim instead of adding to it. A short sentence is fine when it carries a new fact. Cut a closer that repeats. Merge a row of fragments into one sentence with a real claim.
**Before:**
> We moved the API to edge workers. Latency dropped to 40 ms. No cold starts. No regions. No excuses.
>
> That's the power of the edge.
**After:**
> We moved the API to edge workers. Latency dropped to 40 ms, and cold starts stopped, because the code now runs in every region.
**Before (repeated closer):**
> Caching cuts repeat work. That's the real win.
>
> Retries hide short outages. That's the real win.
**After:**
> Caching cuts repeat work. Retries hide short outages.

### §3. Sayings that sound deep

**Watch for:** the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, X is the Y of Z, X becomes a trap, not a tool but a mirror, the language of, the currency of, the architecture of
**Problem:** An ordinary point is dressed as a hidden truth. The dressing adds no detail. Replace the saying with the specific claim.
**Before:**
> At its core, observability is the language of trust between teams.
**After:**
> Shared dashboards let the on-call team see what the API team sees.

### §4. Staged run-up before the point

**Watch for:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk
**Problem:** The writer announces the point instead of making it. Remove the run-up. "Honestly" inside a casual sentence is normal. The tell is the stand-alone opener before a routine claim.
**Before:**
> Let's dive into how rate limiting works. Here's what you need to know.
**After:**
> The API allows 100 requests per minute per key. After that, it returns HTTP 429.
**Before (staged candor):**
> Is the paid plan worth it? Honestly? It depends on your team size.
**After:**
> The paid plan pays off for teams of more than five people.

### §5. Arguing with no one

**Watch for:** This isn't (mainly) about, I'm not saying, To be clear, Don't get me wrong, This is not to say, Some might say... but, A tempting approach would be, One might be tempted to, You might think... but, It would be easy to just
**Problem:** The text answers an objection or rejects an option that appears nowhere else. Usually it is left over from a draft. Remove the defense. If it holds a real claim, state the claim. Keep an objection that someone in the context really made.
**Before:**
> To be clear, I'm not saying microservices are bad. A tempting approach would be to split everything at once, but that would break the deploy. We split the billing service first.
**After:**
> We split the billing service out first.

## B. Rhythm by rule

Shapes and punctuation used everywhere, whether the meaning needs them or not.

### §6. Forced triads

**Problem:** Ideas come in threes to sound complete. It can be one phrase ("fast, reliable, and scalable"), three parallel examples, or three short facts and a lesson. Check that each item adds a distinct idea. Keep three only when the meaning has three parts. Two or four is fine. If the list is itself a claim in the source (stated values, named features), keep its content in plainer form. Cutting it drops a fact.
**Before:**
> The new dashboard is fast, intuitive, and powerful. It brings clarity, speed, and confidence to your team.
**After:**
> The new dashboard loads in under a second and shows all alerts on one page.
**Before (paragraph scale):**
> A deploy can look clean and fail. A test can pass and hide a bug. A metric can be green and lie. Production rarely explains itself.
**After:**
> A deploy can look clean and still fail, and a green test or metric can hide a bug. Production rarely explains itself.

### §7. Repeated sentence openings

**Problem:** Several sentences in a row start with the same subject because repetition is handled by rule, not by ear. Merge sentences, change the subject or start with the action. Do not ban the word. Writers also repeat an opening on purpose for rhythm. *Weak alone.*
**Before:**
> It reads the config. It checks the schema. It starts the server.
**After:**
> It reads the config and checks the schema. Then the server starts.

### §8. Dashes as the universal connector

**Rule:** The final text has no em dashes (—) or en dashes (–), unless the writer's sample uses them. Then match the sample's rate. Replace each dash with a period, comma, colon or parentheses, or rewrite the sentence. This includes spaced dashes and ` -- `. Leave dashes in code, commands, paths and URLs alone.
**Problem:** A dash lets the writer skip the choice of how two clauses relate, so models use it everywhere. Many editors use dashes too, so one dash is *weak alone*. A text full of them is not.
**Before:**
> The migration — which took six weeks — is done. The old cluster -- finally -- is gone.
**After:**
> The migration took six weeks and is done. The old cluster is gone.

### §9. Stacked qualifiers

**Watch for:** to be fair, it's also possible, could potentially, might arguably, in some cases it may, this is an inference
**Problem:** Edit after edit adds qualifiers until every claim sounds unsure. Usually they repair an overstatement, not real doubt. Keep one qualifier when the source supports it. Keep scope statements, legal and safety notes and real corrections. A single "perhaps" or "tends to" is human, not a tell. *Weak alone.* See also S9.
**Before:**
> This change could potentially possibly cause some issues in certain edge cases.
**After:**
> This change can break requests with empty headers.

### §10. Hyphenated pairs everywhere

**Watch for:** high-quality, well-known, well-documented, long-term, real-time, client-facing after the noun they describe
**Problem:** Compound modifiers keep their hyphen in every position. Keep it before the noun ("a well-documented API") and drop it after ("the API is well documented"). Words that always take a hyphen (third-party, cross-platform) keep it. *Weak alone.*
**Before:**
> The API is well-documented and the support is long-term.
**After:**
> The API is well documented and the support is long term.

### §11. Passive voice and missing subjects

**Problem:** The text hides who acts, or drops the subject. Name the actor when it makes the action clearer. *Weak alone.* In Pass 2 this is a full rule (S6).
**Before:**
> No account needed. Your data is synced automatically.
**After:**
> You do not need an account. The app syncs your data automatically.

## C. Inflation and borrowed authority

The fact underneath is usually sound. Keep it and remove the dressing.

### §12. Overused AI words

**Watch for:** actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, gate/gated (figurative), highlight (verb), interplay, intricate, key (adjective), landscape (abstract), leverage, meticulous, pivotal, quietly, robust (figurative), seamless, showcase, tapestry, testament, underscore (verb), utilize, valuable, vibrant
**Problem:** Models use these words far more often than people, especially in groups. They are tells wherever they appear. A formal word outside this list is not a tell by itself. STE gives the plain swap: see `references/word-swaps.md`.
**Before:**
> Additionally, the new SDK leverages a robust caching layer, showcasing our meticulous commitment to performance across the evolving landscape of mobile development.
**After:**
> The new SDK also caches API responses on the device, so screens load faster on slow networks.

### §13. Inflated significance

**Watch for:** stands as a testament, a pivotal or crucial moment, plays a key role, marking or shaping the, underscores its importance, reflects a broader, lasting legacy, setting the stage for, evolving landscape, indelible mark; "Despite these challenges... continues to thrive"; sections called "Challenges and Legacy" or "Future Outlook"; the future looks bright, exciting times ahead
**Problem:** An ordinary detail is said to mark a change, prove a legacy or promise a future. It shows up as a phrase, a stock "challenges and outlook" section, or a send-off paragraph. Keep the fact. End on the last concrete fact.
**Before:**
> Version 2.0 marks a pivotal moment in the project's journey, reflecting a broader shift toward developer-first tooling.
**After:**
> Version 2.0 adds a CLI and drops support for Node 16.
**Before (send-off):**
> The future looks bright for the project. Exciting times lie ahead!
**After:**
> (Cut the paragraph. End on the last concrete fact.)

### §14. Vague connection or association

**Watch for:** associated with, in association with, connected to, in connection with, linked to, tied to
**Problem:** The text says two things are connected but not how. "She is associated with the project" hides whether she founded it, maintains it or once filed a bug. Name the relation the source gives. If the source does not say, keep the vague words. Do not invent a role.
**Before:**
> The outage was linked to the DNS change, and the team is associated with the platform group.
**After:**
> The DNS change caused the outage. The team is part of the platform group.

### §15. Shallow -ing riders

**Watch for:** highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, cultivating, fostering, encompassing, showcasing
**Problem:** An -ing phrase is bolted onto a simple fact to make it sound deeper. Keep the fact. Keep the rider only if the source supports its claim. STE agrees: no "-ing" verb forms as riders (S8).
**Before:**
> The team shipped dark mode in March, highlighting its commitment to accessibility and fostering a more inclusive experience.
**After:**
> The team shipped dark mode in March.

### §16. Sales language

**Watch for:** rich (figurative), profound, exemplifies, commitment to, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array, breathtaking, must-try, stunning, world-class, cutting-edge, best-in-class
**Problem:** The text reads like an ad. State what the thing is and what it does.
**Before:**
> Nestled in the heart of your workflow, our groundbreaking editor offers a stunning, world-class writing experience.
**After:**
> The editor runs inside VS Code and checks spelling as you type.

### §17. Borrowed authority

**Watch for:** experts argue, observers have noted, industry reports, some critics, several publications; featured in [list of outlets]; over N followers
**Problem:** A name or an unnamed authority stands in for what was said. If the source names who said what, use that. Otherwise cut the claim or the list. A missing citation alone is not a tell. Never invent a source.
**Before:**
> Experts agree that Rust is the future of systems programming. The project has been featured in TechCrunch, Wired, The Verge and Hacker News.
**After:**
> The project is written in Rust. It was on the front page of Hacker News in May.

### §18. Avoiding is, are and has

**Watch for:** serves as, stands as, functions as, operates as, marks, represents [a]; boasts, features, offers, maintains [a]; refers to
**Problem:** Simple verbs become longer phrases. Use *is*, *are* and *has*.
**Before:**
> The `config/` folder serves as the central hub for settings and boasts over 40 options.
**After:**
> The `config/` folder holds the settings. It has more than 40 options.

## D. Formatting by rule

Templates also produce clean formatting. The tell is decoration on every item.

### §19. Bold as decoration

**Problem:** Words are bold for no reason, and every list item has a bold label and a colon. Remove the bold. Turn a labeled list into prose when the labels add nothing. Keep bold for warnings, UI labels and terms the reader must find again.
**Before:**
> - **Performance:** Performance has been significantly improved.
> - **Security:** Security has been strengthened with encryption.
> - **Usability:** Usability has been enhanced with a new interface.
**After:**
> The release makes pages load faster, encrypts stored tokens and adds a new settings page.

### §20. Decorative headings

**Problem:** Headings Capitalize Every Word, carry emoji or arrows, and a rule separates every section. A heading written for effect ("The decision, on one screen") should name what the section holds ("How the options compare"). Use sentence case. Remove the decoration. A five-sentence answer does not need three headings.
**Before:**
> ## 🚀 Getting Started With The CLI →
**After:**
> ## Install the CLI

### §21. Curly quotation marks

**Problem:** Curly quotes (“...”) appear where the format uses straight quotes ("..."). Most editors curl quotes automatically, so this is *weak alone*. In Markdown and code, use straight quotes.
**Before:**
> Set the flag to “true” in “config.yaml”.
**After:**
> Set the flag to "true" in `config.yaml`.

## E. Leftovers from the chat and the draft

Remove these outright. Nothing here needs rewriting.

### §22. Chatbot residue

**Watch for:** I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, Should I continue?, let me know, here is a...
**Problem:** A chatbot's greeting, praise, offer or sign-off stays in text that should stand alone. It is the most certain tell and the easiest to miss when it wraps real content. Remove the wrapper. Keep the content.
**Before:**
> Great question! Here's an overview of how JWTs work. A JWT has three parts: a header, a payload and a signature. I hope this helps! Let me know if you'd like more detail.
**After:**
> A JWT has three parts: a header, a payload and a signature.

### §23. Knowledge-limit disclaimers and guesses

**Watch for:** as of [date], up to my last training update, while specific details are limited, based on available information, not publicly available, not widely documented, maintains a low profile, likely [grew up, began], it is believed that
**Problem:** The text says where the model's knowledge ends, or admits it found no source and then fills the gap with a guess. State what the source does not show, or cut the sentence.
**Before:**
> While details about the library's origins are limited, it was likely created around 2015 to address performance concerns.
**After:**
> The sources do not say when the library was created. (Or cut the sentence.)

### §24. A heading repeated in the first sentence

**Problem:** A heading is followed by a one-line paragraph that repeats it. Remove that line.
**Before:**
> ## Security
>
> Security is important.
>
> The server rejects tokens older than one hour.
**After:**
> ## Security
>
> The server rejects tokens older than one hour.

### §25. Writing about the document instead of its subject

**Watch for:** what the text replaced ("was added to replace"); how it was made ("generated from", "compiled from", "anything unconfirmed is flagged"); a layout the reader can see ("the table below compares", "this section is organized by")
**Problem:** The text describes itself instead of its subject. Mention an old version only in change logs and migration guides. Keep a source credit the reader can follow. Cut the story of how you worked. A single description of the page is *weak alone*.
**Before:**
> This function was added to replace the old approach of looping through all users, which caused O(n²) performance.
**After:**
> This function looks up users in a hash map, so each lookup is O(1).

## F. Writing for the wrong reader

A model writes for a reader with no context. A reply in a thread has a reader who already knows the background. Act on this tell only when you can see the conversation or the text is plainly a reply.

### §26. Re-explaining what the reader knows

**Watch for:** a short reply that repeats the problem, walks through the diagnosis and shows the evidence before it reaches the decision; numbers or commands included to prove a plan works; background the other person wrote; the answer in the last line.
**Problem:** The reader already has the context, so rebuilding it buries the point. Each sentence can read fine alone, so this tell survives a sentence-level cleanup. Lead with the decision. Keep only what could change the reader's mind, usually one fact they lack and any link they need.
**Before:**
> Yes, you're right that the cron job fails on the first of the month. I looked into it: the job uses the local time zone, and on the first the date math rolls back to the previous month, which has fewer days. I tested it with three dates. So I think we should switch to UTC.
**After:**
> Agreed. I'll switch the job to UTC. The local time zone breaks the date math on the first of the month.
