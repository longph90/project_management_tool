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


def sync_data():

    if 'tasklist_df' in st.session_state and 'timesheet_df' in st.session_state:
        # Sum the effort in the timesheet based on function ID and PIC
        effort_summary = st.session_state['timesheet_df'].groupby(['function_id', 'task','pic'])['effort (h)'].sum().reset_index()
        
        # Merge the effort summary into the task list
        merged_df = st.session_state['tasklist_df'].merge(
            effort_summary,
            how='left',
            left_on=['function_id','task','pic'],
            right_on=['function_id','task' ,'pic']
        )
        
        # Update the actual_effort column in the task list DataFrame
        merged_df['actual_effort(days)'] = merged_df['effort (h)'].fillna(0)
        
        # Drop the intermediate 'effort' column used for merging
        merged_df.drop(columns=['effort (h)'], inplace=True)
        
        st.session_state['tasklist_df'] = merged_df
        st.write("Merged data:")
        st.dataframe(st.session_state['tasklist_df'])
    else:
        st.write("Please upload both WBS and timesheet data to sync.")


def main():
    st.title("Task List and Timesheet Sync")
    data_show = ""

    with st.container():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Show WBS Data"):
                data_show = "Show WBS Data"
        with col2:
            if st.button("Show Timesheet Data"):
                data_show = "Show Timesheet Data"
        with col3:
            if st.button("Sync Data"):
                data_show = "Sync Data"

    with st.container():
        if data_show == "":
            return
        if data_show == "Show WBS Data":
            show_wbs_data()
        if data_show == "Show Timesheet Data":
            show_timesheet_data()
        if data_show == "Sync Data":
            sync_data()        

if __name__ == "__main__":
    main()