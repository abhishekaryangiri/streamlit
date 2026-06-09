import streamlit as st

st.title("NSAP Chatbot")

question = st.chat_input("Ask your question")

if question:

    with st.chat_message("user"):
        st.write(question)

    question = question.lower()

    if "old age" in question:
        answer = """
Old Age Pension

Age: 60 years or above

Amount: ₹200 per month from Central Government.
Additional pension may be provided by the State Government.
"""

    elif "widow" in question:
        answer = """
Widow Pension

Age: 40 to 79 years

Amount: ₹300 per month from Central Government.
Additional pension may be provided by the State Government.
"""

    elif "disability" in question:
        answer = """
Disability Pension

Eligibility: 80% or more disability

Age: 18 to 79 years

Amount: ₹300 per month from Central Government.
Additional pension may be provided by the State Government.
"""

    elif "amount" in question:
        answer = """
Pension Amount

Old Age Pension: ₹200 per month

Widow Pension: ₹300 per month

Disability Pension: ₹300 per month

Note: States may provide additional pension.
"""

    elif "age" in question:
        answer = """
Age Criteria

Old Age Pension: 60 years and above

Widow Pension: 40 to 79 years

Disability Pension: 18 to 79 years
"""

    elif "document" in question:
        answer = """
Required Documents

- Aadhaar Card
- Bank Passbook
- Income Certificate
- Passport Size Photo
"""

    else:
        answer = """
You can ask about:

- Old Age Pension
- Widow Pension
- Disability Pension
- Pension Amount
- Age Criteria
- Required Documents
"""

    with st.chat_message("assistant"):
        st.write(answer)
        