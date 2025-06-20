# 🧩 CSV Import Project in a Monolithic Environment

This project is a monolithic application composed of:

- **Backend** in Python (FastAPI, Django, or Flask, as applicable)
- **Frontend** in React
- **Database** PostgreSQL
- **Messaging** via RabbitMQ
- **Infrastructure** orchestrated with Docker Compose
- **Embedded CDN** to serve the frontend application

The main goal of the application is to **import large CSV files**, with more than **900,000 rows**, in a performant, reliable, and integrated way.

---

## 🛠️ Technologies Used

### 1. Backend (Python)
- Framework: FastAPI / Django / Flask *(specify as per your case)*
- Handling of large CSV files
- Integration with RabbitMQ for asynchronous processing
- Communication with PostgreSQL for data persistence

### 2. Frontend (React)
- Interface for file upload and progress monitoring
- Real-time status feedback via websocket or polling
- Application served via a local CDN created in the dockerized environment

### 3. Database (PostgreSQL)
- Stores the data extracted from the CSV
- Relational structure optimized for high-performance bulk writes

### 4. Messaging (RabbitMQ)
- Manages import tasks asynchronously
- Ensures scalability in data processing

### 5. Docker / Docker Compose
- The entire environment is isolated and reproducible with `docker compose`
- Defined containers:
  - `backend`: Python API
  - `frontend`: React application
  - `db`: PostgreSQL
  - `rabbitmq`: Message broker
  - `cdn`: Static server (e.g., nginx) to serve the frontend

---

## 🚀 How to Run the Application

Bringing up the complete stack is simple and only requires Docker installed on your machine.

```bash
docker compose up --build
```

## Demo
![](demonstracao.gif)