# 🐓 Farm Management System (Django + DRF)

A modular farm management system built using **Python**, **Django**, and **Django REST Framework**, designed to manage animals, species, food stock, weather logs, tasks, production tracking, and more.

---

## 🚀 Features

### **Core**

* Custom lightweight User model
* JWT Authentication (Login + Refresh)
* User registration endpoint

### **Animals & Species**

* CRUD for Species
* CRUD for Animals
* Search animals by tag, name, species, or user
* Automatic filtering by logged-in user

### **Food Stock**

* Track quantity, unit, expiry date
* Filter items by expiry
* Automatic user association

### **Tasks**

* CRUD operations
* Filter by `completed` and `due_date`
* Custom endpoint `/complete/` to mark task as done

### **Health Logs**

* Nested under animal:
  `/api/animals/<animal_id>/health/`
* Stores condition, treatment, notes, date, and user who recorded it

### **Production Logs**

* Track egg count or weight change
* Unique per day per animal

### **Weather Logs**

* Temp, humidity, UV index, conditions
* Auto-timestamps
* Filtered by logged-in user

---

## 🧱 Project Structure

```
farm_project/
├─ manage.py
├─ farm_project/
│  ├─ settings.py
│  ├─ urls.py
├─ core/
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
├─ farm/
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/
├─ templates/
└─ requirements.txt
```

---

## 🛠️ Installation & Setup

### **1. Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### **2. Install dependencies**

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### **3. Start project & apps**

```bash
django-admin startproject farm_project .
python manage.py startapp core
python manage.py startapp farm
```

### **4. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run server**

```bash
python manage.py runserver
```

---

## 🔐 Authentication (JWT)

* Login: `/api/auth/token/`
* Refresh: `/api/auth/token/refresh/`
* Register: `/api/auth/register/`

---

## 📦 API Endpoints

| Feature              | Endpoint                    |
| -------------------- | --------------------------- |
| Species              | `/api/species/`             |
| Animals              | `/api/animals/`             |
| Food Stock           | `/api/food/`                |
| Tasks                | `/api/tasks/`               |
| Mark task completed  | `/api/tasks/<id>/complete/` |
| Health logs (nested) | `/api/animals/<id>/health/` |
| Production logs      | `/api/production/`          |
| Weather logs         | `/api/weather/`             |

---

## 📌 Status

This project is currently in **Phase 2: API implementation**, with full models, serializers, and viewsets completed.

More phases (authentication, frontend, deployment) will come next.

---
