#!/usr/bin/env python3
"""Generates the static support site from the data below.

Run after editing GAMES:  python3 build.py
The generated .html files are committed — GitHub Pages serves them directly.
"""
from pathlib import Path

ROOT = Path(__file__).parent
DEV = "Jevgeni Agnevstsikov"
MAIL = "agnevstsikov@gmail.com"
UPDATED = "25 August 2026"

# ── Content ───────────────────────────────────────────────────────────────────
# Everything here is checked against the App Store listing and the app's source.
# If you are unsure whether a claim is true, leave it out.

GAMES = [
    dict(
        slug="catchitall", name="Catch It All!", appid="6788710927",
        icon="catchitall.png", tagline="Catch what falls before it lands",
        about=[
            "The game is built out of <b>locations</b> — separate worlds, each with its own "
            "setting, playable characters, things to catch and a cartoon at the end.",
            "<b>One location is free and always will be.</b> You can play it from beginning to "
            "end without paying. Every further location is a separate one-time purchase, yours "
            "permanently once bought. No subscription, no currency, no timer.",
        ],
        howto=[
            ("Catch the falling items.", "They roll off the shelves on both sides and drop. "
             "Four buttons move you left or right, up or down."),
            ("You start with 3 lives.", "Every item that hits the ground costs one."),
            ("Earn lives back.", "After 20 catches, ten in a row without a miss returns a life."),
            ("Catch 100 to finish", "a location and unlock its cartoon."),
        ],
        purchases="Locations beyond the free one are one-time purchases.",
        stored="your best score for each location, and which locations you have unlocked",
        network="The game runs entirely on your device. A connection is only needed the moment "
                "you buy or restore a location.",
        terms=True,
    ),
    dict(
        slug="seabattle", name="Yet Another Sea Battle", appid="6762600309",
        icon="seabattle.png", tagline="Place your fleet, find theirs first",
        about=[
            "Classic naval combat: place your ships, then hunt the opponent's fleet before they "
            "sink yours.",
            "Play against the computer at several difficulty levels, hand one device back and "
            "forth in Pass &amp; Play, or connect two devices on the same Wi-Fi network.",
        ],
        howto=[
            ("Place your fleet.", "Drag ships onto the grid and rotate them until you are happy."),
            ("Take turns firing.", "Pick a cell on the opponent's grid. Hits, misses and sunk "
             "ships are marked for you."),
            ("Sink everything", "to win."),
        ],
        purchases="There is one optional purchase that supports development. The game is fully "
                  "playable without it.",
        stored="your settings and whether you have made the optional purchase",
        network="Single player and Pass &amp; Play work with no connection at all. Two-device "
                "play sends moves <b>directly between the two devices on your local Wi-Fi "
                "network</b> — there is no server in between and nothing is stored online.",
        terms=True,
    ),
    dict(
        slug="spinnwin", name="Spin N Win", appid="6771497345",
        icon="spinnwin.png", tagline="Spin, answer, guess the word",
        about=[
            "A word-guessing trivia game. Spin the wheel to land on a category, answer the "
            "question to reveal a hidden letter, and guess the word before your spins run out.",
            "Categories include History, Geography, Religion, Sport, Mathematics and Art, and the "
            "game is available in 10 languages: English, Russian, French, German, Spanish, "
            "Portuguese, Arabic, Chinese, Japanese and Korean.",
        ],
        howto=[
            ("Spin the wheel", "to land on a category."),
            ("Answer the question", "to reveal a hidden letter."),
            ("Guess the word", "before your spins run out."),
        ],
        purchases="There is one optional purchase that supports development. The game is fully "
                  "playable without it.",
        stored="your progress, statistics and settings, and whether you have made the optional "
               "purchase",
        network="The game runs on your device. A connection is only needed for purchases.",
        terms=True,
    ),
    dict(
        slug="doodle", name="Smash My Doodle", appid="6763943311",
        icon="doodle.png", tagline="Draw your enemy, then smash it",
        about=[
            "Stress relief, roughly. Draw whoever is bothering you, then destroy the drawing with "
            "a barrage of food projectiles before the timer runs out.",
            "Nine levels and a final boss. No connection needed.",
        ],
        howto=[
            ("Draw your target.", "Anything you like — it becomes the thing you smash."),
            ("Smash it.", "Fling projectiles at it before time runs out."),
            ("Clear nine levels", "and the boss at the end."),
        ],
        purchases="There is one optional purchase that supports development. The game is fully "
                  "playable without it.",
        stored="your progress, your settings, and whether you have made the optional purchase",
        network="The game runs on your device. A connection is only needed for purchases.",
        terms=True,
    ),
    dict(
        slug="puzzle", name="Yet Another Puzzle", appid="6763130976",
        icon="puzzle.png", tagline="Turn any photo into a jigsaw",
        about=[
            "Pick a picture from your camera roll, snap a new one, or import any image, and it "
            "becomes a real jigsaw in seconds.",
            "Choose the piece count and a shattering effect — glass, fire, electric, shockwave or "
            "ice — then solve it yourself or send the puzzle to someone else.",
        ],
        howto=[
            ("Pick a photo.", "From your camera roll, the camera, or any image you import."),
            ("Choose piece count and effect.", "More pieces, more evenings."),
            ("Solve it", "or hand it to someone else to solve."),
        ],
        purchases="There is one optional purchase that supports development. The game is fully "
                  "playable without it.",
        stored="your puzzles in progress, your settings, and whether you have made the optional "
               "purchase",
        network="Your photos stay on your device — they are never uploaded to us. A connection "
                "is only needed for purchases.",
        terms=True,
    ),
]

