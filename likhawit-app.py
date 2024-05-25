import os
from openai import AsyncOpenAI
import asyncio
import streamlit as st

client = AsyncOpenAI(api_key=st.secrets["API_key"])

async def generate_lyrics(genre, language, topic):
    """
    Generates song lyrics based on genre, language, and optionally a topic
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

def main():
    st.title("Likhawit: An AI Song Lyricist")

    genre_options = ["O.P.M. (Original Pilipino Music)", "Hugot", "Pinoy Rock", "Kundiman", "Hip-Hop"]
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
