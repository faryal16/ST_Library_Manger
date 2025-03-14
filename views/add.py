import streamlit as st


st.title("➕ Add a New Book")

title = st.text_input("📖 Book Title:")
author = st.text_input("✍️ Author:")
category = st.text_input("📂 Category:")
status = st.radio("📌 Reading Status:", ["Read", "Unread"], index=1)
summary = st.text_area("📄 Book Summary:")

if st.button("✅ Add Book"):
    if title and author and category and summary:
        if 'books' not in st.session_state:
            st.session_state.books = []
        
        st.session_state.books.append({"title": title, "author": author, "category": category, "status": status, "summary": summary})
        st.success(f"📚 '{title}' added successfully!")
    else:
        st.error("⚠️ Please fill in all fields!")
