# Video Storing Platform Readme

## Project Overview

This repository hosts the source code for a straightforward Video Storing Platform. The platform is divided into two major components:

- **Backend:** Developed using Django Rest Framework, this component handles the server-side logic, database management, and API endpoints for video management.

- **Frontend:** Built with Vue.js, this part of the project provides a user-friendly interface for uploading, viewing, and managing videos on the platform.


- `backend/` contains the Django backend code for managing video data, authentication, and API endpoints. It also includes a `requirements.txt` file, listing the required Python packages and dependencies for the backend.

- `frontend/` comprises the Vue.js frontend code for creating an interactive and engaging user interface for the Video Storing Platform.

## Installation

To set up and run the project, follow these steps:

### Backend (Django)

1. Navigate to the `backend/` directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended) and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the required Python packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
7. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
The Django backend should now be accessible at http://localhost:8000/.

### Frontend (Vue.js)
1. Navigate to the frontend/ directory:
   ```bash
   cd frontend
   ```
2. Make sure you have Node.js and npm installed on your system.
3. Install the required frontend dependencies:
   ```bash
   npm install
   ```
4. Start the Vue.js development server:
   ```bash
   npm run serve
   ```
The Vue.js frontend should now be accessible at http://localhost:8080/.
