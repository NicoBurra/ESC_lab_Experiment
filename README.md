# ESC Lab Experiment Manager

This project is a minimal Django-based platform to manage student registrations and psychology experiments.

## Setup
1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r experiment_manager/requirements.txt
   ```
2. Run migrations and start the server:
   ```bash
   python experiment_manager/manage.py migrate
   python experiment_manager/manage.py runserver
   ```

The admin interface is available at `/admin/`.
