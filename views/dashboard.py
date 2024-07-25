import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from datetime import datetime, timedelta

# Initialize session state for file storage
st.title("Dashboard")

with st.container(border=True):
    # Load the data
    if st.session_state.df_wbs is not None:
        data = st.session_state.df_wbs

        # Remove rows where the status is "Unknown"
        data = data[data["Status"] != "Unknown"]

        expected_status = [
            "Open",
            "In-Progress",
            "In-Review",
            "Released",
            "Closed",
        ]
        # Calculate status counts with default value of 0 if the status does not exist
        status_counts = {
            status: int(data["Status"].value_counts().get(status, 0))
            for status in expected_status
        }
        # Add the "Totals" key with the sum of all other statuses
        status_counts["Totals"] = sum(status_counts.values())

        # Calculate previous week's counts
        one_week_ago = datetime.today() - timedelta(days=7)
        previous_week_counts = {
            "Open": 0,
            "In-Progress": 0,
            "In-Review": 0,
            "Released": 0,
            "Closed": 0,
        }

        for i, status in enumerate(data["Status"]):
            if status == "Open":
                continue  # Open tasks don't have a start date

            start_date = data.iloc[i]["Start_Create"]

            if start_date < one_week_ago:
                previous_week_counts["Open"] += 1

            if status == "In-Progress":
                previous_week_counts["In-Progress"] += 1

            if status == "In-Review":
                review_date = data.iloc[i]["Start_Review"]
                if review_date < one_week_ago:
                    previous_week_counts["In-Review"] += 1

            if status == "Released":
                release_date = data.iloc[i]["Release_Date"]
                if release_date < one_week_ago:
                    previous_week_counts["Released"] += 1

            if status == "Closed":
                release_date = data.iloc[i]["Closed_Date"]
                if release_date < one_week_ago:
                    previous_week_counts["Closed"] += 1

        # Add the "Totals" key with the sum of all other statuses
        previous_week_counts["Totals"] = sum(previous_week_counts.values())

        # # Calculate delta
        deltas = {
            key: f"{status_counts[key] - previous_week_counts[key]} from last week"
            for key in status_counts
        }

        st.header("Delivery Status")
        # Display metrics card
        cols = st.columns(6)
        with cols[0]:
            ui.metric_card(
                title="Open",
                content=status_counts["Open"],
                description=deltas["Open"],
                key="card1",
            )
        with cols[1]:
            ui.metric_card(
                title="In-Progress",
                content=status_counts["In-Progress"],
                description=deltas["In-Progress"],
                key="card2",
            )
        with cols[2]:
            ui.metric_card(
                title="In-Review",
                content=status_counts["In-Review"],
                description=deltas["In-Review"],
                key="card3",
            )
        with cols[3]:
            ui.metric_card(
                title="Released",
                content=status_counts["Released"],
                description=deltas["Released"],
                key="card4",
            )
        with cols[4]:
            ui.metric_card(
                title="Closed",
                content=status_counts["Closed"],
                description=deltas["Closed"],
                key="card5",
            )
        with cols[5]:
            ui.metric_card(
                title="Totals",
                content=status_counts["Totals"],
                description=deltas["Totals"],
                key="card6",
            )

    else:
        st.text("No WBS file uploaded.")
