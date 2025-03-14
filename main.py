import streamlit as st

# ______Page Seup
about_page = st.Page(
    page="views/about.py",
    title="Personal Liabrary!!",
    icon="📝",
    default=True
)

project_1_page=st.Page(
    page="views/display.py",
    title="Books Collection",
    icon="📚"
    
)
project_2_page=st.Page(
    page="views/search.py",
    title="Search Books",
    icon="🔍"
    
)
project_3_page = st.Page(
    page="views/add.py",
    title="Add Books",
    icon="➕"
)
project_4_page = st.Page(
    page="views/remove.py",
    title="Remove Books",
    icon="🗑️",
)


project_5_page=st.Page(
    page="views/dashboard.py",
    title="Liabrary Dashboard",
    icon="📊",
)

# ___ Navigation Setup [Without Sections]
# pg =st.navigation(pages=[about_page, project_1_page, project_2_page])

## ___ Navigation Setup [With Sections]
pg=st.navigation(
    {
        
        "info": [about_page],
        "Projects":[project_1_page, project_2_page, project_3_page,project_4_page,project_5_page]
    }
)

# sidebar_logo = st.selectbox("Code With Fairy🍃")
# ___ Shared on Alll pages

# Custom logo styling at the top

st.sidebar.text("Made With ❤ by Fairy")

# Run Navigations
pg.run()
