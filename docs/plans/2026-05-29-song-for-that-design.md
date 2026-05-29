# There's a Song for That — Design Document
*2026-05-29*

## What It Is

A single-page web app where you describe a feeling, a moment, or a place — and it reveals three songs that match. Matching happens through lyrics, mood, texture, atmosphere, and collective human testimony about how music feels. All genres. No lyrics required.

The experience is meant to feel oracular: you bring something formless to it, and it gives back something precise and true.

---

## Architecture

**Two files:**
- `index.html` — the entire frontend
- `app.py` — a tiny Flask server with one endpoint

**Flow:**
1. User types a description and submits
2. Frontend POSTs to `/api/match` with `{ "description": "..." }`
3. Flask sends a crafted prompt to Claude API
4. Claude returns structured JSON with 3 matches
5. Frontend renders the three result cards

**No music database. No lyrics API.** Claude's training knowledge covers songs, classical works, jazz recordings, film scores, and the human commentary that surrounds all of it.

**Hosting:** Run locally with `python app.py`. Deploy to Render.com free tier when ready to share.

---

## The Claude Prompt Framework

The prompt teaches Claude *how to think*, not *what to pick*. Claude is given this framework:

> You are a music oracle with deep knowledge across all genres — pop, rock, classical, jazz, ambient, folk, film scores, world music, and beyond. Given a description, find 3 pieces of music that match through their lyrics, mood, feeling, texture, or atmosphere.
>
> When finding matches, draw from three layers simultaneously:
>
> **1. Direct analysis** — structure, lyrics, tempo, key, instrumentation, texture, dynamics. What the music *is*.
>
> **2. Collective human testimony** — how listeners, critics, fans, and writers have described what this music feels like. What memories people associate with it. What it has soundtracked (films, moments, movements, eras). The phrases people reach for when trying to explain it. This is evidence, not authority — weigh it alongside your own analysis.
>
> **3. Cultural and historical resonance** — what period it belongs to, what emotional landscape it occupied, how its meaning has evolved over time.
>
> Across your 3 results, deliberately vary: genre, era, and whether the match is primarily lyrical or purely felt. Instrumental music is as valid as songs with words.
>
> Avoid the obvious first answer. Prefer the match that makes someone say "how did it know?"
>
> Return valid JSON only. No preamble. Format:
> ```json
> [
>   {
>     "title": "...",
>     "artist": "...",
>     "year": "...",
>     "why": "2-3 sentences explaining the match — specific, poetic, not generic",
>     "spotify_search": "title artist",
>     "youtube_search": "title artist official"
>   }
> ]
> ```

---

## Each Result Card Displays

- Song title (large, in accent colour)
- Artist + year (smaller, charcoal)
- Why it matches (2–3 sentences — the revelation)
- "Listen on Spotify" button → opens `https://open.spotify.com/search/[encoded query]`
- "Watch on YouTube" button → opens `https://www.youtube.com/results?search_query=[encoded query]`

No API keys needed for either link. Pure search URLs.

---

## UI & Visual Design

### The Concept
Oracular. Revelatory. The visual language of stained glass and dawn light — the liminal moment between night and day. Most music apps are dark vending machines. This one should feel like a discovery.

### Background
A layered atmospheric gradient: deep indigo at the edges bleeding into warm rose, dusty peach, and pale gold at the centre. Like the sky at the exact moment between night and day. Not flat — it has depth, as if light is coming from behind it.

### Input State
Sparse and spacious. A single thin line in the centre of the screen — not a box, a line. Placeholder text in barely-there grey: *"describe a feeling, a moment, a place."* Large, elegant typography. Nothing else on the page. The cursor blinks slowly. The whole screen is the invitation.

### Thinking Animation
Not a spinner. The app appears to *listen*. Slow-drifting particles of light catching the gradient, like dust in morning sun or heat shimmer at dusk. Rotating text cycles through phrases: *"searching through sound... crossing genres... finding the feeling..."* Organic, unhurried, unhurried.

### Result Cards — The Revelation
Three cards materialise one at a time, with slight delays between them — like three records placed gently on a table. Each card is **frosted/stained glass**: translucent panels with the gradient bleeding through, a subtle blur behind, a gentle coloured glow at the edges. The quality of light through cathedral glass.

Within each card:
- Song title arrives first, in a single warm accent colour (deep amber or saturated violet) — the moment of revelation
- Artist and year appear beneath
- The explanation paragraph renders as if being written in real time
- Listen buttons emerge last, minimal and elegant

The whole materialisation sequence per card: ~1 second. Staggered across the three cards: 0.3s delay between each.

### Typography
- Titles: Elegant serif — confident, weighty
- Body/explanation: Clean humanist sans-serif — readable, warm
- UI labels: Lighter weight of the same sans-serif

### Colour Palette
- Background: Dawn/dusk gradient (indigo → rose → peach → gold)
- Text: Deep charcoal / dark indigo (dark on light — editorial, not reversed)
- Cards: Frosted translucent glass with coloured edge glow
- Accent: Single saturated colour used only for the song title reveal — warm amber or cold electric violet

---

## What's Out of Scope (for now)

- User accounts / history
- Spotify/Apple Music API integration (real playback)
- Genre or era filters on the UI
- Mobile-specific optimisation (build desktop-first, tidy mobile later)
- Sharing individual results

---

## Files

```
theres-a-song-for-that/
├── index.html
├── app.py
├── requirements.txt
└── docs/
    └── plans/
        └── 2026-05-29-song-for-that-design.md
```
