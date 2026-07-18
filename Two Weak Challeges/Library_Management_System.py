# 3. Library Management System ⭐⭐⭐⭐☆
# Features
# Borrow Book
# Return Book


Books = []
def Add_Book():
    print("\n➕ ----- Add Book -----")
    book_id = input("🆔 Enter Book ID: ")
    for Book in Books:
        if Book["id"] == book_id:
            print("❌ Book ID already exists.")
            return
   
    title = input("📖 Enter Book Title: ")
    author = input("✍️ Enter Author Name: ")
    category = input("📂 Enter Category: ")
    publication_year = int(input("📅 Enter Publication Year: "))
    isbn = input("🔢 Enter ISBN: ")
    status =  'Available'
    borrowed_by = ''
    borrow_date =  ''
    BooksBy = {
        'id' : book_id,
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
    print("✅ Book added successfully.")

def View_Books():
    print("\n📚 ----- Library Books -----")
    if len(Books) == 0:
        print("❌ No books available.")
        return
    for book in Books:
        print("-" * 60)
        print(f"🆔 Book ID          :        {book['id']}")
        print(f"📖 Title            :        {book['title']}")
        print(f"✍️  Author           :        {book['author']}")
        print(f"📂 Category         :        {book['category']}")
        print(f"📅 Publication Year :        {book['publication_year']}")
        print(f"🔢 ISBN             :        {book['isbn']}")
        print(f"📌 Status           :        {book['status']}")
        print(f"👤 Borrowed By      :        {book['borrowed_by']}")
        print(f"📆 Borrow Date      :        {book['borrow_date']}")
        print("-" * 60 )


def Search_Book():
    print("\n🔍 ----- Search Book -----")
    if len(Books) == 0:
        print("❌ No books available.")
        return
    Book_id = input("Enter the Book id: ")
    for Book in Books:
        if Book['id'] == Book_id:
            print(f"ID                  :  {Book['id']}")
            print(f"Title               :  {Book['title']}")
            print(f"Author              :  {Book['author']}")
            print(f"category            :  {Book['category']}")
            print(f"publication_year    :  {Book['publication_year']}")
            print(f"isbn                :  {Book['isbn']}")
            print(f"status              :  {Book['status']}")
            print(f"borrowed_by         :  {Book['borrowed_by']}")
            print(f"borrow_date         :  {Book['borrow_date']}")
            print("-" * 80 )
            return
    print("❌ Book not found.")


def Borrow_Book():
    print("\n📥 ----- Borrow Book -----")
    if len(Books) == 0:
        print("❌ No books available.")
        return
    Book_id = input("Enter the Book id: ")
    for Book in Books:
        if Book['id'] == Book_id:
            if Book["status"] == "Borrowed":
                print("⚠️ Book is already borrowed.")
                return
            borrower_name = input("👤 Enter Borrower Name: ")
            borrow_date = input("📅 Enter Borrow Date (DD/MM/YYYY): ")

            Book["status"] = "Borrowed"
            Book["borrowed_by"] = borrower_name
            Book["borrow_date"] = borrow_date

            print("✅ Book borrowed successfully.")
            return

    print("❌ Book not found.")

            
def Return_Book():
    print("\n📤 ----- Return Book -----")
    if len(Books) == 0:
        print("❌ No books available.")
        return
    Book_id = input("Enter the Book id: ")
    for book in Books:
        if book['id'] == Book_id:
            if book["status"] == "Available":
                print("ℹ️ Book is already available.")
                return
        
            book["status"] = "Available"
            book["borrowed_by"] = ""
            book["borrow_date"] = ""

            print("✅ Book returned successfully.")
            return

    print("❌ Book not found.")
            


while True:
    print("""
==================================================
📚        LIBRARY MANAGEMENT SYSTEM
==================================================

1️⃣ ➕ Add Book
2️⃣ 📚 View Books
3️⃣ 🔍 Search Book
4️⃣ 📥 Borrow Book
5️⃣ 📤 Return Book
6️⃣ 🚪 Exit

==================================================
""")




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
        print("=" * 60)
        print("🙏 Thank you for using Library Management System.")
        print("💻 Developed by Abdul Haseeb")
        print("🌟 Keep Learning, Keep Coding!")
        print("=" * 60) 
        break

    else:
        print("Invalid Choice!")