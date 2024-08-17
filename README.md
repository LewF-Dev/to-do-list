# To-Do List Application

## Overview

The To-Do List application is a full-stack web application built using the Django framework. It allows users to create, manage, and track their daily tasks. The application implements user authentication, including registration, login, and role-based permissions. Users can add, edit, delete, and mark tasks as complete. The app is responsive and designed with a user-friendly interface that adheres to accessibility guidelines and UX principles.

## Table of Contents

1. [Project Purpose](#project-purpose)
2. [Features](#features)
3. [UX Design](#ux-design)
4. [Data Model](#data-model)
5. [Installation and Setup](#installation-and-setup)
6. [Deployment](#deployment)
7. [Testing](#testing)
8. [Technologies Used](#technologies-used)
9. [Security Considerations](#security-considerations)
10. [Future Enhancements](#future-enhancements)
11. [User Stories](#user-stories)
12. [Challenges & Solutions](#challenges--solutions)
13. [Acknowledgements](#acknowledgements)
14. [License](#license)

## Project Purpose

The purpose of this project is to develop a responsive and accessible to-do list application where users can:
- Create, update, and delete tasks.
- Track task completion.
- Manage tasks using a profile with an editable profile picture.
- Access the application via secure role-based authentication.

This project demonstrates the full-stack development of a web application using Django, and follows the principles of good UX design, security practices, and data handling.

## Features

- **User Registration & Login**: Users can sign up, log in, and log out securely. Passwords are hashed, and sensitive data is stored securely.
- **Task Management**: Users can add, edit, delete, and mark tasks as complete. Each task includes a title, description, date, and time.
- **Profile Management**: Users can update their profile picture and manage their personal details.
- **Calendar Integration**: Tasks are displayed on a calendar view, allowing users to visualize their tasks by date.
- **Performance-Based Statistics**: Users can see insights and statistics based on their task completion performance.
- **Responsive Design**: The application is fully responsive and accessible, ensuring a good user experience across all devices.

## UX Design

### Target Audience
- Busy individuals looking for a simple tool to organize and manage their daily tasks.
- Users who value a streamlined, no-nonsense interface with minimal distractions.

### Wireframes and Design Decisions

The application's design is based on the principles of good UX:
- **Information Hierarchy**: Tasks and controls are clearly organized for ease of use. Priority tasks are emphasized.
- **User Control**: All user interactions provide immediate feedback. For example, when tasks are completed, the user receives confirmation.
- **Accessibility**: The design follows accessibility guidelines, ensuring proper color contrast, keyboard navigability, and screen reader compatibility.

### Mockups
Mockups for each page of the application, including:
1. **Home Page** - Displays tasks and allows interaction (edit, delete, complete).
2. **Profile Page** - Allows users to update their profile picture and details.
3. **Task Calendar** - Visualizes tasks on a calendar interface.

### Wireframes

Here are some wireframes representing the design of the application for desktop and mobile views:

1. **Desktop Wireframe**
   
   ![Desktop Wireframe](images/to-do-list-desktop-wireframe.png)

2. **Mobile Wireframe**
   
   ![Mobile Wireframe](images/to-do-list-phone-wireframe.png)

## Database Schema and Relationships

The database schema consists of two primary relationships:
1. **User - Profile**: A one-to-one relationship where each `User` has one `Profile`. The `Profile` stores additional information like the profile picture and bio.
2. **User - Task**: A one-to-many relationship where each `User` can have many `Tasks`, but each `Task` belongs to only one `User`.

### ERD (Entity-Relationship Diagram)

The following ERD diagram illustrates the relationships between the main entities in the database schema. It shows the `User`, `Profile`, and `Task` tables, and the relationships between them.

![Database Schema ERD](images/to-do-list-erd-diagram.png)

- **User - Profile**: There is a one-to-one relationship between the `User` and `Profile` tables. Each user has exactly one profile.
- **User - Task**: There is a one-to-many relationship between the `User` and `Task` tables. Each user can have multiple tasks, but each task is associated with only one user.

This schema is designed to manage users' tasks efficiently, ensuring that each user can maintain their own profile and manage multiple tasks seamlessly.

## Installation and Setup

### Prerequisites
- Python 3.x
- Django 4.x
- Git

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/todo-list.git
   cd todo-list
