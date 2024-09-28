# Django Inventory API with Redis Caching and JWT Authentication

This project is a Django-based inventory management system that provides CRUD (Create, Read, Update, Delete) operations for managing items. It uses **JWT Authentication** to secure the API, **Redis** for caching, and a **logger** to track API usage and errors.

## Features

- User Registration and Login with JWT Authentication.
- CRUD operations for inventory items.
- Caching using Redis to enhance performance.
- Comprehensive logging of API usage and errors.
- Unit tests for all the endpoints.
  
## Requirements

- Python 3.7 or higher
- Django 3.x or higher
- Django REST Framework
- Redis Server
- PostgreSQL (or SQLite for local development)

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/inventory-api.git
cd inventory-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Database
Edit the `settings.py` to configure your database settings (PostgreSQL or SQLite). Then, run the migrations:
```bash
python manage.py migrate
```

### 4. Install and Start Redis
If you don’t have Redis installed, install it and start the server.
(Redis is not officially supported on Windows.)
- on Windows
 - install WSL (ubuntu) on windowns. 
     - refer 
       1. [install wsl on windows](https://learn.microsoft.com/en-us/windows/wsl/install)
       2. [setup wsl environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)
 - install redis after installation and setup environment.
   - refer
     [Install REDIS on windows](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/)

- On Ubuntu:
```bash
sudo apt install redis-server
sudo systemctl start redis
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Populate Demo Data
To populate the database with demo items, run:
```bash
python manage.py populate_demo_data
```

### 7. Run Unit Tests
```bash
python manage.py test
```

## API Endpoints

### 1. **User Registration**: `/api/register/` (POST)
Register a new user.

### 2. **User Login**: `/api/token/` (POST)
Login with `username` and `password` to get a JWT token.

### 3. **Get All Items**: `/api/items/` (GET)
Retrieve a list of all inventory items. Requires authentication.

### 4. **Create Item**: `/api/items/` (POST)
Create a new inventory item. Requires authentication.

### 5. **Update Item**: `/api/items/<id>/` (PUT)
Update an existing item by its `id`. Requires authentication.

### 6. **Delete Item**: `/api/items/<id>/` (DELETE)
Delete an existing item by its `id`. Requires authentication.