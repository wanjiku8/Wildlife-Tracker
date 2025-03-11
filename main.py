import click
from datetime import datetime
from models import Animal, Sighting
from database import SessionLocal, engine, Base

# Ensure tables are created
Base.metadata.create_all(bind=engine)

db = SessionLocal()

@click.group()
def cli():
    """Wildlife Tracker CLI"""
    pass

@cli.command()
@click.option("--species", prompt="Species", help="Species of the animal")
@click.option("--habitat", prompt="Habitat", help="Habitat of the animal")
@click.option("--population", prompt="Population", help="Population of the animal")
def add_animal(species, habitat, population):
    """Add a new animal to the database."""
    animal = Animal(species=species, habitat=habitat, population=int(population))
    db.add(animal)
    db.commit()
    click.echo(f"Added {species} to the database.")

@cli.command()
def list_animals():
    """List all animals in the database."""
    animals = db.query(Animal).all()
    for animal in animals:
        click.echo(f"ID: {animal.id}, Species: {animal.species}, Habitat: {animal.habitat}, Population: {animal.population}")

@cli.command()
@click.option("--location", prompt="Location", help="Location of the sighting")
@click.option("--time", prompt="Time (YYYY-MM-DD HH:MM:SS)", help="Time of the sighting")
@click.option("--observer", prompt="Observer", help="Name of the observer")
@click.option("--animal_id", prompt="Animal ID", help="ID of the animal sighted")
def track_sighting(location, time, observer, animal_id):
    """Track a new sighting."""
    sighting = Sighting(
        location=location,
        time=datetime.strptime(time, "%Y-%m-%d %H:%M:%S"),
        observer=observer,
        animal_id=int(animal_id)
    )
    db.add(sighting)
    db.commit()
    click.echo(f"Added sighting of animal ID {animal_id} at {location}.")

@cli.command()
@click.option("--habitat", prompt="Habitat", help="Habitat to search for")
def find_by_habitat(habitat):
    """Find animals by habitat."""
    animals = db.query(Animal).filter(Animal.habitat == habitat).all()
    for animal in animals:
        click.echo(f"ID: {animal.id}, Species: {animal.species}, Habitat: {animal.habitat}, Population: {animal.population}")

@cli.command()
@click.option("--animal_id", prompt="Animal ID", help="ID of the animal to delete")
def delete_animal(animal_id):
    """Delete an animal record."""
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if animal:
        db.delete(animal)
        db.commit()
        click.echo(f"Deleted animal ID {animal_id}.")
    else:
        click.echo(f"Animal ID {animal_id} not found.")

if __name__ == "__main__":
    cli()