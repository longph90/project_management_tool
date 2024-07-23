import streamlit as st

# Initialize session state for file storage
if 'wbs_file' not in st.session_state:
    st.session_state.wbs_file = None
if 'timesheet_file' not in st.session_state:
    st.session_state.timesheet_file = None

# Define the About Me page
def about_me_page():
    st.title("About Me")
    
    # Add your photo
    st.image("my_photo.jpeg", width=150, caption="Long Phan")
    
 # Add your bio
    st.markdown("""
    ## Bio
    Hi, I'm Long Phan! I'm a Project Manager with a passion for coding. 
    I have been working in the field of project management for several years and specialize in managing software development projects. 
    In addition to my professional work, I enjoy coding and developing my own projects in my spare time.
    """)
    
    # Add more sections as needed
    st.markdown("""
    ## Skills
    - **Project Management**: Agile, Scrum, Waterfall.
    - **Programming Languages**: Python, JavaScript, Abap.
    - **Frameworks**: Streamlit, Django, React.
    - **Tools**: Git, Redmine, Backlog, JIRA.
    """)
    
    st.markdown("""
    ## Projects
    - **Project Management Tool**: Developed a tool to help manage project tasks and timelines.
    - **Automated Reporting System**: Created a system to automate the generation of project status reports.
    """)
    
    st.markdown("""
    ## Contact
    - **Email**: longph90@gmail.com
    """)

about_me_page()    