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