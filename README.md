# Work Time Manager (WTM)

A Django-based web app for tracking employee work hours across projects and regions.

## Features
- Project CRUD with unique job numbers
- Job number prefix validation by region (EMEA, APAC, NA, LATAM)
- Employee profile and role management
- Daily work logging with task descriptions and hours
- Dashboard with basic workload stats
- Job numbers are locked after creation

## Tech Stack
- Django 6.0.1
- PostgreSQL
- Bootstrap 5

## Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/vyankov84/work_time_manager.git
   cd work_time_manager
```

2. **Create and activate a virtual environment:**
```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Create a `.env` file in the root directory:**
```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=127.0.0.1
   DB_PORT=5432
```

5. **Apply migrations:**
```bash
   python manage.py migrate
```

6. **Create a superuser:**
```bash
   python manage.py createsuperuser
```

7. **Run the server:**
```bash
   python manage.py runserver
```