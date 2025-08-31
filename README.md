# 🌍 ALX Travel App 0x03  

**ALX Travel App** is a Django-based backend service designed for managing **travel listings, bookings, and reviews**, while introducing **real-world background processing** with **Celery** and **RabbitMQ**.  

This version focuses on improving **scalability** by moving heavy tasks (like sending emails) into background workers.  

---

## 🚀 Why This Project is Different  

Unlike the earlier versions of the Travel App, this version:  
✨ Integrates **Celery workers** for asynchronous task handling.  
✨ Uses **RabbitMQ** as a reliable message broker.  
✨ Sends **booking confirmation emails** in the background without blocking requests.  
✨ Demonstrates production-level backend practices.  

---

## 🔑 Core Features  

- **🏘️ Listings** → Manage travel properties with host, title, location, and pricing.  
- **📅 Bookings** → Guests book listings with check-in/out dates and status tracking.  
- **⭐ Reviews** → Guests leave ratings and feedback after their stay.  
- **📧 Email Notifications** → Automatic booking confirmation emails.  
- **⚡ Background Tasks** → Powered by Celery + RabbitMQ.  

---

## 🏗️ Tech Stack  

- **Framework**: Django & Django REST Framework  
- **Task Queue**: Celery  
- **Message Broker**: RabbitMQ  
- **Database**: SQLite (default, can be swapped with PostgreSQL)  
- **Containerization**: Docker (optional for RabbitMQ)  

---

## 📂 Project Layout  


