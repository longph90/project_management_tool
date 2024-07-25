import streamlit as st
import pandas as pd
import emoji


def write_session():
    st.write(st.session_state)


# Function to determine status based on % Completed
def determine_status(value):
    value = value * 100
    if value == 0:
        return f"Open"
    elif 0 < value < 80:
        return f"In-Progress"
    elif value == 80:
        return f"In-Review"
    elif value == 90:
        return f"Completed"
    elif value == 95:
        return f"Released"
    elif value == 100:
        return f"Closed"
    else:
        return "Unknown"


def load_data_wbs():
    if "wbs_file" in st.session_state:
        df_wbs = pd.read_excel(st.session_state.wbs_file)
        df_wbs["Due Date"] = pd.to_datetime(df_wbs["Due Date"], errors="coerce")
        df_wbs["Start_Create"] = pd.to_datetime(df_wbs["Start_Create"], errors="coerce")
        df_wbs["End_Create"] = pd.to_datetime(df_wbs["End_Create"], errors="coerce")
        df_wbs["Start_Review"] = pd.to_datetime(df_wbs["Start_Review"], errors="coerce")
        df_wbs["Release_Date"] = pd.to_datetime(df_wbs["Release_Date"], errors="coerce")
        df_wbs["Closed_Date"] = pd.to_datetime(df_wbs["Closed_Date"], errors="coerce")

        df_wbs["Status"] = df_wbs["%completed"].apply(determine_status)
        # Format the '% completed' column
        df_wbs["%completed"] = df_wbs["%completed"].apply(lambda x: f"{x * 100:.0f}%")
        return df_wbs


def sync_actual_effort():
    if "wbs_file" in st.session_state and "timesheet_file" in st.session_state:
        # Sum the effort in the timesheet based on function ID and PIC
        df_wbs = pd.read_excel(st.session_state.wbs_file)
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
        return merged_df


def sync_actual_effort_v2():
    if "wbs_file" in st.session_state and "timesheet_file" in st.session_state:
        # Sum the effort in the timesheet based on function ID and PIC
        effort_summary = (
            st.session_state.df_timesheet.groupby(["Key"])["Worked(h)"]
            .sum()
            .reset_index()
        )

        # Merge the effort summary into the task list
        merged_df = st.session_state.df_wbs.merge(
            effort_summary,
            how="left",
            left_on=["Internal_ID"],
            right_on=["Key"],
        )

        # Update the actual_effort column in the task list DataFrame
        merged_df["actual_effort(days)"] = merged_df["Worked(h)"].fillna(0)

        # Drop the intermediate 'effort' column used for merging
        merged_df.drop(columns=["Key", "Worked(h)"], inplace=True)
        return merged_df
