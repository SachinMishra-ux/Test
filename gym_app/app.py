import streamlit as st

from database import create_table, add_customer, get_customers


# Create database table
create_table()


st.title("🏋️ Gym Customer Registration")

name = st.text_input("Customer Name")

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100
)

membership = st.selectbox(
    "Membership",
    ["Monthly", "Quarterly", "Yearly"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0
)


if st.button("Add Customer"):

    add_customer(
        name,
        gender,
        age,
        membership,
        weight
    )

    st.success("Customer added successfully!")


# Display customers
st.subheader("Customers")

customers = get_customers()

for customer in customers:
    st.write(customer)
