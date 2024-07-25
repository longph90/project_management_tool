import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

st.title("Timesheet Data")

with st.container(border=True):
    # Display Timesheet file
    if st.session_state.timesheet_file is not None:
        st.write(st.session_state.df_timesheet)

        st.title("Summary:")

        grouped_user = st.session_state.df_timesheet.groupby(["User"]).sum(
            numeric_only=True
        )
        grouped_tow = st.session_state.df_timesheet.groupby(["Type Of Work"]).sum(
            numeric_only=True
        )

        with st.container(border=True):
            col1, col2 = st.columns(2, vertical_alignment="bottom")
            with col1:
                st.subheader("Grouped by User:")
                st.dataframe(grouped_user)
            with col2:
                st.subheader("Grouped by Type of Work:")
                st.dataframe(grouped_tow)

        with st.container(border=True):
            col1, col2 = st.columns(2, vertical_alignment="bottom")
            with col1:
                st.subheader("Worked Hours")
                st.bar_chart(data=grouped_user, horizontal=True, y="Worked(h)")

            with col2:
                st.subheader("Type of Work")
                sum_worklog = grouped_tow.sum(numeric_only=True)
                grouped_tow["Worked(%)"] = (
                    (grouped_tow["Worked(h)"]) / sum_worklog["Worked(h)"] * 100
                )
                st.bar_chart(
                    grouped_tow,
                    horizontal=False,
                    y="Worked(%)",
                )
    else:
        st.text("No data available. Please upload a file in the Upload File section.")
