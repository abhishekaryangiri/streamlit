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
#f: we use f string to display the user input in the output
name = st.text_input("Enter Scheme name")
if st.button("Submit"):
    st.write(f"scheme name is {name}")

#text area
description = st.text_area("Enter Scheme description")
if st.button("Submit Description"):
    st.write(f"scheme description is {description}")


#colors
color = st.color_picker("Pick a color")
st.write(f"The selected color is {color}")


#selectbox: to select one option from a list of options
city = st.selectbox('Select a city', 
                    ['','Noida','Delhi','Gurrugram'])
st.write(f"You selected {city}")

#Multiselect: to select multiple options from a list of options
cities = st.multiselect('Select Cities',
                        ['Meerut','Noida','Gurugram','Delhi'])
st.write(f"You selected {cities}")

#Radio Buttons: to select one option from a list of options
gender = st.radio('Select Gender',
                   ['Male','Female',"trans"])
st.write(f"you selected {gender}")

#Checkbox: to select one or more options from a list of options
cities = st.checkbox("Accept Terma and Condirions")

#Buttons: to perform an action when clicked
if st.button("Click me"):
    st.write("Button Clicked")

#Slider: to select a value from a range of values
# age = st.slider("Select Your Age", 0, 100, 0)
# st.write(f"Youa selected  {age}")

#Layout components: to organize the layout of the app

col1, col2 = st.columns(2)

with col1:
    st.button("Login")

with col2:
    st.button("Register")


#Sidebar: to display components in a sidebar
st.sidebar.title("Menu")
options = st.sidebar.selectbox("Choose",
                               ["Home","About","Contact"])

#File Upload: to upload files and display them
upload_file = st.file_uploader("Upload a file", type=["jpg","png","pdf"])
if upload_file:
    st.write("File uploaded successfully")

#Image display: to display images
image_file = st.file_uploader("Upload an image", type=["jpg","png"])
if image_file:
    st.image(image_file, caption="Uploaded Image", use_column_width=True)

# video: to display videos use .video

#chart: to display charts use .line_chart, .bar_chart, .area_chart
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})
st.line_chart(data.set_index('x'))

#Bar chart
st.bar_chart(data.set_index('x'))


#error and success messages: to display error and success messages use .error and .success
st.write("Check your eligibility to vote")
age = st.slider("Select Your Age", 0, 100, 0)
check_eligibility = st.button("Check Eligibility")
if not check_eligibility:
    st.write("Please click the button to check your eligibility")
else:
    if age < 18:
        st.error("You are not eligible to vote")
    else:
        st.success("You are eligible to vote")

