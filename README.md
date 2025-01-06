# ZenFlow

Welcome to **ZenFlow**, the Freelance Collaboration Management System. ZenFlow is designed to help manage freelance collaborations by providing functionalities for managing users, projects, tasks, and invoices.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User management with roles (Client, Freelancer, Project Manager)
- Project management
- Task management
- Invoice management
- Token-based authentication for secure API access

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.6+
- Django 3.2+
- pip (Python package installer)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/zenflow.git
    cd zenflow
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser to see the application running.

## Usage

### Home Page

The home page provides an overview of the system and links to different sections like Users, Projects, Tasks, and Invoices.

### API Authentication

To access protected API endpoints, you need to authenticate using a token. Obtain a token by sending a POST request to the `api-token-auth/` endpoint with your username and password.

```bash
curl -X POST -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/api-token-auth/
