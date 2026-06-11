import streamlit as st

#Price Calculator for discount
st.title("Discount Price Calculator")
original_price = st.text_input("Enter the original price:")
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
   