# ── Templates ─────────────────────────────────────────────────────────────────

def page(title, body, depth=0, desc=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
{f'<meta name="description" content="{desc}">' if desc else ''}
<link rel="icon" href="{up}img/favicon.png">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="wrap">
{body}
</div>
</body>
</html>
"""


def support_page(g):
    howto = "\n".join(
        f"    <li><b>{a}</b> {b}</li>" for a, b in g["howto"])
    about = "\n".join(f'  <p class="a">{p}</p>' for p in g["about"])
    terms_link = ' &nbsp;·&nbsp; <a href="terms.html">Terms of Use</a>' if g.get("terms") else ""
    body = f"""  <a class="back" href="../">&larr; All games</a>

  <header>
    <img src="../img/{g['icon']}" alt="{g['name']} app icon">
    <div>
      <h1>{g['name']}</h1>
      <p class="sub">{g['tagline']}</p>
    </div>
  </header>

  <a class="store" href="https://apps.apple.com/app/id{g['appid']}">GET IT ON THE APP STORE</a>

  <h2>ABOUT</h2>
{about}

  <h2>HOW TO PLAY</h2>
  <ol>
{howto}
  </ol>

  <h2>QUESTIONS</h2>

  <p class="q">I made a purchase but it is not there.</p>
  <p class="a">Look for <b>Restore Purchases</b> in the app. Purchases are tied to your Apple
     Account, so this also works on a new device.</p>

  <p class="q">Does the game need an internet connection?</p>
  <p class="a">{g['network']}</p>

  <p class="q">Are there ads?</p>
  <p class="a">No. None of our games show ads.</p>

  <p class="q">The purchase failed or was charged twice.</p>
  <p class="a">Purchases and refunds are handled by Apple, not by us. Use
     <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>, and write to us as
     well so we can help.</p>

  <h2>CONTACT</h2>
  <div class="mail">
    Questions, bugs or ideas — write to <a href="mailto:{MAIL}">{MAIL}</a>.
    Please mention your device and iOS version; it makes bugs much easier to find.
  </div>

  <footer>
    <span>© 2026 {DEV}</span>
    <span><a href="privacy.html">Privacy Policy</a>{terms_link}</span>
  </footer>"""
    return page(f"{g['name']} — Support", body, depth=1,
                desc=f"Support and help for {g['name']}.")


def privacy_page(g):
    terms_link = ' &nbsp;·&nbsp; <a href="terms.html">Terms of Use</a>' if g.get("terms") else ""
    body = f"""  <a class="back" href="index.html">&larr; {g['name']}</a>

  <h1>Privacy Policy</h1>
  <p class="upd">{g['name']} &middot; Last updated {UPDATED}</p>

  <p>{g['name']} is developed by {DEV}. This policy explains what the app does with your
     information. The short version: it does not collect any.</p>

  <h2>WHAT WE COLLECT</h2>
  <p><b>Nothing.</b> The app collects no personal information. There is no account, no sign-in, no
     analytics, no advertising and no third-party tracking. We operate no servers that could
     receive your data.</p>

  <h2>WHAT STAYS ON YOUR DEVICE</h2>
  <p>The app saves {g['stored']}. This is stored only on your device and is removed when you
     delete the app.</p>

  <h2>CONNECTIVITY</h2>
  <p>{g['network']}</p>

  <h2>PURCHASES</h2>
  <p>{g['purchases']} Payments are processed entirely by Apple. We never see or receive your
     payment details — Apple tells the app only whether a purchase succeeded. Apple's handling of
     that transaction is covered by
     <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

  <h2>CHILDREN</h2>
  <p>Because the app collects no data at all, it collects no data from children either. There is no
     advertising and there are no social features.</p>

  <h2>CHANGES</h2>
  <p>If this policy changes, the revised version will be published on this page with a new date.</p>

  <h2>CONTACT</h2>
  <p>Questions about this policy: <a href="mailto:{MAIL}">{MAIL}</a></p>

  <footer><span>© 2026 {DEV}</span><span><a href="index.html">Support</a>{terms_link}</span></footer>"""
    return page(f"{g['name']} — Privacy Policy", body, depth=1)


def hub_page():
    cards = "\n".join(f"""    <a class="card" href="{g['slug']}/">
      <img src="img/{g['icon']}" alt="">
      <div>
        <b>{g['name']}</b>
        <span>{g['tagline']}</span>
      </div>
    </a>""" for g in GAMES)
    body = f"""  <header class="hub">
    <div>
      <h1>{DEV}</h1>
      <p class="sub">Small games for iPhone and iPad. No ads, no accounts, no data collection.</p>
    </div>
  </header>

  <h2>GAMES</h2>
  <div class="cards">
{cards}
  </div>

  <h2>CONTACT</h2>
  <div class="mail">
    Questions, bugs or ideas about any of these — write to
    <a href="mailto:{MAIL}">{MAIL}</a>.
  </div>

  <footer><span>© 2026 {DEV}</span></footer>"""
    return page(f"{DEV} — Games", body, desc="Support pages for all games by " + DEV)


# ── Write ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    written = []
    (ROOT / "index.html").write_text(hub_page())
    written.append("index.html")
    for g in GAMES:
        d = ROOT / g["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(support_page(g))
        (d / "privacy.html").write_text(privacy_page(g))
        written += [f"{g['slug']}/index.html", f"{g['slug']}/privacy.html"]
    print("wrote:")
    for w in written:
        print(" ", w)
    print("\nterms.html files are hand-written and not regenerated.")
