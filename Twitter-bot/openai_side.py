# Import the necessary library
import openai

openai.api_key = 'your-openai-api-key'


def generate_joke():
    """
    Joke Generation
    :return: str, the generated joke
    """
    response = openai.Completion.create(
        model="got-3.5-turbo",
        engine="text-davinci-002",
        prompt="Tell me a hilarious programming/Computer Science joke/meme",
        temperature=0.7,
        max_tokens=30
    )

    # Get the content of the generated joke
    joke = response.choices[0].text.strip()

    return joke
