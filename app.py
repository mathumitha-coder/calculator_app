import streamlit as st

st.title("Mathu Calculator")

x1 = st.number_input("Enter first number", value=0.0)
x2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox("Operations", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add", x2 not 0:
        result = x1 + x2
    elif operation == "Subtract":
        result = x1 - x2
    elif operation == "Multiply":
        result = x1 * x2
    elif operation == "Divide":
        result = x1 / x2
    else:
        result = "you entered wrong number calculator developed by Mathumitha...!"

    st.success(f"Answer: {result}")
