# Static Files Structure

This directory contains all static files for the Alphatech Solutions Employee Management System.

## Directory Structure

```
static/
├── css/
│   └── style.css          # Main CSS file with custom styles
├── js/
│   └── main.js           # Main JavaScript file with form handling and UI interactions
└── images/
    └── default-profile.png # Default profile picture
```

## CSS Files

- `style.css`: Contains custom styles for:
  - Navbar
  - Cards
  - Tables
  - Buttons
  - Forms
  - Profile pictures
  - Tabs
  - Alerts
  - Footer
  - Responsive adjustments

## JavaScript Files

- `main.js`: Contains client-side functionality for:
  - Form submissions with file uploads
  - Date input handling
  - File upload previews
  - Tab navigation
  - Dynamic form fields
  - Delete confirmations

## Images

- `default-profile.png`: Default profile picture used when no user profile picture is uploaded

## Usage

All static files are automatically served by Django's static files system. Make sure to:

1. Add `'django.contrib.staticfiles'` to your `INSTALLED_APPS` in settings.py
2. Configure `STATIC_URL` and `STATIC_ROOT` in settings.py
3. Run `python manage.py collectstatic` before deploying to production
