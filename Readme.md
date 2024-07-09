# E-Invite App

An application for creating and managing electronic invitations using Django and React.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The E-Invite App is a web application that allows users to create and manage electronic invitations. Users can design invitation cards, generate QR codes for invites, and send invitations via email.

## Features

- User authentication and authorization
- Create, view, and manage invitations
- Generate QR codes for invites
- Send invites via email
- Download designed invitation cards

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Frontend:** React, Axios, React Router DOM
- **Database:** SQLite (for development), PostgreSQL (for production)
- **Styling:** CSS, Bootstrap
- **Others:** Docker, Nginx

## Installation

### Prerequisites

- Python 3.7 or higher
- Node.js and npm
- Docker (for production deployment)

### Backend

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/invite_app.git
   cd invite_app

## Backend configuration

  - Create a Virtual Enviroment
  - python -m venv env
  - source `env/bin/activate`   
  - On Windows use `env\Scripts\activate`

1. Install Backend Dependencies
   ```sh
   pip install -r requirements.txt

2. Django Settings
  - Configure your `settings.py` with your database and other settings
    ```sh
    invite_project/settings.py
  `DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
  }

    ALLOWED_HOSTS = [localhost, 127.0.0.1]

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`
    EMAIL_HOST = 'smtp.gmail.com'`
    EMAIL_PORT = 587`
    EMAIL_USE_TLS = True`
    EMAIL_HOST_USER = 'your-email@gmail.com'`
    EMAIL_HOST_PASSWORD = 'your-app-password'`

3. Run Migrations
   ```sh
   python `manage.py migrate`

4. Create a Superuser
    ```sh 
    python `manage.py createsuperuser`

5. Run the Django Development Server
    ```sh 
    python `manage.py runserver`

## Frontend Configuration

- Navigate to the Frontend Directory
  ```sh
  `cd Frontend/invite-app

- Install Frontend Dependency
  ```sh
  `npm install

- Start the Frontend Development Server
  ```sh
  `npm start

### Running the Application

- Ensure that both the backend and frontend servers are running.
- Access the application at http://localhost:3000.


### API Endpoints

#### Auth Endpoints

- POST /api/auth/login/ - Login a user
- POST /api/auth/register/ - Register a new user
- POST /api/auth/refresh/ - Refresh JWT token

### Invite Endpoints

- POST /api/invites/ - Send an invite
- GET /api/invites/ - Get all invites

### Configuration

#### Environment Variables
   - Create a .env file in the root directory of your project and add the following environment variables:
   - SECRET_KEY= `your_secret_key`
   - DEBUG= True
   - ALLOWED_HOSTS= `localhost,127.0.0.1`
   - EMAIL_BACKEND= `django.core.mail.backends.smtp.EmailBackend`
   - EMAIL_HOST= `smtp.gmail.com`
   - EMAIL_PORT= 587
   - EMAIL_USE_TLS= True
   - EMAIL_HOST_USER= `your_email@gmail.com`
   - EMAIL_HOST_PASSWORD= `your_app_password`

### Usage
 #### Sending Invites
    - Register and log in to your account.
    - Create a new invitation.
    - Fill in the invite details and design your card.
    - Generate a QR code for the invite.
    - Send the invite via email.

### License
- This project is licensed under the MIT License.

