# EDGAR Filing Explorer Tool

## Project Overview
A Django web application that allows users to explore processing results of using LLM to extract trustee information from 485BPOS filings. The app uses Google Cloud services for deployment and data storage.

## Technology Stack
- **Framework**: Django 5.1.4
- **Python Version**: 3.12+
- **Package Manager**: uv (with lock file)
- **Database**: Data loaded from BigQuery at application start and saved into SQLite in-memory database for query later.
- **Deployment**: Google Cloud Run
- **Frontend**: Django templates with django-tables2
- **Authentication**: django-allauth
- **Browser Testing**: Playwright (for automated UI testing)

## Project Structure
```
edgar_explorer/
├── edgar_explorer/          # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── templates/          # HTML templates
│   ├── management/         # Django management commands
│   └── migrations/         # Database migrations
├── edgarui/                # Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── wsgi.py/asgi.py     # WSGI/ASGI application
├── tests/                  # Test suite
├── staticfiles/            # Static files
└── tmp/                    # Temporary files
```

## Development Setup

### Prerequisites
- Python 3.12+
- uv package manager

### Installation
```bash
# Install dependencies
uv sync

# Install development dependencies
uv sync --group dev

# Run database migrations
uv run python manage.py migrate

# Create superuser (optional)
uv run python manage.py createsuperuser

# Load initial data (if available)
uv run python manage.py initapp
```

### Running the Application
```bash
# Development server
uv run python manage.py runserver

# The app will be available at http://localhost:8000
```

## Code Quality Tools

### Linting and Formatting
```bash
# Run Ruff linter (with auto-fix)
uv run ruff check --fix .

# Run Ruff formatter
uv run ruff format .

# Run both linting and formatting in sequence
uv run ruff check --fix . && uv run ruff format .
```

### Type Checking
```bash
# Run Pyright type checker
uv run pyright
```

### Testing
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Run specific test file
uv run pytest tests/test_data_loading.py

# Run tests with verbose output
uv run pytest -v
```

### Browser Testing with Playwright
The project includes Playwright for automated browser testing:

```bash
# Install Playwright
uv add --group dev playwright

# Install browser binaries
uv run playwright install

# Run browser tests (create test scripts as needed)
uv run python your_playwright_test.py
```

**Note**: For testing purposes, use the following credentials:
- Username: `admin`
- Password: `admin`

### Pre-commit Hooks
The project uses pre-commit hooks for automated code quality checks:

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run all pre-commit hooks manually
uv run pre-commit run --all-files

# Run specific hook
uv run pre-commit run ruff --all-files
```

### All Quality Checks (Recommended workflow)
```bash
# Run the complete quality check suite
uv run ruff check --fix . && \
uv run ruff format . && \
uv run pyright && \
uv run pytest
```

## Configuration

### Environment Variables
Create a `.env` file in the project root:
```bash
DEBUG=1
SECRET_KEY=your-secret-key-here
# Add other environment variables as needed
```

### Ruff Configuration
- Line length: 90 characters
- Indent width: 4 spaces
- Excludes: `.git`, `__pycache__`, `venv`, `.venv`, `settings.py`
- Enabled rules: PEP8 (E, F, W), imports (I), complexity (C), and builtins (A)

### Pyright Configuration
- Python version: 3.12
- Includes: `*.py`, `tests/*.py`
- Excludes: `.venv/`

## Deployment

### Google Cloud Run
The application is configured for deployment to Google Cloud Run using Cloud Build.

```bash
# Check service URL
gcloud run services describe edgar-explorer --region us-central1 --format json | jq -r ".status.url"
```

Deployment is automated through Cloud Build triggers connected to the GitHub repository.

## Common Commands

### Django Management
```bash
# Create new migration
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Collect static files
uv run python manage.py collectstatic

# Django shell
uv run python manage.py shell
```

### Package Management
```bash
# Add new dependency
uv add package-name

# Add development dependency
uv add --group dev package-name

# Update dependencies
uv lock --upgrade

# Sync dependencies (after changes)
uv sync
```

## Notes
- The application uses Google Cloud services extensively (Logging, Storage, BigQuery)
- Database and static files are configured for read-only filesystem (Cloud Run compatibility)
- Authentication is handled via django-allauth
- The project follows Django best practices for structure and configuration
