🟩 1. Authentication Endpoints
POST /api/auth/register

Create a new user.

Request:
{
  "username": "raj",
  "email": "raj@example.com",
  "password": "Pass1234!"
}

Response:
{
  "id": 1,
  "username": "raj",
  "email": "raj@example.com"
}

Errors:

400: username/email already exists

400: invalid password



POST /api/auth/login

Login user and return JWT tokens.

Request:
{
  "username": "raj",
  "password": "Pass1234!"
}

Response:
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}

Errors:

401: invalid credentials



🟩 2. Sweets Endpoints (CRUD + Search)
POST /api/sweets/

Create a new sweet (admin only)

Request:
{
  "name": "Gulab Jamun",
  "category": "Traditional",
  "price": 20.5,
  "quantity": 50
}

Response:
{
  "id": 1,
  "name": "Gulab Jamun",
  "category": "Traditional",
  "price": 20.5,
  "quantity": 50
}

Errors:

400: name already exists

400: invalid price or quantity

403: user is not admin


GET /api/sweets/

List all sweets.

Query Parameters (optional):

category=Traditional

min_price=10

max_price=50

name=jam

Response:
[
  {
    "id": 1,
    "name": "Barfi",
    "category": "Traditional",
    "price": 30,
    "quantity": 100
  }
]


GET /api/sweets/:id

Get one sweet by ID.

Example:
GET /api/sweets/1

Response:
{
  "id": 1,
  "name": "Barfi",
  "category": "Traditional",
  "price": 30,
  "quantity": 100
}


PUT /api/sweets/:id

Update sweet details (admin only)

Request:
{
  "name": "New Name",
  "price": 25.0,
  "quantity": 40
}

Response:
{
  "id": 1,
  "name": "New Name",
  "price": 25.0,
  "quantity": 40
}

Errors:

403: user not admin

404: sweet not found



DELETE /api/sweets/:id

Delete sweet (admin only)

Response:
204 No Content


🟩 3. Inventory Endpoints (Purchase + Restock)
POST /api/sweets/:id/purchase

Purchase 1 unit of a sweet.

Response:
{
  "id": 1,
  "name": "Barfi",
  "quantity": 99
}

Errors:

400: out of stock

404: sweet not found

POST /api/sweets/:id/restock

Restock sweet (admin only)

Request:
{
  "amount": 20
}

Response:
{
  "id": 1,
  "name": "Barfi",
  "quantity": 140
}

Errors:

400: invalid amount

403: user not admin


🟩 4. User Roles

Inside Django:

is_staff = True → Admin

Normal users → can only:

view sweets

purchase sweets

Admins can:

add sweets

update sweets

delete sweets

restock sweets

🟩 5. Error Response Format (consistent)

All errors should follow:

{
  "detail": "Error message here"
}