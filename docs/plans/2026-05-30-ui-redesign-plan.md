# UI Redesign — Foggy Beach Dawn — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign `index.html` with a foggy beach dawn palette, Bitter + IBM Plex Sans fonts, golden ratio spacing tokens, and two new result-screen controls (reshuffle + start over).

**Architecture:** Single-file HTML — all changes are CSS, HTML structure (compact bar), and vanilla JS. Flask backend and `app.py` are completely untouched. No new files created.

**Tech Stack:** Vanilla HTML/CSS/JS. Google Fonts CDN (Bitter, IBM Plex Sans).

---

## Task 1: Swap Google Fonts + rewrite `:root` CSS variables

**Files:**
- Modify: `index.html` (line 9 — fonts `<link>`, lines 12–26 — `:root` block)

**What this covers:**
- Remove Cormorant Garamond + DM Sans from the Google Fonts URL
- Add Bitter (ital,wght 400/600/700 + italic 400) + IBM Plex Sans (300/400/500)
- Replace all custom property values in `:root`
- Add golden ratio font and spacing tokens

---

**Step 1: Replace the Google Fonts `<link>` (line 9)**

Find this exact line:
```html
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300;1,9..40,400&display=swap" rel="stylesheet">
```

Replace with:
```html
    <link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Sans:wght@300;400;500&display=swap" rel="stylesheet">
```

---

**Step 2: Replace the entire `:root` block (lines 12–26)**

Find this exact block:
```css
        :root {
            --font-display: 'Cormorant Garamond', 'Georgia', serif;
            --font-body: 'DM Sans', system-ui, sans-serif;

            --text-dark:   #1e1040;
            --text-medium: #3d2060;
            --text-muted:  rgba(30, 16, 64, 0.42);
            --text-ghost:  rgba(30, 16, 64, 0.28);

            --accent: #bf7a08;

            --glow-rose:   rgba(245, 168, 188, 0.6);
            --glow-amber:  rgba(250, 198, 100, 0.6);
            --glow-violet: rgba(190, 120, 210, 0.6);
        }
```

Replace with:
```css
        :root {
            --font-display: 'Bitter', 'Georgia', serif;
            --font-body: 'IBM Plex Sans', system-ui, sans-serif;

            --text-dark:   #1e2d35;
            --text-medium: #3a5260;
            --text-muted:  rgba(30, 45, 53, 0.45);
            --text-ghost:  rgba(30, 45, 53, 0.28);

            --accent: #7db5a0;

            --glow-1: rgba(140, 175, 195, 0.55);
            --glow-2: rgba(200, 210, 200, 0.55);
            --glow-3: rgba(125, 181, 160, 0.50);

            /* Golden ratio font scale (φ = 1.618) */
            --fs-xs: 0.75rem;
            --fs-sm: 1rem;
            --fs-lg: 1.618rem;
            --fs-xl: 2.618rem;

            /* Golden ratio spacing scale */
            --sp-xs: 0.618rem;
            --sp-sm: 1rem;
            --sp-md: 1.618rem;
            --sp-lg: 2.618rem;
            --sp-xl: 4.236rem;
        }
```

---

**Step 3: Replace the background gradient (lines 45–53)**

Find this exact block inside `.bg { ... }`:
```css
            background: radial-gradient(
                ellipse 130% 130% at 50% 58%,
                #fce7c0 0%,
                #f8c4cc 16%,
                #d882b8 36%,
                #9858a8 56%,
                #5c3490 74%,
                #2e1455 100%
            );
```

Replace with:
```css
            background: linear-gradient(
                180deg,
                #7a96aa 0%,
                #a8bfcc 25%,
                #cdd9de 50%,
                #d8cfc4 65%,
                #c8d4d8 80%,
                #b8ccd2 100%
            );
```

---

**Step 4: Verify in browser**

Open `http://localhost:5000`. The page background should now show a vertical grey-blue gradient — sky at top, warm horizon band in the middle, wet sand at the bottom. Text should be dark blue-grey instead of indigo. The grain texture remains.

---

**Step 5: Commit**

```bash
git add index.html
git commit -m "feat: swap fonts to Bitter + IBM Plex Sans, apply foggy beach palette to :root and background"
```

---

