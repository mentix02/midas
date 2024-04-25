# Midas : E-Commerce Store

Midas is a simple online shop powered by a powerful recommendation engine.

# Installation

Midas is composed of two main components: the backend and the frontend. The backend is a Django application that serves the API and the frontend is a Vue application that consumes the API.

## Credentials

Use the following users to login:

| username | password | is_superuser |
|----------|----------|--------------|
| aryan    | abcd     | ❌            |
| kate_h   | kfejk@*_ | ❌            |
| admin    | abcd     | ✅            |

## Backend

Make sure to have Python 3.9 on your machine. Midas' recommendation engine is written in LightFM and I found that it works the most hassle-free with Python 3.9 and earlier.

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the dependencies with `pip install -r requirements.txt`
4. Run the migrations with `python manage.py migrate` and create the db

### Load Sample Data

- Load products
```bash
python3 manage.py load_prods data/products.json
```

- Load users
```bash
python3 manage.py load_users data/users.json
```

- Generate some random interactions (hearts & orders) [OPTIONAL]
```bash
python3 manage.py generate_hearts -n <number_of_hearts>
python3 manage.py generate_orders -n <number_of_orders>
```

### Build the UI

```bash
cd ui
npm install
npm run build
```

### Run the server

```bash
python3 manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## Frontend

1. Navigate to the `ui` directory
2. Install the dependencies with `npm install`
3. Run the development server with `npm run serve`
4. Visit [http://localhost:5173/](http://localhost:5173/) in your browser
