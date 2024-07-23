import streamlit as st
import pandas as pd

# Define the phases and norm for 1KLOC
phases = ["BD", "DD", "CODE", "PCL", "UT"]


# Page title
st.title("Effort Estimation Calculator")

# User inputs for percentage weights for each phase
st.subheader("Enter the percentage weight for each phase")
norm_per_1kloc = st.number_input(f"MD/KLOC", min_value=0.0, max_value=100.0, value=20.0)
weights = {}
for phase in phases:
    weights[phase] = st.number_input(
        f"{phase} % weight", min_value=0.0, max_value=100.0, value=20.0
    )

# File uploader for task list
uploaded_file = st.file_uploader("Upload your task list", type=["xlsx", "csv"])

if uploaded_file:
    # Read the uploaded file
    if uploaded_file.name.endswith(".xlsx"):
        df_tasks = pd.read_excel(uploaded_file)
    else:
        df_tasks = pd.read_csv(uploaded_file)

    # st.write("Uploaded Task List")
    # st.dataframe(df_tasks)

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

        st.write("Calculated Effort for Each Task")
        st.dataframe(df_tasks)

        # Display total effort for all tasks
        total_effort_all_tasks = df_tasks["Total Effort (Person-Days)"].sum()
        st.write(
            f"**Total Effort for All Tasks:** {total_effort_all_tasks:.2f} Person-Days"
        )