## Task 2: Apply tokens and update font styles throughout CSS

**Files:**
- Modify: `index.html` (CSS section — all rules below `:root`)

**What this covers:**
- Replace hard-coded `rgba(30, 16, 64, ...)` with `rgba(30, 45, 53, ...)` everywhere they appear (border colors, dividers, card rules)
- Apply `--fs-*` and `--sp-*` tokens throughout
- Update font-weight 300 → 400 for display font (Bitter has no 300 weight)
- Remove `font-style: italic` from main-input and compact-input (blockier feel)
- Update card shadow colors from purple to blue-grey
- Update card background + border to the design-spec values

---

**Step 1: Update `.wordmark` font-size and color-dependent borders**

Find:
```css
        .wordmark {
            position: absolute;
            top: 2.4rem;
            left: 50%;
            transform: translateX(-50%);
            font-family: var(--font-display);
            font-weight: 300;
            font-size: 0.78rem;
```

Replace with:
```css
        .wordmark {
            position: absolute;
            top: 2.4rem;
            left: 50%;
            transform: translateX(-50%);
            font-family: var(--font-display);
            font-weight: 400;
            font-size: var(--fs-xs);
```

---

**Step 2: Update `.input-stage` gap**

Find:
```css
            gap: 2rem;
```
(inside `.input-stage`)

Replace with:
```css
            gap: var(--sp-lg);
```

---

**Step 3: Update `.line-field` border color**

Find:
```css
            border-bottom: 1px solid rgba(30, 16, 64, 0.22);
```

Replace with:
```css
            border-bottom: 1px solid rgba(30, 45, 53, 0.22);
```

Find:
```css
            border-color: rgba(30, 16, 64, 0.48);
```

Replace with:
```css
            border-color: rgba(30, 45, 53, 0.48);
```

---

**Step 4: Update `#main-input` font properties**

Find this block:
```css
        #main-input {
            width: 100%;
            background: transparent;
            border: none;
            outline: none;
            font-family: var(--font-display);
            font-style: italic;
            font-weight: 300;
            font-size: 1.55rem;
            line-height: 1.4;
            color: var(--text-dark);
            text-align: center;
            caret-color: var(--accent);
        }

        #main-input::placeholder {
            color: var(--text-ghost);
            font-style: italic;
        }
```

Replace with:
```css
        #main-input {
            width: 100%;
            background: transparent;
            border: none;
            outline: none;
            font-family: var(--font-display);
            font-weight: 400;
            font-size: var(--fs-lg);
            line-height: 1.4;
            color: var(--text-dark);
            text-align: center;
            caret-color: var(--accent);
        }

        #main-input::placeholder {
            color: var(--text-ghost);
        }
```

---

**Step 5: Update `.oracle-btn` font-size and weight**

Find:
```css
            font-weight: 300;
            font-size: 0.78rem;
            letter-spacing: 0.16em;
```
(inside `.oracle-btn`)

Replace with:
```css
            font-weight: 400;
            font-size: var(--fs-xs);
            letter-spacing: 0.16em;
```

---

**Step 6: Update `.inline-error` font properties**

Find:
```css
        .inline-error {
            font-family: var(--font-display);
            font-style: italic;
            font-size: 0.88rem;
```

Replace with:
```css
        .inline-error {
            font-family: var(--font-display);
            font-size: var(--fs-xs);
```

---

**Step 7: Update `.oracle-phrase` font properties**

Find:
```css
            font-family: var(--font-display);
            font-style: italic;
            font-weight: 300;
            font-size: 1.25rem;
```

Replace with:
```css
            font-family: var(--font-display);
            font-style: italic;
            font-weight: 400;
            font-size: 1.25rem;
```

(Italic stays here — gives the thinking phrase a slightly softer character)

---

**Step 8: Update `.compact-mark` font properties**

Find:
```css
        .compact-mark {
            font-family: var(--font-display);
            font-weight: 300;
            font-size: 0.72rem;
```

Replace with:
```css
        .compact-mark {
            font-family: var(--font-display);
            font-weight: 400;
            font-size: var(--fs-xs);
```

---

**Step 9: Update `.compact-divider` color**

Find:
```css
            background: rgba(30, 16, 64, 0.18);
```
(inside `.compact-divider`)

