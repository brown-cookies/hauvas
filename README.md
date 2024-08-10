# Hauvas++ LMS

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
  - [Course Management](#course-management)
  - [User Management](#user-management)
  - [Assessment and Grading](#assessment-and-grading)
  - [Communication Tools](#communication-tools)
- [Technology Stack](#technology-stack)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Database](#database)
  - [Caching](#caching)
  - [Hosting and Deployment](#hosting-and-deployment)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)


## [Overview](#overview)

**Hauvas++** is a comprehensive Learning Management System (LMS) built using Django, a high-level Python web framework. Designed to facilitate online education, Hauvas++ offers a robust platform for course management, student tracking, and educational content delivery. In addition to its core LMS features, Hauvas also supports a to-do app, event listing, and student grading functionalities, making it a versatile tool for both educators and learners.


## [Key Features](#key-features)

### [Course Management](#course-management)
- **Course Creation**: Easily create and manage courses, including modules, lessons, and quizzes.
- **Content Delivery**: Support for various types of content, including text and file uploads.
- **To-Do App Integration**: Allows students and instructors to manage tasks and deadlines efficiently.
- **Event Listing Integration**: A centralized calendar for listing and tracking academic events, deadlines, and activities.
- **Student Grading**: Comprehensive tools for grading assignments, quizzes, and exams, with integrated gradebook functionality.
- **Scheduling**: Flexible scheduling options for classes, assignments, and assessments.

### [User Management](#user-management)
- **Roles and Permissions**: Different user roles such as admin, instructor, and student, each with customizable permissions.
- **User Profiles**: Detailed user profiles with information.

### [Assessment and Grading](#assessment-and-grading)
- **Assignments, Quizzes, and Exams**: Tools for creating, administering, and grading assignments, quizzes and exams. (Tentative feature on quizzes and exams)
- **Assignment Submission**: Platforms for students to submit assignments and for instructors to provide feedback.
- **Gradebook**: Integrated gradebook for tracking student performance and progress.

### [Communication Tools](#communication-tools)
- **Announcements**: Centralized announcement board for course updates and important information.
- **Discussion Forums**: Forums for student interaction, questions, and discussions.
- **Inbox**: A gmail-like email application for student and professor nteraction, questions, and discussions.

## [Technology Stack](#technology-stack)

### [Backend](#backend)
- **[Django](https://www.djangoproject.com/)**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **[Django Grappelli Admin](https://django-grappelli.readthedocs.io/en/latest/)**: A customize admin panel.
- **[Django REST Framework](https://www.django-rest-framework.org/)**: Provides powerful and flexible tools for building web APIs.
- **[Django Haystack](https://django-haystack.readthedocs.io/en/master/)**: Provides powerful powerful and modular tools for managing modular search query.
- **[Django View Components](https://django-viewcomponent.readthedocs.io/en/latest/overview.html)**: Provides provides a way to create reusable components.

### [Frontend](#frontend)
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For creating dynamic and interactive user experiences.
- **[Bootstrap](https://getbootstrap.com/)**: For responsive design and pre-built UI components.
- **[Mazer](https://github.com/zuramai/mazer)** For easy integration of Dashboard that can help develop faster. Made with Bootstrap 5.
    - **_NOTE:_** This requires in-depth knowledge on HTML/CSS/BOOTSTRAP for Django implementation
    - **_NOTE:_** This requires Reverse Engineering Techniques
- **[jQuery](https://jquery.com/)**: For simplifying HTML document traversal and manipulation, event handling, and animations.
- **[PerfectScrollbar](https://github.com/mdbootstrap/perfect-scrollbar)**: For custom scrollbar styling and smooth scrolling.
- **[Quill](https://quilljs.com/)**: A rich text editor for creating and editing content.
- **[ToastifyJS](https://apvarun.github.io/toastify-js/)**: For showing customizable toast notifications.
- **[SweetAlert](https://sweetalert.js.org/)**: For beautiful, responsive, and customizable alerts.
- **[DataTables.net](https://datatables.net/)**: A powerful plugin for enhancing HTML tables with advanced features.
- **[Choices.js](https://choices-js.github.io/Choices/)**: For customizable select boxes and input fields.
- **[FilePond](https://pqina.nl/filepond/)**: For elegant and customizable file upload components.
- **[Bootstrap Icons](https://icons.getbootstrap.com/)**: For a wide range of icons integrated with Bootstrap.
- **[FontAwesome](https://fontawesome.com/)**: For scalable vector icons and social logos.


### [Database](#database)
- **SQLite**: For lightweight, embedded database solutions during development. (First approach)
- **PostgreSQL**: A powerful, open-source object-relational database system. (Planning to switch later)

### [Caching](#caching)
- **Redis**: A powerful, open-source for caching web pages, and datas for increased performance

### [Hosting and Deployment](#hosting-and-deployment) (Finals na namin decide ano gagamitin)
- **Azure**: App service
- **Upstash Redis**: Redis cache

## [Getting Started](#getting-started)

### [Prerequisites](#prerequisites)
- **Python 3.10+**
- **Django 5.0+**

### [Installation](#installation)

1. Clone the repository:
    ```bash
    git clone https://github.com/<your github username>/hauvas.git
    cd hauvas
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate virtual environment:
      Windows:
     ```bash
      venv/Scripts/activate
      ```
     MacOS and Linux:
     ```bash
      . venv/bin/activate
      ```
   - **_NOTE:_** your terminal should have ``` (venv) ``` indicating that venv is active.
   
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:
    ```bash
    python manage.py migrate
    ```

7. Create Superuser:
   ```bash
    python manage.py createsuperuser
    ```
   - **_NOTE:_** Fill up the form (do not forget it as you will need to access admin)

8. Visit Admin panel at [127.0.0.1:8000](127.0.0.1:8000) and login to your newly created super user:

9. Create user account with username, password:
  - **_NOTE:_** do not forget this as you will need to login to the dashboard and start designing the application
11. Go to Profile table and create profile that correspond to the user account (make sure that it is a professor type)
12. Lastly go to Professor table and create a professor that correspond to user

7. Run the development server:
    ```bash
    python manage.py runserver
    ```
8. Visit [127.0.0.1:8000](127.0.0.1:8000)
