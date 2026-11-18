# Dasher: driving a language model

Dasher is a way to write by steering. Letters stream toward you from the right side of the screen,
each in a box, and you point at the one you want and fly into it. Inside each box are smaller
boxes for the letters that could come next, and so on. A language model, a program that predicts
how likely each next letter is from the letters before it, sizes the boxes: likely letters get
big boxes and unlikely ones get small boxes, so the text you probably mean is easy to reach and
everything else is still there, only smaller. You never click, and if you drift off course, you
steer back.

David MacKay created Dasher at the University of Cambridge, starting with a prototype in 1997, and
his student David Ward turned it into working software and measured how well it works. It is free
software. It works with any alphabet, and with any muscle that can move a pointer: a hand on a
mouse, a finger on a touch screen, the eyes, the head, the breath, or a single switch. People who
can't use a keyboard have written a university thesis, email, and code with it.

I've written about Dasher on Hacker News since 2016, usually in threads about something else:
Palm's Graffiti, pie menus, a neural implant, the demoscene. This essay gathers those comments in
one place, checks them against the sources, and adds what has happened since. It's the serious
companion to Palm's essay
[*One Monkey, Infinite Typewriters*](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md),
which tells the same story in the voice of a monkey who lives in MOOLLM's adventure world. I wrote
it with Anthropic's Claude, from my comments, MacKay's 2007 Google Tech Talk, Ada Majorek's 2016
video, and the Dasher project's own pages.

### An idea on a bus

MacKay told the origin story at Google in April 2007. About ten years earlier he was on a bus to
the Denver airport with his friend Mike Lewicki and got out his PDA, and Lewicki "looked at this
thing in disgust and he said, gee, that thing is so damn big." Most of the size was the keyboard.
So they asked how you could write with something the size of a button on your lapel, and then how
you could write with nothing but a head-mounted display that could track where you were looking.

