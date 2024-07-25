import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime
import controller.wbs as wbs


# Design GUI
st.title("WBS Data")

with st.container(border=True) as container:
    if st.session_state.df_wbs is not None:
        # containter for filtering
        with st.container(border=True, height=200) as filter_container:

            if st.session_state.df_wbs is not None:
                # Create checkboxes dynamically
                filter_columns = st.multiselect(
                    "Select columns to filter", st.session_state.df_wbs.columns.tolist()
                )

                filtered_df = st.session_state.df_wbs.copy()

                for column in filter_columns:
                    unique_values = st.session_state.df_wbs[column].unique()
                    selected_values = st.multiselect(
                        f"Select values for {column}", unique_values
                    )
                    if selected_values:
                        filtered_df = filtered_df[
                            filtered_df[column].isin(selected_values)
                        ]

                # Display the filtered dataframe
                st.session_state.filtered_df = filtered_df

        # containter for displaying
        with st.container(border=True, height=500) as data_container:
            if st.session_state.filtered_df is not None:
                st.dataframe(st.session_state.filtered_df)
            else:
                st.dataframe(st.session_state.df_wbs)

        # containter for event handlers
        with st.container(border=True) as event_container:
            st.write("Event handlers")
            col1, col2, col3, col4, col5, col6 = st.columns(
                6,
            )
            if col1.button("Sync-up worklog"):
                st.session_state.df_wbs = wbs.sync_actual_effort_v2()
                st.success("sync-up worklog successful")
                st.rerun()
    else:
        st.text("No data available. Please upload a file in the Upload File section.")
