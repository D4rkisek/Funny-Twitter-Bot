# Import the necessary library
import openai

openai.api_key = 'api key'


def generate_joke():
    """
    Joke Generation
    :return: str, the generated joke
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Tell me a python meme",
        temperature=1,
        max_tokens=32
    )

    joke = response.choices[0].text.strip()
    return joke

