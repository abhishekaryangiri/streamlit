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
