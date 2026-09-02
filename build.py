#!/usr/bin/env python3
"""Generates the static support site from the data below.

Run after editing APPS:  python3 build.py
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

APPS = [
    dict(
        slug="decanted", name="Decanted", appid="6807045534",
        icon="decanted.png", kind="app",
        tagline="Photograph the label, keep the note",
        about=[
            "A private journal for the wine you drink. Photograph the label and Decanted reads "
            "what it can &mdash; producer, name, vintage, region, grapes, alcohol &mdash; and fills "
            "the form in for you. Everything it suggests is yours to correct before you save.",
            "<b>There is no account and no server.</b> Your bottles, photos, notes and ratings are "
            "stored on your device and nowhere else. Nothing is uploaded, and there is nothing to "
            "sign in to.",
            "Over time the journal adds up to a picture of what you actually drink &mdash; which "
            "countries and styles, which vintages, where you were, and how you score. Your best "
            "bottles are ranked from your own ratings alone: there is nobody else's score to "
            "compare against, and none is asked for.",
        ],
        howto=[
            ("Photograph the label.", "Take a new photo or pick one you already have. The text is "
             "read on your device, and nothing is sent anywhere to do it."),
            ("Check what it read.", "The fields it filled in are marked, so you can see what came "
             "from the label and what did not. Correct anything that is wrong."),
            ("Rate it and add a note.", "A rating from 1 to 10, where you drank it, what you paid, "
             "and whatever you want to remember."),
            ("Find it again.", "Search by producer, name, region or grape, or filter by style, "
             "country, vintage or rating. Similar bottles are suggested from what you have "
             "already saved."),
            ("See what it adds up to.", "Charts of your collection by country, style, grape and "
             "vintage, where you drank each bottle, and how you tend to score. Alongside them, "
             "your top wines overall and within each style and country."),
            ("Send a bottle to someone.", "Share wines with another Decanted user as a file. What "
             "arrives is kept aside until they choose to add it, and their journal remembers who "
             "sent it."),
            ("Put your name to it.", "A name and a photograph of your own, if you want them. Both "
             "stay on your phone; the name travels only inside a file you choose to send, and the "
             "photograph never leaves at all."),
            ("Keep a copy.", "Export your whole journal &mdash; entries and photos &mdash; as a "
             "single file you can store where you like, and import it back on another device."),
        ],
        purchases=None,
        stored="the wines you add, their photos, your ratings, notes and tags, the name and "
               "photograph you set for yourself, and your settings",
        network="Decanted works with no connection at all. Reading a label and searching your "
                "journal happen entirely on your device. The one exception: if you allow location "
                "access, the app asks Apple to turn your coordinates into a place name so it can "
                "fill in where you were &mdash; that request goes to Apple, and only the place "
                "name is saved. Your coordinates are not stored, and you can leave location "
                "switched off. Sharing a wine sends a file the way any file leaves your phone "
                "&mdash; you choose the app and the person, and nothing goes anywhere until you "
                "do. Your profile photograph is never part of it: it is left out of shared files, "
                "out of backups, and off the cards you export.",
        terms=True,
    ),
    dict(
        slug="catchitall", name="Catch It All!", appid="6788710927",
        icon="catchitall.png", tagline="Catch what falls before it lands",
        about=[
            "The game is built out of <b>locations</b> — separate worlds, each with its own "
            "setting, playable characters, its own way to play and a cartoon at the end.",
            "<b>One location is free and always will be.</b> You can play it from beginning to "
            "end without paying. Every further location is a separate one-time purchase, yours "
            "permanently once bought. No subscription, no currency, no timer.",
        ],
        howto=[
            ("Catch the falling items.", "In most locations things roll off the shelves on both "
             "sides and drop. Four buttons move you left or right, up or down."),
            ("Some locations invert that.", "In Lake Fishing the fish bite and the fishermen reel "
             "them up. You move onto the line a fish is on and cut it, setting the fish free "
             "before it is pulled out of the water."),
            ("You start with 3 lives.", "Every item you fail to catch &mdash; or, in Lake Fishing, "
             "every fish that gets landed &mdash; costs one."),
            ("Earn lives back.", "After 20 catches, ten in a row without a miss returns a life. "
             "Lake Fishing has no life recovery: the 3 you start with are all you get."),
            ("Reach 100 to finish", "a location and unlock its cartoon."),
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
    is_game = g.get("kind", "game") == "game"
    howto_heading = "HOW TO PLAY" if is_game else "HOW IT WORKS"
    howto = "\n".join(
        f"    <li><b>{a}</b> {b}</li>" for a, b in g["howto"])
    about = "\n".join(f'  <p class="a">{p}</p>' for p in g["about"])
    terms_link = ' &nbsp;·&nbsp; <a href="terms.html">Terms of Use</a>' if g.get("terms") else ""
    paid = g.get("purchases") is not None
    restore_q = ("""  <p class="q">I made a purchase but it is not there.</p>
  <p class="a">Look for <b>Restore Purchases</b> in the app. Purchases are tied to your Apple
     Account, so this also works on a new device.</p>

""" if paid else "")
    charged_q = ("""  <p class="q">The purchase failed or was charged twice.</p>
  <p class="a">Purchases and refunds are handled by Apple, not by us. Use
     <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>, and write to us as
     well so we can help.</p>

""" if paid else """  <p class="q">Does it cost anything?</p>
  <p class="a">No. The app is free, and there is nothing to buy inside it.</p>

""")
    body = f"""  <a class="back" href="../">&larr; All apps</a>

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

  <h2>{howto_heading}</h2>
  <ol>
{howto}
  </ol>

  <h2>QUESTIONS</h2>

{restore_q}  <p class="q">Does the game need an internet connection?</p>
  <p class="a">{g['network']}</p>

  <p class="q">Are there ads?</p>
  <p class="a">No. None of our apps show ads.</p>

{charged_q}  <h2>CONTACT</h2>
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
    purchases_section = (f"""  <h2>PURCHASES</h2>
  <p>{g['purchases']} Payments are processed entirely by Apple. We never see or receive your
     payment details — Apple tells the app only whether a purchase succeeded. Apple's handling of
     that transaction is covered by
     <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

""" if g.get("purchases") else """  <h2>PURCHASES</h2>
  <p>There are none. The app is free and contains nothing to buy, so no payment information is
     ever involved.</p>

""")
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

{purchases_section}  <h2>CHILDREN</h2>
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
    </a>""" for g in APPS)
    body = f"""  <header class="hub">
    <div>
      <h1>{DEV}</h1>
      <p class="sub">Small apps and games for iPhone and iPad. No ads, no accounts, no data
         collection.</p>
    </div>
  </header>

  <h2>APPS</h2>
  <div class="cards">
{cards}
  </div>

  <h2>CONTACT</h2>
  <div class="mail">
    Questions, bugs or ideas about any of these — write to
    <a href="mailto:{MAIL}">{MAIL}</a>.
  </div>

  <footer><span>© 2026 {DEV}</span></footer>"""
    return page(f"{DEV} — Apps", body, desc="Support pages for all apps by " + DEV)


# ── Write ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    written = []
    (ROOT / "index.html").write_text(hub_page())
    written.append("index.html")
    for g in APPS:
        d = ROOT / g["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(support_page(g))
        (d / "privacy.html").write_text(privacy_page(g))
        written += [f"{g['slug']}/index.html", f"{g['slug']}/privacy.html"]
    print("wrote:")
    for w in written:
        print(" ", w)
    print("\nterms.html files are hand-written and not regenerated.")
