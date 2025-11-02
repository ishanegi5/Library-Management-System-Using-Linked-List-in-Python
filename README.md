# 📚 Library Management System (Using Linked List in Python)

A **console-based Library Management System** developed in **Python** that demonstrates the practical implementation of **Linked Lists** for managing dynamic data.  
This project allows users to **add books**, **issue (delete) books**, **search for books**, and **display available books** — all performed through simple user inputs.

---

## 🏫 Project Details

- **Project Title:** Library Management System Application (Using Linked List in Python)  
- **Institute Name:** Doon University, Dehradun  
- **Developed By:** Isha Negi  
- **Course:** B.Tech – Computer Science & Engineering (2nd Year)  
- **Language Used:** Python  
- **Data Structure Used:** Linked List  

---

## 🧠 Project Overview

The Library Management System is a simple yet efficient Python console application designed to manage a small library’s book records without the use of databases.  
It uses the **Linked List Data Structure** to dynamically store and update book information.

Each **book** is represented as a **Node**, and the **Linked List** handles all the core operations such as:
- Adding new books  
- Issuing (deleting) books  
- Searching for a specific book  
- Displaying all available books  

---

## ⚙️ Features

✅ Add new books to the library  
✅ Issue (delete) a specific or all books  
✅ Search for any book by name  
✅ Display all available books  
✅ Case-insensitive book name handling  
✅ Exception handling for invalid inputs  
✅ Fully dynamic — no fixed storage size required  

---

## 🧩 Concepts Used

- **Classes and Objects (OOPs)** – for Node and LinkedList structure  
- **Linked List Data Structure** – to store books dynamically  
- **Conditional Statements** – to handle user choices  
- **Loops (while)** – for traversing through the list  
- **Functions (Methods)** – to modularize the logic  
- **Exception Handling (try-except)** – for clean user interaction  
- **Input/Output Handling** – for user-driven actions  

---

## 🧮 Workflow of the Application

1. The program starts and displays a menu with four options:
   - Add a book  
   - Issue a book  
   - Search for a book  
   - Display all books  

2. Based on the user’s input:
   - A new node (book) is added  
   - A node (book) is deleted if issued  
   - The list is traversed to search for a book  
   - The list is displayed with all available books  

3. The program continues in a loop until the user decides to exit.

---

## 💻 Code Structure

```python
class Node():
    def __init__(self, book_name):
        self.book_name = book_name
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self):
        if self.head == None:
            book = input("Enter book name: ")
            self.head = Node(book.lower())
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            book = input("Enter book name: ")
            temp.next = Node(book.lower())

    def issue(self):
        if self.head == None:
            print("There is no book in the library right now!")
        else:
            choice = int(input("Enter\n 1. To issue all books\n 2. To issue a specific book\n"))
            if choice == 1:
                self.head = None
                print("\nAll books have been issued.\n")
            elif choice == 2:
                book = input("Enter the book name you want to issue: ")
                if self.head.book_name == book.lower():
                    self.head = self.head.next
                    print("The book has been issued successfully.")
                else:
                    temp = self.head.next
                    prev = self.head
                    while temp != None and temp.book_name != book.lower():
                        prev = prev.next
                        temp = temp.next
                    if temp == None:
                        print("There is no such book in the library.")
                    else:
                        prev.next = temp.next
                        temp.next = None
                        print("The book has been issued successfully.")
            else:
                print("Invalid choice.")

    def search(self):
        book = input("Enter book name to search: ")
        temp = self.head
        if self.head != None and self.head.book_name == book.lower():
            print("Yes, the book is available in the library.\n")
        elif self.head != None:
            while temp != None and temp.book_name != book.lower():
                temp = temp.next
            if temp != None and temp.book_name == book.lower():
                print("Yes, the book is available in the library.\n")
            else:
                print("The book is not available right now.")
        else:
            print("There are no books in the library right now.")

    def display(self):
        temp = self.head
        i = 0
        if self.head == None:
            print("\nNo books are available in the library.\n")
        while temp != None:
            i += 1
            print(f"{i}. {temp.book_name}")
            temp = temp.next

ll = LinkedList()
while True:
    try:
        user_input = int(input("Enter your choice:\n1. Add\n2. Issue\n3. Search\n4. Display\n"))
        if user_input == 1:
            ll.add()
        elif user_input == 2:
            ll.issue()
        elif user_input == 3:
            ll.search()
        elif user_input == 4:
            ll.display()
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Please enter a valid number.\n")

    cont = input("Enter 'y' to continue or 'n' to stop: ")
    if cont.lower() == 'n':
        break
🧾 Sample Output
Enter your choice:
1. Add
2. Issue
3. Search
4. Display

1
Enter book name: Atomic Habits

1
Enter book name: Python Crash Course

4
1. atomic habits
2. python crash course

3
Enter book name you wanna search: Atomic Habits
Yes the book you searched for is present here.

2
Enter
 1.if you want to take all the books of the library.
 2.if you want to take a specific book from the library
2
Enter book name you wanna issue: Python Crash Course
The book is successfully issued now.
🧩 Future Enhancements

🚀 Add a GUI using Tkinter
🗄️ Integrate with a database like MySQL or SQLite
🔍 Implement Merge Sort to display books in sorted order
🌐 Add a web version using Flask or Django
