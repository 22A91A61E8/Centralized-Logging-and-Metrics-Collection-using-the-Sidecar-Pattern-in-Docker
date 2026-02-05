# Centralized Logging and Metrics Collection using Sidecar Pattern (Docker)

## Step 1: Project Objective
The objective of this project is to demonstrate **Centralized Logging and Metrics Collection** using the **Sidecar Pattern** in Docker-based microservices architecture.

Each application service runs with a **sidecar container** that handles logging and metrics independently.

---

## Step 2: What is the Sidecar Pattern
The **Sidecar Pattern** is a design pattern where a helper container runs alongside the main application container to provide additional features such as:
- Logging
- Monitoring
- Metrics collection

This avoids modifying the core application code.

---

## Step 3: Services Used in This Project
This project consists of the following services:

1. **User Service**
2. **Product Service**
3. **Order Service**
4. **Logging Sidecar**
5. **Metrics Sidecar / Aggregator**

Each main service has a sidecar for logging and metrics.

---

## Step 4: Project Structure
docker-sidecar-demo/
│
├── docker-compose.yml
├── .env.example
├── README.md
│
├── user-service/
├── user-logging-sidecar/
├── user-metrics-sidecar/
│
├── product-service/
├── product-logging-sidecar/
├── product-metrics-sidecar/
│
├── order-service/
├── order-logging-sidecar/
├── order-metrics-sidecar/
│
├── logging-sidecar/
└── log-aggregator/
## Step 5:Prerequisites
Docker
Docker Compose
Start all services
docker-compose up --build
This command:
Starts all services
Starts all sidecars
Starts the log aggregator
Connects everything automatically
