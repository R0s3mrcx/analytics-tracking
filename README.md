# Analytics Tracking API

![Python](https://img.shields.io/badge/python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/flask-2.3.3-orange?logo=flask)
![Docker](https://img.shields.io/badge/docker-20.10-blue?logo=docker)
![Cloud Run](https://img.shields.io/badge/cloud_run-deployed-lightgrey)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-github_actions-brightgreen)

---

## 📌 Overview

The **Analytics Tracking API** is a secure, scalable, and cloud-native service designed to capture events and metadata for analytics purposes. It is containerized with Docker and deployed on **Google Cloud Run**, following best practices in **structured logging, token-based authentication, and cloud observability**. This API is designed to be **flexible and extensible**, allowing integration with any analytics pipeline, data warehouse, or custom dashboard.

---

## 📁 Project Structure

<pre>
analytics-tracking/
├── Dockerfile
├── main.py
├── requirements.txt
├── tests/
│   └── test_api.py
├── README.md
└── .gitignore
</pre>

---

## 🏗️ Architecture

```
      ┌─────────┐
      │ Client  │
      │ (Any)   │
      └────┬────┘
           │ POST /track (X-API-Key)
           ▼
    ┌───────────────┐
    │ Flask API      │
    │ - Token Auth   │
    │ - Validation   │
    │ - Logging      │
    └─────┬─────────┘
          │
┌─────────┴─────────┐
│ Cloud Run / Docker │
└─────┬─────────────┘
      │ Structured Logs
      ▼
┌───────────────┐
│ BigQuery /    │
│ Cloud Logging │
└───────────────┘

```

---

## ⚡ Key Features

* RESTful API built with **Flask**
* **Token-based authentication** for secure access
* **Structured logging** for observability and debugging
* Cloud-native deployment on **Google Cloud Run**
* Extensible for integration with **BigQuery**, **Cloud Logging**, or other analytics platforms
* Supports **flexible event payloads**, allowing clients to send relevant event data
* **Automated testing** included with `pytest` examples for senior-level coverage

---

## 📊 Example Payload

```json
{
  "user_id": "12345",
  "event_type": "page_view",
  "timestamp": "2025-09-04T22:00:00Z",
  "metadata": {
    "page": "/home",
    "referrer": "/login"
  }
}
```

---

## 🛠️ API Endpoints

### POST /track
**Description:** Accepts analytics events from clients.

* **Headers:**
  * `X-API-Key`: Secret token for authentication
* **Body:**
  * Accepts **flexible JSON payloads**
* **Response:**
```json
{
  "status": "ok",
  "received": { /* your payload */ }
}
```

### GET /health
**Description:** Simple health check endpoint to monitor service status.
* **Response:**
```
API OK
```

---

## 🚀 Deployment

### Using Docker
```bash
docker build -t analytics-tracking-api .
docker run -p 8080:8080 --env SECRET_TOKEN=your_secret_token analytics-tracking-api
```

### Deploy to Google Cloud Run
```bash
gcloud run deploy analytics-api \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars SECRET_TOKEN=your_secret_token
```

---

## 🤖 CI/CD (GitHub Actions)

* Automatic Docker build on push
* Optional deployment to Cloud Run
* Python dependency checks and linting
* Unit tests with `pytest` located in `tests/` folder
* Badges reflect current build and deployment status

---

## ✅ Best Practices

* **Structured Logging:** Logs include raw and parsed JSON payloads for observability
* **Token Authentication:** Secures API endpoints for production use
* **Cloud-Native Design:** Optimized for containerized deployment on Cloud Run
* **Flexible Payloads:** Can handle any type of event data sent by clients
* **CI/CD Ready:** Integration with GitHub Actions allows automated builds and deployments
* **Extensible:** Future integration with analytics platforms like BigQuery or Cloud Logging is straightforward
* **Testing:** Unit tests in `tests/` ensure reliability and maintainability
* **Documentation:** Clear examples, architecture diagram, and testing guide included

---

## 🤝 Notes

* Designed as a **general-purpose analytics tracking solution**
* Focused on **security, scalability, observability, and cloud-native best practices**
* Clients can send any structured data relevant to their analytics pipeline

---

## 📄 License

MIT © 2025 - Built with ❤️ by [R0s3mrcx](https://github.com/R0s3mrcx)