The [Dasher site](https://www.inference.org.uk/mackay/dasher/) credits both of them: "Dasher was
conceived by David MacKay and Mike Lewicki and written in tcl by David MacKay." MacKay wrote the
first summary of the concept in April 1998.

### Two old metaphors and a new one

MacKay started from what writing is. "One metaphor about writing is a 200 year old metaphor that
says writing is pressing buttons," he said, and "another metaphor for what writing is is a 10,000
year old metaphor that says writing is scribbling with a stick." Shrink the buttons and you get
tiny keyboards. Shrink the stick and you get Graffiti, the one-stroke-per-letter alphabet on Palm
handhelds, and Unistrokes, a similar alphabet from Xerox PARC.

"I'm a bit of a fundamentalist at heart," MacKay said, and he offered a third metaphor: "writing
is navigating, navigating in the library of all possible books."

The Dasher site [lays out the library](https://www.inference.org.uk/dasher/Novice.html). "Imagine
a library containing all possible books, ordered alphabetically on a single shelf." Every book
anyone could write is on that shelf, along with every misspelled and meaningless one. To write
"hello there," you go into the h section, then the he section inside it, and so on. "Thus writing
can be described as zooming in on an alphabetical library, steering as you go."

Then comes the part that makes it work, on the
[next page](https://www.inference.org.uk/dasher/Novice2.html): "we alter the SIZE of the shelf
space devoted to each book in proportion to the probability of the corresponding text." In the
talk MacKay said "we're using our language model to allocate more shelf space to the probable
characters." After an h, the ha, he, hi, and ho sections are wide, and hb is a sliver.

### Why keyboards waste bits

The abstract of MacKay's talk makes the case in one sentence: "Keyboards are inefficient for two
reasons: they do not exploit the redundancy in normal language; and they waste the fine analogue
capabilities of the user's motor system (fingers and eyes, for example)."

A bit is the information in one choice between two equally likely options. Claude Shannon
estimated that English carries about one bit per character, because most of what you'll write
next is predictable from what you've written. Pressing one of 64 keys could carry six bits, since
2 to the 6th power is 64. "So there's a factor of 6 in efficiency there," MacKay said, "because
keyboards don't do language modeling. Of course they were invented 200 years ago, before we had
such things as language models."

The second waste is the hand. "These things on the ends of my hands," MacKay said, "we call them
digits, but they're not actually digital devices, they're analogs." Each finger is capable of fine, continuous
motion, and a keyboard reads only whether it's up or down. MacKay cited an estimate that a single
finger can produce about 14 bits per second. Feed that into a model that needs one bit per
character and you'd write 14 characters per second, about 170 words per minute, with one finger.
That was the goal.

### Arithmetic coding, run backwards

Text compression already knows how to turn predictable text into a few bits. "Text compression is
sort of an inverse process to writing," MacKay said. "In text compression you put in text and out
comes a bit string, and if it's a good compressor the bit string is short. Writing: you make some
sort of gesture and out comes text."

The best compression method he knew was arithmetic coding. An arithmetic coder starts with the
range of numbers from 0 to 1. For each character it narrows the range to that character's slice,
and each slice is as wide as the model says the character is likely. A probable character narrows
the range a little and an improbable one narrows it a lot. At the end, any number inside the final
range identifies the whole text, and probable text needs fewer binary digits to pin down.

"Dasher is just back to front arithmetic coding," MacKay said. The screen shows the slices. Your
steering picks a point, more and more precisely as you zoom, and the same model a compressor would
use decodes that point into text. Ada Majorek, who revived Dasher in 2016, said it in one line:
"It started as a visualization of arithmetic coding algorithm." In
[a 2023 comment](https://news.ycombinator.com/item?id=36613058) I put it as decompression: think of
Dasher "as extremely efficiently decompressing cursor motion (or other device inputs) into text."

The box sizes aren't arbitrary. Each box's height is proportional to the probability of its
text, which MacKay explained in the questions after the talk is "the optimal way in terms of getting the best possible writing
speed if we assume that the user drives at a steady rate." Zooming in by a factor of two is one
bit, so "four factors of two of zooming every second would be four bits per second."

Dasher's model was PPM, prediction by partial matching, a compression model that "just looks at
the last five characters that have been written and uses that as a context to predict the next
character." It's fast, it learns as you write, and it works in any language. It gets English down
to about two bits per character, not Shannon's one, and that gap comes up again below.

### Steering

"It's just like driving a car," MacKay said, more than once. "You point where you want to go."
Point up or down to choose among the boxes. How far you point from the center of the screen sets
your speed. Point left to back out of the library, "a way of undoing what I've recently written."
There is no clicking and no dragging: "You just point, and wherever you're pointing, if Dasher is
running, then you're going in that direction."

Some people find the motion queasy to watch, and he had an answer for them too. "If you go for a
ride with Ralf Schumacher and you're the passenger, he's the driver, who gets sick? The
passengers, right? And Ralf is fine because he's the driver, and he can anticipate the motions and
things that are going to happen, because he's in control." Writing is normally a solo activity, he
added, so the passengers don't matter.

The joke is also the design principle. The person steering knows where they're going, so the
motion isn't noise to them. It's feedback.

### No modes, and mistakes you steer out of

Dasher looks like word completion, and MacKay took that on. With a word completion menu on a
handheld, "you have to make that decision": stop typing, look at the suggestions, search them, and
if your word isn't there, go back and find your place. "Those changes of mode have a cognitive
cost. In Dasher there are no modes. There is just using Dasher." When the predictions are good you
go fast, and when they're poor "you still write in exactly the same way," only slower.

The other half is correction. "Inaccurate gestures can be compensated by later gestures," MacKay
said, the way you navigate anywhere: "you modify your future motor gestures to make up for the
error that you made a moment before, so you're perpetually correcting your errors." Steering with
a head mouse during the talk, he said "I was wobbling all over the place, but nevertheless I got to
my destination, just like a wobbly car driver."

That property is what first drew me in, because pie menus have it. A pie menu puts its choices
around the cursor by direction, so you choose by moving toward one, and you can keep adjusting
until you release. In [2016](https://news.ycombinator.com/item?id=12311758) I wrote: "Unlike
Graffiti-like gesture recognition systems, and like pie menus: inaccurate gestures can be
compensated for by later gestures -- you can continuously and perpetually correct your errors
without changing mode, canceling or repeating gestures." The history of pie menus, including my
part in it, is in
[Pie Menus: A 30-Year Retrospective](https://donhopkins.medium.com/pie-menus-a-30-year-retrospective-5bdcb24a835a).

When I wrote to Ada Majorek about pie menus, she pointed me to
[D@sher](https://www.youtube.com/watch?v=5oSfEM8XpH4), Aubrey Hesselgren's prototype of "an
adaptive, hierarchical radial menu" that dives through nested options the way Dasher dives through
letters, and grows the options you pick most.

### Any muscle

"One of our mottos in the Dasher project is write with any muscle," MacKay said, and the talk was
a tour of them.

- **A finger.** He gave his demonstrations by moving one finger on a touchpad "the same size as a
  lapel." David Ward wrote on a Pocket PC touch screen with a stylus in 2001.
- **The eyes.** With an eye tracker, you look where you want to go. David Ward and MacKay compared
  Dasher with an on-screen keyboard, which MacKay called "the cruelest form of torture known to
  man": experts on the keyboard managed about 15 words per minute with perhaps a fifth of the
  words misspelled, while experienced Dasher users reached about 25 words per minute after an
  hour, and "the error rate was essentially zero." They published the comparison in *Nature* in
  2002. A later mode tuned for eye trackers brought Dasher close to 30 words per minute.
- **The head.** A head mouse moves the pointer as you turn your head. Mick Donegan at the ACE
  Centre in Oxford studied a young man named Paul with cerebral palsy, who couldn't talk and had
  been writing with an on-screen keyboard and a head mouse. With Dasher he needed less head
  movement and no clicking or dwelling, he thought he could write about four times faster, he made
  fewer spelling mistakes, and "he used Dasher to write his final thesis at Aston University and
  graduated in 2004 with a bachelor's degree."
- **The breath.** MacKay and Ryan Adams built a breath mouse. Breathing in and out moves the
  pointer up and down, one dimension instead of two, and Dasher maps that dimension around a dial
  so you can still go forward and back. Beginners went from 2 to about 6 words per minute in an
  hour of practice, and MacKay went from 11 to 15.
- **A tilt.** MacKay tried to persuade Samsung and Nokia to make a phone you could write on by
  tilting it.
- **Buttons.** If someone can press only two switches, the best use of them is up and down, not
  letters. If they can also choose when to press, the timing carries information too. Dasher's
  dynamic two-button mode, which MacKay credited as "an idea of Radford Neal," drives steadily
  forward while you press to recenter the view. MacKay wrote a sentence with 13 presses at about
  one a second. Radford Neal is also, with Ian Witten and John Cleary, an author of the 1987
  paper "Arithmetic coding for data compression."

"If you can move any muscle," MacKay said, "we can get a piece of hardware and we can have that one
muscle drive Dasher."

### Any language

"Having said we're going to base our thing in information theory," MacKay said, "we instantly get
a writing solution for every language on the planet." Graffiti needs a new stroke designed for
every letter of every alphabet. Dasher needs an alphabet and some text to learn from. MacKay wrote
Japanese in Hiragana during the talk, though he can't write it by hand, because he knew the order
of the alphabet. Dasher needs no special learning, he said, "though it does help to know the
alphabetical order of the language that you're writing in."

Adding characters costs little. He switched to an alphabet with every character on a keyboard and
more Unicode besides, capitals grouped in yellow boxes, and showed that "it isn't slowing me down,"
because the model keeps unlikely characters small. After a period, the space and the capitals grow,
because they're what comes next. When he took the trouble to write "microsoft" with a lowercase m,
Dasher kept it lowercase: "my feeling is that's the way that smart software ought to work."

The talk ended with screenshots of Dasher in Danish, Finnish, Swedish, Polish, Arabic, Hebrew,
Persian, Bengali, Tamil, Korean, and the International Phonetic Alphabet, and with Chinese and
Japanese, where you write the sounds and then steer through the model's guesses at the characters.
Bliss-Dasher, by MacKay, Seb Wills, and Annalu Waller, writes in Blissymbolics, a language of
symbols for meanings rather than sounds.

PPM learns as you write, so Dasher adapts to you. MacKay showed it trained on a hundred favorite
phrases, the kind of thing someone who can't speak needs to say quickly, like "please turn up the
music" or "please give me some water," and the library turned into a tree of those sentences. Ada
Majorek kept hers set up to switch between English and Polish, which she did "many times per day."

### How fast

These numbers come from different studies with different people and tasks, so read them as rough
magnitudes, not as a race.

- **Learning.** David Ward had volunteers from Cambridge's astrophysics group take dictation from
  Jane Austen's *Emma*, with the model trained on 90 percent of the book, in twelve five-minute
  sessions. "Bottom of the class started out at about five words per minute and after an hour of
  practice was still bottom of the class and going at about 10 words per minute. Top of the class
  started immediately in the first five minutes going at 12 words per minute and was up above 25
  words per minute after one hour of practice." On the keyboard they typed about 50, with perhaps
  18 years of practice. "We're not aware of any writing system that has a learning curve steeper
  than this."
- **Experts.** The talk's abstract: "Users can achieve single-finger writing speeds of 35 words per
  minute and hands-free writing speeds of 25 words per minute."
- **Two buttons.** About 20 words per minute.
- **Speech, for comparison.** Raw dictation can run at something like 140 words per minute,
  MacKay said, but correcting a recognizer's mistakes with a mouse and keyboard brings it down to
  about 14.
- **Stylus alphabets, for comparison.** In a 2008 study by Steven J. Castellucci and I. Scott
  MacKenzie, over twenty sessions, Graffiti went from 4.0 to 11.4 words per minute and Unistrokes
  from 4.1 to 15.8, with high correction rates.

### Ada Majorek and Dasher 5

Ada Majorek, a software engineer at Google, was diagnosed with ALS in 2013. In a
[video](https://www.youtube.com/watch?v=LvHQ83pMLQQ) for the release of Dasher 5 in April 2016,
she said: "ALS robbed me from ability to speak and ability to use computer keyboard. Thanks to
Dasher I am still able to communicate at reasonable speed." And: "Since my ALS diagnosis in 2013 I
tried countless number of alternative text entry and speech generation methods. So far Dasher is
the fastest and least tiring."

Dasher had gone quiet. "Unfortunately at the time Dasher was not actively maintained. I was a
software engineer in desperate need for a fast alternative communication tool. Dasher was an
open-source project. I decided to start coding." With help from friends and support from Google,
she added features for people who use Dasher to communicate, and "after almost 6 years of silence"
released Dasher 5.00. She presented it with Raquel Romano at the
[CSUN Assistive Technology Conference in 2016](https://www.youtube.com/watch?v=qFlkM_e-sDg). She
used Dasher with a head mouse to write code as well as email.

MacKay died in April 2016, at 48. He had also been Chief Scientific Advisor to the UK Department of
Energy and Climate Change and the author of
[*Sustainable Energy: Without the Hot Air*](http://www.withouthotair.com/). Afterward I wrote to Ada
offering to help port Dasher to Unity and to head-mounted displays. She was swamped with work at
Google, replied anyway, and signed it "Written with Dasher and Headmouse." Her reply describes how
Dasher is built: "There is Dasher Core. It is platform independent. And 'all' you need to do is to
extend several classes." Implementing it in JavaScript, she wrote, "is an interesting idea. You are
second person suggesting it."

### The Dasher Project today

The Dasher site's [history page](https://www.inference.org.uk/dasher/History.html) is a long list
of the people who carried the project after MacKay and Ward; they're all in the credits below.
GNOME hosted the free software release for years, with Patrick Welche at Cambridge keeping it
building. Later the ACE Centre, the UK assistive technology charity where Mick
Donegan did his head mouse study, stewarded the project, with Gavin Henderson and Will Wade as its
delegates.

"As of 2026, the project is led independently by Will Wade and the Dasher Project maintainer
team," says its [governance document](https://github.com/dasher-project/governance). Its
[GitHub organization](https://github.com/dasher-project) holds:

- [DasherCore](https://github.com/dasher-project/DasherCore), MIT licensed: "This fork of the
  Dasher-MIT version aims at modernizing the Dasher backend and making it buildable again on all
  major platforms."
- Front ends on that core for Apple platforms in SwiftUI, for Windows in Avalonia, and for GTK,
  which describes itself as "Still in very early development."
- [dasher-web](https://github.com/dasher-project/dasher-web): "Dasher text entry in HTML, CSS,
  JavaScript, and SVG."
- A design guide for version 6 and beyond.

Most of them were updated in November 2026.

### Relatives

Built, at least as prototypes:

- **Speech Dasher**, by Keith Vertanen, from 2003 to 2007. In the
  [Dasher site's words](https://www.inference.org.uk/dasher/Directions.html): "Speak into an
  imperfect speech-recognizer, and watch as its inferences are displayed as predictions; wherever
  it is not sure what you said, use dasher to steer into the correct sentence." In the talk MacKay
  played Keith's recording of someone correcting a recognizer by voice alone, select, scratch
  that, spell that, and then Keith's prototype fixing the same sentence by steering.
  ([Video](https://www.youtube.com/watch?v=cCF6a00Bcoo),
  [project page](https://www.inference.org.uk/kv227/speechdasher/).)
- **Search Dasher**, which only lets you write strings that exist in a document: "if you want to
  search for a string in a document, it's stupid to allow the user to type in strings that don't
  exist."
- **Menus in Dasher.** A prototype that put "all of the menus in principle of all the applications
  running on your computer" inside Dasher, "a user-friendly alternative to the wheelchair alley of
  death, which is the sequence of pull-down menus." It wasn't shipped "because it might cause
  problems and crashes."
- **VI Dasher**, a prototype for people who are visually impaired and also can't use a
  keyboard. It speaks one dividing word, and two switches say whether what you want comes before
  or after it in alphabetical order.
- **D@sher**, Aubrey Hesselgren's radial menu, above.
- **Dasher in VR.** The developer xanxys built Dasher into
  [construct](https://github.com/xanxys/construct), a VR environment, so you can write by pointing
  your head. ([Video](https://www.youtube.com/watch?v=FFQgluUwV2U).)

Listed on the Dasher site as ideas:

- **Translation Dasher**: "Assume we have a poor translation system that translates badly from
  French to English. An expert has to zip through the translation and clean up errors. This
  cleaning-up could be done within Dasher, using the output of the translator to define a language
  model."
- **basher**: "a mouse-driven command-line interface; a one-handed, keyboardless alternative to
  tcsh, csh, bash, etc."

### Dasher and large language models

MacKay knew what would make Dasher faster. PPM "can compress English down to about two bits per
character, so in principle, if we could make a better language model with all human knowledge
built into it, and if Shannon's right that English is really about one bit per character, Dasher
should be able to go twice as fast. And that's something we're still working on." At four bits per
second of steering, a model that needs two bits per character gives you two characters per second,
and a model that needs one bit gives you four.

A large language model is a program trained on a large share of everything people have written,
which predicts the next token, a word or piece of a word, from everything before it. It is the
nearest thing yet to the "better language model with all human knowledge built into it" that
MacKay asked for in 2007.

Putting one inside Dasher has two problems I know of. Dasher needs the probability of each next
character, and a model that predicts tokens has to be asked for it, by adding up the probabilities
of every token that starts with each character and then following tokens that run across several
characters. And Dasher asks for predictions continuously, for every box it is about to draw, so the
model has to keep up with your steering. PPM answers instantly. A large model is slower and costs
money per call.

There's a deeper connection. Compression and generation are the same machinery run in opposite
directions. In 2023 I described a low-tech way to see it: "Take a huge text file of HN postings,
and compress it with gzip or compress or some other robust compression algorithm. The better the
algorithm, the more the output will look like random noise. Then slice the compressed file in
half, and replace the second half with random numbers. Then uncompress it. You'll find that at the
point you sliced it, it keeps on writing out almost plausible text for a while, consisting of
highly probably snippets of commonly encountered words and phrases, then goes downhill towards
incoherence."

In the same comment I quoted Ed Fredkin's story about John Cocke, the IBM computer architect, who
called him late one night in the early 1960s with a theory of dreams. If memory is an efficient
encoding, then "if when you’re asleep, the decoder is decoding random bits (digital noise) mixed in
with a few sensory inputs and taking into account recent memories and stuff like that, the output
of the decoder would be a dream."

A chatbot is that decoder running on dice. To pick each next token, the software usually draws a
random number and takes the token whose slice of the probability range it lands in, which is
arithmetic decoding with random bits for input. Dasher is the same decoder running on your hand.
Both write from a model; what differs is where the bits that choose among its possibilities come
from. In a chatbot they come from a random number generator, you get what you get, and your only
correction is to ask again. In Dasher they come from you, a few bits per second, and each one is a
choice whose result you can see, and take back by pointing left.

That is the difference between riding as a passenger and driving, and it's why I keep saying we
need [interfaces to agency, not agents instead of interfaces](https://github.com/SimHacker/moollm/blob/main/designs/INTERFACE-TO-AGENCY.md):
anything an agent can do, a person should be able to do through an interface, with the result in
view and a way to take it back. A model makes writing cheaper either way. Only one of the two
arrangements lets the person writing decide what gets written.

Chuanqi Sun's [Spaceship IDE](https://github.com/chuanqisun/spaceship) (2026), from the MIT Media
Lab, steers a large language model while it writes. Its premise is a conjecture: "In the near
future, LLM and Decision Models will reach 60 FPS interactivity." A main knob scrubs forward and
back through the generated text, and going back lets you "explore alternative futures." Future
knobs pull out of the main knob like a pie menu: the direction you pull picks a dimension to steer
along, the swing around the main knob picks a value on it, and the distance sets the strength.
Generation runs on Cerebras, with Gemini as what Sun calls a decision model, and the README
describes what real time took: speculative generation, and throwing away future text and canceling
requests whenever the main knob moves backward. You can
[try a simulation of it in the browser](https://chuanqisun.github.io/spaceship/), or go live with
your own API keys.

That pull-out knob is the gesture of the font pie menu I made for NeWS, where the direction picked
the style and the distance picked the point size, with the menu showing the result as you moved. I
shipped pull-out font and size pie menus in UniPress Emacs 2.20.

### What I'd build

These are designs and wishes, mine and MacKay's, not software.

- **Dasher in every operating system and phone.** "Why isn't Dasher built into every operating
  system and mobile phone?" I asked in
  [2023](https://news.ycombinator.com/item?id=38400368). MacKay tried to persuade Samsung and Nokia
  to make a phone you write on by tilting, and wanted a manufacturer to put two-button Dasher on a
  phone. Asked whether he could imagine a million people using Dasher within a decade, he said "I definitely can": people texting one-handed, "maybe they're holding a
  beer in the other hand," people who can't use a keyboard, and people writing Japanese and
  Chinese.
- **A large language model in Dasher**, solving the two problems above.
- **Dasher at every level.** Fly through candidate words, phrases, sentences, and paragraphs when
  the model is right, and dash down to letters to spell what it didn't guess, then back up. Keith
  Vertanen and MacKay's [Speech Dasher](https://www.keithv.com/pub/sd/speechdasher.pdf) did it at
  two levels in 2010, with whole words from a speech recognizer and an escape box for spelling.
  Box sizes should come from all the context, so names you've already used get more area. Worked
  out in [Link pumps](webtop/LINK-PUMPS.md#dasher-at-every-level), with Spaceship's anchors.
- **Dasher in a programming environment.** From
  [2018](https://news.ycombinator.com/item?id=17105728): "Now think of what you could do with a
  version of dasher integrated with a programmer's IDE, that knew the syntax of the programming
  language you're using, as well as the names of all the variables and functions in scope, plus how
  often they're used!"
- **The grammar as the language model.** A
  [design for the teletype](https://github.com/SimHacker/WillWrightShowForFood/blob/main/packages/cabinet/TELETYPE-DASHER.md)
  of the emulated PDP-7 in the WillWrightShowForFood repo: "The teletype should offer Dasher-style
  text entry, steered by the grammar of whatever program is running on the machine." The grammar
  decides what's legal, and a language model only ranks within it.
- **An emoji branch.** From [2025](https://news.ycombinator.com/item?id=44195187): "You could even
  have an 'emoji' branch where you spell out the :smile: codes, constrained to just the defined
  codes so it's easier to select them (and see the growing emojis as you get near to spelling them
  out all the way), incrementally learning your favorites and making them easier to pick."
- **Dasher for every application.** MacKay prototyped every application's menus inside Dasher. My
  long-term plan,
  [aQuery](https://web.archive.org/web/20180826132551/http://donhopkins.com/mediawiki/index.php/AQuery),
  a JavaScript-based programmable accessibility system, like jQuery for accessibility, "would be a
  great way to deeply integrate Dasher with different input devices and applications across
  platforms."
- **Pull-out pie menus for steering a language model**, as in Spaceship, with Dasher's rule that
  every gesture can be corrected by the next one.
- **A neural interface.** In [2021](https://news.ycombinator.com/item?id=27134909), in a thread
  about an implant that let a paralyzed person type by imagining handwriting: "I'd love a neural
  interface to Dasher, which adaptively learns as you use it which letter combinations are the most
  popular, and adjusts over time to make it easier and faster to input common text."

### Credits

From the Dasher site's history page, MacKay's talk, and the Dasher Project's repositories:

- **Invention.** David MacKay and Mike Lewicki conceived Dasher, and MacKay wrote the first
  prototype, in Tcl, in 1997.
- **The research version, 1998 to 2002.** David Ward turned Dasher into working software for his
  PhD, wrote version 1 and the Pocket PC version, and ran the experiments. Alan Blackwell helped
  design them. Phil Cowans and Tim Hospedales contributed, especially to the eye-tracking work.
- **The free software release.** Iain Murray prepared the open source release in summer 2002.
  Phil Cowans wrote version 3 for GNU/Linux, and Hanna Wallach worked on version 3 for the iPAQ.
  With funding from the Gatsby Foundation, Matthew Garrett became project manager and developer in
  December 2002, followed by Chris Ball from 2003 to 2005 and Phil Cowans from January 2006.
- **Version 4 and research from 2005.** Tadashi Kaburagi wrote the Asian language model, Brian
  Williams game mode, and Chris Hack automatic speed control. Ingrid Jendrzejewski ran experiments
  on Button Dasher, and Frederik Eaton fixed a cursor display problem. Piotr Zielinski developed
  Ollie Williams's gaze, head, and gesture tracking software and two-dimensional Dasher. Keith
  Vertanen built Speech Dasher. Seb Wills and Annalu Waller built Bliss-Dasher with MacKay. Ryan
  Adams built the breath mouse with MacKay, and Radford Neal proposed dynamic two-button mode. Mick
  Donegan at the ACE Centre ran the head mouse study.
- **Funding.** The Gatsby Foundation, and the European Commission through the AEGIS project.
- **Maintenance and Dasher 5.** Patrick Welche kept the GNOME version building. Ada Majorek, with
  friends and support from Google, released Dasher 5 in 2016 and presented it with Raquel Romano.
- **The Dasher Project, 2026.** Will Wade leads it, and Gavin Henderson was the ACE Centre's other
  delegate. Contributors to DasherCore and its front ends include Sebastian Pape, Owen Kent, and
  Cagdas Evren Gerede, and contributors to dasher-web include Jim Hawkins and Alexander Gutkin of
  Google Research.
- **Relatives.** Aubrey Hesselgren made D@sher, and xanxys built Dasher into construct.
- **This essay.** Written by me, Don Hopkins, with Anthropic's Claude.

### Sources

Quotes from MacKay's talk and Ada Majorek's video are from YouTube's captions, with punctuation
added and misheard names corrected against the Dasher project's pages.

Talks and video:

- David MacKay, [Dasher: information-efficient text entry](https://www.youtube.com/watch?v=wpOxbesRNBc),
  Google Tech Talk, April 19, 2007, 54 minutes. Also posted
  [here](https://www.youtube.com/watch?v=ie9Se7FneXE).
- Ada Majorek, [Ada Majorek on Dasher](https://www.youtube.com/watch?v=LvHQ83pMLQQ), April 2016.
- Ada Majorek and Raquel Romano, [Dasher, CSUN 2016](https://www.youtube.com/watch?v=qFlkM_e-sDg).
- Keith Vertanen, [Speech Dasher: An Efficient Correction Interface for Speech Recognition](https://www.youtube.com/watch?v=cCF6a00Bcoo).
- Aubrey Hesselgren, [D@sher Prototype: An adaptive, hierarchical radial menu](https://www.youtube.com/watch?v=5oSfEM8XpH4).
- xanxys, [Text Input with Oculus Rift](https://www.youtube.com/watch?v=FFQgluUwV2U).
- Don Hopkins, [Precision Pie Demo](https://www.youtube.com/watch?v=c0scs59va4c), a pie menu you
  pull out of to dial in an exact value.

The Dasher project:

- [Dasher](https://www.inference.org.uk/dasher/), the Inference Group's site, with the
  [history](https://www.inference.org.uk/dasher/History.html),
  [future directions](https://www.inference.org.uk/dasher/Directions.html),
  [publications](https://www.inference.org.uk/dasher/Publications.html), and the library
  explanation ([one](https://www.inference.org.uk/dasher/Novice.html),
  [two](https://www.inference.org.uk/dasher/Novice2.html)).
- MacKay's [first summary of the Dasher concept](https://www.inference.org.uk/mackay/dasher/),
  April 1998.
- [The Dasher Project on GitHub](https://github.com/dasher-project) and
  [GNOME Dasher](https://gitlab.gnome.org/GNOME/dasher).

Papers and books:

- David J. Ward, Alan F. Blackwell, and David J. C. MacKay. "Dasher: a data entry interface using
  continuous gestures and language models." UIST 2000.
  [doi:10.1145/354401.354427](https://doi.org/10.1145/354401.354427)
- David J. Ward and David J. C. MacKay. "Fast hands-free writing by gaze direction." *Nature* 418,
  838 (2002). [doi:10.1038/418838a](https://doi.org/10.1038/418838a)
- David J. Ward, Alan F. Blackwell, and David J. C. MacKay. "Dasher: A gesture-driven data entry
  interface for mobile computing." *Human-Computer Interaction* 17, 2002.
  [doi:10.1207/S15327051HCI172&3_3](https://doi.org/10.1207/S15327051HCI172&3_3)
- Ian H. Witten, Radford M. Neal, and John G. Cleary. "Arithmetic coding for data compression."
  *Communications of the ACM* 30(6), June 1987.
  [doi:10.1145/214762.214771](https://doi.org/10.1145/214762.214771)
- Steven J. Castellucci and I. Scott MacKenzie. "Graffiti vs. Unistrokes: An empirical
  comparison." CHI 2008. [doi:10.1145/1357054.1357106](https://doi.org/10.1145/1357054.1357106)
- David J. C. MacKay. *Information Theory, Inference, and Learning Algorithms.* Cambridge
  University Press, 2003. [Free online](https://www.inference.org.uk/itila/).

My Hacker News comments about Dasher:

- [12311758](https://news.ycombinator.com/item?id=12311758) and
  [12316262](https://news.ycombinator.com/item?id=12316262), 2016, in "A History of Palm, Part 1:
  Before the PalmPilot"
- [17105728](https://news.ycombinator.com/item?id=17105728), 2018, in "Pie Menus: A 30-Year
  Retrospective"
- [27134909](https://news.ycombinator.com/item?id=27134909), 2021, in "Neural implant lets
  paralyzed person type by imagining writing"
- [36613058](https://news.ycombinator.com/item?id=36613058), 2023, in "Demoscene accepted as
  UNESCO cultural heritage in The Netherlands"
- [38400368](https://news.ycombinator.com/item?id=38400368), 2023, in "AI is currently just
  glorified compression"
- [44176481](https://news.ycombinator.com/item?id=44176481) and
  [44195187](https://news.ycombinator.com/item?id=44195187), 2025, in "Ask HN: Options for
  One-Handed Typing"
- [48966007](https://news.ycombinator.com/item?id=48966007), 2026, in "If You Build It, They Will
  Come"

Companions in this repo:

- Palm, [*One Monkey, Infinite Typewriters*](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md),
  the whimsical version, and the [video reading](https://www.youtube.com/watch?v=lL2sw2oYU98) of
  Dasher, Palm, and Tog's "The Infinite Number of Monkeys."
- [The Infinite Typewriters](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/infinite-typewriters.md),
  Palm's Dasher-class typewriter object.
- [An interface to agency](https://github.com/SimHacker/moollm/blob/main/designs/INTERFACE-TO-AGENCY.md).
- [The noisy channel](https://github.com/SimHacker/moollm/blob/main/designs/NOISY-CHANNEL.md), on
  Shannon, noise, and priors.
