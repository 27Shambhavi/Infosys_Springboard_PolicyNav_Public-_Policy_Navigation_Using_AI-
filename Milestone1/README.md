🔐 Milestone 1 – User Authentication System
📌 Project Overview

In Milestone 1, we developed a secure User Authentication System using:

Streamlit – Frontend Web Interface

JWT (JSON Web Tokens) – Secure Authentication

Ngrok – Public URL exposure for local deployment

The system allows users to sign up, log in securely, access a protected dashboard, and reset their passwords.

🚀 Features Implemented
✅ 1. User Signup

Input validation (email format, password strength)

Duplicate user prevention

Secure password hashing

Error handling for invalid entries

✅ 2. Secure Login (JWT Based)

Authentication using email & password

Password verification using hashed comparison

JWT token generation after successful login

Token-based session handling

✅ 3. Protected Dashboard

Accessible only after login

JWT verification before access

Secure session control

✅ 4. Forgot Password

Password reset mechanism

User identity validation

Secure password update

✅ 5. Ngrok Integration

Exposes Streamlit app to public internet

Generates temporary public URL

🔐 Authentication Flow

User signs up → Password is hashed and stored.

User logs in → Credentials verified.

JWT token is generated.

Token is validated for dashboard access.

Forgot password allows secure password reset.

🛡️ Security Implementation Details

Passwords are never stored in plain text

JWT tokens contain:

User ID

Expiration time

Tokens expire after a defined duration

Dashboard requires valid token verification

Proper exception handling for:

Expired tokens

Invalid tokens

Incorrect credentials

🖼️ Screenshots
🔑 Login Page

<img width="1919" height="864" alt="Screenshot 2026-02-23 131759" src="https://github.com/user-attachments/assets/7f3ce10b-eb25-4626-86d8-62591e77ac7b" />


📝 Signup Page

<img width="1919" height="801" alt="Screenshot 2026-02-23 131806" src="https://github.com/user-attachments/assets/7e871d70-c5d8-4cdf-b507-ec45e6bef9f0" />


📊 Dashboard

<img width="1917" height="862" alt="Screenshot 2026-02-23 172041" src="https://github.com/user-attachments/assets/cc3a77ed-40bd-4490-9830-e0910a4b7f95" />


🔁 Forgot Password

<img width="1919" height="832" alt="Screenshot 2026-02-23 131824" src="https://github.com/user-attachments/assets/fbc3db7e-3786-4956-82a1-e887dfb9a9e6" />
