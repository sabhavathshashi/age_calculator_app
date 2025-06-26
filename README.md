# age_calculator_app
# 🔴 Dynamic Age Calculator – Streamlit App

## 🚀 Description

A modern web app built using **Python** and **Streamlit** that calculates a user's age based on their date of birth. It features a **custom red-on-white theme** inspired by *Whole Lotta Red* aesthetics, using the `.streamlit/config.toml` configuration for consistent branding. The app auto-updates the current date daily and provides real-time age output in years.

---

## 🧠 Features

* 📅 `st.date_input()` for entering Date of Birth
* 📌 Auto-updating current date
* 🔄 Real-time age calculation
* 🎨 Custom UI theme (red text, white background, bold font)
* 🧾 Displays age accurately, adjusting for birthday occurrence
* 💾 Clean and minimal UI with bold styling using Streamlit’s theming config

---

## 🧰 Tech Stack

* **Python**
* **Streamlit**
* `datetime` module

---

## 📁 Folder Structure

```
Age-Calculator-App/
├── app.py
└── .streamlit/
    └── config.toml
```

---

## 🧑‍💻 Run Locally

```bash
git clone https://github.com/your-username/age-calculator-app.git
cd age-calculator-app
streamlit run app.py
```

---

## 📸 Screenshots

*Add screenshots of your UI here, especially showing the red-themed age output.*

---

## 🧾 Sample Code Snippet

```python
from datetime import date
import streamlit as st

today = date.today()
dob = st.date_input("Enter your Date of Birth", value=date(2000,1,1), min_value=date(1900,1,1), max_value=today)
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.write(f"Your age is: {age} years")
```

---

## 📦 Bonus Ideas

* Add session state to store and re-use DOB
* Show age in months and days
* Deploy on **Streamlit Cloud** for public access
* Add animations, emoji styling, or music vibe intro
