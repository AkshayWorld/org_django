Multi-Organizational Management System with Role Management
A Django-based web application to support multiple organizations, each with its own users and role-based management.

Overview
This system supports multiple organizations with features like:

A Main Organization (e.g., "Admin Organization") to oversee sub-organizations.
Role-based management for users within each organization.
Admins of sub-organizations can manage their users and assign roles.

Features
Organizational Management: Create, update, and delete organizations.
User Management: Add, view, update, and delete users within an organization.
Role Assignment: Assign roles to users, restricting their access and permissions.
Custom User Model: Extend Django's AbstractUser to include organization and role.

Built With
Django - High-level Python web framework.
MySQL 
