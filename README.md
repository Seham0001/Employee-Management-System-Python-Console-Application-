# Employee Management System (Python)

A role-based console application built in Python that manages employee records for three types of users: **Boss**, **Manager**, and **Employee**. The system allows secure login, profile management, employee registration, search, deletion, and password updates. This project demonstrates Python fundamentals including functions, lists, dictionaries, validation loops, and modular design.

---

## 📌 Features

### 🔐 Authentication System
- Three login roles:
  - **Boss**
  - **Manager**
  - **Employee**
- Three login attempts before automatic termination.

---

### 👑 Boss Functionalities
- Add a new employee  
- View all employees  
- Search for an employee  
- Edit Boss profile  
- Delete employee or manager accounts  

---

### 👨‍💼 Manager Functionalities
- Add a new employee (with extended details)  
- View all employees  
- Search employees  
- Edit manager profile  
- Reset password  

---

### 👤 Employee Functionalities
- View personal profile  
- Edit personal profile  
- Reset password  

---

## 🗂️ Project Structure


Main components include:

- `login()` – Handles authentication  
- `m_boss()`, `m_manager()`, `m_employee()` – Role-based menus  
- `emp_add()`, `emp_add_manager()` – Add employees  
- `emp_view()` – View all records  
- `emp_search()` – Search employee data  
- `emp_delete()` – Remove employees/managers  
- `edit_profile()` – Update user details  
- `reset_password()` – Change password  
- `main_menu()` – Runs the system  


