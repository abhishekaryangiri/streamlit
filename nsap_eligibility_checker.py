import streamlit as st

st.title("NSAP Eligiblity Checker")

#basic for 1 scheme: Old age pension
# age = st.number_input("Enter your age", min_value=0, max_value=120,)
# income = st.number_input("Enter your annual income", max_value=100000)

# if st.button("Check eligibility"):
#     if(age >=60 and income <= 100000):
#         st.write("You are eligible for Old age pension")
        
#     else:
#         st.write("you are not eligible for Old age pension")


# Moderate for 3 schemes: Old age pension, Widow pension, Disability pension
# age = st.number_input("Enter your age", min_value=0, max_value=120,)
# income = st.number_input("Enter your annual income", max_value=100000)
# gender = st.selectbox("Select your gender", options=["Male", "Female", "Other"])
# disability = st.selectbox("Do you have any disability?", options=["Yes", "No"])
# if st.button("Check eligibility"):
#     if(age >=60 and income <= 100000):
#         st.write("You are eligible for Old age pension")
#     else:
#         st.write("you are not eligible for Old age pension")
    
#     if(gender == "Female" and income <= 100000):
#         st.write("You are eligible for Widow pension")
#     else:
#         st.write("you are not eligible for Widow pension")
    
#     if(disability == "Yes" and income <= 100000):
#         st.write("You are eligible for Disability pension")
#     else:
#         st.write("you are not eligible for Disability pension")


#show only eligible sheme , for widow pension also, if not eligible for any scheme show not eligible for any scheme
age = st.number_input("Enter your age", min_value=0, max_value=120,)
income = st.number_input("Enter your annual income", max_value=100000)
gender = st.selectbox("Select your gender", options=["Male", "Female", "Other"])
widow_status = st.selectbox("Are you a widow?", options=["Yes", "No"])
disability = st.selectbox("Do you have any disability?", options=["Yes", "No"])
if st.button("Check eligibility"):
    if(age >=60 and income <= 100000):
        st.write("You are eligible for Old age pension")
    
    if(widow_status == "Yes" and income <= 100000 and age <= 59):
        st.write("You are eligible for Widow pension")
    
    if(disability == "Yes" and income <= 100000):
        st.write("You are eligible for Disability pension")

    if not (age >=60 and income <= 100000) and not (widow_status == "Yes" and income <= 100000 and age <= 59) and not (disability == "Yes" and income <= 100000):
        st.write("You are not eligible for any scheme")