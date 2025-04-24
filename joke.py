import streamlit as st
import openai
from openai import OpenAI
import os

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Title of the web app
st.title("Joke Explanation App")

# Text box for user to enter the joke
joke_input = st.text_area("Enter your joke here:")

# Button to submit the joke
if st.button("Submit"):
    if joke_input:
        # Call the OpenAI API to get an explanation of the joke
        try:
            response = client.chat.completions.create(
                model="openai/gpt-4o-mini",  # Change model as needed
                messages=[
                    {"role": "user", "content": f"Explain this joke: {joke_input}"}
                ]
            )
            # Extract the message from the response
            explanation = response.choices[0].message.content
            # Display the explanation
            st.subheader("Explanation:")
            st.write(explanation)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a joke before submitting.")
