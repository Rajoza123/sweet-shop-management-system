
# 🍬 Sweet Shop Management System

A full-stack Sweet Shop Management System built using **Django REST Framework**, **React**, and **Test-Driven Development (TDD)** principles.
The application supports complete inventory management, role-based access, and a modern SPA frontend, with CI enforced via GitHub Actions.

---

## 🚀 Project Overview

This project simulates a real-world sweet shop where:

* Customers can browse and purchase sweets
* Admins can manage inventory (add, update, restock, delete)
* All backend features are developed using **strict TDD (RED → GREEN → REFACTOR)**
* CI ensures code quality and prevents regressions

The goal is to demonstrate **clean architecture**, **testing discipline**, and **modern development workflows**.

---

## 🛠 Tech Stack

### Backend

* **Python 3**
* **Django**
* **Django REST Framework**
* **PostgreSQL**
* **Pytest**
* **Django Filters**
* **JWT Authentication**
* **Service Layer Architecture**

### Frontend

* **React (SPA)**
* **Axios**
* **React Router**
* **Modern UI (Tailwind / MUI – planned)**

### DevOps & Tooling

* **Git & GitHub**
* **GitHub Actions (CI)**
* **Docker (optional / future)**
* **AWS Free Tier (planned deployment)**

---

## 🧪 Test-Driven Development (TDD)

Every backend feature follows:

1. 🔴 **RED** – Write failing tests
2. 🟢 **GREEN** – Write minimal code to pass tests
3. 🔁 **REFACTOR** – Improve structure without changing behavior

### What this ensures:

* High confidence in code changes
* Clear API contracts
* Regression prevention via CI
* Interview-ready commit history

---

## 🔐 Authentication & Roles

### User Roles

* **Admin (`is_staff = True`)**

  * Add sweets
  * Update sweets
  * Delete sweets
  * Restock inventory
* **Normal User**

  * View sweets
  * Search & filter
  * Purchase sweets

JWT-based authentication protects all sensitive endpoints.

---

## 📡 API Endpoints (Backend)

### Auth

* `POST /api/auth/register`
* `POST /api/auth/login`

### Sweets

* `POST /api/sweets/create` (Admin)
* `GET /api/sweets` (List + Search)
* `GET /api/sweets/:id`
* `PUT /api/sweets/:id/update` (Admin)
* `DELETE /api/sweets/:id/delete` (Admin)

### Inventory

* `POST /api/sweets/:id/purchase`
* `POST /api/sweets/:id/restock` (Admin)

All error responses follow a consistent format:

```json
{
  "detail": "Error message"
}
```

---

## 🧱 Backend Architecture

```text
sweets/
├── models.py        # Domain models + validation
├── serializers.py  # Input/output validation
├── services.py     # Business logic
├── views.py        # HTTP layer
├── urls.py         # Routing
└── tests/           # TDD test suite
```

This separation ensures:

* Thin views
* Reusable business logic
* Easier testing and refactoring

---

## ⚙️ Local Setup Instructions

### Backend Setup

```bash
git clone <your-repo-url>
cd sweet-shop-management-system/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

---

### Run Tests

```bash
pytest
```

CI runs the same tests automatically on every push and pull request.

---

## 🧠 My AI Usage

AI tools were used **responsibly and transparently** throughout development.

### Tools Used

* **ChatGPT**

### How AI Was Used

* Understanding TDD workflows
* Writing initial test cases (then manually reviewed and refined)
* Clarifying Django REST Framework patterns
* Improving error handling and architecture consistency
* Drafting documentation and commit messages

### Human Oversight

* All generated code was **reviewed, modified, and validated**
* Tests were written and interpreted by me
* Architectural decisions were made consciously

### Reflection

AI significantly improved productivity and learning speed, but all final decisions, debugging, and design choices were made manually. The tool acted as a **development assistant**, not a replacement.

---

## 📸 Screenshots

*(To be added after frontend completion)*

---

## 🌍 Deployment

* Backend: **AWS Free Tier (planned)**
* Frontend: **Vercel / Netlify (planned)**

---

## ✅ Status

* ✔ Backend complete
* ✔ Full TDD coverage
* ✔ CI enforced
* 🔜 Frontend implementation
* 🔜 Deployment

---

## 👤 Author

**Raj Oza**
Final-year student & aspiring Software Engineer

---

## 📄 License

This project is for educational and evaluation purposes.
