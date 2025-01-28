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


# Testing the classes
if __name__ == "__main__":
    # Create an Address instance
    address = Address("123", "AIRFORCE BASE", "456", "Kaduna")

    # Create a PartTimeEmployee instance
    part_time_emp = PartTimeEmployee("OLAMIDE", "JUMMY", 500)
    print(f"Part-Time Employee: {part_time_emp.get_firstname()} {part_time_emp.get_secondname()}")
    print(f"Weekly Pay for 20 hours: ${part_time_emp.calculate_payment(20):.2f}")
    print(f"Address: {address.get_address()}")

    # Create a FullTimeEmployee instance
    full_time_emp = FullTimeEmployee("AISHA", "AKANBI", 4000)
    print(f"\nFull-Time Employee: {full_time_emp.get_firstname()} {full_time_emp.get_secondname()}")
    print(f"Monthly Pay: ${full_time_emp.calculate_payment():.2f}")
    print(f"Address: {address.get_address()}")
