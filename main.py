import streamlit as st

# Page settings
# Material Icons: https://fonts.google.com/icons

about_page = st.Page(
    title="About Me",
    icon=":material/account_circle:",
    page="views/about_me.py",
    default=True,
)

estimations_page = st.Page(
    title="Effort Estimation",
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

config_page = st.Page(
    title="Config Settings",
    icon=":material/manufacturing:",
    page="views/config.py",
)

member_page = st.Page(
    title="Member List",
    icon=":material/person:",
    page="views/members.py",
)

# Navigation bar
pg = st.navigation(
    pages=[
        about_page,
        estimations_page,
        wbs_page,
        timesheet_page,
        # sync_page,
        # chat_page,
        # page_test,
        member_page,
        config_page,
    ]
)


# Shared all pages
st.sidebar.title("Navigation")
st.sidebar.header("Project Management")
st.sidebar.markdown("Welcome to the project management app!")
st.sidebar.markdown("---")
st.sidebar.text("Made with by Long Phan")

pg.run()
