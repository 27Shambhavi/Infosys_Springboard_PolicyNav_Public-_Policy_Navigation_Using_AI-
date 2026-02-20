# PolicyNav – AI Powered Policy Navigation System

## 📌 Project Overview

PolicyNav is a secure AI-powered portal developed as part of the Infosys Springboard Internship Program.

This project enhances Milestone 1 by integrating advanced authentication and analytics features.

---

## 🔐 Implemented Features

### 1️⃣ OTP Authentication
- Secure login using email-based OTP verification
- Rate limiting to prevent brute-force attacks
- Password reuse protection
- JWT-based session authentication

### 2️⃣ Readability Dashboard
- Text Readability Analysis using `textstat`
- Supports:
  - Flesch Reading Ease
  - Flesch-Kincaid Grade
  - SMOG Index
  - Gunning Fog
  - Coleman-Liau Index
- Upload TXT and PDF files
- Interactive gauge visualization using Plotly

### 3️⃣ Admin Panel
- View all registered users
- Delete users (admin protected)
- Secure admin authentication

---

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- bcrypt
- JWT
- Plotly
- PyPDF2
- textstat

---

## 📸 Screenshots

### 🔐 OTP Login
![OTP Screenshot](screenshots/otp.png)

### 📊 Readability Dashboard
![Dashboard Screenshot](screenshots/readability.png)

### 🛡 Admin Panel
![Admin Screenshot](screenshots/admin.png)

