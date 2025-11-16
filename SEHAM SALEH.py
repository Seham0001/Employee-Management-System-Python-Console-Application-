'''Name: Seham Saleh Yaslam Bin Tayeb, TP084085 '''

print('Employee Management System')

# Employee records
emp = [
    {'name': 'Mary James', 'id': '101', 'username': 'mary', 'email': 'mary.J@hotmail.com', 'password': 'mary123',
     'job': 'Developer'},
    {'name': 'Alex Freburg', 'id': '102', 'username': 'alex', 'email': 'alex@hotmail.com', 'password': 'alex123',
     'job': 'Designer'},
    {'name': 'nancy Brown', 'id': '103', 'username': 'nancy', 'email': 'nancy@example.com',
     'password': 'charlie123', 'job': 'Manager'},
]

# Manager profiles
managers = [{'username': 'manager', 'password': '9976', 'name': 'Manager Name', 'email': 'manager@example.com'}]

# Boss profile with username
boss_profile = {'username': 'boss', 'name': 'sary', 'email': 'sary@hotmail.com', 'password': '8878'}


def login():
    for _ in range(3):
        username = input("enter username: ").strip().lower()
        password = input("Enter password: ").strip()

        # Boss login
        if username == boss_profile['username']:
            if password == boss_profile['password']:
                print("Hello, Boss")
                return 'boss'

        # Manager login
        elif username == 'manager':
            for manager in managers:
                if manager['username'] == username and manager['password'] == password:
                    print("Hello, Manager")
                    return 'manager'

        # Employee login
        else:
            for employee in emp:
                if employee['username'] == username and employee['password'] == password:
                    print("Hello, " + employee['name'])
                    return 'employee', employee  # Return employee details

        print("Username or password is incorrect.")

    print("You have entered the username and password incorrectly more than 3 times. System terminating.")
    return None


def main_menu():
    login_info = login()
    if login_info == 'boss':
        m_boss()
    elif login_info == 'manager':
        m_manager()
    elif isinstance(login_info, tuple) and login_info[0] == 'employee':
        m_employee(login_info[1])  # Pass the employee details
    else:
        print("Login error.")


def m_boss():
    print("Boss menu")
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Edit Profile")
        print("5. Delete Employee/Manager")
        choice = input("What do you want: ")

        if choice == '1':
            emp_add()
        elif choice == '2':
            emp_view()
        elif choice == '3':
            emp_search()
        elif choice == '4':
            edit_profile(boss_profile)
        elif choice == '5':
            emp_delete()
        else:
            print("Error. Exiting menu.")
            break


def m_manager():
    print("Manager menu")
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Edit Profile")
        print("5. Reset Password")
        choice = input("What do you want to do: ")

        if choice == '1':
            emp_add_manager()
        elif choice == '2':
            emp_view()
        elif choice == '3':
            emp_search()
        elif choice == '4':
            edit_profile(managers[0])  # Assuming the first manager is logged in
        elif choice == '5':
            reset_password(managers[0])  # Resetting the password for the manager
        else:
            print("Error. Exiting menu.")
            break


def m_employee(employee):
    print("Employee menu")
    while True:
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Reset Password")
        choice = input("What do you want to do: ")

        if choice == '1':
            print(employee)  # Display employee profile
        elif choice == '2':
            edit_profile(employee)  # Edit own profile
        elif choice == '3':
            reset_password(employee)  # Reset own password
        else:
            print("Error. Exiting menu.")
            break


def emp_add():
    emp_name = input("Enter employee name: ")
    emp_id = input("Enter ID: ")
    emp_username = input("Enter username: ")
    emp_email = input("Enter employee email: ")
    emp_password = input("Enter employee password: ")
    emp_job = input("Enter employee job: ")

    emp1 = {'name': emp_name, 'id': emp_id, 'username': emp_username, 'email': emp_email,
            'password': emp_password, 'job': emp_job}
    emp.append(emp1)
    print("Employee added.")


def emp_add_manager():
    emp_name = input("Enter employee name: ")
    emp_id = input("Enter ID: ")
    emp_username = input("Enter username: ")
    emp_email = input("Enter employee email: ")
    emp_password = input("Enter employee password: ")
    emp_designation = input("Enter employee designation: ")
    emp_age = input("Enter employee age: ")
    emp_address = input("Enter employee address: ")
    emp_salary = input("Enter employee salary: ")

    emp1 = {
        'name': emp_name, 'id': emp_id, 'username': emp_username, 'email': emp_email,
        'password': emp_password, 'designation': emp_designation, 'age': emp_age,
        'address': emp_address, 'salary': emp_salary
    }
    emp.append(emp1)
    print("Employee added by Manager.")


def emp_view():
    if not emp:
        print("No employees found.")
    else:
        for e in emp:
            print(f"ID: {e['id']}, Name: {e['name']}, Username: {e['username']}, "
                  f"Email: {e['email']}, Job: {e['job']}")


def emp_search():
    search_type = input("choose (id/email/username): ").strip().lower()
    search_value = input(f"Enter {search_type}: ")

    for e in emp:
        if e[search_type] == search_value:
            print(e)
            return
    print("Employee not found.")


def emp_delete():
    search_type = input("Delete by (name/id/email/username): ").strip().lower()
    search_value = input(f"Enter {search_type}: ")

    global emp
    emp = [e for e in emp if e[search_type] != search_value]
    print(f"Employees with {search_type} '{search_value}' deleted.")


def edit_profile(profile):
    profile['name'] = input("Enter new name: ")
    profile['email'] = input("Enter new email: ")
    profile['password'] = input("Enter new password: ")
    print("Profile updated.")


def reset_password(user):
    new_password = input("Enter new password: ")
    user['password'] = new_password
    print("Password reset.")


main_menu()
