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
    page_title="Contact / Inqueries",
    page_icon="💬",
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
# Contact / inquiries Form
# -----------------------
st.markdown("<h5 style='text-align:center;'>Talk to us about your interest</h5>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="Enter your email address")
    message = st.text_area("Message", placeholder="Type your message here...")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not name or not email or not message:
            st.warning("⚠️ Please fill in all required fields.")
        else:
            payload = {"name": name, "email": email, "message": message}
            try:
                res = requests.post(f"{API_BASE}/contact/", json=payload)

                if res.status_code == 200:
                    st.success("✅ Thank you for your inquiry! We'll be in touch soon.")
                else:
                    st.error(f"❌ Submission failed: {res.text}")
            except Exception as e:
                st.error(f"⚠️ Could not connect to API: {e}")
                

image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\APIProject\frontend\images\kt37.png"
)

if image_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(image_path), caption="", use_container_width=False)

# -----------------------
# Footer Section
# -----------------------
st.markdown(
    """
    <div class="footer" style="margin-top: 40px;">
        <center>
            <a href="mailto:contact@savingsorinvestment.com">
                contact@savingsorinvestment.com
            </a>
        </center>
    </div>
    """,
    unsafe_allow_html=True
)

