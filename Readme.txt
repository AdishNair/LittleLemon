Little Lemon API paths for peer testing
========================================

Home page:
/restaurant/

Menu API (public):
GET, POST               /restaurant/menu/
GET, PUT, PATCH, DELETE /restaurant/menu/<id>/
GET, POST               /api/menu-items/
GET, PUT, PATCH, DELETE /api/menu-items/<id>/

Booking API (token required):
GET, POST               /restaurant/booking/tables/
GET, PUT, PATCH, DELETE /restaurant/booking/tables/<id>/
GET, POST               /api/bookings/

User authentication:
POST /auth/users/          Register a user
POST /auth/token/login/    Obtain a token
POST /auth/token/logout/   Revoke the current token
POST /restaurant/api-token-auth/  Alternative token endpoint

For authenticated booking requests, send this header:
Authorization: Token <your-token>

Setup
-----
1. Create and activate a Python virtual environment.
2. Run: pip install -r requirements.txt
3. Run: python manage.py migrate
4. Run: python manage.py runserver

SQLite is used by default. To use MySQL, copy .env.example values into
your shell environment, set DB_ENGINE=mysql, create the LittleLemon
database, and run migrations again.
