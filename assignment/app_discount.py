import streamlit as st

#Price Calculator for discount
st.title("Discount Price Calculator")
original_price = st.text_input("Enter the original price:")
discount_percentage = st.text_input("Enter the discount percentage:")
discounted_price = st.button("Calculate Discounted Price")
if discounted_price:
    original_price = float(original_price)
    discount_percentage = float(discount_percentage)
    discounted_price = original_price - (original_price * discount_percentage / 100)
    st.success(f"The discounted price is: {discounted_price}")

    #comparison table - Before | After in simple table
    st.write("Price Comparison Table:")
    st.table({"Before": [original_price], "After": [discounted_price]})
   

