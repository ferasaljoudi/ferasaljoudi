import requests
from bs4 import BeautifulSoup

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
response = requests.get(joke_url)
joke_svg = response.text

soup = BeautifulSoup(joke_svg, "html.parser")
for script in soup(["script", "style"]):
    script.decompose()

cleaned_joke_svg = str(soup)

with open("README.md", "r") as file:
    readme = file.readlines()

marker = "<!-- JOKE HERE -->"

def insert_joke_at_marker(marker, cleaned_joke_svg, readme):
    for idx, line in enumerate(readme):
        if marker in line:
            readme[idx] = f"{marker}\n\n{cleaned_joke_svg}\n"
            break

insert_joke_at_marker(marker, cleaned_joke_svg, readme)

with open("README.md", "w") as file:
    file.writelines(readme)
