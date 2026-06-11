# GenAI Task 8

## app_basic.py

```python
import streamlit as st

st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if st.button("Greet Me"):
    st.write(f"Hello, {name}!")
```

---


## app_discount.py

```python
import streamlit as st

#Price Calculator for discount
st.title("Discount Price Calculator")
original_price = st.number_input("Enter the original price:")
discount_percentage = st.slider("Select the discount percentage:", 0, 50, 10)  # Slider for discount percentage from 0% to 100% with a default of 10%
discounted_price = st.button("Calculate Discounted Price")
if discounted_price:
    original_price = float(original_price)
    discount_percentage = float(discount_percentage)
    discounted_price = original_price - (original_price * discount_percentage / 100)
    st.success(f"The discounted price is: {discounted_price}")

    #comparison table - Before | After in simple table
    st.write("Price Comparison Table:")
    st.table({"Before": [original_price], "After": [discounted_price]})
```

---

## app_product_form.py

```python
import streamlit as st

#Product Form
st.title("Product Form")
st.header("Add a new product")
#use streamlit sidebar to enter: product name, category(selectbox with 3-5 option), price,we can add product shown a successfull message. use sidebar.text_input,sidebar.selectbox. sidebar.number_input, sidebar.button
product_name = st.sidebar.text_input("Enter product name")
product_category = st.sidebar.selectbox("Select product category", ["Electronics", "Clothing", "Books", "Groceries"])
product_price = st.sidebar.number_input("Enter product price", min_value=0.0, step=0.01)
#add product price
if st.sidebar.button("Add Product"):
    st.success(f"Product {product_name} added successfully in category {product_category} with price {product_price}")
```

---

## app_dashboard.py

```python
import streamlit as st

#Small Dashboard without pandas. 
st.title("Simple Sales Dashboard")
st.write("Welcome to the Sales Dashboard!")
#selectbox with month
month = st.selectbox("Select Month", ["January", "February", "March", "April"])
#static dictionary of month sales

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

#displaying selected month sales using st.matric() or st.write()
st.subheader("Monthly Sales")
st.write(f"{month} Sales: {sales [month]}"
)

#display using bar chart: st.bar_chart
st.subheader("Sales Bar Chart")
st.bar_chart(list(sales.values()))
```
