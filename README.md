# There's a Song for That

A web app that matches any description — a feeling, a moment, a place — to three songs through their mood, lyrics, texture, and cultural resonance. Powered by the Claude API.

## What it does

Type anything into the input — "leaving a party early", "the light just before a storm", "pure joy, sunlight on water" — and the app returns three song matches across different genres and eras, each with a short explanation of why it fits. Results can be reshuffled for a fresh set of matches from a different angle.

## How to run

1. Create a `.env` file in the project root with your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   python app.py
   ```

5. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Tech stack

- **Backend:** Python / Flask — serves the page and proxies requests to the Claude API
- **Frontend:** Single-file vanilla HTML/CSS/JS — no framework, no build step
- **AI:** Anthropic Claude (`claude-sonnet-4-6`) with a three-layer matching prompt (direct analysis, human testimony, cultural resonance)
- **Fonts:** Bitter (slab serif) + IBM Plex Sans via Google Fonts

## Design

Foggy beach at dawn — muted grey-blue gradient sky, warm horizon light, wet sand. Frosted glass cards with sea glass accent (`#5a9e8a`). Golden ratio spacing and type scale throughout.

## Features

- Match any description to 3 songs across genres and eras
- Each result links directly to Spotify search and YouTube
- **↺ reshuffle** — same description, 3 genuinely different matches
- **× start over** — return to the blank input instantly
- Thinking animation while the oracle searches

## Notes

- The `.env` file must be UTF-8 encoded (not UTF-16)
- Flask's auto-dotenv discovery is disabled (`load_dotenv=False` in `app.run`) to prevent it finding a wrong `.env` in a parent directory — `python-dotenv` handles loading instead
