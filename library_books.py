 #Library 

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = [
            Book("The Pragmatic Programmer", "Andrew Hunt", 1999),
            Book("Clean Code", "Robert C. Martin", 2008),
            Book("Automate the Boring Stuff", "Al Sweigart", 2015),
        ]

    def list_books(self):
        if not self.books:
            print("\nNo books in library.")
            return
        print("\n--- Library Books ---")
        for i, b in enumerate(self.books, 1):
            print(f"{i}. {b.title} — {b.author} ({b.year})")

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))
        print("Book added.")

    def remove_book(self, number):
        idx = number - 1
        if 0 <= idx < len(self.books):
            removed = self.books.pop(idx)
            print(f"Removed: {removed.title}")
        else:
            print("Invalid number.")

    def search_title(self, text):
        text = text.lower()
        results = [b for b in self.books if text in b.title.lower()]
        if not results:
            print("No matches.")
            return
        print("\nMatches:")
        for b in results:
            print(f"- {b.title} — {b.author} ({b.year})")

# ---------- Main ----------
lib = Library()

while True:
    print("\n1) List books")
    print("2) Add book")
    print("3) Remove book")
    print("4) Search by title")
    print("5) Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        title = input("Title: ")
        author = input("Author: ")
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Year must be a number.")
            continue
        lib.add_book(title, author, year)
    elif choice == "3":
        lib.list_books()
        try:
            n = int(input("Enter book number to remove: "))
        except ValueError:
            print("Enter a number.")
            continue
        lib.remove_book(n)
    elif choice == "4":
        q = input("Search text: ")
        lib.search_title(q)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
