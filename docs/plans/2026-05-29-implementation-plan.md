# There's a Song for That — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a single-page web app where users describe a feeling and receive 3 musically matched songs via the Claude API, with a visually stunning dawn/dusk stained-glass aesthetic.

**Architecture:** Flask serves both the frontend HTML at `/` and the `/api/match` POST endpoint. The Claude API does all music matching using a carefully crafted prompt. No external music database needed. Two files: `app.py` and `index.html`.

**Tech Stack:** Python 3.10+, Flask 3.x, Anthropic Python SDK, vanilla HTML/CSS/JS (no framework), Google Fonts (Playfair Display + Inter)

---

### Task 1: Project Setup

**Files:**
- Create: `requirements.txt`
- Create: `.env.example`
- Create: `.gitignore`

**Step 1: Create `requirements.txt`**

```
flask==3.0.3
anthropic==0.28.0
python-dotenv==1.0.1
```

**Step 2: Create `.env.example`**

```
ANTHROPIC_API_KEY=your_key_here
```

**Step 3: Create `.gitignore`**

```
.env
__pycache__/
*.pyc
venv/
.venv/
```

**Step 4: Set up virtual environment and install**

```bash
cd theres-a-song-for-that
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Expected: All packages install without error. `flask`, `anthropic`, and `python-dotenv` all appear in `pip list`.

**Step 5: Create `.env` with real API key**

Your Anthropic API key is already set up in `C:\Users\hamis\OneDrive\Coding\index-ma-study\.env`. Copy the `ANTHROPIC_API_KEY` value from there into a new `.env` file in this project. No need to generate a new key.

**Step 6: Commit**

```bash
git add requirements.txt .env.example .gitignore
git commit -m "chore: project setup and dependencies"
```

---

### Task 2: Flask Backend

**Files:**
- Create: `app.py`
- Create: `tests/test_app.py`

**Step 1: Write the failing tests**

```python
# tests/test_app.py
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_match_requires_description(client):
    """Empty body returns 400, no Claude call made."""
    response = client.post('/api/match',
        data=json.dumps({}),
        content_type='application/json')
    assert response.status_code == 400

def test_match_requires_non_empty_description(client):
    """Blank description returns 400."""
    response = client.post('/api/match',
        data=json.dumps({'description': '   '}),
        content_type='application/json')
    assert response.status_code == 400

def test_index_route_exists(client):
    """Root route returns something (200 once index.html exists, 404 until then — both are ok here)."""
    response = client.get('/')
    assert response.status_code in [200, 404]
```

**Step 2: Run tests to verify they fail**

```bash
pip install pytest
pytest tests/test_app.py -v
```

Expected: `ImportError: cannot import name 'app' from 'app'` — correct, app doesn't exist yet.

**Step 3: Create `app.py`**

```python
import os
import json
from flask import Flask, request, jsonify, send_from_directory
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.')
client = Anthropic()

