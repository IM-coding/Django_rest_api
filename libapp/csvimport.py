from libapp.models import Book, Opinion

""" Importing script """

class CsvImport:
    
    #  Populating books table
    def insert_books(self, books):
        
        #  Check format of input data from csv
        if books[0][1] != 'Tytuł' or books[0][2] != 'Autor' or books[0][3] != 'Gatunek':
            raise Exception ('Wrong format of input data [ISBN;Tytuł;Autor;Gatunek;]')
        

        for i in range(1, len(books)):

            # ISBN no could be 10 or 13 digits only
            if len(books[i][0]) != 10 and len(books[i][0]) != 13:
                print('Wrong ISBN no, should be 10 or 13: {}'.format(books[i][0]))
                continue

            # get_or_create to avoid duplicating data
            try: 
                Book.objects.get_or_create(
                    isbn = books[i][0], 
                    title = books[i][1],
                    author = books[i][2],
                    book_type = books[i][3],
                    )
            except:
                #TODO: uniqueness violation check (string format, language, )
                print('Warning! Book with ISBN {} already in DB: {} with different data'.format(books[i][0],books[i]))

    #  Populating opinions table
    def insert_opinions(self, opinions):

        #  Check format of input data from csv
        if opinions[0][1] != 'Ocena' or opinions[0][2] != 'Opis':
            raise Exception ('Wrong format of input data [ISNB;Ocena;Opis;]')

        for i in range(1, len(opinions)):
            # checking for book in database
            try: 
                bres = Book.objects.get(isbn=opinions[i][0])
            except:
                print('Sorry, there is no book with ISBN {} in DB.')
                continue
            
            # get_or_create will raise exception if duplicated data
            try: 
                Opinion.objects.get_or_create(
                    book = bres, 
                    rating = opinions[i][1],
                    description = opinions[i][2],
                    )
            except:
                print('Warning! Duplicated opinion: {}'.format(opinions[i]))
                #TODO: handle duplicates: debuging
                """ 
                res = Opinion.objects.filter(
                    book = bres, 
                    rating = opinions[i][1],
                    description = opinions[i][2],
                )
                tmp = res.first().pk
                res = res.exclude(pk=tmp)
                res.delete()
                """

