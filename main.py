import streamlit as st
import json

# Page settings
# Material Icons: https://fonts.google.com/icons

# Initialize session state for file storage
# Session for file upload
if "upload_files" not in st.session_state:
    st.session_state.upload_files = None
if "wbs_file" not in st.session_state:
    st.session_state.wbs_file = None
if "timesheet_file" not in st.session_state:
    st.session_state.timesheet_file = None
if "resource_file" not in st.session_state:
    st.session_state.resource_file = None

# Session for DataFrame storage
if "df_wbs" not in st.session_state:
    st.session_state.df_wbs = None
if "df_timesheet" not in st.session_state:
    st.session_state.df_timesheet = None
if "df_filtered" not in st.session_state:
    st.session_state.df_filtered = None
if "df_resource" not in st.session_state:
    st.session_state.df_resource = None

# ------------------ Streamlit UI Configuration ------------------ #
st.set_page_config(
    page_title="SPM",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ Sidebar ------------------ #
with st.sidebar:
    st.markdown("Welcome to the project management app!")
    st.markdown("Created by [Long Phan]")
    st.markdown("""---""")

# Add "FAQs" section to the sidebar

about_page = st.Page(
    title="About Me",
    icon=":material/account_circle:",
    page="views/about_me.py",
)

dashboard_page = st.Page(
    title="Dashboard",
    icon=":material/bar_chart:",
    page="views/dashboard.py",
)

estimations_page = st.Page(
    title="Estimation",
    icon=":material/calculate:",
    page="views/estimations.py",
)

wbs_page = st.Page(
    title="WBS",
    icon=":material/task:",
    page="views/wbs.py",
)

timesheet_page = st.Page(
    title="Timesheet",
    icon=":material/timer:",
    page="views/timesheet.py",
)

sync_page = st.Page(
    title="Sync Data",
    icon=":material/timer:",
    page="views/sync_data.py",
)

chat_page = st.Page(
    title="Chat with assistant",
    icon=":material/smart_toy:",
    page="views/chatbot.py",
)

page_test = st.Page(
    title="Page Tests",
    icon=":material/quiz:",
    page="views/page_test.py",
)


resource_page = st.Page(
    title="Resources",
    icon=":material/person:",
    page="views/resource.py",
)
upload_page = st.Page(
    title="Template - Upload Files",
    icon=":material/manufacturing:",
    page="views/upload_files.py",
    default=True,
)
faq_page = st.Page(
    title="FAQ",
    icon=":material/person:",
    page="views/faq.py",
)

# Load the selected page
pg = st.navigation(
    pages=[
        about_page,
        dashboard_page,
        estimations_page,
        wbs_page,
        timesheet_page,
        # sync_page,
        # chat_page,
        # page_test,
        resource_page,
        upload_page,
        faq_page,
    ]
)

pg.run()
