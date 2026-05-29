import os
import json
from flask import Flask, request, jsonify, send_from_directory
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

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
