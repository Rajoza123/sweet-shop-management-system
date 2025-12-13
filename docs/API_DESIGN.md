# Sweet Shop Management System — API Design

This document defines the REST API contract for the Sweet Shop Management System.  
It is created before backend implementation to support Test-Driven Development (TDD).

---

## 1. Authentication Endpoints

### 1.1 POST /api/auth/register
Registers a new user.

#### Request
{
"username": "raj",
"email": "raj@example.com",
"password": "Pass1234!"
}



#### Response
{
"id": 1,
"username": "raj",
"email": "raj@example.com"
}



#### Errors

| Status | Description |
|--------|-------------|
| 400 | Username or email already exists |
| 400 | Invalid password format |

---

### 1.2 POST /api/auth/login
Authenticates a user and returns JWT tokens.

#### Request
{
"username": "raj",
"password": "Pass1234!"
}



#### Response
{
"access": "<jwt-access-token>",
"refresh": "<jwt-refresh-token>"
}



#### Errors

| Status | Description |
|--------|-------------|
| 401 | Invalid credentials |

---

## 2. Sweets Endpoints (CRUD + Search)

### 2.1 POST /api/sweets/
Creates a new sweet (Admin only).

#### Request
{
"name": "Gulab Jamun",
"category": "Traditional",
"price": 20.5,
"quantity": 50
}



#### Response
{
"id": 1,
"name": "Gulab Jamun",
"category": "Traditional",
"price": 20.5,
"quantity": 50
}



#### Errors

| Status | Description |
|--------|-------------|
| 400 | Name already exists |
| 400 | Invalid price or quantity |
| 403 | User is not an admin |

---

### 2.2 GET /api/sweets/
Returns all sweets.

#### Optional Query Parameters

| Parameter | Example | Purpose |
|-----------|---------|---------|
| category | Traditional | Filter by category |
| min_price | 10 | Minimum price |
| max_price | 50 | Maximum price |
| name | jam | Case-insensitive search |

#### Response
[
{
"id": 1,
"name": "Barfi",
"category": "Traditional",
"price": 30,
"quantity": 100
}
]



---

### 2.3 GET /api/sweets/:id
Returns a specific sweet.

#### Response
{
"id": 1,
"name": "Barfi",
"category": "Traditional",
"price": 30,
"quantity": 100
}



#### Errors

| Status | Description |
|--------|-------------|
| 404 | Sweet not found |

---

### 2.4 PUT /api/sweets/:id
Updates a sweet (Admin only).

#### Request
{
"name": "New Name",
"price": 25.0,
"quantity": 40
}


#### Response
{
"id": 1,
"name": "New Name",
"price": 25.0,
"quantity": 40
}


#### Errors

| Status | Description |
|--------|-------------|
| 403 | User is not an admin |
| 404 | Sweet not found |

---

### 2.5 DELETE /api/sweets/:id
Deletes a sweet (Admin only).

#### Response
204 No Content


#### Errors

| Status | Description |
|--------|-------------|
| 403 | User is not an admin |
| 404 | Sweet not found |

---

## 3. Inventory Endpoints (Purchase + Restock)

### 3.1 POST /api/sweets/:id/purchase
Purchases one unit of a sweet.

#### Response
{
"id": 1,
"name": "Barfi",
"quantity": 99
}


#### Errors

| Status | Description |
|--------|-------------|
| 400 | Out of stock |
| 404 | Sweet not found |

---

### 3.2 POST /api/sweets/:id/restock
Restocks a sweet (Admin only).

#### Request
{
"amount": 20
}

#### Response
{
"id": 1,
"name": "Barfi",
"quantity": 140
}

#### Errors

| Status | Description |
|--------|-------------|
| 400 | Invalid restock amount |
| 403 | User is not an admin |
| 404 | Sweet not found |

---

## 4. User Roles

### Normal User Can:
- View sweets
- Search sweets
- Purchase sweets

### Admin User Can:
- Add sweets
- Update sweets
- Delete sweets
- Restock sweets

(Admin = is_staff = True)

---

## 5. Error Response Format

All errors use the following structure:

{
"detail": "Error message here"
}

Examples:
{ "detail": "Invalid credentials" }
{ "detail": "Sweet not found" }
{ "detail": "Permission denied" }

