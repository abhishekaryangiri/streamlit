# Streamlit


# Streamlit Complete Interview Notes

## What is Streamlit?

Streamlit is an open-source Python framework used to build interactive web applications for Data Science, Machine Learning, Deep Learning, Data Analytics, and Generative AI projects without requiring frontend technologies like HTML, CSS, JavaScript, or React.

It allows developers to create production-ready web applications using only Python.

---

# Why Streamlit?

Traditional web development requires:

* HTML
* CSS
* JavaScript
* Backend Framework

Streamlit eliminates these requirements and enables rapid development using pure Python.

Benefits:

* Fast Development
* Easy Learning Curve
* Interactive UI Components
* Data Visualization Support
* ML Model Deployment
* GenAI Application Development
* Chatbot Development
* Dashboard Creation

---

# Installation

```bash
pip install streamlit
```

Verify installation:

```bash
streamlit hello
```

Check version:

```bash
streamlit --version
```

---

# Running a Streamlit Application

Create:

```python
app.py
```

Run:

```bash
streamlit run app.py
```

Default URL:

```text
http://localhost:8501
```

---

# Streamlit Execution Model

Important Interview Question

Streamlit executes the entire script from top to bottom whenever a user interacts with a widget.

Examples:

* Button Click
* Text Input
* Selectbox Change
* Checkbox Selection

This behavior is called Reactive Programming.

---

# Basic Components

## Title

```python
st.title("GenAI Application")
```

## Header

```python
st.header("Machine Learning Dashboard")
```

## Subheader

```python
st.subheader("Model Prediction")
```

## Text

```python
st.text("Hello World")
```

## Write

```python
st.write("Flexible output")
```

---

# Displaying Data

## DataFrame

```python
import pandas as pd

df = pd.read_csv("data.csv")

st.dataframe(df)
```

## Static Table

```python
st.table(df)
```

---

# User Input Widgets

## Text Input

```python
name = st.text_input("Enter Name")
```

## Number Input

```python
age = st.number_input("Enter Age")
```

## Text Area

```python
message = st.text_area("Message")
```

## Selectbox

```python
city = st.selectbox(
    "Select City",
    ["Delhi","Mumbai","Patna"]
)
```

## Multiselect

```python
skills = st.multiselect(
    "Skills",
    ["Python","ML","GenAI"]
)
```

## Radio Button

```python
choice = st.radio(
    "Gender",
    ["Male","Female"]
)
```

## Checkbox

```python
agree = st.checkbox("Accept Terms")
```

## Slider

```python
value = st.slider(
    "Select Value",
    0,
    100
)
```

---

# Buttons

```python
if st.button("Submit"):
    st.success("Submitted")
```

Interview Point:

Button returns True only once when clicked.

---

# Layout Components

## Columns

```python
col1,col2 = st.columns(2)

with col1:
    st.write("Left")

with col2:
    st.write("Right")
```

## Container

```python
container = st.container()

with container:
    st.write("Content")
```

## Expander

```python
with st.expander("Details"):
    st.write("Hidden Content")
```

---

# Sidebar

```python
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose",
    ["Home","About"]
)
```

Interview Question:

Why Sidebar?

Answer:
Used for navigation and application controls.

---

# File Upload

```python
file = st.file_uploader(
    "Upload File"
)
```

Supported:

* CSV
* PDF
* TXT
* DOCX
* Images

GenAI applications heavily use file uploader.

---

# Image Display

```python
st.image("image.png")
```

---

# Audio

```python
st.audio("audio.mp3")
```

---

# Video

```python
st.video("video.mp4")
```

---

# Charts

## Line Chart

```python
st.line_chart(data)
```

## Bar Chart

```python
st.bar_chart(data)
```

## Area Chart

```python
st.area_chart(data)
```

---

# Session State

Most Important Interview Topic

Used for preserving values across reruns.

Example:

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)
```

Why needed?

Because Streamlit reruns the entire script.

---

# Caching

Important Interview Question

Used to improve performance.

## Data Cache

```python
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

## Resource Cache

```python
@st.cache_resource
def load_model():
    return model
```

Benefits:

* Faster Execution
* Reduced API Calls
* Reduced Database Queries

---

# Forms

```python
with st.form("myform"):

    name = st.text_input("Name")

    submitted = st.form_submit_button(
        "Submit"
    )
```

Why Forms?

Avoid unnecessary reruns.

---

# Multipage Applications

Folder Structure:

```text
project/

app.py

pages/
    home.py
    about.py
    chatbot.py
```

Streamlit automatically creates navigation.

---

# Streamlit and Machine Learning

Workflow:

1. Train Model
2. Save Model
3. Load Model
4. Take User Input
5. Predict
6. Display Result

Example:

```python
prediction = model.predict(data)

st.write(prediction)
```

---

# Streamlit and Generative AI

Most common use case today.

Applications:

* ChatGPT Clone
* PDF Chatbot
* RAG System
* AI Assistant
* Image Generation
* SQL Assistant
* Resume Analyzer

Libraries Used:

* OpenAI
* LangChain
* LlamaIndex
* FAISS
* ChromaDB
* HuggingFace

---

# Chat Interface

```python
st.chat_message("user")

st.chat_message("assistant")
```

Input:

```python
prompt = st.chat_input(
    "Ask anything"
)
```

This is heavily used in GenAI projects.

---

# Streamlit Deployment

## Streamlit Community Cloud

Free deployment.

## Docker

Production deployment.

## AWS

* EC2
* ECS
* EKS

## Azure

* Azure App Service

## GCP

* Cloud Run

---

# Advantages

* Easy
* Fast
* Python Only
* Great for ML
* Great for GenAI
* Rapid Prototyping
* Rich Components

---

# Limitations

* Not ideal for complex frontend applications
* Limited customization compared to React
* Full rerun behavior
* Not suitable for enterprise-scale UI

---

# Frequently Asked Interview Questions

Q1. What is Streamlit?

A framework for building interactive data and AI web applications using Python.

Q2. Why use Streamlit?

Rapid development without frontend coding.

Q3. What happens when a widget changes?

Entire script reruns.

Q4. What is Session State?

Stores data across reruns.

Q5. Difference between cache_data and cache_resource?

cache_data → Data

cache_resource → Models, DB connections, resources

Q6. What is st.write()?

Universal display function.

Q7. How to deploy Streamlit?

Community Cloud, Docker, AWS, Azure, GCP.

Q8. Why is Streamlit popular in GenAI?

Fast chatbot and RAG development.

Q9. What is st.chat_input()?

Creates ChatGPT-like input.

Q10. What are the biggest advantages of Streamlit?

Fast development, Python-only coding, ML/GenAI integration.

## All .py copy into Readme.md
for %f in (*.py) do type "%f" >> README.md