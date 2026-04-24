# biome/templates/

Directory scaffolds for instantiating new biomes (and, future: new bridges, new instances).

## Available templates

| Template | Use to instantiate |
|---|---|
| [`BIOME/`](BIOME/) | A new daughter biome — copy the entire directory tree to `skills/<new-biome>/`, fill placeholders, declare `inherits: biome`, register in `../biomes/registry.yml` |

## To use

```bash
# Clone the scaffold
cp -r skills/biome/templates/BIOME/ skills/<new-biome-name>/

# Fill in placeholders (search for {{...}} markers)
$EDITOR skills/<new-biome-name>/CARD.yml
$EDITOR skills/<new-biome-name>/GLANCE.yml
$EDITOR skills/<new-biome-name>/SKILL.md
$EDITOR skills/<new-biome-name>/README.md

# Register
$EDITOR skills/biome/biomes/registry.yml   # add entry under biomes:

# Add bridges if it shares machinery with existing biomes
$EDITOR skills/biome/biomes/gateways.yml
```
