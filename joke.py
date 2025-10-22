import json
import random
import sys
import urllib.request

API_URLS = [
    # Returns { "joke": "..." }
    ("https://icanhazdadjoke.com/", {"Accept": "application/json"}),
    # Returns { "setup": "...", "punchline": "..." }
    ("https://official-joke-api.appspot.com/random_joke", {}),
]

FALLBACK_JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break... and it froze.",
    "There are 10 types of people in the world: those who understand binary and those who don’t.",
]

def fetch_json(url, headers=None, timeout=6):
    """Fetch JSON data from a URL with optional headers."""
    req = urllib.request.Request(url)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        return json.loads(data.decode("utf-8"))

def get_joke():
    """Try multiple APIs to get a random joke, fall back to local list if needed."""
    for url, headers in API_URLS:
        try:
            data = fetch_json(url, headers)
            if "joke" in data:
                return data["joke"]
            if "setup" in data and "punchline" in data:
                return f"{data['setup']} — {data['punchline']}"
        except Exception:
            continue
    return random.choice(FALLBACK_JOKES)

if __name__ == "__main__":
    joke = get_joke()
    print("😄 Random joke:")
    print(joke)
    sys.exit(0)