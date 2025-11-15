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
            <h5>AAPL | TSLA | MSFT | AMD | AAL</h5>
            <h5>TARGETED INVESTMENT</h5>
            <p>
                Every investor wishes they had bought Apple stock in the 1990s, 
                but you still would have realized a substantial return if you 
                had bought it during the Great Recession or even five years ago.
            </p>
            <p>
                <a href="https://finance.yahoo.com/news/pick-next-apple-stock-according-144835186.html"
                target="_blank">
                How to pick stocks
                </a>
            </p>
            <p>
                With the crypto market continuing to rally in very impressive fashion, it should be no surprise to investors to see shares of centralized crypto trading platform Coinbase (COIN) absolutely take off.
            </p>
            <p>
                <a href="https://finance.yahoo.com/news/coinbase-wants-national-trust-charter-190618805.html"
                target="_blank">
                Crypto Trading Platform
                </a>
            </p>
            <h6>
                <a href="https://join.robinhood.com/khandkt" target="_blank">
                    Open Account with Robinhood
                </a>
            </h6>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------
# Secondary Image Section
# -----------------------
image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\APIProject\frontend\images\bank01.png"
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
