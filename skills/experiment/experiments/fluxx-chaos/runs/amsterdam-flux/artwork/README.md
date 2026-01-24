# Amsterdam Flux Card Artwork

Pure illustrated artwork for the MOOLLM Amsterdam Flux card game — a chaotic experiment where AI characters play Fluxx while the rules constantly change.

## What Is This?

This directory contains **AI-generated card artwork** for a custom Fluxx deck. Each image is:

- **Pure artwork** — no text, no card frames, no UI elements
- **Generated via stereo prompts** — structured YAML + evocative prose fed together to the image generator
- **Quality-controlled** — each image is mined for composition, symbolism, and emotional impact
- **Iteratively refined** — failed generations are documented and re-rolled until perfect

## Browse The Cards

**[📖 View Slideshow →](SLIDESHOW.md)** — See each card with full descriptions of what it does in the game

## Quick Reference

| # | Card | Type | Image |
|---|------|------|-------|
| 00 | [Bread](SLIDESHOW.md#00-bread) | Keeper | ![](00-bread.png) |
| 01 | [Cookies](SLIDESHOW.md#01-cookies) | Keeper | ![](01-cookies.png) |
| 02 | [The Rocket](SLIDESHOW.md#02-the-rocket) | Keeper | ![](02-rocket.png) |
| 03 | [The Moon](SLIDESHOW.md#03-the-moon) | Keeper | ![](03-moon.png) |
| 04 | [The Rainbow](SLIDESHOW.md#04-the-rainbow) | Keeper | ![](04-rainbow.png) |
| 05 | [The LLM](SLIDESHOW.md#05-the-llm) | Keeper | ![](05-llm.png) |
| 06 | [Love](SLIDESHOW.md#06-love) | Keeper | ![](06-love.png) |
| 07 | [Time](SLIDESHOW.md#07-time) | Keeper | ![](07-time.png) |
| 08 | [The Sun](SLIDESHOW.md#08-the-sun) | Keeper | ![](08-sun.png) |
| 09 | [Milk](SLIDESHOW.md#09-milk) | Keeper | ![](09-milk.png) |
| 10 | [Peace](SLIDESHOW.md#10-peace) | Keeper | ![](10-peace.png) |
| 11 | [Chocolate](SLIDESHOW.md#11-chocolate) | Keeper | ![](11-chocolate.png) |
| 12 | [Music](SLIDESHOW.md#12-music) | Keeper | ![](12-music.png) |
| 13 | [Movies](SLIDESHOW.md#13-movies) | Keeper | ![](13-movies.png) |
| 14 | [Television](SLIDESHOW.md#14-television) | Keeper | ![](14-television.png) |
| 15 | [Moola](SLIDESHOW.md#15-moola) | Keeper | ![](15-moola.png) |
| 16 | [Simulation](SLIDESHOW.md#16-simulation) | Keeper | ![](16-simulation.png) |
| 17 | [Cake](SLIDESHOW.md#17-cake) | Keeper | ![](17-cake.png) |
| 18 | [The Party](SLIDESHOW.md#18-the-party) | Keeper | ![](18-party.png) |
| 19 | [The Unicorn](SLIDESHOW.md#19-the-unicorn) | Keeper | ![](19-unicorn.png) |
| 20 | [The Dragon](SLIDESHOW.md#20-the-dragon) | Keeper | ![](20-dragon.png) |
| 21 | [The Crown](SLIDESHOW.md#21-the-crown) | Keeper | ![](21-crown.png) |
| 22 | [The Sword](SLIDESHOW.md#22-the-sword) | Keeper | ![](22-sword.png) |
| 23 | [The Castle](SLIDESHOW.md#23-the-castle) | Keeper | ![](23-castle.png) |
| 24 | [The Tree](SLIDESHOW.md#24-the-tree) | Keeper | ![](24-tree.png) |
| 25 | [The Flower](SLIDESHOW.md#25-the-flower) | Keeper | ![](25-flower.png) |
| 26 | [The Crystal Ball](SLIDESHOW.md#26-the-crystal-ball) | Keeper | ![](26-crystal-ball.png) |
| 27 | [The Gift](SLIDESHOW.md#27-the-gift) | Keeper | ![](27-gift.png) |
| 28 | [The Key](SLIDESHOW.md#28-the-key) | Keeper | ![](28-key.png) |
| 29 | [Books](SLIDESHOW.md#29-books) | Keeper | ![](29-books.png) |
| 30 | [War](SLIDESHOW.md#30-war) | Creeper | ![](30-war.png) |
| 31 | [Death](SLIDESHOW.md#31-death) | Creeper | ![](31-death.png) |

## Card Types Explained

### Keepers 🏆
Cards you **want** to collect. Place them in front of you. Most Goals require specific combinations of Keepers to win.

### Creepers 💀
Cards you **don't want**. They prevent you from winning and often attach to your Keepers, corrupting them. You can't win while you have a Creeper (unless the Goal specifically requires it).

## File Structure

Each card has up to 4 files:
- `NN-name.yml` — Structured prompt (YAML skeleton)
- `NN-name.md` — Prose prompt (evocative description)
- `NN-name.png` — Generated artwork
- `NN-name-mined.yml` — Quality analysis and semantic layers

## Generation Pipeline

See [ARTWORK.md](ARTWORK.md) for the full protocol including:
- Stereo prompt format (YML + MD fed together)
- Image mining layers
- Quality control and re-rolling
- Lessons learned from failures

---

*Part of the [MOOLLM](https://github.com/SimHacker/moollm) project — AI agents playing games, learning, and making art.*
