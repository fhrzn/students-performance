import streamlit as st
import requests

# Title of the app
st.title("Student Evaluation Form")

# Input fields
gender = st.selectbox("Gender", options=["Male", "Female"])
race = st.selectbox(
    "Race/Ethnicity", options=["group A", "group B", "group C", "group D", "group E"]
)
parental_edu = st.selectbox(
    "Parental Education",
    options=[
        "Master's Degree",
        "Bachelor's Degree",
        "Associate's Degree",
        "Some College",
        "High School",
        "Some High School",
    ],
)
lunch = st.selectbox("Lunch Type", options=["Standard", "Free/reduced"])
test_prep = st.selectbox("Test Preparation Course", options=["Completed", "None"])
math_score = st.number_input("Math Score", min_value=0, max_value=100)
read_score = st.number_input("Reading Score", min_value=0, max_value=100)
write_score = st.number_input("Writing Score", min_value=0, max_value=100)

# Define the API endpoint
api_url = "http://127.0.0.1:8000/predict"

# Submit Button
if st.button("Submit"):
    # Prepare the payload for the request
    payload = {
        "gender": gender,
        "race": race,
        "parental_edu": parental_edu,
        "lunch": lunch,
        "test_prep": test_prep.lower(),
        "math_score": math_score,
        "read_score": read_score,
        "write_score": write_score,
    }

    # Make the POST request
    try:
        response = requests.post(
            api_url,
            headers={"accept": "application/json", "Content-Type": "application/json"},
            json=payload,
        )
        response_data = response.json()

        # Display the response
        st.write("Predicted Score: ", round(response_data["predicted_score"], 2))
    except Exception as e:
        st.error(f"An error occurred: {e}")
