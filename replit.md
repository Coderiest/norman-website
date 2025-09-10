# Norman Website - Replit Setup

## Overview
This is Norman's website - a simple Flask web application now configured to run in the Replit environment.

## Project Structure
- `app.py` - Main Flask application with routes for home page and health check
- `pyproject.toml` - Python project configuration with Flask dependency
- `.replit` - Replit configuration
- `.gitignore` - Python-specific gitignore rules

## Recent Changes (September 10, 2025)
- Set up Python 3.11 environment
- Installed Flask framework
- Created basic web application with welcome page
- Configured Flask to run on 0.0.0.0:5000 for Replit proxy compatibility
- Set up "Norman Website" workflow to run the Flask application
- Configured deployment for autoscale mode

## Architecture
- **Frontend**: Simple HTML served directly from Flask routes
- **Backend**: Flask web server with development configuration
- **Port**: 5000 (frontend)
- **Host**: 0.0.0.0 for Replit proxy compatibility

## Running the Application
The application runs automatically via the "Norman Website" workflow. It serves on port 5000 and is accessible through Replit's web preview.

## Deployment
Configured for autoscale deployment, suitable for stateless web applications.