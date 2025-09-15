### Hexlet tests and linter status:
[![Actions Status](https://github.com/DARIAkuch/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DARIAkuch/python-project-52/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DARIAkuch_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DARIAkuch_python-project-52)

# Task Manager

A Django-based task tracker

## Features

- User authentication and authorization
- Task management (create, read, update, delete)
- Status management for tasks
- Label management for task categorization
- Internationalization support (i18n)
- Responsive design

## Tech Stack

- Python 3.11+
- Django 5.2
- PostgreSQL
- Bootstrap 5

## Project Structure

- `task_manager/` - Main application directory
  - `users/` - User management
  - `tasks/` - Task management
  - `statuses/` - Task status management
  - `labels/` - Task label management
  - `templates/` - HTML templates
  - `locale/` - Translation files

## Setup and Installation

1. Clone the repository
   ```bash
   gh repo clone DARIAkuch/python-project-52
   ```
2. Install dependencies:
   ```bash
   make install
   ```
3. Start the application:
   ```bash
   make run
   ```

## Development

- Run tests:
  ```bash
  make test
  ```
- Check code style:
  ```bash
  make lint
  ```