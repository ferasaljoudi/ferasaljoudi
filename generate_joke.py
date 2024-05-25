import requests

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
response = requests.get(joke_url)
joke_svg = response.text

with open("README.md", "r") as file:
    readme = file.readlines()

marker = "<!-- JOKE HERE -->"

def insert_joke_at_marker(marker, joke_svg, readme):
    for idx, line in enumerate(readme):
        if marker in line:
            readme[idx] = f"{marker}\n\n{joke_svg}\n"
            break

insert_joke_at_marker(marker, joke_svg, readme)

with open("README.md", "w") as file:
    file.writelines(readme)
