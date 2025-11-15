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
# Absolute path to the image
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
            <h2> NEWS! | NEWS! | NEWS!</h2>
            <h6> WORLD | FINANCE | SPORTS | LOCAL | FASHION </h6>
            <p>
               The three scientists' work could tackle some of the biggest problems on our planet, including capturing carbon dioxide to help tackle climate change and reducing plastic pollution using chemistry.
            </p>
            <p>
                <a href="https://www.bbc.com/news/articles/c0r0l742kpjo"
                target="_blank">
                World
                </a>
            </p>
            <p>
               Gold extended its historic rally to break above $4,000 an ounce for the first time on Wednesday, as investors piled into the safe haven to seek cover from mounting geopolitical uncertainty while betting on more US interest rate cuts.
            </p>
            <p>
                <a href="https://www.businessoffashion.com/news/luxury/gold-smashes-4000-milestone-for-first-time-in-record-run/"
                target="_blank">
                Finance
                </a>
            </p>
            <p>
              In the 2000s, big things were expected from an England squad that included the likes of Gerrard, David Beckham, Paul Scholes, Rio Ferdinand and Frank Lampard but the team never progressed past the quarter-finals at a major tournament.
            </p>
            <p>
                <a href="https://www.reuters.com/sports/soccer/englands-golden-generation-were-egotistical-losers-says-gerrard-2025-10-08/"
                target="_blank">
                Sports
                </a>
            </p>
            <p>
              This is similar to past shutdowns where federally funded institutions like the National Gallery of Art and Smithsonian museums had to suspend operations once reserve funds ran out.
            </p>
            <p>
                <a href="https://wtop.com/dc/2025/10/national-gallery-of-art-temporarily-closed-due-to-government-shutdown/"
                target="_blank">
                Local
                </a>
            </p>
            <p>
              Not long after legendary performer Elton John was ushered in through a more discreet entrance the show began, tracked by music from the late Ozzy Osbourne’s Black Sabbath.
            </p>
            <p>
                <a href="https://www.cnn.com/2025/09/23/style/burberry-london-fashion-week-summer26"
                target="_blank">
                Fashion
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

image_path = Path(
    r"C:\Users\khand\OneDrive\Desktop\APIProject\frontend\images\news02.png"
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
