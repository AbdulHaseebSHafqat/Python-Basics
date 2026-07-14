# 3. Library Management System ⭐⭐⭐⭐☆
# Features
# Borrow Book
# Return Book


print("==========Library Management System==========")

Books = []
def Add_Book():
    Book_Id = input("Enter the Book id: ")
    for Book in Books:
        if Book["id"] == Book_Id:
            print("Book Already Added")
            return
   
    title = input("Enter the title of Book: ")
    author = input("Enter the author of Book: ")
    category = input("Enter the Category of Book: ")
    publication_year =  int(input("Enter publication Year: "))
    isbn = input("Enter the ISBN of Book: ")
    status =  'Available'
    borrowed_by = ''
    borrow_date =  ''
    BooksBy = {
        'id' : Book_Id,
        'title' : title,
        'author' : author,
        'category' :  category,
        'publication_year' :  publication_year, 
        'isbn' : isbn,
        'status' :  status,
        'borrowed_by' : borrowed_by,
        'borrow_date' : borrow_date
    }
    Books.append(BooksBy)
    print("Books Added Successfully")

def View_Books():
    if len(Books) == 0:
        print("There is no Book")
        return
    for Book in Books:
        print("-" * 60)
        print(f"ID :  {Book['id']}")
        print(f"Title :  {Book['title']}")
        print(f"Author :  {Book['author']}")
        print(f"category :  {Book['category']}")
        print(f"publication_year :  {Book['publication_year']}")
        print(f"isbn :  {Book['isbn']}")
        print(f"status :  {Book['status']}")
        print(f"borrowed_by :  {Book['borrowed_by']}")
        print(f"borrow_date :  {Book['borrow_date']}")
        
        print("-" * 60 )




def Search_Book():
    if len(Books) == 0:
        print("There is no Book")
        return
    Book_id = input("Enter the Book id")
    for Book in Books:
        if Book['id'] == Book_id:
            print(f"ID :  {Book['id']}")
            print(f"Title :  {Book['title']}")
            print(f"Author :  {Book['author']}")
            print(f"category :  {Book['category']}")
            print(f"publication_year :  {Book['publication_year']}")
            print(f"isbn :  {Book['isbn']}")
            print(f"status :  {Book['status']}")
            print(f"borrowed_by :  {Book['borrowed_by']}")
            print(f"borrow_date :  {Book['borrow_date']}")
            print("-" * 80 )
            return
    print("Book Not Found.")


def Borrow_Book():
    if len(Books) == 0:
        print("There is no Book")
        return
    Book_id = input("Enter the Book id")
    for Book in Books:
        if Book['id'] == Book_id:
            if Book["status"] == "Borrowed":
                print("Book is already borrowed.")
                return
            borrower_name = input("Enter Borrower Name: ")
            borrow_date = input("Enter Borrow Date (DD/MM/YYYY): ")

            Book["status"] = "Borrowed"
            Book["borrowed_by"] = borrower_name
            Book["borrow_date"] = borrow_date

            print("Book Borrowed Successfully!")
            return

    print("Book Not Found.")             

            
def Return_Book():
     if len(Books) == 0:
        print("There is no Book")
        return
     Book_id = input("Enter the Book id")
     for Book in Books:
        if Book['id'] == Book_id:
            if Book["status"] == "Available":
                print("Book is already available.")
                return
        
        Book["status"] = "Available"
        Book["borrowed_by"] = ""
        Book["borrow_date"] = ""

        print("Book Returned Successfully!")
        return

print("Book Not Found.")
            


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Add_Book()

    elif choice == "2":
        View_Books()

    elif choice == "3":
        Search_Book()

    elif choice == "4":
        Borrow_Book()

    elif choice == "5":
        Return_Book()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")