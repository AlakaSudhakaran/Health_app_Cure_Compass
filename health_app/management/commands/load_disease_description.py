# management/commands/load_disease_descriptions.py
import pandas as pd
from django.core.management.base import BaseCommand
from health_app.models import DiseaseDescription

class Command(BaseCommand):
    help = 'Load disease descriptions from an Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the Excel file
        file_path = 'health_app\description.csv'
        df = pd.read_csv(file_path)

        # Iterate over the rows and save to the database
        for index, row in df.iterrows():
            DiseaseDescription.objects.update_or_create(
                disease_name=row['Disease'],
                defaults={'description': row['Description']}
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded disease descriptions'))
