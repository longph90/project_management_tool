import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 78, 92],
    'Passed': [True, True, False, True]
}

df = pd.DataFrame(data)

# Function to add icons to the DataFrame
def add_icons(val):
    if val:
        return '✅'  # Unicode for check mark
    else:
        return '❌'  # Unicode for cross mark

# Apply the function to the 'Passed' column
df['Passed'] = df['Passed'].apply(add_icons)

# Display the DataFrame in Streamlit
st.write(df.to_html(escape=False), unsafe_allow_html=True)
