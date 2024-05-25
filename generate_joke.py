import requests
from bs4 import BeautifulSoup
import subprocess

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
response = requests.get(joke_url)
joke_svg = response.text

soup = BeautifulSoup(joke_svg, "html.parser")
for script in soup(["script", "style"]):
    script.decompose()

cleaned_joke_svg = str(soup)

with open("randomJoke.svg", "w") as file:
    file.write(cleaned_joke_svg)