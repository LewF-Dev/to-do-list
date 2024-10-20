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

This application is deployed on Heroku, a cloud-based platform ideal for deploying full-stack applications. Below are the steps taken to deploy the project, including the necessary commands and configurations. These steps can be used by anyone looking to replicate the deployment process.

### Prerequisites

- Ensure you have a Heroku account and the Heroku CLI installed.

- Set up a PostgreSQL database (e.g., with Heroku Postgres or another managed database 
  provider) since this project uses PostgreSQL in production.

### Step-by-Step Deployment Guide

1. ***Create a New Heroku App***:

   ```bash
   heroku create <your-app-name>
-This command initializes a new Heroku app and sets up a remote Git repository that 
 points to Heroku.

2. ***Set Up Environment Variables***:
- In Heroku, navigate to your app dashboard.
- Under "Settings," click on "Reveal Config Vars."
- Add the following environment variables:

  - `DATABASE_URL`: The URL of your PostgreSQL database.

  - `SECRET_KEY`: A unique Django secret key.
  - Any other sensitive variables from `env.py`, such as API keys for third-party services.


3. ***Prepare the Application for Deployment***:
- Make sure the `Procfile` is set up with:

   ```plaintext
   web: gunicorn <your_project_name>.wsgi
- Ensure `requirements.txt` includes `gunicorn` for running the app in a production environment.  

4. ***Update Django Settings for Production***:
- Set `DEBUG = False` in your `settings.py` to prevent detailed error messages in production.
- Allow Heroku's domain in `ALLOWED_HOSTS`:

   ```python
   ALLOWED_HOSTS = ['<your-app-name>.herokuapp.com']
5. ***Deploy to Heroku***:
- Commit any final changes:
   ```bash
   git add .
   git commit -m "Prepare for Heroku deployment"
- Push to Heroku:
   ```bash
   git push heroku main
6. ***Run Database Migrations***:
- Once deployed, run the following commands to apply database migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
7. ***Collect Static Files***:
- Run the `collectstatic` command to gather static files for production:
   ```bash
   heroku run python manage.py collectstatic --noinput
