import requests

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
response = requests.get(joke_url)
joke_svg = response.text

with open("randomJoke.svg", "w") as file:
    file.write(joke_svg)