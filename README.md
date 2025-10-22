# 🐳 Random Joke App

A simple and lightweight **Python** application that prints a random joke every time it runs — all inside a **Docker container**.  
It uses free public APIs to fetch jokes and includes built-in fallback jokes for offline use.

---

## 📖 Project Description

This project was created as a small Python + Docker exercise.  
It demonstrates how to:

- Build a Docker image from a Python script  
- Run a containerized Python application  
- Push and share a Docker image on Docker Hub  

The application runs instantly, prints a random joke in the terminal, and then exits.

---

## 🧰 Technologies Used

- **Python 3.12**
- **Docker**

---
## ⚙️ How to Build and Run the Project Yourself

Follow these simple steps to clone, build, and run the project on your own system.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/EmilHakobyan0808/jock_generator.git
cd joke-app
docker build -t emilhakobyan08/joke-app:latest
docker run --rm emilhakobyan08/joke-app:latest