Replace with:
```css
            background: rgba(30, 45, 53, 0.18);
```

---

**Step 10: Update `#compact-input` font and border**

Find this block:
```css
        #compact-input {
            flex: 1;
            min-width: 0;
            background: transparent;
            border: none;
            border-bottom: 1px solid rgba(30, 16, 64, 0.18);
            outline: none;
            font-family: var(--font-display);
            font-style: italic;
            font-weight: 300;
            font-size: 0.98rem;
            color: var(--text-dark);
            padding: 0.2rem 0;
            transition: border-color 0.3s ease;
        }

        #compact-input::placeholder {
            color: var(--text-ghost);
        }

        #compact-input:focus {
            border-color: rgba(30, 16, 64, 0.38);
        }
```

Replace with:
```css
        #compact-input {
            flex: 1;
            min-width: 0;
            background: transparent;
            border: none;
            border-bottom: 1px solid rgba(30, 45, 53, 0.18);
            outline: none;
            font-family: var(--font-display);
            font-weight: 400;
            font-size: var(--fs-sm);
            color: var(--text-dark);
            padding: 0.2rem 0;
            transition: border-color 0.3s ease;
        }

        #compact-input::placeholder {
            color: var(--text-ghost);
        }

        #compact-input:focus {
            border-color: rgba(30, 45, 53, 0.38);
        }
```

---

**Step 11: Update `.cards-wrap` padding**

Find:
```css
            padding: 2.5rem 1.5rem 4rem;
```

Replace with:
```css
            padding: var(--sp-lg) var(--sp-sm) var(--sp-xl);
```

---

**Step 12: Update `.reveal-label` font properties**

Find:
```css
        .reveal-label {
            font-family: var(--font-display);
            font-weight: 300;
            font-size: 0.72rem;
            letter-spacing: 0.2em;
            text-transform: lowercase;
            color: var(--text-ghost);
            text-align: center;
            margin-bottom: 2rem;
        }
```

Replace with:
```css
        .reveal-label {
            font-family: var(--font-display);
            font-weight: 400;
            font-size: var(--fs-xs);
            letter-spacing: 0.2em;
            text-transform: lowercase;
            color: var(--text-ghost);
            text-align: center;
            margin-bottom: var(--sp-lg);
        }
```

---

**Step 13: Update `.song-card` background, border, and box-shadow**

Find this exact block:
```css
        .song-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(22px);
            -webkit-backdrop-filter: blur(22px);
            border: 1px solid rgba(255, 255, 255, 0.42);
            border-radius: 22px;
            padding: 2rem 2.2rem 1.8rem;
            position: relative;
            overflow: hidden;
            opacity: 0;
            transform: translateY(32px);
            transition:
                opacity  700ms ease-out,
                transform 700ms cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 280ms ease;
            box-shadow:
                0 4px 28px rgba(46, 20, 85, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.52);
        }
```

Replace with:
```css
        .song-card {
            background: rgba(255, 255, 255, 0.14);
            backdrop-filter: blur(22px);
            -webkit-backdrop-filter: blur(22px);
            border: 1px solid rgba(255, 255, 255, 0.38);
            border-radius: 22px;
            padding: var(--sp-lg) var(--sp-md) var(--sp-lg);
            position: relative;
            overflow: hidden;
            opacity: 0;
            transform: translateY(32px);
            transition:
                opacity  700ms ease-out,
                transform 700ms cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 280ms ease;
            box-shadow:
                0 4px 28px rgba(30, 45, 53, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.52);
        }
```

---

**Step 14: Update `.song-card.visible:hover` box-shadow**

Find:
```css
            box-shadow:
                0 10px 44px rgba(46, 20, 85, 0.17),
                inset 0 1px 0 rgba(255, 255, 255, 0.6);
```

Replace with:
```css
            box-shadow:
                0 10px 44px rgba(30, 45, 53, 0.17),
                inset 0 1px 0 rgba(255, 255, 255, 0.6);
```

---

**Step 15: Update `.song-title` font properties**

Find:
```css
        .song-title {
            font-family: var(--font-display);
            font-weight: 500;
            font-size: 1.9rem;
```

Replace with:
```css
        .song-title {
            font-family: var(--font-display);
            font-weight: 600;
            font-size: var(--fs-lg);
```

