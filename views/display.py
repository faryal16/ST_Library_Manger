import streamlit as st

st.title("📖 Your Book Collection")

# Initialize book list if not already in session state
if 'books' not in st.session_state:
    st.session_state.books = [
        {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help", "status": "Read", "summary": "A practical guide to building good habits and breaking bad ones."},
        {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "category": "Programming", "status": "Unread", "summary": "A classic book on software craftsmanship and best practices."},
        {"title": "Deep Work", "author": "Cal Newport", "category": "Productivity", "status": "Read", "summary": "A book about mastering focus in a distracted world."},
        {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming", "status": "Unread", "summary": "Guidelines for writing maintainable and efficient code."},
        {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "category": "Finance", "status": "Read", "summary": "A book that challenges the way people think about money and investing."},
        {"title": "The Psychology of Money", "author": "Morgan Housel", "category": "Finance", "status": "Unread", "summary": "Timeless lessons on wealth, greed, and happiness."},
        {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Psychology", "status": "Read", "summary": "Explores the two systems that drive how we think and make decisions."},
        {"title": "The Art of War", "author": "Sun Tzu", "category": "Strategy", "status": "Unread", "summary": "Ancient wisdom on strategy, leadership, and warfare."},
        {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction", "status": "Read", "summary": "A mystical journey of a shepherd in search of his personal legend."},
        {"title": "The 4-Hour Workweek", "author": "Tim Ferriss", "category": "Productivity", "status": "Unread", "summary": "Escape the 9-5, live anywhere, and join the new rich."},
        {"title": "1984", "author": "George Orwell", "category": "Fiction", "status": "Read", "summary": "A dystopian novel on surveillance, freedom, and power."},
        {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History", "status": "Unread", "summary": "The history of human civilization from prehistoric times to today."},
        {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "category": "Self-Help", "status": "Read", "summary": "A counterintuitive approach to living a good life."}
    ]

# Display message if no books exist
if not st.session_state.books:
    st.write("No books available. Add some!")
else:
    # Filters for category and status
    category_filter = st.selectbox("📂 Filter by category:", ["All"] + sorted(set(b['category'] for b in st.session_state.books)))
    status_filter = st.selectbox("📌 Filter by status:", ["All", "Read", "Unread"])
    
    # Filtered book list
    filtered_books = [b for b in st.session_state.books 
                      if (category_filter == "All" or b['category'] == category_filter) and
                         (status_filter == "All" or b['status'] == status_filter)]
    
    # Book selection dropdown
    if filtered_books:
        selected_book = st.selectbox("📖 Select a book to view details:", [b['title'] for b in filtered_books])
        book_details = next((b for b in filtered_books if b['title'] == selected_book), None)
        
        # Display book details
        if book_details:
            st.subheader(f"📘 {book_details['title']}")
            st.write(f"**Author:** {book_details['author']}")
            st.write(f"**Category:** {book_details['category']}")
            st.write(f"**Status:** {book_details['status']}")
            st.info(f"📄 **Summary:** {book_details['summary']}")
    else:
        st.warning("No books match your selected filters.")
