import streamlit as st
import pandas as pd

# Initialize session state for file storage
if "wbs_file" not in st.session_state:
    st.session_state.wbs_file = None
if "timesheet_file" not in st.session_state:
    st.session_state.timesheet_file = None


# Define the pages
def upload_page():
    st.title("Upload Files")

    # File uploader for WBS
    wbs_file = st.file_uploader(
        "Upload WBS Excel file", type=["xlsx"], key="wbs_uploader"
    )
    if wbs_file is not None:
        st.session_state.wbs_file = wbs_file
        st.success("WBS file uploaded successfully!")

    # File uploader for Timesheet
    timesheet_file = st.file_uploader(
        "Upload Timesheet Excel file", type=["xlsx"], key="timesheet_uploader"
    )
    if timesheet_file is not None:
        st.session_state.timesheet_file = timesheet_file
        st.success("Timesheet file uploaded successfully!")

    # File uploader for Members
    member_file = st.file_uploader(
        "Upload Members Excel file", type=["xlsx"], key="member_uploader"
    )
    if member_file is not None:
        st.session_state.member_file = member_file
        st.success("Members file uploaded successfully!")


upload_page()
