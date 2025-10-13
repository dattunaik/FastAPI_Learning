import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # Your FastAPI server URL

st.title("Employee Management System")

menu = ["Add Employee", "View Employees", "Update Employee", "Delete Employee"]
choice = st.sidebar.selectbox("Menu", menu)

# --------------------- ADD EMPLOYEE ---------------------
if choice == "Add Employee":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Add Employee"):
        if name and email:
            response = requests.post(f"{BASE_URL}/employees", json={"name": name, "email": email})
            if response.status_code == 200:
                st.success("Employee added successfully!")
            else:
                st.error(f"Error: {response.json()['detail']}")
        else:
            st.warning("Please provide both name and email.")

# --------------------- VIEW EMPLOYEES ---------------------
elif choice == "View Employees":
    st.subheader("All Employees")
    response = requests.get(f"{BASE_URL}/employees")
    if response.status_code == 200:
        employees = response.json()
        if employees:
            for emp in employees:
                st.write(f"ID: {emp['id']} | Name: {emp['name']} | Email: {emp['email']}")
        else:
            st.info("No employees found.")
    else:
        st.error("Failed to fetch employees.")

# --------------------- UPDATE EMPLOYEE ---------------------
elif choice == "Update Employee":
    st.subheader("Update Employee")
    emp_id = st.number_input("Employee ID", min_value=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")

    if st.button("Update Employee"):
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email

        if data:
            response = requests.put(f"{BASE_URL}/employees/{emp_id}", json=data)
            if response.status_code == 200:
                st.success("Employee updated successfully!")
            else:
                st.error(f"Error: {response.json()['detail']}")
        else:
            st.warning("Provide at least one field to update.")

# --------------------- DELETE EMPLOYEE ---------------------
elif choice == "Delete Employee":
    st.subheader("Delete Employee")
    emp_id = st.number_input("Employee ID", min_value=1)

    if st.button("Delete Employee"):
        response = requests.delete(f"{BASE_URL}/employees/{emp_id}")
        if response.status_code == 200:
            st.success("Employee deleted successfully!")
        else:
            st.error(f"Error: {response.json()['detail']}")
