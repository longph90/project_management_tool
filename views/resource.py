import streamlit as st
import pandas as pd
import openpyxl

st.title("Resource Allocation")


# Function to find idle members
def find_idle_members(members_df, tasks_df):
    # Filter tasks that are currently in "Processing" status
    processing_tasks = tasks_df[tasks_df["Status"] == "Processing"]

    # Convert the 'PIC' column to lowercase for case-insensitive comparison
    processing_resources = processing_tasks["PIC"].str.lower().unique()

    # Identify members whose usernames are not listed as PIC in processing tasks
    idle_members = members_df[
        ~members_df["User Name"].str.lower().isin(processing_resources)
    ]

    return idle_members


# Design GUI
with st.container(border=True) as container:
    columns_to_display = [
        "User Name",
        "Display Name",
        "Job",
        "Seniority",
    ]

    # Display Timesheet file
    if st.session_state.resource_file is not None:
        st.dataframe(st.session_state.df_resource[columns_to_display])

        # Get idle members
        idle_members = find_idle_members(
            st.session_state.df_resource, st.session_state.df_wbs
        )

        # Extract unique User Names
        unique_idle_members = idle_members.drop_duplicates(subset=["User Name"])

        # Display in Streamlit
        st.header("Idle Resource")
        st.dataframe(unique_idle_members[columns_to_display])
    else:
        st.text("No data available. Please upload a file in the Upload File section.")
