import streamlit as st
from pathlib import Path

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="About - Savings or Investment",
    page_icon="💰",
    layout="centered"
)

# -----------------------
# Load External CSS
# -----------------------
css_file = Path("styles.css")
if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------
# Header Image Section (Top)
# -----------------------
image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\tk74.png"
)

if image_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider
    with col2:
        st.image(str(image_path), caption="", use_container_width=False)

# -----------------------
# About Content
# -----------------------
st.markdown(
    """
    <div class="box">
        <div class="Text">
            <h5>BTC | ETH | BNB | SOL | USDC </h5>
            <h6>RISKY INVESTMENT</h6>
            <p>
                Trust, sophistication, and innovation. We strike a balance between security and simplicity, making you feel confident and in control of your digital assets. We emphasize secure, innovative, and future-ready financial tools.
            </p>
            <h3> If an exchange have to move large amounts of crypto before or after they demonstrate their wallet addresses, it is a clear sign of problems. Stay away.
            <p>CZ BINANCE</p>
            </h3>
            <h6><a href="https://coin.space/" target="_blank">
            <p> Open Account with Coin</p></h6>
        </div>
    </div>
           
    """,
    unsafe_allow_html=True
)

# -----------------------
# Secondary Image Section
# -----------------------
image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\APIProject\frontend\images\invest02.png"
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
    <div class="footer">
        <center>
            <a href="mailto:contact@savingsorinvestment.com">
                contact@savingsorinvestment.com
            </a>
        </center>
    </div>
    """,
    unsafe_allow_html=True
)
