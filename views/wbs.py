import streamlit as st
import pandas as pd
import openpyxl

# Initialize session state for file storage
if 'wbs_file' not in st.session_state:
    st.session_state.wbs_file = None
if 'timesheet_file' not in st.session_state:
    st.session_state.timesheet_file = None
    
def display_data():
    st.title("WBS Data")
    
    # Display WBS file
    if st.session_state.wbs_file is not None:
        st.write("WBS File:")
        df_wbs = pd.read_excel(st.session_state.wbs_file)
        st.write(df_wbs)
    else:
        st.write("No WBS file uploaded.")


display_data()


