# streamlit_app.py

import streamlit as st
import random

# Title
st.title("User Info Collector")

# User inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
email = st.text_input("Enter your email (optional):")
occupation = st.text_input("Enter your occupation (optional):")

# Submit button
if st.button("Submit"):
    if not name or age == 0:
        st.error("Please enter at least your name and age.")
    else:
        # Simulate determining location (replace with real API later)
        countries = ['USA', 'India', 'Germany', 'Brazil', 'Japan']
        selected_country = random.choice(countries)

        # Dummy details based on country
        country_info = {
            'USA': "You might be from a place known for tech and diversity.",
            'India': "India! A land of languages, festivals, and IT talent.",
            'Germany': "Germany — precise engineering and great football.",
            'Brazil': "Brazil brings vibrant culture and football passion.",
            'Japan': "Japan — technology, tradition, and anime!",
        }

        # Display user info
        st.success("Information submitted successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        if email:
            st.write(f"**Email:** {email}")
        if occupation:
            st.write(f"**Occupation:** {occupation}")
        st.write(f"**Detected Country (dummy):** {selected_country}")
        st.info(country_info[selected_country])
