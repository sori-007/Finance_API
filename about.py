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
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------
# Header Image Section
# -----------------------
image_path = Path(r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\tk74.png")

if image_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider
    with col2:
        st.image(str(image_path), caption=" ", use_container_width=False)

# -----------------------
# About Content
# -----------------------
st.markdown(
    """
    <div class="box">
        <div class="Text">
            <h5>Targeted Investment for Better Returns than Savings</h5>
            <h3>Our Vision</h3>
            <p>
                Investing savings in targeted stocks can yield higher returns than traditional savings accounts.
                This strategy involves selecting stocks based on market analysis, company performance, and growth potential.
                While offering the opportunity for significant gains, it also carries higher risks due to market volatility.
            </p>
            <p>
                Diversification and thorough research are crucial to mitigate risks.
                Regularly monitoring investments and staying informed about market trends
                can help make informed decisions and maximize returns.
            </p>
            <h6><a href="https://join.robinhood.com/khandkt" target="_blank">
            <p> Open Account with Robinhood</p></h6>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------
# Images Section
# -----------------------
# -----------------------
# Secondary Image Section
# -----------------------
image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\save03.png"
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
            <a href="mailto:contact@savingsorinvestment.com">contact@savingsorinvestment.com</a>
        </center>
    </div>
    """,
    unsafe_allow_html=True
)
