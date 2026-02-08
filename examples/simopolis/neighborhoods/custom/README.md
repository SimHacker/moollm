# Custom District

**Your neighborhood. Your rules.**

The frontier of Simopolis. Drop your own save files here. Build your own lots. Place your own families. Import 25-year-old saves from dusty hard drives. Create entirely new Sims from scratch. This is where Simopolis grows beyond its founders.

## How To Add a Neighborhood

1. Create a directory under `custom/` with your neighborhood name
2. Add a `README.md` describing the neighborhood
3. Import families via the [Exchange](../../exchange/)
4. Place them in [houses](../../houses/) on your lots
5. Let them live

## Import Your Own Saves

```bash
# Uplift a family from your old save
python3 -m simobliterator uplift /path/to/your/Family_1.FAM --output ../../characters/

# Create a neighborhood for them
mkdir -p your-neighborhood/
```

Everyone who played The Sims has an abandoned family somewhere. A USB stick in a drawer. A CD-R in a box. A hard drive from a computer that doesn't exist anymore. Those families have been frozen for a quarter century.

Give them a second chance.
