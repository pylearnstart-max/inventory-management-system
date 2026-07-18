# Sprint 13 - Authentication & Role Management

## Sprint Goal

Implement complete authentication system with role-based dashboards, permissions, password management and logout functionality.


---

# Sprint Stories Status


| Story ID | Title | Description | Status |
|----------|-------|-------------|--------|
| INV-1301 | Main Login Menu | Create login and exit menu | Done |
| INV-1302 | Admin Dashboard | Implement admin role dashboard | Done |
| INV-1303 | Manager Dashboard | Implement manager role dashboard | Done |
| INV-1304 | Employee Dashboard | Implement employee role dashboard | Done |
| INV-1305 | Role-Based Menu Access | Restrict modules based on user role | Done |
| INV-1306 | Change Password | Allow users to change password securely | Done |
| INV-1307 | Logout Module | Implement common logout functionality | Done |
| INV-1308 | Testing & Documentation | Complete testing and sprint documentation | Done |


---

# INV-1301 Main Login Menu

## Completed Tasks

- Created Inventory Management Login Screen
- Added Username and Password validation
- Connected login with UserService
- Added Exit option

Status:

✅ Completed


---

# INV-1302 Admin Dashboard

## Completed Tasks

- Created admin_dashboard.py
- Added Admin menu
- Added full module access

Admin Access:

- Product Management
- Supplier Management
- Customer Management
- Purchase Management
- Sales Management
- Order Management
- User Management
- Dashboard


Status:

✅ Completed


---

# INV-1303 Manager Dashboard

## Completed Tasks

- Created manager_dashboard.py
- Added Manager menu
- Restricted User Management access


Manager Access:

- Product Management
- Supplier Management
- Customer Management
- Purchase Management
- Sales Management
- Order Management
- Dashboard


Status:

✅ Completed


---

# INV-1304 Employee Dashboard

## Completed Tasks

- Created employee_dashboard.py
- Added employee limited menu
- Restricted admin features


Employee Access:

- Product View
- Customer View
- Sales Entry
- Order View


Status:

✅ Completed


---

# INV-1305 Role-Based Menu Access

## Completed Tasks

- Created role_permission.py
- Added role permissions
- Implemented permission checking


Roles:

Admin:
- Full Access


Manager:
- Business Modules Access


Employee:
- Limited Access


Status:

✅ Completed


---

# INV-1306 Change Password

## Completed Tasks

- Created change_password.py
- Added old password validation
- Updated password in database
- Integrated with main login flow


Status:

✅ Completed


---

# INV-1307 Logout Module

## Completed Tasks

- Created logout.py
- Implemented common logout function
- Integrated logout with user menu


Status:

✅ Completed


---

# INV-1308 Testing & Documentation

## Completed Tasks

- Tested Admin Login
- Tested Manager Login
- Tested Employee Login
- Tested Invalid Login
- Tested Change Password
- Tested Logout
- Updated Sprint Documentation


Status:

✅ Completed


---

# Files Created / Updated


Created:

- admin_dashboard.py
- manager_dashboard.py
- employee_dashboard.py
- role_permission.py
- change_password.py
- logout.py
- sprint13.md


Updated:

- main.py
- user_service.py
- user_repo.py


---

# Technology Used

- Python
- SQL Server
- pyodbc
- Repository Pattern
- Service Layer
- Git


---

# Sprint 13 Final Result

Authentication and Role Management module completed successfully.

All users can:
- Login
- Access role-based dashboard
- Change password
- Logout securely


Sprint Status:

✅ COMPLETED