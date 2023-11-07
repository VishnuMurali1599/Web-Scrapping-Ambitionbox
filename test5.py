import streamlit as st
import pandas as pd


df = pd.read_csv('Company_details.csv')

st.sidebar.title("Company Details")

st.sidebar.image('https://small-bizsense.com/wp-content/uploads/2018/09/it_service.jpg')
    
Company_Name=st.selectbox("Company_Name",df['Company_Name'].unique().tolist())

# Create a button to filter the data
if st.button("Filter Data"):
    filtered_data = df[df['Company_Name'] == Company_Name]

    # Display the filtered data
    st.table(filtered_data)
    

    
