import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kiran Weds 💍", layout="wide")

wedding_date = "2026-04-26T00:00:00"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    padding: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}}

.main {{
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
    background: rgba(0,0,0,0.6);
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
    font-size: 30px;
    margin-top: 20px;
}}

.quote {{
    font-size: 24px;
    margin-top: 25px;
    font-style: italic;
    color: #FFDAB9;
}}
</style>
</head>

<body>

<div id="mainDiv" class="main">
    <div class="overlay">
        <div class="title">Kiran 💖 </div>
        <div class="subtitle">Kiran Weds ______</div>
        <div id="countdown" class="countdown"></div>
        <div id="quote" class="quote"></div>
    </div>
</div>

<script>
const weddingDate = new Date("{wedding_date}").getTime();

const backgrounds = [
"https://images.unsplash.com/photo-1522673607200-164d1b6ce486",
"https://images.unsplash.com/photo-1519741497674-611481863552",
"https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d",
"https://images.unsplash.com/photo-1606214174585-fe31582dc6ee",
"https://images.unsplash.com/photo-1537633552985-df8429e8048b"
];

const quotes = [
"Two souls, one heart 💕",
"Together is a beautiful place to be ❤️",
"A journey of love begins forever ✨",
"From this day forward, you shall not walk alone 💍",
"Where there is love, there is life 🌸"
];

let index = 0;

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
    const main = document.getElementById("mainDiv");
    main.style.backgroundImage = "url('" + backgrounds[index] + "')";
    document.getElementById("quote").innerHTML = '"' + quotes[index] + '"';
    index = (index + 1) % backgrounds.length;
}}

setInterval(updateCountdown, 1000);
setInterval(changeBackground, 5000);

updateCountdown();
changeBackground();
</script>

</body>
</html>
"""

components.html(html_code, height=800)
