import requests

# joke_url = "https://readme-jokes.vercel.app/api?hideBorder&qColor=%238C52FF&aColor=%23EFE372&bgColor=black"
joke_url = "https://v2.jokeapi.dev/joke/Programming,Spooky?format=txt"
response = requests.get(joke_url)
joke_text = response.text

def style_joke(joke_text):
    parts = joke_text.split("\n")
    if len(parts) == 1:
        return f"""
        <div style="border: 2px solid #4CAF50; padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">
            <p style="font-family: Arial, sans-serif; font-size: 1.2em; color: #333;">
                {parts[0]}
            </p>
        </div>
        """
    elif len(parts) == 2:
        return f"""
        <div style="border: 2px solid #4CAF50; padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">
            <p style="font-family: Arial, sans-serif; font-size: 1.2em; color: #333;">
                <span style="color: #007bff;">{parts[0]}</span><br><br>
                <span style="color: #dc3545;">{parts[1]}</span>
            </p>
        </div>
        """
    else:
        return joke_text

styled_joke = style_joke(joke_text)

with open("README.md", "r") as file:
    readme = file.readlines()

start_marker = "<!-- JOKE START -->"
end_marker = "<!-- JOKE END -->"

def insert_joke_between_markers(start_marker, end_marker, styled_joke, readme):
    start_idx = None
    end_idx = None
    
    for idx, line in enumerate(readme):
        if start_marker in line:
            start_idx = idx
        if end_marker in line:
            end_idx = idx

    if start_idx is not None and end_idx is not None:
        readme = readme[:start_idx+1] + [f"\n{styled_joke}\n"] + readme[end_idx:]
    return readme

readme = insert_joke_between_markers(start_marker, end_marker, styled_joke, readme)

with open("README.md", "w") as file:
    file.writelines(readme)