---

**Step 16: Update `.song-meta` margin and `.artist` font-size**

Find:
```css
            margin-bottom: 1.3rem;
```
(inside `.song-meta`)

Replace with:
```css
            margin-bottom: var(--sp-sm);
```

Find:
```css
        .artist {
            font-family: var(--font-body);
            font-weight: 500;
            font-size: 0.9rem;
```

Replace with:
```css
        .artist {
            font-family: var(--font-body);
            font-weight: 500;
            font-size: var(--fs-sm);
```

Find:
```css
        .year {
            font-family: var(--font-body);
            font-weight: 300;
            font-size: 0.82rem;
```

Replace with:
```css
        .year {
            font-family: var(--font-body);
            font-weight: 300;
            font-size: var(--fs-xs);
```

---

**Step 17: Update `.card-rule` gradient color**

Find:
```css
            background: linear-gradient(90deg, rgba(30,16,64,0.14) 0%, transparent 100%);
```

Replace with:
```css
            background: linear-gradient(90deg, rgba(30,45,53,0.14) 0%, transparent 100%);
```

---

**Step 18: Update `.song-why` font-size and margin**

Find:
```css
        .song-why {
            font-family: var(--font-body);
            font-weight: 300;
            font-size: 0.93rem;
            line-height: 1.8;
            color: var(--text-dark);
            margin-bottom: 1.55rem;
        }
```

Replace with:
```css
        .song-why {
            font-family: var(--font-body);
            font-weight: 300;
            font-size: var(--fs-sm);
            line-height: 1.8;
            color: var(--text-dark);
            margin-bottom: var(--sp-sm);
        }
```

---

**Step 19: Update `.song-links` gap**

Find:
```css
            gap: 0.65rem;
```
(inside `.song-links`)

Replace with:
```css
            gap: var(--sp-xs);
```

---

**Step 20: Verify in browser**

Open `http://localhost:5000`. Check:
- [ ] Wordmarks and labels use Bitter (slab serif, slightly chunkier)
- [ ] Body text uses IBM Plex Sans (clean, modern)
- [ ] Main input is non-italic, Bitter weight 400
- [ ] Song titles are Bitter SemiBold (600), slightly smaller than before (1.618rem)
- [ ] Cards have cooler, less transparent background — readable against the foggy gradient
- [ ] No purple in any shadow or border

---

**Step 21: Commit**

```bash
git add index.html
git commit -m "feat: apply golden ratio tokens and update font weights/colors throughout CSS"
```

---

## Task 3: Update JS arrays, add reshuffle + start-over controls

**Files:**
- Modify: `index.html` (compact-bar HTML, CSS additions, JS section)

**What this covers:**
- Update `GLOWS` array to foggy beach glow colours
- Update `PARTICLE_COLORS` to grey-blue foggy palette
- Add `<div class="compact-actions">` with two new buttons to the compact bar
- Add `.compact-actions` and `.compact-action` CSS
- Add `currentDescription` variable in JS closure
- Update `query()` to save `currentDescription`
- Add reshuffle event handler
- Add start-over event handler

---

**Step 1: Update the `GLOWS` array in JS (line ~513)**

Find:
```javascript
        const GLOWS = [
            'rgba(245, 168, 188, 0.65)',
            'rgba(250, 196, 96, 0.65)',
            'rgba(188, 114, 210, 0.65)'
        ];
```

Replace with:
```javascript
        const GLOWS = [
            'rgba(140, 175, 195, 0.55)',
            'rgba(200, 210, 200, 0.55)',
            'rgba(125, 181, 160, 0.50)'
        ];
```

---

**Step 2: Update `PARTICLE_COLORS` to foggy beach palette**

Find:
```javascript
        const PARTICLE_COLORS = [
            '#f5b4c2', '#fde0b0', '#c070aa',
            '#f0c060', '#e890b4', '#d4a0e8', '#fbd0a0'
        ];
```

Replace with:
```javascript
        const PARTICLE_COLORS = [
            '#a8c4d4', '#cdd9de', '#7db5a0',
            '#b8ccd2', '#8fb5c8', '#c8d4d8', '#7a96aa'
        ];
```

---

**Step 3: Add the two new buttons to the compact bar HTML**

