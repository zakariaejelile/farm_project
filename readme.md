🐓 Farm Management System (Django + DRF)

A modular Farm Management System built with Python, Django, and Django REST Framework, designed to help farmers manage animals, production, food stock, health, tasks, and environmental data in a structured and scalable way.
---

🚀 Features
------------

🔐 Authentication & Users

Custom lightweight User model

JWT Authentication (Login & Refresh)

User registration endpoint

Automatic data isolation per logged-in user

🐄 Animals & Species

* CRUD operations for Species

* CRUD operations for Animals


🌾 Food Stock Management



* Track food quantity, unit, and expiry date

* Automatic user association

* Prepared for future low-stock alerts

🧾 Tasks Management

* CRUD operations for tasks

* Custom endpoint to mark tasks as completed

* Prepared for future reminder & notification system

🩺 Health Logs

* Linked to individual animals

Nested endpoints:
/api/animals/<animal_id>/health/

* Track condition, treatment, notes, date, and recording user

* Supports multiple health records per animal

🥛 Production Logs

* Track animal production: milk, eggs, meat, wool, honey

* Quantity-based logging

* Enforced uniqueness per animal per day

* Ready for analytics and reporting

🌦️ Weather Logs

* Stores temperature, humidity, UV index, and conditions

* Designed to build historical weather insights
---

## 🧱 Project Structure

farm_project/
├─ manage.py
├─ README.md
├─ farm_project/
│ ├─ __init__.py
│ ├─ settings.py
│ ├─ urls.py
|
├─ core/
│ ├─ __init__.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ migrations/
│ │ └─ __init__.py
│ ├─ models.py
│ ├─ tests.py
│ ├─ urls.py
│ └─ views.py
├─ farm/
│ ├─ __init__.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ forms.py
│ ├─ migrations/
│ │ └─ __init__.py
│ ├─ models.py
│ ├─ serializers.py
│ ├─ tests.py
│ ├─ urls.py
│ ├─ views.py
│ ├─ templates/
│ │ ├─ farm/
│ │ │ ├─ base.html
│ │ │ ├─ animal_list.html
│ │ │ ├─ animal_form.html
│ │ │ ├─ food_stock.html
│ │ │ ├─ task_list.html
│ │ │ └─ dashboard.html
│ │ └─ registration/
│ │     ├─ login.html
│ │     └─ logged_out.html
│ └─ static/
│   └─ farm/
│     ├─ css/
│     ├─ js/
│     ├─ images/
│     ├─ fonts/
│     └─ json/


---

## 🔐 Authentication (JWT)

* Login: `/api/token/`
* Refresh: `/api/token/refresh/`
* Register: `/api/auth/register/`
---

## 📦 API Endpoints

| Feature              | Endpoint                     |
| -------------------- | ---------------------------- |
| Species              | `/api/species/`              |
| Animals              | `/api/animals/`              |
| Food Stock           | `/api/food/`                 |
| Tasks                | `/api/tasks/`                |
| Health logs (nested) | `/api/animals/<id>/health/`  |
| Production logs      | `/api/production/`           |
| Weather logs         | `/api/weather/`              |

---
## 📌 Status

- **Phase 0 – Setup** ✅ Completed  
- **Phase 1 – Models** ✅ Completed  
- **Phase 2 – API** ✅ Completed  
- **Phase 3 – Authentication & Permissions** ✅ Completed  
- **Phase 4 – Frontend / UI**  ✅ Completed    
- **Phase 5 – Deployment** 🔜 Upcoming

#######################
## 🔮 Future Roadmap #
#######################

# 🔔 Notification System
***************************

** Food stock expiry alerts

** Task due-date reminders

** Weather-based warnings (heat stress, humidity risks)

** Historical weather analysis (Weather trends over time)

** Linking weather data to: 

# Production drops

# Animal stress indicators

# 🤖 AI & Video Monitoring (Long-term)
************************************

** Camera-based animal monitoring

** Python-trained ML model for:

* Behavior tracking

* Movement analysis

* Early illness detection

* Real-time alerts for abnormal behavior
