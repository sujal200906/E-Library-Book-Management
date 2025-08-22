
# E-Library Book Management (Simple Version)

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.next = None  


class Library:
    def __init__(self):
        self.head = None
        self.history = []  

    def add_book(self, title, author, copies):
        new_book = Book(title, author, copies)
        if not self.head:
            self.head = new_book
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_book
        print(f"Book '{title}' added.\n")

    def show_books(self):
        if not self.head:
            print("No books in library.\n")
            return
        curr = self.head
        while curr:
            print(f"{curr.title} by {curr.author} (Copies: {curr.copies})")
            curr = curr.next
        print()

    def borrow_book(self, title):
        curr = self.head
        while curr:
            if curr.title.lower() == title.lower() and curr.copies > 0:
                curr.copies -= 1
                self.history.append(("borrow", curr))
                print(f"You borrowed '{curr.title}'.\n")
                return
            curr = curr.next
        print("Book not available.\n")

    def return_book(self, title):
        curr = self.head
        while curr:
            if curr.title.lower() == title.lower():
                curr.copies += 1
                self.history.append(("return", curr))
                print(f"You returned '{curr.title}'.\n")
                return
            curr = curr.next
        print("Book not found.\n")

    def search_book(self, keyword):
        curr = self.head
        found = False
        while curr:
            if keyword.lower() in curr.title.lower() or keyword.lower() in curr.author.lower():
                print(f"{curr.title} by {curr.author} (Copies: {curr.copies})")
                found = True
            curr = curr.next
        if not found:
            print("No matching books.\n")
        print()

    def undo(self):
        if not self.history:
            print("Nothing to undo.\n")
            return
        action, book = self.history.pop()
        if action == "borrow":
            book.copies += 1
            print(f"Undo: Returned '{book.title}'.\n")
        elif action == "return":
            book.copies -= 1
            print(f"Undo: Borrowed '{book.title}'.\n")


def main():
    lib = Library()

    while True:
        print("1. Add Book")
        print("2. Show Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Undo Last Action")
        print("7. Exit")
        ch = input("Choose option: ")

        if ch == "1":
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            lib.add_book(title, author, copies)
        elif ch == "2":
            lib.show_books()
        elif ch == "3":
            title = input("Book title to borrow: ")
            lib.borrow_book(title)
        elif ch == "4":
            title = input("Book title to return: ")
            lib.return_book(title)
        elif ch == "5":
            keyword = input("Enter title/author to search: ")
            lib.search_book(keyword)
        elif ch == "6":
            lib.undo()
        elif ch == "7":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