Find the compact bar block (around line 483):
```html
        <div class="compact-bar">
            <span class="compact-mark">there's a song for that</span>
            <div class="compact-divider"></div>
            <input
                type="text"
                id="compact-input"
                placeholder="try another feeling..."
                autocomplete="off"
                spellcheck="false"
            />
            <button class="compact-go" id="compact-submit">→</button>
        </div>
```

Replace with:
```html
        <div class="compact-bar">
            <span class="compact-mark">there's a song for that</span>
            <div class="compact-divider"></div>
            <input
                type="text"
                id="compact-input"
                placeholder="try another feeling..."
                autocomplete="off"
                spellcheck="false"
            />
            <button class="compact-go" id="compact-submit">→</button>
            <div class="compact-actions">
                <button class="compact-action" id="reshuffle-btn">↺ reshuffle</button>
                <button class="compact-action" id="start-over-btn">× start over</button>
            </div>
        </div>
```

---

**Step 4: Add CSS for the new action buttons**

Find the `.compact-go:hover { color: var(--text-dark); }` rule (the last compact-bar rule, around line 290). Add the following CSS block immediately after it:

```css
        .compact-actions {
            display: flex;
            align-items: center;
            gap: var(--sp-xs);
            flex-shrink: 0;
        }

        .compact-action {
            background: transparent;
            border: none;
            cursor: pointer;
            font-family: var(--font-body);
            font-size: var(--fs-xs);
            letter-spacing: 0.08em;
            color: var(--text-muted);
            padding: 0.2rem var(--sp-xs);
            flex-shrink: 0;
            transition: color 0.2s ease;
            white-space: nowrap;
        }

        .compact-action:hover {
            color: var(--text-dark);
        }
```

---

**Step 5: Add `currentDescription` variable to JS closure**

Find the comment and DOM section opening in JS:
```javascript
        // ── DOM ────────────────────────────────────────────
        const inputScreen    = document.getElementById('input-screen');
```

Add one line immediately before it:
```javascript
        // ── State ──────────────────────────────────────────
        let currentDescription = '';

        // ── DOM ────────────────────────────────────────────
        const inputScreen    = document.getElementById('input-screen');
```

---

**Step 6: Update `query()` to save `currentDescription`**

Find this block inside the `query` function:
```javascript
        async function query(description) {
            if (!description.trim()) return;
            showThinking();
```

Replace with:
```javascript
        async function query(description) {
            if (!description.trim()) return;
            currentDescription = description.trim();
            showThinking();
```

---

**Step 7: Add reshuffle and start-over event handlers**

Find the last event listener block:
```javascript
        // Focus on load
        mainInput.focus();
```

Add the two new handlers immediately before it:
```javascript
        document.getElementById('reshuffle-btn').addEventListener('click', () => {
            if (currentDescription) query(currentDescription);
        });

        document.getElementById('start-over-btn').addEventListener('click', () => {
            resultsScreen.style.display = 'none';
            inputScreen.style.display = 'flex';
            mainInput.value = '';
            mainInput.focus();
        });

        // Focus on load
        mainInput.focus();
```

---

**Step 8: Verify in browser — full flow test**

Open `http://localhost:5000`. Run through this checklist:

- [ ] Enter a description (e.g. "watching the tide go out at dusk") → hit enter or the → button
- [ ] Thinking screen appears with floating particles in grey-blue palette (no pink/purple particles)
- [ ] Results appear: three cards with misty blue / pale sand / sea glass glows
- [ ] Song titles are sea glass green (`#7db5a0`), Bitter SemiBold
- [ ] Compact bar has wordmark | divider | input | → | ↺ reshuffle | × start over
- [ ] Click **↺ reshuffle** — thinking screen reappears, 3 new results load for the same description
- [ ] Click **× start over** — input screen reappears, input is empty and focused
- [ ] Type a new description in compact bar → → — new results replace old ones
- [ ] The whole page looks like a foggy dawn beach — no purple, no pink

---

**Step 9: Commit**

```bash
git add index.html
git commit -m "feat: redesign UI with foggy beach dawn palette and reshuffle/start-over controls"
```

---

## Done

All three tasks complete. The redesign is live. `app.py` and all other files are untouched.
