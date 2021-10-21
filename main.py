from rethinkdb import r
import pandas as pd

pd.set_option('display.max_columns', None)

def research_book_by(value, filter):
    lBOOk = []
    cursor = r.table("Books").filter(r.row[filter] == value).run()
    for document in cursor:
        lBOOk.append(document)
    if len(lBOOk)==0:
        print("Book not found\nHere are some suggestions :\n")
        for elem in r.table('Books').filter({'availablity': 'available'}).pluck(filter).sample(3).run() :
            print(elem)
        new_value = input("Which one do you want? ")
        return research_book_by(new_value, filter)
    elif len(lBOOk)>1:
        print("More than one book found")
        dframe = pd.DataFrame(lBOOk)
        print(dframe)
        id_book = input("Copy/Past the id of the desired book : ")
        return id_book
    else :
        print("This book was found.")
        dframe = pd.DataFrame(lBOOk)
        print(dframe)
        return dframe['id'].values[0]
        
def filter_manager(filter):
    print("Here is some suggestions")
    for elem in r.table('Books').filter({'availablity': 'available'}).pluck(filter).sample(3).run() :
        print(elem)
    author_wanted = input("write the desired "+filter)
    id_book = research_book_by(author_wanted, filter)
    if id_book != None :
        if (input("Are you sure you want to make it unavailable?(y/n)\n").lower() == 'y'):
            r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "unavailable"}).run()
            print("Book succesfully rented")

if __name__ == "__main__":
    r.connect('localhost', 28015).repl()
    #faire suggestion de livre
    choice = input("\nChoose an operation :\nR - Rent a book\nT - Return a book\nS - Search for a book\nN - None\nYour choice : ")
    if choice == "R":
        title_book = input("\nWhat is the title of the book you want to rent?")
        id_book = research_book_by(title_book, 'title')
        if id_book != None :
            if (input("Are you sure you want to make it unavailable?(y/n)\n").lower() == 'y'):
                r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "unavailable"}).run()
                print("Book succesfully rented")
    elif choice == "T":
        title_book = input("\nWhat is the title of the book you want to rent?")
        id_book = research_book_by(title_book, 'title')
        if id_book != None :
            if (input("Are you sure you want to make it available?(y/n)\n").lower() == 'y'):
                r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "available"}).run()
                print("Book succesfully returned")
    elif choice == "S":
        filter_wanted = input("\nChoose a filter :\nA - By author\nT - By title\nY - By year\nP - By period\nL - By language\nN - None\nYour choice : ")
        if filter_wanted == "A":
            filter_manager('author')
        elif filter_wanted == "T":
            filter_manager('title')
        elif filter_wanted == "L":
            filter_manager('language')
        elif filter_wanted == "Y":
            print("Here is some suggestions")
            for elem in r.table('Books').filter({'availablity': 'available'}).pluck('year').sample(3).run() :
                print(elem)
            year_wanted = int(input("write the desired year :"))
            id_book = research_book_by(year_wanted, 'year')
            if id_book != None :
                if (input("Are you sure you want to make it unavailable?(y/n)\n").lower() == 'y'):
                    r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "unavailable"}).run()
                    print("Book succesfully rented")
        elif filter_wanted == "P":
            year_start = int(input("Write the starting year of the period: "))
            year_end = int(input("Write the ending year of the period: "))
            lBOOk = []
            cursor = r.table("Books").filter((r.row["year"] > year_start) & (r.row["year"] < year_end)).run()
            for document in cursor:
                lBOOk.append(document)
            if len(lBOOk)==0:
                print("Book not found")
            elif len(lBOOk)>1:
                print("More than one book found")
                dframe = pd.DataFrame(lBOOk)
                print(dframe)
                id_book = input("Copy/Past the id of the desired book : ")
                if (input("Are you sure you want to make it unavailable?(y/n)\n").lower() == 'y'):
                    r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "unavailable"}).run()
                    print("Book succesfully rented")
            else :
                print("This book was found.")
                dframe = pd.DataFrame(lBOOk)
                print(dframe)
                id_book = dframe['id'].values[0]
                if (input("Are you sure you want to make it unavailable?(y/n)\n").lower() == 'y'):
                    r.table("Books").filter(r.row['id'] == id_book).update({"availablity": "unavailable"}).run()
                    print("Book succesfully rented")