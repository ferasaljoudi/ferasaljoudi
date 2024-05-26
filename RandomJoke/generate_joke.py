import requests

joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%231E90F0&aColor=%23EFE372&bgColor=%230d1117"
# joke_url = "https://v2.jokeapi.dev/joke/Programming,Spooky?format=txt"
response = requests.get(joke_url)
joke_text = response.text

with open("randomJoke.svg", "r") as file:
    readme = file.readlines()

start_marker = "<!-- JOKE START -->"
end_marker = "<!-- JOKE END -->"

def insert_joke_between_markers(start_marker, end_marker, joke_text, readme):
    start_idx = None
    end_idx = None
    
    for idx, line in enumerate(readme):
        if start_marker in line:
            start_idx = idx
        if end_marker in line:
            end_idx = idx

    if start_idx is not None and end_idx is not None:
        readme = readme[:start_idx+1] + [f"\n{joke_text}\n"] + readme[end_idx:]
    return readme

readme = insert_joke_between_markers(start_marker, end_marker, joke_text, readme)

with open("randomJoke.svg", "w") as file:
    file.writelines(readme)
