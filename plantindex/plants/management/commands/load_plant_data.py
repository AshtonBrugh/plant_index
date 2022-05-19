from csv import DictReader

from django.core.management import BaseCommand

from plants.models import Plant


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        if Plant.objects.exists():
            print('Plant data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating new plant data")
        for row in DictReader(open('./plant_spreadsheet_1.csv')):
            plant = Plant()
            plant.name = row['Name']
            plant.genus = row['Genus']
            plant.plant_img = row['Plant_img']
            plant.description = row['Description']
            plant.category = row['Category']
            plant.save()