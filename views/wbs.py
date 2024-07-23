import streamlit as st
import pandas as pd

def show_wbs_data():
    if 'tasklist_df' in st.session_state:
        st.dataframe(st.session_state['tasklist_df'])
    else:
        st.write("No WBS data available. Please upload a file in the Upload File section.")

def show_timesheet_data():
    if 'timesheet_df' in st.session_state:
        st.dataframe(st.session_state['timesheet_df'])
    else:
        st.write("No timesheet data available. Please upload a file in the Upload File section.")

def main():
    st.title = "WBS data"
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df)
    else:
        st.write("Please upload an Excel file.")


if __name__ == "__main__":
    main()    


