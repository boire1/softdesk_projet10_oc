# SoftDesk

SoftDesk is an API built with Django REST framework for project management and issue tracking, divided into three key sub-applications.

    user_app handles user management, authentication, as well as profiles and permissions.

    proj_contrib_app is dedicated to project and contributor management, allowing for the creation of projects and the assignment of roles and responsibilities to project members.

    issue_com_app focuses on tracking and managing issues related to a project, offering features to comment, prioritize, and tag these issues, while also associating each issue with an author and an assigned contributor.


## Prerequisites
- Python (version 3.11)
- Django (version 4.2)

## Installation
Install Python 3.11.
In your directory, open the console.

Clone this repository.
`git clone https://github.com/boire1`

2. Navigate to the project directory: `cd rep....`.

    In this directory `rep...`, create a virtual environment.

    Type: `python -m venv env`.

    (To activate the environment on Windows) Type:` env\scripts\activate`.

    Install the dependencies: `pip install -r requirements.txt`.

    Navigate to the project's root directory (where `manage.py` is located).

## Usage

1.    Start the development server: `python manage.py runserver`.

2.    Retrieve the address `http://127.0.0.1`, then paste it into our browser.

## Features


n this `SoftDesk API`, users can `sign up`, `log in`, and `manage projects`, `issues`, and `comments`. 
They can `create projects` and `become contributors` to existing projects. 
They can also `add, view, edit, or delete` `issues and comments`, but only in `projects` where they are `contributors` or for which they are the `authors`. 
Session security is ensured by `JWT`, and users have the option to `log out`.
The API provides stringent access control to ensure that users can only interact with authorized resources.