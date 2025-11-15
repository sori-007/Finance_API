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
            <h4> BLOGS</h4>
            <h6> FINANCE & INVESTMENT BLOGS </h6>
            <p>
               There are still risks involved, however. While U.S. savings bonds are considered one of the safest investments, bonds issued by individual companies or municipalities may be risky if the issuer runs into financial difficulties. The issuer can also buy back the bond, which effectively pays the remaining principal balance in full and cancels the bond.
            </p>
            <p>
                <a href="https://finred.usalearning.gov/Saving/StocksBondsMutualFunds"
                target="_blank">
                Savings & Bonds
                </a>
            </p>
            <p>
               The Indonesia People’s Business Program (Kredit Usaha Rakyat, KUR) is one of the world’s largest public credit schemes for MSMEs. Since its inception in 2007, the program has disbursed more than 50 million loans totaling more than US$100 billion. By subsidizing interest rates (capped at 6%) and providing partial credit guarantees, KUR aims to help small businesses access formal bank loans for the first time and transition to commercial credit.
            </p>
            <p>
                <a href="https://blogs.worldbank.org/en/allaboutfinance/should-governments-intervene-to-improve-financing-for-small-busi"
                target="_blank">
                Business Programs
                </a>
            </p>
            <h6>
                <a href="https://join.robinhood.com/khandkt" target="_blank">
                    <p>Open Account with Robinhood</p>
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
    r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\tk102.png"
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
