import streamlit as st
import pandas as pd
import json
import controller.wbs as wbs
import os
import zipfile
from io import BytesIO

st.header("Templates")


# Function to zip all files in a specified folder# Function to zip all files in a specified folder
def zip_folder(folder_path):
    # st.write(f"Zipping folder: {folder_path}")

    # Create a bytes buffer to store the zip file in memory
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # st.write(f"Current directory: {root}")
            for file in files:
                # st.write(f"File: {file}")
                file_path = os.path.join(root, file)
                # st.write(f"Full path: {file_path}")
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    zip_buffer.seek(0)
    return zip_buffer


with st.container(border=True):

    # Path to the 'template' folder
    folder_path = os.path.join(os.path.dirname(__file__), "../template")

    # Button to trigger the download
    if st.button("Download All Files"):
        # Zipping the folder
        zip_buffer = zip_folder(folder_path)

        # Creating the download button
        st.download_button(
            label="Download ZIP",
            data=zip_buffer,
            file_name="all_files.zip",
            mime="application/zip",
        )


st.header("Upload Files")
# Load config file data
with st.container(border=True):
    # File uploader for config
    upload_files = st.file_uploader(
        "Please remember to upload all the files as specified in the template, making sure to include the config.json file.",
        type=["json", "xlsx", "xls"],
        key="config_uploader",
        accept_multiple_files=True,
    )

    if upload_files is not None:
        for upload_file in upload_files:
            if upload_file.name == "config.json":
                st.session_state.upload_files = upload_file

        if st.session_state.upload_files is not None:
            # Read the content of the uploaded file
            content = st.session_state.upload_files.getvalue().decode("utf-8")
            data = json.loads(content)
            st.success("Config file uploaded successfully!")
            st.session_state.wbs_filename = data["tasks"]["filename"]
            st.session_state.timesheet_filename = data["timesheet"]["filename"]
            st.session_state.resource_filename = data["members"]["filename"]
    if st.session_state.upload_files is None:
        st.error("Please upload config file")
    else:
        if upload_files is not None:
            for upload_file in upload_files:

                # mapping filename of wbs file
                if upload_file.name == st.session_state.wbs_filename:
                    st.session_state.wbs_file = upload_file
                    st.session_state.df_wbs = wbs.load_data_wbs()
                    st.success("WBS file uploaded successfully!")

                # mapping filename of timesheet file
                if upload_file.name == st.session_state.timesheet_filename:
                    st.session_state.timesheet_file = upload_file
                    st.session_state.df_timesheet = pd.read_excel(
                        st.session_state.timesheet_file
                    )
                    st.success("Timesheet file uploaded successfully!")

                # mapping filename of resource file
                if upload_file.name == st.session_state.resource_filename:
                    st.session_state.resource_file = upload_file
                    st.session_state.df_resource = pd.read_excel(
                        st.session_state.resource_file
                    )
                    st.success("Resource file uploaded successfully!")
    # st.rerun()
