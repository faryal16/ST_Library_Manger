import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Page
st.title("📊 Library Dashboard")

if 'books' not in st.session_state or not st.session_state.books:
    st.write("No data available. Add some books to see insights!")
else:
    # Convert books data into DataFrame
    df = pd.DataFrame(st.session_state.books)

    # 📌 Total Books
    total_books = len(df)
    st.metric(label="📚 Total Books", value=total_books)

    # 📌 Pie Chart: Category Distribution
    category_counts = df['category'].value_counts()
    fig_category = px.pie(names=category_counts.index, values=category_counts.values, title="📂 Book Categories")
    st.plotly_chart(fig_category, use_container_width=True)

    # 📌 Bar Chart: Read vs Unread Books
    status_counts = df['status'].value_counts()
    fig_status = px.bar(x=status_counts.index, y=status_counts.values, title="📌 Reading Status", 
                         labels={"x": "Status", "y": "Count"}, color=status_counts.index)
    st.plotly_chart(fig_status, use_container_width=True)
