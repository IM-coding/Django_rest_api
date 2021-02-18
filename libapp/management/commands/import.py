from django.core.management.base import BaseCommand, CommandError
from libapp.csvimport import CsvImport
import csv

# Base command for importing csv files
class Command(BaseCommand):
    # help
    help = 'Usage: python manage.py import [path/to/BOOKS_file.csv] [path/to/OPINIONS_file.csv]'

    # arguments recieving
    def add_arguments(self, parser):
        parser.add_argument('method', nargs='+', type=str)

    # func for reading files and sending to csvimport script
    def handle(self, *args, **options):
        method = options.get('method')
        # checking correct usage
        if method[0][-4:] != '.csv' or method[1][-4:] != '.csv':
            CommandError('Please provide CSV files')
        self.stdout.write(self.style.SUCCESS(f'{method} import started.'))
        
        book_data = []
        opinion_data = []
        
        # check and read input book file
        try:
            with open(method[0], newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    book_data.append(row)
        except:
            CommandError("It doesn't look like CSV file (Books file)")
        
        # check and read input opinion file
        try:
            with open(method[1], newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    opinion_data.append(row)
        except:
            print("It doesn't look like CSV file (Opinions file), but Books file is ok - processing.")

        # sending data to saving script
        if book_data:
            try:
                CsvImport().insert_books(book_data,)
                self.stdout.write(self.style.SUCCESS(f'{method[0]} loaded to database.'))
            except Exception as e:
                print('Exception while inserting data {}'.format(e))
        
        # sending data to saving script
        if opinion_data:
            try:
                CsvImport().insert_opinions(opinion_data,)
                self.stdout.write(self.style.SUCCESS(f'{method[1]} loaded to database.'))
            except Exception as e:
                print('Exception while inserting data {}'.format(e))
        
        


        
        


        
