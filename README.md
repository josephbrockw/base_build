# BaseBuild

A comprehensive full-stack web application template designed for rapid development of modern web applications with a Django backend and React frontend.

## Overview

BaseBuild is a template that provides a complete development environment with:

- **Backend**: Django 5.1 with Django REST Framework
- **Frontend**: React 18 with Vite
- **Database**: PostgreSQL 15
- **Asynchronous Processing**: Celery with Redis
- **Documentation**: Dedicated documentation site
- **Testing**: Comprehensive testing setup for both frontend and backend
- **Containerization**: Docker and Docker Compose for easy development and deployment

This template is designed to help you quickly start new projects with a solid foundation, following best practices for modern web development.

## Features

- **Authentication System**: JWT-based authentication with Django REST Framework Simple JWT
- **API Documentation**: Automatic API documentation with DRF Spectacular
- **Payment Integration**: Stripe payment processing integration
- **Task Queue**: Background task processing with Celery and Redis
- **Monitoring**: Celery task monitoring with Flower
- **Testing**: Pytest for backend and Cypress/Vitest for frontend
- **Code Quality**: Pre-commit hooks, Black, Flake8, and ESLint

## Environment Variables

### Backend

- `DEBUG`: Enable/disable debug mode
- `SECRET_KEY`: Django secret key
- `DJANGO_ALLOWED_HOSTS`: Allowed hosts for Django
- `SQL_ENGINE`: Database engine
- `SQL_DATABASE`: Database name
- `SQL_USER`: Database user
- `SQL_PASSWORD`: Database password
- `SQL_HOST`: Database host
- `SQL_PORT`: Database port
- `DATABASE`: Database type

### DB

- `POSTGRES_USER`: PostgreSQL user
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: PostgreSQL database name

### Frontend

- `CHOKIDAR_USEPOLLING`: Enable polling for file changes
- `REACT_APP_API_BASE_URL`: Backend API base URL
- `REACT_APP_NAME`: Application name
- `REACT_APP_URL`: Frontend application URL

## Project Structure

- `/backend`: Django backend application
- `/client`: React frontend application
- `/docs`: Project documentation
- `/celeryworker`: Independent Celery worker
- `docker-compose.yml`: Docker Compose configuration
- `bb.sh`: Utility script for project management
- `dev_setup.sh`: Development environment setup script

## Utility Scripts

BaseBuild comes with powerful utility scripts to streamline development workflows:

### dev_setup.sh

The `dev_setup.sh` script automates the setup of your development environment. When executed, it performs the following tasks:

- Installs system dependencies using Homebrew (jpeg, zlib, freetype, etc.)
- Installs or updates pip and npm if needed
- Creates and configures a Python virtual environment (`bb-dev`)
- Installs Python dependencies from `backend/requirements.txt`
- Installs Node.js dependencies for the frontend
- Sets up pre-commit hooks for code quality
- Creates necessary environment files
- Installs the `bb` command-line utility globally

To use it, simply run:

```bash
./dev_setup.sh
```

### bb.sh (bb command)

The `bb.sh` script (installed as `bb` command) is a comprehensive project management tool that provides numerous commands to streamline development workflows:

#### Testing Commands
- `bb test`: Run the full test suite (Django, Cypress E2E, Cypress Component, Vitest)
- `bb test -b`: Run only Django backend tests
- `bb test -c`: Run only client tests
- `bb test --e2e`: Run only Cypress end-to-end tests
- `bb test --component`: Run only Cypress component tests
- `bb test -v`: Run only Vitest tests

#### Database Commands
- `bb clean`: Rebuild Docker containers and reset the database
- `bb flush-db`: Flush the database
- `bb db`: Enter PostgreSQL shell
- `bb dumpdata [filename]`: Dump database data to YAML file
- `bb loaddata <filepath>`: Load data from fixture file
- `bb makemigrations`: Create database migrations
- `bb migrate`: Apply database migrations

#### Development Commands
- `bb shell`: Enter Django shell
- `bb app <name>`: Create a new Django app
- `bb manage <command>`: Run Django management commands
- `bb coverage`: Generate test coverage reports
- `bb quality`: Run code quality checks (flake8, black, isort)

For detailed help on any command, use:

```bash
bb <command> --help
```

These utility scripts significantly reduce development friction and enforce consistent practices across the project.

## Process to Sync Changes from the Original Template

1. **Make sure you're in your new project directory**:
   Navigate to the directory of your new project that was created based on the template.

2. **Fetch the latest changes from the original template repository (upstream)**:
   Your new project should already have the original template repo set as an upstream remote (from the script we ran earlier). To fetch the changes from the original template repo, use the following command:
   ```bash
   git fetch upstream
   ```

3. **Review changes (optional)**:
   If you want to see what changes have been made in the original repository, you can check the difference (diff) between your `main` branch and the `upstream/main` branch:
   ```bash
   git diff main..upstream/main
   ```

4. **Merge the changes from the upstream repository**:
   Now, you can merge the changes from the original template repository into your new project’s `main` branch:
   ```bash
   git merge upstream/main
   ```
   If there are no conflicts, this will successfully merge the changes from the original template into your new project.

5. **Resolve conflicts (if any)**:
   If there are any conflicts between your changes and the changes in the original template, Git will flag those as conflicts, and you'll need to manually resolve them.

   After resolving the conflicts, mark the conflicts as resolved:
   ```bash
   git add <resolved-file>
   ```

   Then, commit the resolved changes:
   ```bash
   git commit
   ```

6. **Push the changes to your repository**:
   After merging the changes from the upstream repository, push the merged changes to your new repository (on GitHub):
   ```bash
   git push origin main
   ```

### Summary of Commands:
```bash
# Fetch changes from the upstream (original template repo)
git fetch upstream

# Optionally, check the differences between your branch and upstream/main
git diff main..upstream/main

# Merge changes from upstream/main into your current branch
git merge upstream/main

# Resolve any conflicts if they arise and commit them

# Push the merged changes to your remote repository
git push origin main
