# Restaurant-website

 - Restaurant website implemented in  ![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)<br>

 - Contains complete templates and DRF api endpoints yet to be integrated to a frontend.
 
## DEPLOY LINKS

 - Frontend [https://restaurant-web-app-j13l.onrender.com/restaurant/]
 - API [https://restaurant-web-app-j13l.onrender.com/restaurant/]

## MAIN API ENPOINTS
```bash
/auth/users
/auth/token/login
/restaurant/api-token-auth
/restaurant/booking-api
/restaurant/menu-api
```
## RUN APP

### 1. Create and Activate a virtual environment

```bash
python3 -m venv env
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Make database migrations

```bash
py manage.py makemigrations
```

then

```bash
py manage.py migrate
```

### 4. Run server

```bash
py manage.py runserver
```

