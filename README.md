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
- Manage tasks using a profile with an editable profile picture and display name.
- Access the application via secure role-based authentication.

This project demonstrates the full-stack development of a web application using Django, and follows the principles of good UX design, security practices, and data handling.

## Features

- **User Registration & Login**: Users can sign up, log in, and log out securely. Passwords are hashed, and sensitive data is stored securely.

- **Task Management**: Users can add, edit, delete, and mark tasks as complete. Each task includes a title, description, date, and time.

- **Profile Management**: Users can update their profile picture and display name, which is shown on the task page next to their profile picture.

- **Username/Display Name Display**: The app dynamically displays either the user's username or their display name (if set) in the task list header.

- **Calendar Integration**: Tasks are displayed on a calendar view, allowing users to visualize their tasks by date.

- **Holiday Integration**: The app fetches holidays via an external API and displays them on the task calendar.

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
2. **Profile Page** - Allows users to update their profile picture and display name.
3. **Task Calendar** - Visualizes tasks on a calendar interface.

### Wireframes

Here are some wireframes representing the design of the application for desktop and mobile views:

1. **Desktop Wireframe**
   
   ![Desktop Wireframe](images/to-do-list-desktop-wireframe.png)

2. **Mobile Wireframe**
   
   ![Mobile Wireframe](images/to-do-list-phone-wireframe.png)

## Database Schema and Relationships

The database schema consists of three primary relationships:
1. **User - Profile**: A one-to-one relationship where each `User` has one `Profile`. The `Profile` stores additional information like the profile picture, display name, and username.
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

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Apply Migrations**:
   ```bash
   python manage.py migrate

4. **Create Superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser

5. **Run the Server**:
   ```bash
   python manage.py runserver      

## Deployment
### To deploy the application, you can use platforms such as:

- Heroku

- DigitalOcean

- AWS


## Testing

#### Testing for this project involved:

- **Unit Tests**: Written for individual components like task creation, task completion, profile updates, etc.

- **Integration Tests**: Ensure that various parts of the application (e.g., task management and calendar integration) work together correctly.

- **Manual Testing**: Performed for responsive design and user interactions across different devices.


## Technologies Used
**Frontend**:
- HTML5

- CSS3

- Bootstrap 5

**Backtend**:
- Python

- Django

**Database**:
- SQLite (for development)

- PostgreSQL (for production)

**Other Technologies**:
- Cloudinary (for profile picture storage)

- FullCalendar.js (for calendar integration)

- JavaScript (for handling dynamic interactions)

**Version Control**:
- Git

## Security Considerations
- **CSRF Protection**: Implemented via Django's built-in CSRF tokens.

- **Password Hashing**: Django’s authentication system securely hashes passwords.

- **Data Validation**: Forms are validated on both the client and server sides to prevent malicious input.

## Future Enhancements
- **Performance-Based Statistics**: Users can see insights and statistics based on their task completion performance.

- **Light/Dark Mode Toggle**: Users can switch between light and dark modes for better readability based on their preferences.

- **Push Notifications**: Implement push notifications to remind users of their tasks.

- **Task Categorization**: Allow users to categorize tasks with labels like "Work", "Personal", etc.

- **Task Prioritization**: Implement a priority feature to order tasks based on urgency.

- **Collaboration Features**: Add the ability for users to share tasks with others or collaborate on group projects.

## User Stories

- **As a user**, I want to create tasks with a title, description, date, and time so I can manage my schedule.

- **As a user**, I want to mark tasks as complete so I can track my progress.

- **As a user**, I want to update my profile picture and display name to personalize my account.

- **As a user**, I want to view my tasks on a calendar so I can see them by date.

- **As a user**, I want to toggle between light and dark modes based on my preference.

## Challenges & Solutions

- **User Authentication**: Implementing secure user authentication and role management was a challenge. This was solved by using Django’s built-in authentication system and customizing it for the project.


- **Responsive Design**: Ensuring that the application worked seamlessly on all screen sizes required careful testing and media queries. Bootstrap was instrumental in helping achieve this.


- **Calendar Integration**: Integrating FullCalendar.js with Django to display tasks required converting task data to a JSON format. This was solved by using Django’s DjangoJSONEncoder to serialize the task data properly.


## Acknowledgements

- **Django Documentation**: For providing excellent resources on building full-stack applications.

- **Bootstrap**: For offering a responsive framework that made UI design easier.

- **FullCalendar.js**: For providing a robust calendar integration.

## License
The MIT License (MIT)
Copyright © 2024 <Lewis Freeman>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.