PROMPT = """You are a music oracle with deep knowledge across all genres — pop, rock, classical, jazz, ambient, folk, film scores, world music, and beyond. Given a description, find 3 pieces of music that match through their lyrics, mood, feeling, texture, or atmosphere.

When finding matches, draw from three layers simultaneously:

1. Direct analysis — structure, lyrics, tempo, key, instrumentation, texture, dynamics. What the music *is*.

2. Collective human testimony — how listeners, critics, fans, and writers have described what this music feels like. What memories people associate with it. What it has soundtracked (films, moments, movements, eras). The phrases people reach for when trying to explain it. This is evidence, not authority — weigh it alongside your own analysis.

3. Cultural and historical resonance — what period it belongs to, what emotional landscape it occupied, how its meaning has evolved over time.

Across your 3 results, deliberately vary: genre, era, and whether the match is primarily lyrical or purely felt. Instrumental music is as valid as songs with words.

Avoid the obvious first answer. Prefer the match that makes someone say "how did it know?"

Return valid JSON only. No preamble. No markdown fences. Just the raw JSON array:
[
  {
    "title": "...",
    "artist": "...",
    "year": "...",
    "why": "2-3 sentences explaining the match — specific, poetic, not generic",
    "spotify_search": "title artist",
    "youtube_search": "title artist official"
  }
]"""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/match', methods=['POST'])
def match():
    data = request.get_json()
    if not data or not data.get('description', '').strip():
        return jsonify({'error': 'description is required'}), 400

    description = data['description'].strip()

    message = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=1024,
        messages=[{
            'role': 'user',
            'content': f'{PROMPT}\n\nDescription: {description}'
        }]
    )

    try:
        text = message.content[0].text
        songs = json.loads(text)
        return jsonify(songs)
    except (json.JSONDecodeError, IndexError):
        return jsonify({'error': 'Failed to parse response'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Step 4: Run tests**

```bash
pytest tests/test_app.py -v
```

Expected: All 3 tests pass. These tests do NOT call the Claude API — they only test routing and validation logic.

**Step 5: Smoke test the real endpoint manually**

```bash
python app.py
```

Then in a second terminal:

```bash
curl -X POST http://localhost:5000/api/match -H "Content-Type: application/json" -d "{\"description\": \"standing at the edge of something\"}"
```

Expected: A JSON array of 3 song objects. If you see 3 varied results with a "why" field that feels specific and resonant, the backend is working.

**Step 6: Commit**

```bash
git add app.py tests/test_app.py
git commit -m "feat: Flask backend with Claude matching endpoint"
```

---

### Task 3: Frontend — Invoke the frontend-design Skill

**Files:**
- Create: `index.html`

**Step 1: Invoke the `frontend-design` skill**

This task must use the `frontend-design` skill — it is purpose-built for distinctive, production-grade UI and will produce far better results than a manually written page.

Brief the skill with the following spec:

---

*Build a single-file `index.html` (vanilla HTML/CSS/JS, no framework, no build step) for an app called "There's a Song for That."*

**Concept:** Oracular. Revelatory. The visual language of stained glass at dawn. Most music apps feel like dark vending machines. This one should feel like a discovery.

**Fonts (Google Fonts):**
- `Playfair Display` — for the app title and song title reveals
- `Inter` — for body text, explanations, UI labels

**Background:**
A layered radial gradient suggesting dawn/dusk sky. Example:
```css
background: radial-gradient(ellipse at center, #f5d0a9 0%, #e8a0b4 30%, #b06090 55%, #4a2060 80%, #1a0a30 100%);
```
Not flat — it should feel like light coming from within. Full viewport height, no scroll on the input screen.

**Input state (the whole first screen):**
- App title at top: "there's a song for that" — small, elegant, Playfair Display, deep charcoal, barely there
- Centred on the screen: a single thin horizontal line (not a box — literally `border-bottom: 1px solid`)
- The `<input>` sits on this line, transparent background, no border except the bottom line
- Placeholder text: `"describe a feeling, a moment, a place."`
- Placeholder in barely-there grey (opacity ~0.4), large and elegant (Playfair Display, ~1.4rem)
- A submit button beneath: minimal, no heavy border, just text "find the song →" in Inter, small
- Nothing else on screen. Maximum spaciousness. The gradient fills everything.

**Thinking animation (shown while awaiting API response):**
- Hide the input section
- Show a full-screen centred state
- Floating particles: 20–30 small dots (2–4px) slowly drifting upward/sideways with varying speeds and opacity — achieved with CSS keyframe animations and JS-generated elements. Colours drawn from the gradient palette (rose, amber, violet, soft gold)
- Rotating text below centre, cycling every 2.5s through:
  - `"searching through sound..."`
  - `"crossing genres..."`
  - `"tracing the feeling..."`
  - `"listening..."`
  - `"finding what you mean..."`
- Text in Playfair Display italic, deep charcoal, medium size

**Result cards — the revelation:**
- Cards appear below the (now minimised) input section — input shrinks to a small line at the top so user can search again
- Three cards materialise one at a time with a 400ms stagger between them
- Each card uses CSS `backdrop-filter: blur(12px)` with a semi-transparent background — frosted/stained glass
- Card border: `1px solid rgba(255,255,255,0.3)` with a subtle box-shadow in a warm tinted colour
- Card border-radius: generous (~20px)
- Inside each card:
  1. Song title — Playfair Display, large (1.6rem), warm amber (`#c8860a` or similar)
  2. Artist — Inter, medium weight, deep charcoal
  3. Year — Inter, smaller, muted
  4. Divider line — thin, semi-transparent
  5. "Why it matches" paragraph — Inter, readable size (~1rem), line-height 1.7, dark charcoal, feels like a personal letter
  6. Two buttons side by side: "Listen on Spotify" and "Watch on YouTube"
     - Minimal style: small text, subtle border, rounded pill shape
     - Spotify button: soft green tint; YouTube button: soft rose tint
     - Links: `https://open.spotify.com/search/[encodeURIComponent(spotify_search)]` and `https://www.youtube.com/results?search_query=[encodeURIComponent(youtube_search)]`
- Cards animate in with: `opacity: 0 → 1` + `translateY(20px → 0)`, duration 600ms, ease-out

**JS behaviour:**
- On submit: validate input not empty, show thinking animation, POST to `/api/match` with `{"description": "..."}`, then hide thinking, show cards
- Handle errors: if API returns error or network fails, show a gentle message: `"Something slipped through the ether. Try again."`
- After results show: input at top shrinks to allow new searches (typing a new description and submitting replaces the cards)
- No page reload at any point

---

**Step 2: Run manually and verify**

```bash
python app.py
```

Open `http://localhost:5000` and verify:

- [ ] Gradient background fills the screen beautifully
- [ ] Input line is centred, minimal, elegant
- [ ] Placeholder text is visible but not heavy
- [ ] Typing and submitting triggers the particle animation
- [ ] Cycling text changes every ~2.5s
- [ ] Three cards appear with staggered timing
- [ ] Song titles are in amber, large, Playfair Display
- [ ] "Why it matches" reads as specific and poetic
- [ ] Spotify and YouTube buttons open correct search pages in new tab
- [ ] A second search from the same page works without refresh

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add frontend with dawn/dusk stained glass design"
```

---

### Task 4: End-to-End Quality Check

**Step 1: Test a range of descriptions**

Run `python app.py` and test:

| Description | What to look for |
|---|---|
| `"standing at the edge of something"` | At least one instrumental; varied eras |
| `"the feeling of leaving a party early and walking home alone"` | Avoids the obvious (no "Mr. Brightside") |
| `"pure joy, sunlight on water"` | Something surprising — not just "Happy" by Pharrell |
| `"grief that has softened into something quiet"` | Deep cuts, not just "Hallelujah" |
| `"a 4am city, alone but not lonely"` | Jazz or classical alongside something modern |
| `"the colour blue, but as a sound"` | Tests abstract interpretation |

For each: confirm 3 results, varied genres/eras, specific "why" explanations, working links.

**Step 2: Test edge cases**

- One word: `"sad"` — should still return 3 varied, thoughtful results
- Long paragraph — should handle without error
- Special characters: `"café, autumn, rain"` — should handle encoding correctly

**Step 3: Final commit if any fixes were made**

```bash
git add -A
git commit -m "fix: polish from end-to-end testing"
```

---

### Task 5: GitHub Remote

**Step 1: Create remote repo**

```bash
gh repo create theres-a-song-for-that --public --description "A music oracle: describe a feeling, discover the song"
```

**Step 2: Push**

```bash
git push -u origin master
```

Expected: Repo appears at `github.com/[your-username]/theres-a-song-for-that`.

---

## File Tree at Completion

```
theres-a-song-for-that/
├── index.html
├── app.py
├── requirements.txt
├── .env              (not committed — contains API key)
├── .env.example      (committed — shows structure)
├── .gitignore
├── tests/
│   └── test_app.py
└── docs/
    └── plans/
        ├── 2026-05-29-song-for-that-design.md
        └── 2026-05-29-implementation-plan.md
```

## Notes for Claude Executing This Plan

- The `frontend-design` skill is **mandatory** for Task 3. Do not skip it or build the HTML manually — the design quality is the product.
- Use model `claude-sonnet-4-6` in `app.py` — good quality, affordable. Do not downgrade to Haiku (quality matters here) or upgrade to Opus unnecessarily.
- The `.env` file must never be committed. Verify `.gitignore` is working before Task 5.
- The particle animation must be CSS/JS only — no canvas libraries, no three.js, no external animation deps.
