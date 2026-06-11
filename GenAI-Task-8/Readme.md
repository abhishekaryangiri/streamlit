# GenAI Task 8

## app_basic.py

```python
import streamlit as st

st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if st.button("Greet Me"):
    st.write("Hello, !")
```

---


## app_discount.py

```python
import streamlit as st

st.title("Discount Price Calculator")

original_price = st.text_input("Enter the original price:")
discount_percentage = st.slider("Select the discount percentage:", 0, 50, 10)

if st.button("Calculate Discounted Price"):
    original_price = float(original_price)

    discounted_price = original_price - (
        original_price * discount_percentage / 100
    )

    st.success(f"The discounted price is: {discounted_price}")

    st.write("Price Comparison Table:")
    st.table({
        "Before": [original_price],
        "After": [discounted_price]
    })
```

---

## app_product_form.py

```python
import streamlit as st

st.title("Product Form")
st.header("Add a New Product")

product_name = st.sidebar.text_input("Enter product name")

product_category = st.sidebar.selectbox(
    "Select product category",
    ["Electronics", "Clothing", "Books", "Groceries"]
)

product_price = st.sidebar.number_input(
    "Enter product price",
    min_value=0.0,
    step=0.01
)

if st.sidebar.button("Add Product"):
    st.success(
        f"Product {product_name} added successfully "
        f"in category {product_category} "
        f"with price {product_price}"
    )
```

---

## app_dashboard.py

```python
import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Welcome to the Sales Dashboard!")

month = st.selectbox("Select Month", ["January", "February", "March", "April"])

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.subheader("Monthly Sales")
st.write(f"{month} Sales: {sales[month]}")

st.subheader("Sales Bar Chart")
st.bar_chart(list(sales.values()))
```
