import streamlit as st


# App Title
st.title("📚 Personal Library Manager")
st.subheader("Your Smart Digital Bookshelf!")

# 📖 Introduction
st.write(
    """
    Welcome to **Personal Library Manager** – your go-to app for organizing, tracking, and discovering books effortlessly! 📖  
    Whether you're an avid reader, a student, or just someone who wants to keep track of their books, this app is designed to help you manage your personal collection efficiently.
    
    ### ✨ **What You Can Do?**
    - 📌 **Store & Organize**: Keep all your books in one place.
    - 🔍 **Search Books Online**: Find new reads with detailed summaries.
    - ➕ **Add Books**: Manually enter books to your collection.
    - 🗑️ **Remove Books**: Declutter by removing unwanted books.
    - 📊 **Analyze Your Reading Habits**: Track your progress and visualize data.
    """
)

# 📚 **Why Use a Digital Library? (Benefits)**
st.markdown("## 🌟 Why Manage Your Books Digitally?")
st.write(
    """
    - ✅ **Never Forget a Book**: Keep track of what you've read or want to read.  
    - ✅ **Easier Access**: Search and filter books instantly.  
    - ✅ **Better Organization**: Categorize books by genre, author, or status.  
    - ✅ **Track Your Reading Progress**: See how much you've read over time.  
    - ✅ **Discover New Reads**: Get book recommendations and online searches.  
    """
)

# 📌 Feature Overview (Using Columns)
st.markdown("## 🚀 Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📚 Manage Your Books")
    st.image("assets/books_managerr.png", use_container_width=True)
    st.write("Easily add, view, and remove books from your collection.")

with col2:
    st.markdown("### 🔍 Search for Books")
    st.image("assets/search.png", use_container_width=True)
    st.write("Find new books online and get their details instantly.")

with col3:
    st.markdown("### 📊 View Insights")
    st.image("assets/dashboard.png", use_container_width=True)
    st.write("Analyze your reading trends using an interactive dashboard.")

# 💡 Call to Action
st.success("📌 **Start managing your books today!** Use the sidebar to navigate different features and explore your digital library.")
