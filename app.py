import streamlit as st

# Employee class
class Employee:
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def get_firstname(self):
        return self.firstname

    def get_secondname(self):
        return self.secondname


# PartTimeEmployee class
class PartTimeEmployee(Employee):
    def __init__(self, firstname, secondname, weekly_pay):
        super().__init__(firstname, secondname)
        self.weekly_pay = weekly_pay

    def calculate_payment(self, hours_worked):
        return self.weekly_pay * hours_worked / 40  # Assuming a 40-hour work week


# FullTimeEmployee class
class FullTimeEmployee(Employee):
    def __init__(self, firstname, secondname, monthly_pay):
        super().__init__(firstname, secondname)
        self.monthly_pay = monthly_pay

    def calculate_payment(self):
        return self.monthly_pay


# Address class
class Address:
    def __init__(self, street_number, street_name, state_code, state_name):
        self.street_number = street_number
        self.street_name = street_name
        self.state_code = state_code
        self.state_name = state_name

    def get_address(self):
        return f"{self.street_number} {self.street_name}, {self.state_code}, {self.state_name}"


# Streamlit App
st.title("Employee Management System")

# Address input
st.subheader("Enter Address Details")
street_number = st.text_input("Street Number")
street_name = st.text_input("Street Name")
state_code = st.text_input("State Code")
state_name = st.text_input("State Name")

# Check if all address fields are filled before creating the Address object
address = None
if street_number and street_name and state_code and state_name:
    address = Address(street_number, street_name, state_code, state_name)

# Employee type selection
st.subheader("Select Employee Type")
emp_type = st.selectbox("Type", ["Part-Time", "Full-Time"])

# Employee details
st.subheader("Enter Employee Details")
firstname = st.text_input("First Name")
secondname = st.text_input("Second Name")

if emp_type == "Part-Time":
    weekly_pay = st.number_input("Weekly Pay", min_value=0.0, step=100.0)
    hours_worked = st.number_input("Hours Worked", min_value=0.0, step=1.0)
    if st.button("Calculate Pay"):
        if firstname and secondname and address:
            part_time_emp = PartTimeEmployee(firstname, secondname, weekly_pay)
            st.write(f"Name: {part_time_emp.get_firstname()} {part_time_emp.get_secondname()}")
            st.write(f"Address: {address.get_address()}")
            st.write(f"Weekly Pay for {hours_worked} hours: ${part_time_emp.calculate_payment(hours_worked):.2f}")
        else:
            st.error("Please fill in all employee and address details.")

elif emp_type == "Full-Time":
    monthly_pay = st.number_input("Monthly Pay", min_value=0.0, step=100.0)
    if st.button("Calculate Pay"):
        if firstname and secondname and address:
            full_time_emp = FullTimeEmployee(firstname, secondname, monthly_pay)
            st.write(f"Name: {full_time_emp.get_firstname()} {full_time_emp.get_secondname()}")
            st.write(f"Address: {address.get_address()}")
            st.write(f"Monthly Pay: ${full_time_emp.calculate_payment():.2f}")
        else:
            st.error("Please fill in all employee and address details.")
