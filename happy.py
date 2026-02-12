import streamlit as st
import time
from datetime import datetime
import base64

BIRTHDAY_PERSON = "Mahi"
IMAGE_FILE = "february-13-2019-nebula-sharpless-2-106"
SONG_URL = "song.mp3"



questions = [
    {"q": "🌹 What’s your idea of a perfect date?",
     "options": ["Dinner under the stars", "Movie night with popcorn", "Long drive with music", "Coffee in a cozy café"]},

     {"q": "🎁 What kind of surprise would make you smile the most?",
    "options": ["Handwritten letter", "Chocolate hamper", "Cute plush toy", "Me doing random rizz or efforts😆"]},

    {"q": "🎶 What kind of music would you like on our date?",
     "options": ["Romantic acoustic", "Lo-fi chill vibes", "Bollywood love songs", "Pop hits"]},

     {"q": "😜 If we got lost on a trip, what would you do?",
    "options": ["Blame Google Maps", "Blame me 😅", "Just enjoy the adventure", "Panic and call mom"]},

    {"q": "🍨 Which dessert would make the night sweeter?",
     "options": ["Chocolate cake", "Ice cream", "Cheesecake", "Brownies"]},

    {"q": "🍕 If I steal your food on the date, what would you do?",
    "options": ["Feed me anyway", "Steal mine back", "Give death stare 😒", "Order extra"]},

    {"q": "🌆 Where would you love to end the date?",
    "options": ["Long drive", "Late-night chai stall", "Café with live music", "Home with cozy vibes"]},

    {"q": "🤣 If I sang a super off-key song for you, what would you do?",
    "options": ["Clap & cheer", "Roast me", "Join in singing worse", "Run away fast"]},

    {"q": "Last any words for me? 👀",
    "options": []},

]

# ---------- PAGE -----
st.set_page_config(page_title="🎉 Birthday Surprise", page_icon="🎂", layout="centered")
st.title(f"🎂 Happy Birthday, {BIRTHDAY_PERSON}!")
st.markdown("### 🎈 I got a little surprise for you...")

# ---------- SAFE STATE INIT ----------
st.session_state.setdefault("play_song", False)
st.session_state.setdefault("image_mode", False)
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("quiz_done", False)
st.session_state.setdefault("q_index", 0)
st.session_state.setdefault("answers", {})

# ---------- SURPRISE BUTTON ----------
if st.button("🎉 Click for a Surprise", type="primary"):
    st.session_state.play_song = True
    st.balloons()
    st.success(f"🎂 Happy Birthday {BIRTHDAY_PERSON}! Wishing you joy, love, and endless music! 🎶")
    time.sleep(1)
    st.snow()
    st.rerun()

# ---------- AFTER SURPRISE ----------
if st.session_state.play_song:
    # Autoplay audio
    
    with open(SONG_URL, "rb") as f:
        data = f.read()
        b64_song = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <audio autoplay hidden>
            <source src="data:audio/mp3;base64,{b64_song}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )
    
    time.sleep(5)  # Allow some time for the audio to start

    st.markdown("## 🎤 Some words for the birthday girl")
    styled_message = """
    <style>
    .birthday-message {
        font-family: 'Georgia', serif;
        font-size: 20px;
        line-height: 1.8;
        color: #333;
        background: linear-gradient(135deg, #fff0f5, #ffe4e1, #fffaf0);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(255, 150, 180, 0.4);
        text-align: justify;
    }

    /* Highlighted special lines */
    .highlight {
        font-family: 'Brush Script MT', cursive;
        font-size: 28px;
        font-weight: bold;
        background: linear-gradient(90deg, #ff6f91, #ff9671, #ffb3c6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 8px rgba(255, 120, 160, 0.5);
        display: block;
        text-align: center;
        margin: 20px 0;
    }
    </style>

    <div class="birthday-message">
    We’ve only met once, but that one meeting was enough to leave a really positive impression.  
    There’s something genuinely kind and refreshing about your presence that’s hard to miss.

    <span class="highlight">On your birthday, I just want to wish you happiness that feels light, peaceful, and truly yours. ✨</span>

    May this year bring you growth, success, good health, and moments that make you proud of how far you’re going.  
    Keep smiling, keep shining, and keep being exactly who you are.

    <span class="highlight">🎂 Happy Birthday, Mahi! 🌸</span>
</div>
    """

    st.markdown(styled_message, unsafe_allow_html=True)

    colA, colB = st.columns(2)
    with colA:
        if st.button("🛰️ What did Hubble see on your birthday?"):
            st.session_state.image_mode = True
            st.rerun()
    with colB:
        if st.button("💕 Start the mini-game"):
            st.session_state.quiz_started = True
            st.rerun()

