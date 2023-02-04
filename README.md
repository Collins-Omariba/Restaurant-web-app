# Restaurant-website

 - Restaurant website implemented in  ![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)<br>

 - Contains complete templates and DRF api endpoints yet to be integrated to a frontend.

## MAIN API ENPOINTS
```bash
/auth/users
/auth/token/login
/restaurant/api-token-auth
/restaurant/booking-api
/restaurant/menu-api
```
## RUN APP

### 1. Install `pipenv`

```bash
pip install pipenv
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Make database migrations

```bash
py manage.py makemigrations
```

then

```bash
py manage.py migrate
```

### 4. RUN

```bash
py manage.py runserver
```
