import streamlit as st
import time

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Quiz App", page_icon="🎯")

# -------------------------
# Questions
# -------------------------
questions = [
    {"question": "What is the capital of France?",
     "options": ["Berlin", "Madrid", "Paris", "Rome"],
     "answer": "Paris"},

    {"question": "Which language is used for web development?",
     "options": ["Python", "JavaScript", "C++", "Java"],
     "answer": "JavaScript"},

    {"question": "What does CPU stand for?",
     "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Power Unit"],
     "answer": "Central Processing Unit"},

    {"question": "What is 8 × 7?",
     "options": ["54", "56", "58", "60"],
     "answer": "56"},

    {"question": "Which data structure uses FIFO?",
     "options": ["Queue", "Stack", "Tree", "Graph"],
     "answer": "Queue"},

    {"question": "Who is the father of computers?",
     "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
     "answer": "Charles Babbage"},

    {"question": "Which keyword defines a function in Python?",
     "options": ["func", "define", "def", "function"],
     "answer": "def"},

    {"question": "What is the output of 3 + 2 * 2?",
     "options": ["10", "8", "7", "12"],
     "answer": "7"},

    {"question": "Which planet is known as the Red Planet?",
     "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": "Mars"},

    {"question": "What is the largest ocean on Earth?",
     "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
     "answer": "Pacific"}
]

# -------------------------
# Session State Init
# -------------------------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.name = ""
    st.session_state.q = 0
    st.session_state.score = 0

# -------------------------
# Restart (Full Reset)
# -------------------------
if st.sidebar.button("🔄 Restart"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# -------------------------
# START SCREEN (Name Input)
# -------------------------
if not st.session_state.started:
    st.title("🎯 Welcome to the Quiz App")

    name = st.text_input("Enter your name:")

    if st.button("Start Quiz"):
        if name.strip() == "":
            st.warning("Please enter your name")
        else:
            st.session_state.name = name
            st.session_state.started = True
            st.rerun()

# -------------------------
# QUIZ SCREEN
# -------------------------
else:
    st.sidebar.title("📊 Quiz Info")
    current_q_display = min(st.session_state.q + 1, len(questions))
    st.sidebar.write(f"👤 {st.session_state.name}")
    st.sidebar.write(f"Question: {current_q_display}/{len(questions)}")
    st.sidebar.write(f"Score: {st.session_state.score}")

    st.title(f"🎯 Good luck, {st.session_state.name}!")

    progress = st.session_state.q / len(questions)
    st.progress(progress)

    if st.session_state.q < len(questions):

        q = questions[st.session_state.q]

        st.subheader(f"Q{st.session_state.q + 1}: {q['question']}")

        choice = st.radio("Choose one:", q["options"], key=st.session_state.q)

        if st.button("Submit Answer"):

            if choice == q["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Correct answer: {q['answer']}")

            time.sleep(1)
            st.session_state.q += 1
            st.rerun()

    else:
        st.balloons()
    
        # Show user name clearly
        st.title(f"🏆 Quiz Completed!")
        st.subheader(f"👤 Player: {st.session_state.name}")

        score = st.session_state.score
        total = len(questions)
        percent = (score / total) * 100

        st.metric("Score", f"{score}/{total}")
        st.metric("Percentage", f"{percent:.2f}%")

        # Personalized feedback
        if percent >= 80:
            st.success(f"🔥 Excellent work, {st.session_state.name}!")
        elif percent >= 50:
            st.info(f"👍 Good job, {st.session_state.name}!")
        else:
            st.warning(f"📘 Keep practicing, {st.session_state.name}!")

        # Restart button
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()