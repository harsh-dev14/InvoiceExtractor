import streamlit as st

def login():
    admin_password="InvoiceExtractor"
    st.header("Log In")
    role=st.selectbox("Choose your role",Roles)
    password=""

    if role=="Admin":
        password=st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        if role=="Admin":
            if password == admin_password: 
                st.session_state.role = role
                st.rerun()  
            else:
                st.error("Invalid Admin Password")
        else:
            st.session_state.role=role
            st.rerun()

def logout():
    st.session_state.role=None
    st.rerun()

Roles=[None, "User","Admin"]

if "role" not in st.session_state:
    st.session_state.role = None

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
user = st.Page(
    "request/request.py",
    title="User",
    icon=":material/help:",
    default=(role == "User"),
)

admin = st.Page(
    "admin/admin.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)

account_pages = [logout_page, settings]
request_pages = [user]
admin_pages = [admin]

st.title("Invoice Extractor using Google Gemini")
st.logo("images/logo.png", icon_image="images/logo.png")

page_dict = {}
if st.session_state.role in ["User", "Admin"]:
    page_dict["User"] = request_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()