8. ***Open the Application***:
- After deployment is complete, you can open your app with:
   ```bash
   heroku open
**Testing deployment**

After deploying, verify that the production app behaves as expected by testing all features, such as task management, profile updates, and calendar functionality. Ensure there are no debug messages visible in production, and that all sensitive information is secure.

## Testing

Testing for this project involved various levels of validation, including unit tests, integration tests, and detailed manual testing. Each test case was designed to assess functionality, usability, responsiveness, and data management across the entire web application. Below are the structured test cases conducted.

### 1. Unit Tests
Unit testing was conducted for individual components and functions within the application. These tests primarily focused on verifying the correct behavior of key functions and methods:

- **Task Creation**: Ensured that tasks could be created with the correct attributes (title, description, date, and time).
- **Task Completion**: Verified that the task status updates correctly when marked as complete.
- **Profile Updates**: Ensured that users can update their profile picture and display name without issues.

These tests isolated specific functionalities, confirming each component worked as intended independently of the others.

### 2. Integration Tests
Integration tests were performed to validate the proper interaction between different parts of the application, ensuring seamless functionality across the stack:

- **Task Management and Calendar Integration**: Verified that task data could be serialized and displayed on the calendar, confirming tasks appear on the correct dates.
- **Profile Management and Task List**: Checked that the user’s display name and profile picture are reflected in the task list and user header in real-time.

These tests ensured that various sections of the application could interact correctly, reducing potential bugs from interconnected components.

### 3. Manual Testing
The manual testing process involved objective, detailed test cases to verify expected outcomes for typical user actions. Both expected and unexpected scenarios were tested to verify how the application handles different flows.

#### Test Cases

| Test Case                          | Expected Outcome                                                                 | Steps                                                                                                                                                          | Result                                                                                       |
|------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **1. Login Functionality**         | User should be able to log in successfully with correct credentials               | 1. Go to login page<br>2. Enter valid credentials<br>3. Click login button                                              | User logged in successfully and redirected to home page.                                     |
|                                    | Error message shown for incorrect credentials                                    | 1. Go to login page<br>2. Enter incorrect credentials<br>3. Click login button                                          | Error message displayed: "Please enter a correct username and password. Note that both fields may be case-sensitive.".                                     |
| **2. Task Creation**               | User should be able to create a task                                             | 1. From the home page, click the "Add Task" button<br>2. Fill out title, description, date, and time<br>3. Click "Add Task"                     | Task appears on home page and in the calendar view. Notification appears at the top of the page saying "Task created successfully!".                                          |
|                                    | Error message for missing required fields                                        | 1. Click the "Add Task" button<br>2. Leave title empty<br>3. Click "Add task"                                              | Error message displayed: "Please fill in this field".                                           |
| **3. Task Completion**             | User should be able to mark a task as complete                                   | 1. Go to home page<br>2. Click "Complete" button on an existing task                                                    | Task status updated to complete, task moves to completed section, notification saying "Task marked as completed!" appears at the top of the screen.                            |
| **4. Task Deletion**               | User should be able to delete a task                                             | 1. Go to home page<br>2. Click "Delete" button on an existing task<br>3. Confirm deletion                               | Task is removed from the home page and calendar view, notifcation saying "Task deleted successfully!" appears at the top of the screen.                                        |
| **5. Profile Update**              | User should be able to update profile picture and display name                   | 1. Click the user option in the navigation bar<br>2. Click the profile option in the dropdown menu<br>3. Change display name and choose an image file to be used as your profile picture<br>4. Click "Update Profile"                       | Profile picture and display name update successfully, notification saying "Profile updated successfully!" appears at the top of the screen.          |
| **6. Error Handling on Forms**     | Error messages should appear for invalid inputs                                  |                                | The date and time options for tasks only accept numeric inputs and no other pages consider any characters as invalid inputs,  therefore a situation where the user has used invalid inputs cannot occur.                             |
| **7. Calendar Date Selection**     | User should be able to navigate to specific dates on the calendar and see any tasks or events that are on said date.                             | 1. Go to the calendar view by pressing the calendar button at the top right of the home page.<br>2. Use the on-screen arrow buttons to navigate to different months.                                                                          | Holiday periods, events and date-specific tasks are displayed on the correct dates, user can click on a specific task or event in the calendar view to see more information.                                      |
| **8. Responsiveness Testing**      | Layout should adjust for mobile and desktop views                                | 1. Resize browser window to different screen sizes (mobile, tablet, desktop)                                            | Layout adapts properly, displaying content without overflow or cut-off issues.               |
| **9. Logout Functionality**        | User should be able to log out successfully                                      | 1. Click on "User" in the navigation bar at the top left of any page, this will open a dropdown menu.<br>2. In the dropdown menu click "Logout"                                                                               | User is logged out and redirected to login page.                                             |
| **10. On-Screen Notifications**    | Notifications should appear for each CRUD operation                              | 1. Perform any CRUD operation (add, edit, delete task)<br>2. Observe notification                                      | Notifications appear at the top of the page confirming success of operation (e.g., "Task created successfully"). |

#### Observed Results
Each test was conducted following the documented steps, and results matched expected outcomes. Any discrepancies were documented and resolved through code adjustments.

#### Edge Cases
**Calendarific API rendering issue**: During testing, it was observed that when opening the calendar modal, the Calendarific API data wasn't properly rendering in the calendar view on initial load. This led to the calendar appearing blank until the browser window was resized or manually refreshed. Upon investigation, the issue was found to be related to the calendar’s rendering mechanism. The calendar was being initialized before the modal was fully displayed and ready, which caused it to miscalculate its dimensions and appear empty.

- ***Resolution***: To resolve this issue, the calendar’s rendering function was tied to the modal’s `shown` event. By attaching the `calendar.render()` function to the event listener that triggers when the modal is fully displayed, the calendar is now properly rendered every time the modal is opened. The following code was added to handle this:

```javascript
document.getElementById('calendarModal').addEventListener('shown.bs.modal', function () {
    calendar.render();
});
```
<br>

**Profile Creation Issue**: During testing, I encountered an error when a newly registered user attempted to log in. The error occurred because the application was trying to access the user's profile, but no profile had been created yet. This resulted in an exception and prevented users from accessing the app immediately after signing up.

- ***Resolution***: To resolve this issue, I implemented Django signals to ensure that a `Profile` object is automatically created for every new user when they sign up. Using the `post_save` signal, a profile is created when a new `User` object is saved. This ensures that users have a profile upon their first login, avoiding any access issues related to missing profiles.

<br>

**Cloudinary API Configuration Error**: While integrating Cloudinary for media file storage, I encountered an error during profile image uploads. The error was related to missing Cloudinary API configuration values, causing the app to crash when attempting to handle image uploads.

- ***Resolution***: I resolved this by ensuring that the necessary Cloudinary API credentials (`CLOUD_NAME`, `API_KEY`, `API_SECRET`) were added correctly in the environment variables and referenced in the `settings.py` file. I also verified that these variables were correctly set on the hosting platform (Heroku).

<br>

**Invalid Signature Error with Cloudinary**: During testing, I received an "Invalid Signature" error from Cloudinary when uploading images. This occurred because the signature generation for the image uploads was failing due to mismatched or incorrect API credentials.

- ***Resolution***: The issue was resolved by regenerating the Cloudinary API keys, ensuring that the correct values were used in both the environment variables and the Cloudinary dashboard. I also confirmed that the Cloudinary URL in the environment variables matched the correct API configuration.

<br>

**Static Files Not Loading Properly in Production**: In production, I encountered an issue where static files (like CSS and JavaScript) were not loading correctly, causing the site layout to break. This was due to the fact that static files weren't being served properly in the Heroku environment.

- ***Resolution***: I resolved this by adding the `Whitenoise` middleware to the Django settings, ensuring that static files are served correctly in production. Additionally, I verified that the `STATIC_ROOT`, `STATICFILES_DIRS`, and `STATIC_URL` settings were properly configured in the `settings.py` file. I also ran `collectstatic` to gather all static files into a single location for production.


### Summary
Most test cases passed as expected, demonstrating the functionality of the application in typical use cases. For the few issues encountered, fixes were implemented as documented in the edge cases section, ensuring the application operates as intended after resolving those challenges.


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

## Agile Methodology and Project Management

**User Stories**

To effectively manage the development of this project, I chose to use Trello as my Agile project management tool. Trello allowed me to organize user stories, track tasks, and manage the workflow efficiently through different stages of development, from "To Do" to "Done." Below is a screenshot of my Trello board, demonstrating how I planned and executed the project using Agile practices.

[Trello Board](https://trello.com/invite/b/66adefdd1707236be0e94b4d/ATTI24b3f9b97614f96cd95dbadc9b8a0d3dFD3C2BF6/to-do-list)

![Mobile Wireframe](images/trello-board-screenshot-to-do-list-project.png)

## Challenges & Solutions

- **User Authentication**: Implementing secure user authentication and role management was a challenge. This was solved by using Django’s built-in authentication system and customizing it for the project.


- **Responsive Design**: Ensuring that the application worked seamlessly on all screen sizes required careful testing and media queries. Bootstrap was instrumental in helping achieve this.


- **Calendar Integration**: Integrating FullCalendar.js with Django to display tasks required converting task data to a JSON format. This was solved by using Django’s DjangoJSONEncoder to serialize the task data properly.


## Acknowledgements

- **Django Documentation**: For providing excellent resources on building full-stack applications.

- **Bootstrap**: For offering a responsive framework that made UI design easier.

- **FullCalendar.js**: For providing a robust calendar integration.

- **ChatGPT**: for providing valuable insights, coding assistance, and answering technical queries throughout the development process. Its guidance was instrumental in overcoming challenges and enhancing the functionality of the application.



## License
The MIT License (MIT)
Copyright © 2024 Lew-F Dev

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.