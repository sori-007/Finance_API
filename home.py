import streamlit as st
from pathlib import Path

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Savings or Investment - Main",
    page_icon="💰",
    layout="centered"
)

# -----------------------
# Load External CSS
# -----------------------
css_path = Path("styles.css")
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ styles.css file not found!")

# -----------------------
# Header Image
# -----------------------
image_path = Path(r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\tk74.png")

if image_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])  # Center the image
    with col2:
        st.image(str(image_path), caption="", use_container_width=False)
else:
    st.warning("⚠️ Header image not found!")

# -----------------------
# Main Content Section
# -----------------------
st.markdown(
    """
    <center>
        <div class="box">
            <div class="Text">
                <h5>Savings or Investment</h5>
                <h3>Taha Khandker</h3>
                <p>In the vault of time, let coins of thrift align. Each penny spared is a seed for wealth's design.</p>
                <p>Investment blooms in the fertile ground of thought, compounding interest and dreams to be sought.</p>
                <p>With patience as our guide and wisdom as our aid, we nurture our fortunes where prudence is displayed.</p>
                <p>For every sacrifice made, we secure a future. In the treasury of foresight, our wealth will endure.</p>
                <p>So let us sow the seeds of financial care, for in the golden harvest of stocks, prosperity we share.</p>
                <h6>
                    <a href="https://join.robinhood.com/khandkt" target="_blank">
                        <p>Open Account with Robinhood</p>
                    </a>
                </h6>
            </div>
        </div>
    </center>
    """,
    unsafe_allow_html=True
)

# -----------------------
# Secondary Media Section
# -----------------------
video_path = Path(r"C:\Users\khand\OneDrive\Desktop\FinanceAPI\image\pv002.mp4")

if video_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])  # Center video
    with col2:
        st.video(str(video_path))
else:
    st.warning("⚠️ Video file not found!")

# -----------------------
# Footer Section
# -----------------------
st.markdown(
    """
    <center>
        <div class="footer">
            <p>
                <a href="mailto:contact@savingsorinvestment.com">
                    contact@savingsorinvestment.com
                </a>
            </p>
        </div>
    </center>
    """,
    unsafe_allow_html=True
)
