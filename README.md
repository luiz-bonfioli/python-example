# Simple Python FastAPI and Postgres demo

This is a small example of using Postgres to persist and FastAPI to process requests.

## Features

- API to handle a GET request
- Postgres database init and persistence to a single table

## Requirements

- Python 3.11
- Pip (for dependency management)

## Installation

To get started with this project, you'll need to have pip installed. If you don't have pip installed yet, you can install it by following these steps:

### Install Pip

You can install Pip using the following command:

```bash
python -m ensurepip --upgrade
```

### Install Dependencies

```bash
 pip install -r requirements.txt
```

### Install infra (postgres)

```bash
docker-compose up -d
```
