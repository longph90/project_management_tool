import streamlit as st
import pandas as pd
import openpyxl

# Initialize session state for file storage
if "member_file" not in st.session_state:
    st.session_state.member_file = None


def display_data():
    st.title("List Member")

    # Display Timesheet file
    if st.session_state.member_file is not None:
        st.write("Member File:")
        df_members = pd.read_excel(st.session_state.member_file)
        st.dataframe(df_members)
    else:
        st.write("No Member file uploaded.")


display_data()
