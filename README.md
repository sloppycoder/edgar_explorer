
# Welcome to Python project

This project is set up Python project with dev tooling pre-configured

* ruff
* pyright
* pre-commit
* VS Code support

## Setup

The easiest way to get started is use [Visual Studio Code with devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)

[uv](https://github.com/astral-sh/uv) is the blazing fast python project manager tool. Install it first before proceeding.


## Quick Start

```shell

# the easiest way to install uv
curl -LsSf https://astral.sh/uv/install.sh | sh


cd my_project_directory

# create virtualenv and install dependencies
uv sync
source .venv/bin/activate

# fix various formatting and import issues automatically
ruff check . --fix


# setup database needed and
# and edit connection info in .env file
# see below for more info
cp env .env


# use pre-commit to ensure only clean code is commiteed
pre-commit install -f

# run test to ensure the basic setup is working
pytest -s -v

# Hack away!!

```


## Start the application in dev models
```shell

quart --app=main run

```





## Database setup
```tests/conftest.py``` contains logic to prepare the test database. By default, the database ar configured by ```.env``` file the projevt root directory.

```DATABASE_URL``` is used by the main application.
```TEST_DATABASE_URL``` is used when running test cases with ```pytest```. When not specificed, a default sqlite in memory database is used.

## Schema migration
Run the following command to populate your database with latest database schema.
```shell
aerich init-db
aerich upgrade

```



See the [generated pyproject.toml](pyproject.toml) for more details on the tools and configurations.
