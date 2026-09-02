# Support site — Code Harbour apps

Help, privacy policy and terms for the published apps, served by GitHub Pages at
<https://jevgenitig.github.io/my-apps/>.

**This repository is the only copy.** A second copy once lived inside the Catch
It All source tree at `site/`; the two drifted apart — that one never got the
Decanted pages and still called everything "games" — and it was deleted on
2 September 2026. Edit here, nowhere else.

## Pages and where each URL is used

| App | Folder | App Store ID |
|---|---|---|
| Decanted | `decanted/` | 6807045534 |
| Catch It All! | `catchitall/` | 6788710927 |
| Yet Another Sea Battle | `seabattle/` | 6762600309 |
| Spin N Win | `spinnwin/` | 6771497345 |
| Smash My Doodle | `doodle/` | 6763943311 |
| Yet Another Puzzle | `puzzle/` | 6763130976 |

Within each folder:

| Page | Used as |
|---|---|
| `index.html` | Support URL and Marketing URL in App Store Connect |
| `privacy.html` | Privacy Policy URL in App Store Connect, and in Play Console for the three Android apps (Sea Battle, Spin N Win, Smash My Doodle) |
| `terms.html` | linked from both of the above |

## Editing

The HTML is generated. Edit `APPS` in `build.py`, then:

```
python3 build.py
```

Commit the regenerated `.html` files — Pages serves them directly, there is no
build step on GitHub.

## Before renaming anything

These URLs are live in two store consoles. Renaming a folder, the repository, or
the account changes them and breaks a privacy policy link that Apple and Google
both check — Google refuses an app whose privacy URL does not resolve. If the
address ever has to change, update every field in both consoles in the same
sitting.
