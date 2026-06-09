import streamlit as st
import pandas as pd
#use command prompt to run the app
#1. pip install streamlit
#2. streamlit run app.py

#basic Components of Streamlit
st.write("Hello World")
st.title("This is title of StelioAI")
st.header("This is header of StelioAI")
st.subheader("This is subheader of StelioAI")
st.text("This is text of StelioAI")
st.markdown("This is markdown of StelioAI")
st1 = st.button("Click me")
if st1:
    st.write("Button Clicked")

animal_shelter = ['cat', 'dog','lion']
animal = st.text_input("Enter your favorite animal")
if st.button("Check Availability"):
    if animal in animal_shelter:
        st.write(f"{animal} is available in the shelter")
    else:
        st.write(f"{animal} is not available in the shelter")


#Displaying Data

#Dataframe: to display data in tabular format
file = st.file_uploader("Upload Excel File", type=["xlsx"])
#pip install openpyxl to read excel files i
if file:
    df = pd.read_excel(file)
    st.dataframe(df)

#for csv files
file_csv = st.file_uploader("Upload CSV File", type=["csv"])
if file_csv:
    df_csv = pd.read_csv(file_csv)
    # .dataframe: to display data in interactive format
    st.dataframe(df_csv)
    # .table: to display data in static format
    st.table(df_csv)


#User input widgets
name = st.text_input("Enter Scheme name")
if st.button("Submit"):
    st.write(f"scheme name is {name}")



