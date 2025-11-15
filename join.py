import streamlit as st
import requests
from pathlib import Path

# -----------------------
# API Configuration
# -----------------------
API_BASE = "http://127.0.0.1:8000"

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Register Member",
    page_icon="💰",
    layout="centered"
)

# -----------------------
# Display Logo (Centered)
# -----------------------
image_path = Path(r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\tk74.png")

if image_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(image_path), caption="", use_container_width=False)

# -----------------------
# Registration Form
# -----------------------
st.title("Join Savings or Investment Club")

# Session state to reset the form
if "form_cleared" not in st.session_state:
    st.session_state.form_cleared = False

with st.form("register_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    country = st.text_input("Country")
    city = st.text_input("City (optional)")
    message = st.text_area("Message (optional)")

    submitted = st.form_submit_button("Register")

    if submitted:
        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "country": country,
            "city": city if city else None,
            "message": message if message else None,
        }

        try:
            res = requests.post(f"{API_BASE}/members/", json=payload)
            if res.status_code == 200:
                st.success("✅ Member registered successfully!")
                st.session_state.form_cleared = True
            else:
                st.error(f"❌ {res.json().get('detail', 'Registration failed')}")
        except Exception as e:
            st.error(f"⚠️ Could not connect to API: {e}")

image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\invest.png"
)
