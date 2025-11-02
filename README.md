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