# ---------- OPTIONAL HUBBLE IMAGE INFO ----------
if st.session_state.image_mode:
    image_info = (
        '''Galaxy HUDF-JD2 \n
The small red object at the center of this image (just above the large spiral galaxy) is one of the most distant galaxies ever seen. Called HUDF-JD2, it is one of about 10,000 galaxies found in the Hubble Ultra Deep Field.'''
    )
    try:
        st.image(IMAGE_FILE, use_container_width=True, caption=image_info)
    except Exception:
        st.warning("Couldn't load the image file. Make sure the path/name is correct.")

    

# ---------- QUIZ: ONE QUESTION AT A TIME ----------
if st.session_state.quiz_started and not st.session_state.quiz_done:
    st.markdown("## 💕 Mini Game: Choose Answer Wisely")

    idx = st.session_state.q_index
    total = len(questions)

    # Progress & counter
    st.progress(idx / total if total else 0)
    st.caption(f"Question {idx + 1} of {total}")

    q = questions[idx]
    # Add "Other" option to choices
    options = q["options"] + ["Other(write your answer)"]

    # Radio button for choice
    choice = st.radio(q["q"], options, key=f"radio_{idx}")

    # If "Other" is chosen → show text box
    other_text = ""
    if choice == "Other(write your answer)":
        other_text = st.text_input("Your answer:", key=f"other_{idx}")

    # Navigation buttons
    nav1, nav2, nav3 = st.columns([1,1,2])
    with nav1:
        if st.button("⬅ Back", disabled=(idx == 0)):
            st.session_state.q_index -= 1
            st.rerun()
    with nav2:
        if st.button("Next ➜" if idx < total - 1 else "✅ Finish & Save"):
            # Save/overwrite answer for the current question
            if choice == "Other(write your answer)" and other_text.strip():
                st.session_state.answers[q["q"]] = other_text.strip()
            else:
                st.session_state.answers[q["q"]] = choice

            if idx < total - 1:
                st.session_state.q_index += 1
                st.rerun()
            else:
                # Save to file on finish
                filename = "birthday_answers.txt"
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(f"--- {BIRTHDAY_PERSON}'s Birthday Quiz — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                    for q_text, ans in st.session_state.answers.items():
                        f.write(f"{q_text}\nAnswer: {ans}\n\n")
                    f.write("\n")

                # Provide download button
                with open(filename, "r", encoding="utf-8") as f:
                    st.download_button(
                        "📥 Download Saved Answers",
                        data=f,
                        file_name="birthday_answers.txt",
                        mime="text/plain"
                    )
                st.balloons()
                st.session_state.quiz_done = True


# ---------- QUIZ SUMMARY ----------
if st.session_state.quiz_done:
    st.success("💖 Your perfect date choices have been saved forever!")
    st.success("Download your answers before you leave—and share them with your date buddy!")
    st.markdown("### ✨ Your Answers")
    for q_text, ans in st.session_state.answers.items():
        st.markdown(f"- **{q_text}** — {ans}")

    colx, coly = st.columns([1,1])
    with colx:
        if st.button("🔁 Play Again"):
            st.session_state.q_index = 0
            st.session_state.answers = {}
            st.session_state.quiz_done = False
            st.session_state.quiz_started = True
            st.rerun()
    # with coly:
    #     st.caption("Saved to file: `birthday_answers.txt`")
