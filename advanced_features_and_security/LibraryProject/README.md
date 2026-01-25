# Permissions and Groups Setup

## Custom Permissions
The Book model defines the following permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups were created using Django Admin:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: all permissions

## Views Protection
Views are protected using Django's permission_required decorator to ensure only authorized users can access create, edit, and delete actions.






# LibraryProject

This is a basic Django project created for the ALX Django learning task.

## Description
This project demonstrates:
- Django installation
- Project creation
- Running the Django development server

## Usage
To start the development server:



