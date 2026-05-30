# UI Redesign — Foggy Beach Dawn
*2026-05-30*

## What's Changing

A full visual redesign of `index.html` — palette, fonts, spacing, and two new result controls. The HTML structure, Flask backend, and Claude prompt are untouched.

---

## Palette

**Background:** Vertical linear gradient (top → bottom), replacing the radial pink/purple:
- Top: `#7a96aa` — muted blue-grey sky
- 25%: `#a8bfcc` — lighter sky, fog thickening
- 50%: `#cdd9de` — near horizon, dense mist
- 65%: `#d8cfc4` — the horizon band, barely-warm first light
- 80%: `#c8d4d8` — wet sand reflecting sky
- 100%: `#b8ccd2` — wet sand foreground

Grain texture stays (same SVG noise overlay, same opacity).

**Text:**
- Dark: `#1e2d35` — deep blue-grey (replaces indigo)
- Medium: `#3a5260` — mid blue-grey
- Muted: `rgba(30, 45, 53, 0.45)`
- Ghost: `rgba(30, 45, 53, 0.28)`

**Accent:** `#7db5a0` — sea glass (muted sage-green with blue undertones). Used on song titles only.

**Card glows (three cards):**
- Card 1: `rgba(140, 175, 195, 0.55)` — misty blue
- Card 2: `rgba(200, 210, 200, 0.55)` — pale sand
- Card 3: `rgba(125, 181, 160, 0.50)` — sea glass

**Card background:** `rgba(255, 255, 255, 0.14)` — slightly cooler/more transparent than before. Border: `rgba(255, 255, 255, 0.38)`.

---

## Typography

**Display font:** `Bitter` (Google Fonts, weights 400/600/700) — slab serif, sturdy, grounded.
**Body font:** `IBM Plex Sans` (Google Fonts, weights 300/400/500) — clean, cool-toned.

Both replace Cormorant Garamond and DM Sans entirely.

**Font scale (golden ratio, φ = 1.618):**
| Token | Size | Use |
|---|---|---|
| `--fs-xs` | `0.75rem` | Labels, year, wordmark |
| `--fs-sm` | `1rem` | Body text, "why" paragraph |
| `--fs-md` | `1rem` medium | Artist name |
| `--fs-lg` | `1.618rem` | Song title |
| `--fs-xl` | `2.618rem` | (reserved / future) |

**Spacing scale (golden ratio):**
| Token | Size | Use |
|---|---|---|
| `--sp-xs` | `0.618rem` | Tight gaps (meta row spacing) |
| `--sp-sm` | `1rem` | Default padding, button padding |
| `--sp-md` | `1.618rem` | Card inner padding (sides) |
| `--sp-lg` | `2.618rem` | Card inner padding (top/bottom), section gaps |
| `--sp-xl` | `4.236rem` | Large screen breathing room |

---

## New Controls on Results Page

Two ghost-text buttons added to the compact bar (right side), alongside the existing search input:

**↺ reshuffle** — reruns `query(currentDescription)` with the description stored from the last search. Gets 3 fresh song matches for the same input.

**× start over** — resets to the input screen: hides results, shows `#input-screen`, clears `mainInput.value`.

Both styled as small text buttons matching the compact bar's restraint — no borders, letter-spaced, muted colour, hover darkens slightly.

`currentDescription` must be stored in the JS closure so reshuffle can access it.

---

## Files

Only `index.html` changes. No other files touched.

---

## Scope

- CSS variables updated
- Google Fonts link updated (Bitter + IBM Plex Sans)
- Background gradient updated
- All `--font-display` and `--font-body` references updated
- Card glow values updated
- Golden ratio spacing tokens added and applied throughout
- Two new buttons added to compact bar HTML
- JS: store `currentDescription`, add reshuffle handler, add start-over handler
- Commit: `feat: redesign UI with foggy beach dawn palette and reshuffle/start-over controls`
