import streamlit as st

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
    st.title = "Timesheet data"
    show_timesheet_data()

if __name__ == "__main__":
    main()    