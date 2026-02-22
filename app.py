import streamlit as st
import datetime
import random

st.set_page_config(page_title="Kiran Weds Anusha 💍", layout="wide")

# Wedding date
wedding_date = datetime.datetime(2026, 4, 26, 0, 0, 0)

# Background images
backgrounds = [
    "https://images.unsplash.com/photo-1522673607200-164d1b6ce486",
    "https://images.unsplash.com/photo-1519741497674-611481863552",
    "https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d",
    "https://images.unsplash.com/photo-1606214174585-fe31582dc6ee",
    "https://images.unsplash.com/photo-1537633552985-df8429e8048b"
]

# Quotes
quotes = [
    "Two souls, one heart 💕",
    "Together is a beautiful place to be ❤️",
    "A journey of love begins forever ✨",
    "From this day forward, you shall not walk alone 💍",
    "Where there is love, there is life 🌸"
]

# Initialize session state counter
if "bg_index" not in st.session_state:
    st.session_state.bg_index = 0

# Auto refresh every second
st.markdown(
    """
    <meta http-equiv="refresh" content="1">
    """,
    unsafe_allow_html=True
)

# Change background every 5 seconds
current_second = datetime.datetime.now().second
if current_second % 5 == 0:
    st.session_state.bg_index = (st.session_state.bg_index + 1) % len(backgrounds)

bg_image = backgrounds[st.session_state.bg_index]
quote = quotes[st.session_state.bg_index % len(quotes)]

# Background styling
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.overlay {{
    background: rgba(0,0,0,0.6);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    color: white;
}}

.title {{
    font-size: 60px;
    font-weight: bold;
    color: gold;
}}

.subtitle {{
    font-size: 35px;
    margin-top: 10px;
}}

.countdown {{
    font-size: 32px;
    margin-top: 20px;
}}

.venue {{
    font-size: 24px;
    margin-top: 25px;
}}

.note {{
    font-size: 20px;
    margin-top: 25px;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}}

.quote {{
    font-size: 26px;
    margin-top: 30px;
    font-style: italic;
    color: #FFDAB9;
}}
</style>
""", unsafe_allow_html=True)

# Countdown calculation
now = datetime.datetime.now()
remaining = wedding_date - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# Page Content
st.markdown('<div class="overlay">', unsafe_allow_html=True)

st.markdown('<div class="title">Kiran 💖 Anusha</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kiran Weds Anusha</div>', unsafe_allow_html=True)

st.markdown(
    f'<div class="countdown">⏳ {days} Days {hours} Hours {minutes} Minutes {seconds} Seconds</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="venue">📍 Venue: Sri Kanyaka Parimeshwari Temple, Rajoli</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="note">'
    'With the blessings of our elders and by the grace of God, '
    'we joyfully invite you to share in the celebration of our wedding. '
    'Your presence and blessings will make our special day truly memorable. '
    'Kindly join us as we begin our beautiful journey together.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(f'<div class="quote">"{quote}"</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
