# Task Management System

This is a simple Task Management System built with FastAPI. The system includes user authentication, task assignment, and task categorization features.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Setup](#setup)
   1. [1. Install Dependencies](#3-install-dependencies)
   2. [2. Run the Application](#4-run-the-application)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)

## Features

- User authentication (registration, login)
- JWT-based authorization
- Task creation, update, deletion
- Task assignment to users
- Categorization of tasks (e.g., Work, Personal, etc.)
- Filter tasks by category or deadline

## Project Structure
    TaskManagementSystemV1/ 
    ├── README.md 
    ├── requirements.txt 
    ├── /venv 
    ├── app/ 
        │ ├── init.py 
        │ ├── main.py 
        │ ├── models.py 
        │ ├── auth.py 
        │ ├── tasks.py 
        │ ├── database.py 
        │ └── utils.py

## Create virtual environment
    # Create virtual environment
    python3 -m venv venv
    
    # Activate the virtual environment
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate

## Install Dependencies
    # After activating the virtual environment, install the project dependencies:
    pip install -r requirements.txt

##  Run the Application
    # Now, you can run the FastAPI server using Uvicorn:
    uvicorn app.main:app --reload
    
    DEFAULT URL: http://127.0.0.1:8000/
    SWAGGER DOCS URL: http://127.0.0.1:8000/docs

---

### Key Points Covered:

- How to create or activate the virtual environment.
- Install dependencies using the `requirements.txt` file.
- Running the FastAPI app with `uvicorn`.
- Basic usage and example commands for registering a user, logging in, and creating tasks.
- Link to interactive API documentation.
