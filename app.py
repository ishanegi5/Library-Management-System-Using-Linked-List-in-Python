import streamlit as st

# -------------------------
# Data structure: Linked List
# -------------------------
class Node:
    def __init__(self, book_name):
        self.book_name = book_name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, book):
        book = book.strip()
        if not book:
            return "Please provide a valid book name."
        if not self.head:
            self.head = Node(book)
            return f"'{book}' added."
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(book)
        return f"'{book}' added."

    def issue_all(self):
        if not self.head:
            return "No books to issue."
        self.head = None
        return "All books issued."

    def issue_specific(self, book):
        if not self.head:
            return "No books in library."
        if self.head.book_name.lower() == book.lower():
            self.head = self.head.next
            return f"'{book}' issued."
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.book_name.lower() == book.lower():
                prev.next = cur.next
                return f"'{book}' issued."
            prev = cur
            cur = cur.next
        return f"'{book}' not found."

    def search(self, book):
        cur = self.head
        while cur:
            if cur.book_name.lower() == book.lower():
                return True
            cur = cur.next
        return False

    def to_list(self):
        cur = self.head
        books = []
        while cur:
            books.append(cur.book_name)
            cur = cur.next
        return books


# -------------------------
# Streamlit App
# -------------------------
st.set_page_config(page_title="Library System — Isha Negi", page_icon="📚", layout="wide")

st.markdown(
    """
    <div style="display:flex;align-items:center;gap:18px;">
      <div style="font-size:40px;">📚</div>
      <div>
        <h1 style="margin:0;color:#8e44ad;">Library Management System (Linked List)</h1>
        <div style="color: #9aa4ad;">Small DSA-based system — add, search, issue, and visualize books.</div>
      </div>
    </div>
    <hr/>
    """,
    unsafe_allow_html=True,
)

# initialize library in session state
if "library" not in st.session_state:
    st.session_state.library = LinkedList()

lib = st.session_state.library

# TOP DASHBOARD: counters
books_now = lib.to_list()
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.metric("Total books", len(books_now))
with col2:
    next_action = "Empty" if not books_now else books_now[0].title()
    st.metric("Next (head) book", next_action)
with col3:
    st.info("Tip: Use the Add box to add books. Issue by selecting a book from the dropdown to show live updates.")

st.markdown("---")

# Main interactive area: left controls, right live view
left, right = st.columns([1, 1.2])

with left:
    st.subheader("➕ Add Book")
    add_book = st.text_input("Book name", key="add_book_input", placeholder="e.g. Python Crash Course")
    if st.button("Add Book"):
        msg = lib.add(add_book)
        if "added" in msg.lower():
            st.success(msg)
        else:
            st.warning(msg)
        st.rerun()   # <--- updated here

    st.markdown("---")
    st.subheader("🔍 Search Book")
    search_book = st.text_input("Search book name", key="search_input", placeholder="Type a name to search")
    if st.button("Search"):
        if search_book.strip():
            found = lib.search(search_book.strip())
            if found:
                st.success(f"🔎 Yes — '{search_book.strip()}' is available.")
            else:
                st.error(f"❌ '{search_book.strip()}' not found.")
        else:
            st.warning("Please enter a book name to search.")

    st.markdown("---")
    st.subheader("📦 Issue Book")
    books_list = lib.to_list()
    if books_list:
        issue_choice = st.selectbox("Choose a book to issue", options=["-- select a book --"] + [b for b in books_list])
        if st.button("Issue Selected Book"):
            if issue_choice and issue_choice != "-- select a book --":
                res = lib.issue_specific(issue_choice)
                if "issued" in res.lower():
                    st.success(res)
                else:
                    st.error(res)
                st.rerun()   # <--- updated here
            else:
                st.warning("Select a book first.")
        st.write("")  # spacing
        if st.button("Issue All Books"):
            res = lib.issue_all()
            if "issued" in res.lower():
                st.success(res)
            else:
                st.info(res)
            st.rerun()   # <--- updated here
    else:
        st.info("No books available to issue. Add some first.")

with right:
    st.subheader("📚 Current Library (Live)")
    books_now = lib.to_list()
    if books_now:
        for idx, b in enumerate(books_now, start=1):
            st.write(f"**{idx}.** {b.title()}")
        st.markdown("---")
        try:
            import pandas as pd
            df = pd.DataFrame({"Book Name": [b.title() for b in books_now]})
            st.dataframe(df, use_container_width=True)
        except Exception:
            pass
    else:
        st.info("Library is empty. Add books using the left panel.")

    st.markdown("---")
    st.subheader("📋 Quick Demo Inputs (use these to test)")
    st.write("- Python Crash Course") 
    st.write("- C++ Advanced") 
    st.write("- Machine Learning Basics") 
    st.write("- Data Structures & Algorithms")

# FOOTER with your name
st.markdown(
    """
    <hr>
    <div style="text-align:center;color:#9aa4ad;">
      Developed by <b>ISHANEGI</b> | DSA-based Library System using Linked List
    </div>
    """,
    unsafe_allow_html=True,
)
