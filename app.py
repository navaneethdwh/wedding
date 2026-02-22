import streamlit as st

st.set_page_config(page_title="Kiran Weds Anusha 💍", layout="wide")

# Wedding Date (YYYY-MM-DD HH:MM:SS)
wedding_date = "2026-04-26T00:00:00"

backgrounds = [
    "https://images.unsplash.com/photo-1522673607200-164d1b6ce486",
    "https://images.unsplash.com/photo-1519741497674-611481863552",
    "https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d",
    "https://images.unsplash.com/photo-1606214174585-fe31582dc6ee",
    "https://images.unsplash.com/photo-1537633552985-df8429e8048b"
]

quotes = [
    "Two souls, one heart 💕",
    "Together is a beautiful place to be ❤️",
    "A journey of love begins forever ✨",
    "From this day forward, you shall not walk alone 💍",
    "Where there is love, there is life 🌸"
]

background_js_array = str(backgrounds)
quotes_js_array = str(quotes)

st.markdown(f"""
<style>
body {{
    margin: 0;
    padding: 0;
    overflow: hidden;
}}

.wedding-container {{
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    background-size: cover;
    background-position: center;
    transition: background-image 1.5s ease-in-out;
}}

.overlay {{
    background: rgba(0,0,0,0.55);
    padding: 50px;
    border-radius: 20px;
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
}}

.quote {{
    font-size: 26px;
    margin-top: 30px;
    font-style: italic;
    color: #FFDAB9;
}}
</style>

<div id="main" class="wedding-container">
    <div class="overlay">
        <div class="title">Kiran 💖 Anusha</div>
        <div class="subtitle">Kiran Weds Anusha</div>
        <div id="countdown" class="countdown"></div>
        <div class="venue">📍 Venue: Sri Kanyaka Parimeshwari Temple, Rajoli</div>
        <div class="note">
            With the blessings of our elders and by the grace of God,
            we joyfully invite you to celebrate our wedding.
            Your presence and blessings will make our special day truly memorable.
        </div>
        <div id="quote" class="quote"></div>
    </div>
</div>

<script>
const weddingDate = new Date("{wedding_date}").getTime();
const backgrounds = {background_js_array};
const quotes = {quotes_js_array};

let bgIndex = 0;

function updateCountdown() {{
    const now = new Date().getTime();
    const distance = weddingDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML =
        "⏳ " + days + " Days " + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds";
}}

function changeBackground() {{
    const mainDiv = document.getElementById("main");
    mainDiv.style.backgroundImage = "url('" + backgrounds[bgIndex] + "')";
    document.getElementById("quote").innerHTML = '"' + quotes[bgIndex] + '"';
    bgIndex = (bgIndex + 1) % backgrounds.length;
}}

setInterval(updateCountdown, 1000);   // every second
setInterval(changeBackground, 5000);  // every 5 seconds

changeBackground();
updateCountdown();
</script>
""", unsafe_allow_html=True)
