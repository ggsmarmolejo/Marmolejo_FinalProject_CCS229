import os  # Import for potential environment variable access (optional)
from openai import AsyncOpenAI
import asyncio
import streamlit as st

# Load API key securely from Streamlit Secrets
client = AsyncOpenAI(api_key=st.secrets["API_key"])


async def generate_lyrics(genre: str, language: str, topic: str = None) -> str:
    """
    Generates song lyrics based on genre, language, and optionally a topic

    Args:
        genre (str): The desired genre of the song lyrics.
        language (str): The language in which the lyrics should be generated.
        topic (str, optional): A specific theme for the song lyrics. Defaults to None.

    Returns:
        str: The generated song lyrics.
    """

    prompt_text = f"I am an AI Song Lyricist. Write me a song in the {genre} genre in {language}."
    if topic:
        prompt_text += f" The song should be about {topic}."

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_text}
        ],
    )
    return response.choices[0].message.content

# Add spacing between sentences (replace with your preferred separator)
    spaced_lyrics = lyrics.replace(". ", ". \n")  # Replace with "\n\n" for double spacing

    return spaced_lyrics

def main():
    """
    Main function to run the Streamlit application
    """
    st.title("Likhawit: An AI Song Lyricist")

    genre_options = [
        "O.P.M. (Original Pilipino Music)",
        "Hugot",
        "Pinoy Rock",
        "Kundiman",
        "Hip-Hop"
    ]
    language_options = ["Filipino", "English", "Hiligaynon"]

    genre = st.selectbox("Choose Genre", genre_options)
    language = st.selectbox("Choose Language", language_options)
    topic = st.text_input("Enter Song Topic (Optional)")

    if st.button("Generate Lyrics"):
        with st.spinner("Generating lyrics..."):
            lyrics = asyncio.run(generate_lyrics(genre, language, topic))
            st.write(f"**{genre} Song Lyrics ({language})**\n{lyrics}")


# Run the Streamlit app
if __name__ == "__main__":
    main()
