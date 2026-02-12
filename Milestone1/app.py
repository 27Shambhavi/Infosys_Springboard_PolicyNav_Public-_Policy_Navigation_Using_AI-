import streamlit as st
import re
from db import get_connection
from auth import create_token

st.set_page_config(page_title="PolicyNav Authentication", layout="centered")

# ---------- SESSION DEFAULT ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "email" not in st.session_state:
    st.session_state.email = ""

menu = ["Signup", "Login", "Forgot Password"]
choice = st.sidebar.selectbox("Menu", menu)


# ---------------- SIGNUP ----------------
if choice == "Signup":
    st.title("User Signup")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    question = st.selectbox(
        "Security Question",
        [
            "What is your pet name?",
            "What is your mother’s maiden name?",
            "What is your favorite teacher?"
        ]
    )

    answer = st.text_input("Security Answer")

    if st.button("Signup"):

        username = username.strip()
        email = email.strip()
        password = password.strip()
        confirm = confirm.strip()
        answer = answer.strip()

        # validations
        if username == "" or email == "" or password == "" or confirm == "" or answer == "":
            st.error("All fields are mandatory")

        elif not re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", email):
            st.error("Invalid email format")

        elif not password.isalnum():
            st.error("Password must be alphanumeric")

        elif password != confirm:
            st.error("Passwords do not match")

        else:
            conn = get_connection()
            cursor = conn.cursor()

            try:
                cursor.execute(
                    "INSERT INTO users (username,email,password,security_question,security_answer) VALUES (%s,%s,%s,%s,%s)",
                    (username, email, password, question, answer)
                )
                conn.commit()

                token = create_token(email)

                st.success("Signup successful ✅")
                st.write("JWT Token generated:")
                st.code(token)

            except Exception:
                st.error("Email already exists or database error")

            finally:
                conn.close()


# ---------------- LOGIN ----------------
elif choice == "Login":
    st.title("User Login")

    if not st.session_state.logged_in:

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT username, password FROM users WHERE email=%s", (email,))
            user = cursor.fetchone()
            conn.close()

            if user and user[1] == password:
                st.session_state.logged_in = True
                st.session_state.username = user[0]
                st.session_state.email = email
                st.session_state.token = create_token(email)

                st.success("Login successful ✅")
                st.rerun()
            else:
                st.error("Invalid email or password")


# ---------------- DASHBOARD ----------------
if st.session_state.logged_in:

    st.title("📊 Dashboard")
    st.subheader(f"Welcome, {st.session_state.username} 🎉")
    st.info("You are successfully logged into PolicyNav.")

    st.write("🔐 Your JWT token:")
    st.code(st.session_state.token)

    if st.button("Logout"):
        st.session_state.clear()
        st.success("Logged out successfully")
        st.rerun()


# ---------------- FORGOT PASSWORD ----------------
if choice == "Forgot Password" and not st.session_state.logged_in:
    st.title("Forgot Password")

    email = st.text_input("Enter your Email")

    if st.button("Verify Email"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT security_question, security_answer FROM users WHERE email=%s",
            (email,)
        )
        data = cursor.fetchone()
        conn.close()

        if data:
            st.session_state.reset_email = email
            st.session_state.question = data[0]
            st.session_state.answer = data[1]
        else:
            st.error("Email not found")

    if "question" in st.session_state:
        st.write("Security Question:")
        st.info(st.session_state.question)

        ans = st.text_input("Your Answer")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Reset Password"):
            if ans == st.session_state.answer and new_pass.isalnum():

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    "UPDATE users SET password=%s WHERE email=%s",
                    (new_pass, st.session_state.reset_email)
                )
                conn.commit()
                conn.close()

                st.success("Password updated successfully ✅")
                st.session_state.clear()
                st.rerun()
            else:
                st.error("Wrong answer or invalid password")
