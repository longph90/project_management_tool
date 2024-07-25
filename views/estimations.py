import streamlit as st
import pandas as pd

# Define the phases and norm for 1KLOC
phases = ["BD", "DD", "CODE", "PCL", "UT"]

# Page title
st.title("Effort Estimation Calculator")

# User inputs for percentage weights for each phase
st.subheader("Enter the percentage weight for each phase")

with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns(6, vertical_alignment="bottom")
    weights = {}
    columns = [col1, col2, col3, col4, col5, col6]
    labels = [
        "MD/KLOC",
        "BD % weight",
        "DD % weight",
        "CODE % weight",
        "PCL % weight",
        "UT % weight",
    ]
    keys = [None, "BD", "DD", "CODE", "PCL", "UT"]
    values = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0]

    for col, label, key, value in zip(columns, labels, keys, values):
        with col:
            if key is None:
                norm_per_1kloc = st.number_input(
                    label, min_value=0.0, max_value=100.0, value=value
                )
            else:
                weights[key] = st.number_input(
                    label, min_value=0.0, max_value=100.0, value=value
                )

with st.container(border=True):
    # File uploader for task list
    uploaded_file = st.file_uploader("Upload your task list", type=["xlsx", "csv"])

with st.container(border=True, height=600):
    if uploaded_file:
        # Read the uploaded file
        if uploaded_file.name.endswith(".xlsx"):
            df_tasks = pd.read_excel(uploaded_file)
        else:
            df_tasks = pd.read_csv(uploaded_file)

        # Assuming the task list contains a column 'KLOC' for the size of each task
        if "KLOC" not in df_tasks.columns:
            st.error("The uploaded file must contain a 'KLOC' column.")
        else:
            # Calculate efforts for each task
            for phase in phases:
                df_tasks[f"{phase} Effort (Person-Days)"] = df_tasks["KLOC"].apply(
                    lambda x: (weights[phase] / 100) * norm_per_1kloc * x
                )

            # Calculate total effort for each task
            df_tasks["Total Effort (Person-Days)"] = df_tasks[
                [f"{phase} Effort (Person-Days)" for phase in phases]
            ].sum(axis=1)

            # Calculate summary row
            summary_row = (
                df_tasks[[f"{phase} Effort (Person-Days)" for phase in phases]]
                .sum()
                .to_dict()
            )
            summary_row["KLOC"] = df_tasks["KLOC"].sum()
            summary_row["Total Effort (Person-Days)"] = df_tasks[
                "Total Effort (Person-Days)"
            ].sum()
            summary_row = pd.DataFrame([summary_row], index=["Total"])

            # Append summary row to the dataframe
            df_tasks = pd.concat([df_tasks, summary_row])

            st.write("Calculated Effort for Each Task")
            st.dataframe(df_tasks, height=450)

            # Display total effort for all tasks
            total_effort_all_tasks = df_tasks.loc["Total", "Total Effort (Person-Days)"]

            st.write(
                f"**Total Effort for All Tasks:** {total_effort_all_tasks:.2f} Person-Days"
            )
