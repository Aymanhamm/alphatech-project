# Alphatech Solutions - Employee Management System

A comprehensive Employee Management System built with Django for Alphatech Solutions.

## Features

- Employee Management
  - Employee profiles with photos
  - Department management
  - Position management
  - Contract management
- Task Management
  - Task assignment and tracking
  - Task status updates
- Leave Management
  - Leave requests
  - Leave balance tracking
- Payroll Processing
  - Salary calculations
  - Payment history
- Performance Evaluation
  - Employee performance tracking
  - Evaluation forms
- Report Generation
  - Various employee reports
  - Export capabilities

## Prerequisites

- Python 3.8+
- MySQL Server
- Visual C++ Build Tools (for mysqlclient installation)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd alphatech-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure MySQL Database:
   - Install MySQL Server
   - Create a database named 'alphatech_db'
   - Update the database settings in `alphatech/settings.py`

5. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Database Setup

1. Install MySQL Server:
   - Download from: https://dev.mysql.com/downloads/mysql/
   - During installation, note down the root password
   - Create a database named 'alphatech_db'

2. Install Visual C++ Build Tools:
   - Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

3. Update database settings in `alphatech/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alphatech_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Configuration

1. Update the following settings in `alphatech/settings.py`:
   - `SECRET_KEY`: Change to a secure random string
   - `ALLOWED_HOSTS`: Add your domain or IP address
   - `DATABASES`: Update MySQL database credentials
   - `STATIC_URL` and `STATIC_ROOT`: Configure static files
   - `MEDIA_URL` and `MEDIA_ROOT`: Configure media files

2. Create a `.env` file for environment variables if needed

## Usage

1. Access the application at: http://localhost:8000
2. Login with your credentials
3. Navigate through the different modules using the navigation menu

## Project Structure

```
alphatech-project/
├── alphatech/              # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI config
├── employees/             # Employee management app
├── tasks/                # Task management app
├── leaves/               # Leave management app
├── payroll/             # Payroll processing app
├── performance/         # Performance evaluation app
├── reports/             # Report generation app
├── static/              # Static files
│   ├── css/            # CSS styles
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
└── templates/          # HTML templates
```

## Security

- Password validation is enabled
- CSRF protection is enabled
- Secure middleware is configured
- User authentication is required for most features
- Role-based access control is implemented

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the development team.
