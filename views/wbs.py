import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime
import emoji

# Initialize session state for file storage
if "wbs_file" not in st.session_state:
    st.session_state.wbs_file = None
if "timesheet_file" not in st.session_state:
    st.session_state.timesheet_file = None
if "df_wbs" not in st.session_state:
    st.session_state.df_wbs = None


# Function to determine status based on % Completed
def determine_status(value):
    value = value * 100
    if value == 0:
        return f'Not Started {emoji.emojize(":cross_mark:")}'
    elif 0 < value < 90:
        return f'In Progress {emoji.emojize(":desktop_computer:")}'
    elif value == 90:
        return f'Waiting Leader Review {emoji.emojize(":detective:")}'
    elif value == 95:
        return f'Ready to Release {emoji.emojize(":rocket:")}'
    elif value == 100:
        # return f'Released {emoji.emojize(":check_mark_button:")}'
        return f'Released {emoji.emojize(":check_mark_button:")}'


def display_data():
    st.title("WBS Data")

    # Display WBS file
    if st.session_state.wbs_file is not None:
        st.write("WBS File:")
        if st.session_state.timesheet_file is not None:
            if st.button("sync-up actual effort"):
                sync_actual_effort()
                return

        if st.session_state.df_wbs is not None:
            st.write(st.session_state.df_wbs)
        else:
            df_wbs = pd.read_excel(st.session_state.wbs_file)
            df_wbs["note"] = df_wbs["% completed"].apply(determine_status)
            # Format the '% completed' column
            df_wbs["% completed"] = df_wbs["% completed"].apply(
                lambda x: f"{x * 100:.0f}%"
            )
            st.session_state.df_wbs = df_wbs
            st.write(st.session_state.df_wbs)
    else:
        st.write("No WBS file uploaded.")
        if st.button("Download wbs template"):
            st.warning("The feature is developing")

        # Create a dummy DataFrame based on the uploaded image
        data = {
            "function_id": [
                "F001",
                "F001",
                "F001",
                "F001",
                "F002",
                "F002",
                "F002",
                "F002",
            ],
            "task": ["DD", "PCL", "CODE", "UT", "DD", "PCL", "CODE", "UT"],
            "pic": [
                "LongPH5",
                "LongPH5",
                "LongPH5",
                "LongPH5",
                "VuongNV5",
                "VuongNV5",
                "VuongNV5",
                "VuongNV5",
            ],
            "reviewer": [None, None, None, None, None, None, None, None],
            "plan_effort(days)": [1, 1, 1, 1, 1, 1, 1, 1],
            "plan_start": [
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
            ],
            "plan_end": [
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
            ],
            "actual_start": [
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
            ],
            "actual_end": [
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
                datetime(2024, 7, 6),
                datetime(2024, 7, 7),
                datetime(2024, 7, 8),
                datetime(2024, 7, 9),
            ],
            "actual_effort(days)": [None, None, None, None, None, None, None, None],
            "% completed": [1, 1, 1, 0.9, 1, 1, 1, 1],
            "note": [None, None, None, None, None, None, None, None],
        }

        df = pd.DataFrame(data)
        st.dataframe(df)


def sync_actual_effort():

    # Sum the effort in the timesheet based on function ID and PIC
    df_wbs = st.session_state["df_wbs"]
    df_timesheet = pd.read_excel(st.session_state.timesheet_file)
    effort_summary = (
        df_timesheet.groupby(["function_id", "task", "pic"])["effort (h)"]
        .sum()
        .reset_index()
    )

    # Merge the effort summary into the task list
    merged_df = df_wbs.merge(
        effort_summary,
        how="left",
        left_on=["function_id", "task", "pic"],
        right_on=["function_id", "task", "pic"],
    )

    # Update the actual_effort column in the task list DataFrame
    merged_df["actual_effort(days)"] = merged_df["effort (h)"].fillna(0)

    # Drop the intermediate 'effort' column used for merging
    merged_df.drop(columns=["effort (h)"], inplace=True)

    st.session_state["df_wbs"] = merged_df
    st.success("Merge data is completed successfully")
    st.dataframe(st.session_state["df_wbs"])


display_data()
