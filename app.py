import streamlit as st
import datetime
import time
import random

st.set_page_config(page_title="Kiran Weds Anusha 💍", layout="wide")

# Wedding Date
wedding_date = datetime.datetime(2026, 4, 26, 0, 0, 0)

# Background images (royalty free wedding images)
backgrounds = [
    "https://images.unsplash.com/photo-1522673607200-164d1b6ce486",
    "https://images.unsplash.com/photo-1519741497674-611481863552",
    "https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d",
    "https://images.unsplash.com/photo-1606214174585-fe31582dc6ee",
    "https://images.unsplash.com/photo-1537633552985-df8429e8048b"
]

# Marriage Quotes
quotes = [
    "Two souls, one heart 💕",
    "Together is a beautiful place to be ❤️",
    "A journey of love begins forever ✨",
    "From this day forward, you shall not walk alone 💍",
    "Where there is love, there is life 🌸"
]

# Random selection
bg_image = random.choice(backgrounds)
quote = random.choice(quotes)

# Background styling
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    transition: background-image 1s ease-in-out;
}}

.main-container {{
    background: rgba(0, 0, 0, 0.55);
    padding: 40px;
    border-radius: 15px;
    text-align: center;
    color: white;
}}

.title {{
    font-size: 60px;
    font-weight: bold;
    color: #FFD700;
}}

.subtitle {{
    font-size: 30px;
    margin-top: 10px;
    color: #FFDEE9;
}}

.venue {{
    font-size: 22px;
    margin-top: 20px;
}}

.quote {{
    font-size: 26px;
    font-style: italic;
    margin-top: 30px;
    color: #FFE4E1;
}}

.invite-note {{
    font-size: 20px;
    margin-top: 25px;
    color: #F8F8FF;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Countdown function
def get_countdown():
    now = datetime.datetime.now()
    remaining = wedding_date - now
    days = remaining.days
    seconds = remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return days, hours, minutes, secs

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="title">Kiran 💖 Anusha</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kiran Weds Anusha</div>', unsafe_allow_html=True)

days, hours, minutes, secs = get_countdown()

st.markdown(
    f"<h2>⏳ Countdown to Our Big Day:</h2>"
    f"<h1>{days} Days {hours} Hours {minutes} Minutes {secs} Seconds</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<div class="venue">📍 Venue: Sri Kanyaka Parimeshwari Temple, Rajoli</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="invite-note">'
    'With the blessings of our elders and the grace of God, '
    'we joyfully invite you to celebrate the auspicious occasion of our marriage. '
    'Your presence will make our special day even more memorable. '
    'Kindly join us and bless the couple for a lifetime of love and happiness.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(f'<div class="quote">"{quote}"</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Auto refresh every 5 seconds
time.sleep(5)
st.experimental_rerun()
