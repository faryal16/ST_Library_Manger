import streamlit as st
import requests


st.title("🌍 Search Books Online")

query = st.text_input("🔎 Enter book title or author:")
if st.button("🔍 Search") and query:
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(api_url)
    data = response.json()
    
    if "items" in data:
        for item in data["items"][:5]:  # Show top 5 results
            title = item["volumeInfo"].get("title", "Unknown Title")
            authors = ", ".join(item["volumeInfo"].get("authors", ["Unknown Author"]))
            description = item["volumeInfo"].get("description", "No description available.")
            link = item["volumeInfo"].get("previewLink", "#")
            image = item["volumeInfo"].get("imageLinks", {}).get("thumbnail", "")
            
            st.subheader(f"📘 {title}")
            st.write(f"**Author:** {authors}")
            st.write(description[:300] + "...")
            if image:
                st.image(image, width=100)
            st.markdown(f"[📖 Read More]({link})", unsafe_allow_html=True)
            st.write("---")
    else:
        st.error("No books found. Try a different search!")
