import streamlit as st


st.title("❌ Remove a Book")

if 'books' not in st.session_state or not st.session_state.books:
    st.write("No books to remove.")
    

book_titles = [b['title'] for b in st.session_state.books]
selected_book = st.selectbox("📖 Select a book to remove:", book_titles)

if st.button("🗑️ Remove Book"):
    st.session_state.books = [b for b in st.session_state.books if b['title'] != selected_book]
    st.success(f"🗑️ '{selected_book}' removed successfully!")
