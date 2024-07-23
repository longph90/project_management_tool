import streamlit as st
import pandas as pd
import json


def upload_json_file():
       # File uploader
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        # Read the file content
        file_content = uploaded_file.read()
        
        # Parse JSON
        try:
            data = json.loads(file_content)

            # Extract paths
            wbs_path = data.get("wbs", {}).get("path", "Path not found")
            timesheet_path = data.get("timesheet", {}).get("path", "Path not found")
            
            # Display paths
            st.write("WBS Path:", wbs_path)
            st.write("Timesheet Path:", timesheet_path)

            # Ensure session state is initialized
            if 'tasklist_df' not in st.session_state:
                st.session_state['tasklist_df'] = None
            if 'timesheet_df' not in st.session_state:
                st.session_state['timesheet_df'] = None

            # Load WBS file if path exists
            if wbs_path and wbs_path != "Path not found":
                try:
                    st.session_state['tasklist_df'] = pd.read_excel(wbs_path)
                    st.success("WBS loaded successfully.")    
                except Exception as e:
                    st.error(f"Error loading Task List: {e}")    

            # Load Timesheet file if path exists
            if timesheet_path and timesheet_path != "Path not found":
                try:
                    st.session_state['timesheet_df'] = pd.read_excel(timesheet_path)
                    st.success("Timesheet loaded successfully.")    
                except Exception as e:
                    st.error(f"Error loading Timesheet: {e}")

        except json.JSONDecodeError:
            st.error("Uploaded file is not a valid JSON")


# Streamlit application
def main():
    st.title("JSON File Upload and Display")
    upload_json_file()
 

if __name__ == "__main__":
    main()
