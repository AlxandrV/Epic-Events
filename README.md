# Epic-Events

Epic Event web app

## Summary

- [Local development](#local-development)
- [Admin](#admin)
- [API Documentation](#api-documentation)

## Local development 

### Prerequisites

- Git CLI
- A Python runtime environment, version 3.6 or higher

In the rest of the local development documentation, it is assumed that the `python` command in your shell OS runs the above Python interpreter (unless a virtual environment is enabled).

### macOS / Linux

#### Clone the repository

- `git clone https://github.com/AlxandrV/Epic-Events.git`

#### Create the virtual environment

- `cd /path/to/app`
- `python -m venv venv`
- Activate the environment `source venv/bin/activate`
- To disable the environment, `deactivate`

#### Run the site

- `cd /path/to/app`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python epic_events/manage.py runserver`
- Go to `http://localhost:8000` in a browser.

### Windows

Using PowerShell, as above except :

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 

## Admin

You have access to admin interface with `http://localhost:8000/admin/`

## API Documentation

Go to read the documentation [Postman](https://documenter.getpostman.com/view/22332147/2s8Z6saaxr)