import streamlit as st

from database import (
    create_tables,
    add_customer,
    add_membership,
    get_customers_with_membership
)


create_tables()

st.title("🏋️ Gym Management")


# Customer
st.header("Customer Details")

name = st.text_input("Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=1, max_value=100)


if st.button("Add Customer"):

    customer_id = add_customer(
        name,
        gender,
        age
    )

    st.success(f"Customer added! ID: {customer_id}")


# Membership
st.header("Membership Details")

customer_id = st.number_input(
    "Customer ID",
    min_value=1
)

membership = st.selectbox(
    "Membership",
    ["Monthly", "Quarterly", "Yearly"]
)

duration = st.number_input(
    "Duration (Months)",
    min_value=1
)


if st.button("Add Membership"):

    add_membership(
        customer_id,
        membership,
        duration
    )

    st.success("Membership added!")

st.subheader("Customers & Memberships")

data = get_customers_with_membership()

for customer in data:
    st.write(customer)