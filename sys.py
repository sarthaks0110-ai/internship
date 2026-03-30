import streamlit as st
import calendar
from datetime import datetime

# Session storage for reminders
if "reminders" not in st.session_state:
    st.session_state.reminders = {}

st.set_page_config(page_title="Calendar Reminder App", page_icon="📅", layout="centered")

st.title("📅 Calendar & Reminder App")

# ---------------- Calendar Section ----------------

st.subheader("📆 View Calendar")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=1900, max_value=2100, value=datetime.now().year)

with col2:
    month = st.number_input("Month", min_value=1, max_value=12, value=datetime.now().month)

if st.button("Show Calendar"):
    cal = calendar.month(year, month)
    st.code(cal)

# ---------------- Reminder Section ----------------

st.subheader("⏰ Add Reminder")

date = st.date_input("Select Date")
reminder_text = st.text_input("Reminder")

if st.button("Add Reminder"):

    if reminder_text == "":
        st.warning("Please enter reminder text")
    else:
        date_str = str(date)

        if date_str not in st.session_state.reminders:
            st.session_state.reminders[date_str] = []

        st.session_state.reminders[date_str].append(reminder_text)

        st.success(f"Reminder added for {date_str}")

# ---------------- View Reminders ----------------

st.subheader("📌 View Reminders")

view_date = st.date_input("Select date to view reminders", key="view")

view_date_str = str(view_date)

if st.button("Show Reminders"):

    if view_date_str in st.session_state.reminders:

        st.write(f"### Reminders for {view_date_str}")

        for r in st.session_state.reminders[view_date_str]:
            st.markdown(f"- {r}")

    else:
        st.info("No reminders for this date")

# ---------------- All Reminders ----------------

st.subheader("📋 All Stored Reminders")

if st.session_state.reminders:

    for d, items in st.session_state.reminders.items():

        st.write(f"**{d}**")

        for r in items:
            st.markdown(f"- {r}")

else:
    st.write("No reminders added yet")