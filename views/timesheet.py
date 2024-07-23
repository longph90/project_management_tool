import streamlit as st
import pandas as pd
import openpyxl

# Initialize session state for file storage
if 'wbs_file' not in st.session_state:
    st.session_state.wbs_file = None
if 'timesheet_file' not in st.session_state:
    st.session_state.timesheet_file = None

def display_data():
    st.title("Timesheet Data")
    
    # Display Timesheet file
    if st.session_state.timesheet_file is not None:
        st.write("Timesheet File:")
        df_timesheet = pd.read_excel(st.session_state.timesheet_file)
        st.write(df_timesheet)
    else:
        st.write("No Timesheet file uploaded.") 

display_data()        