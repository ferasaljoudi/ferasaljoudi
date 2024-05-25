import requests

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
response = requests.get(joke_url)
joke_svg = response.text

with open("README.md", "r") as file:
    readme = file.readlines()

start_idx = None
end_idx = None
for idx, line in enumerate(readme):
    if '<!-- JOKE START -->' in line:
        start_idx = idx
    if '<!-- JOKE END -->' in line:
        end_idx = idx + 1

if start_idx is not None and end_idx is not None:
    del readme[start_idx:end_idx]

readme.insert(1, f"\n<!-- JOKE START -->\n{joke_svg}\n<!-- JOKE END -->\n")

with open("README.md", "w") as file:
    file.writelines(readme)
