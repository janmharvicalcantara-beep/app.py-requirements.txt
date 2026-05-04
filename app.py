import streamlit as st
import pandas as pd

st.title("Smart Expense Tracker")

# Initialize data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Input form
date = st.date_input("Date")
category = st.selectbox("Category", ["Food", "Transport", "Bills", "Other"])
amount = st.number_input("Amount", min_value=0.0)

if st.button("Add Expense"):
    new_row = pd.DataFrame([[date, category, amount]],
                           columns=["Date", "Category", "Amount"])
    st.session_state.data = pd.concat([st.session_state.data, new_row],
                                      ignore_index=True)

# Display table
st.subheader("Expenses")
st.dataframe(st.session_state.data)

# Delete option
st.subheader("Delete Expense")

if not st.session_state.data.empty:
    idx = st.selectbox("Select row to delete", st.session_state.data.index)
    if st.button("Delete"):
        st.session_state.data = st.session_state.data.drop(idx).reset_index(drop=True)

# Summary
st.subheader("Total Expenses")
st.write(st.session_state.data["Amount"].sum())

#pip install streamlit pandas
#streamlit run app.py
