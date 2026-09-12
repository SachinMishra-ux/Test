import streamlit as st #alias for streamlit
from bank import BankAccount


st.title("🏦 Bank Account")

# # Create account
account = BankAccount("Sachin", 10000)

st.write(f"Account Holder: **{account.name}**")

amount = st.number_input(
    "Enter Amount",
    min_value=0,
    value=1000
)

# # Buttons
if st.button("Deposit"):
    result = account.deposit(amount)
    st.success(result)

if st.button("Withdraw"):
    result = account.withdraw(amount)
    st.success(result)

if st.button("Display Balance"):
    result = account.display_balance()
    st.info(result)