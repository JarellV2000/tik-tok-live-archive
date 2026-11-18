# LIVE VAULT — development v1

A phone-friendly **local watchlist dashboard** and a separate **experimental Python recorder** for public TikTok LIVE streams. This is not a hosted recorder or cloud archive.

## Dashboard
Open `index.html` in a browser (or host it as static content). Add usernames and **Export watchlist JSON**. Watchlist data lives only in the browser until exported.

## Worker (computer/server, not iPhone Safari)
Install Python 3.10+ and [Streamlink](https://streamlink.github.io/):
```bash
python -m pip install streamlink
python live-vault/worker.py --watchlist live-vault-watchlist.json --output recordings --once
```
Run from the repository root after placing the exported JSON file there. Omit `--once` for repeated checks. The worker processes one stream at a time, so simultaneous streams can be missed. Streamlink support for TikTok varies; test with a permitted public LIVE. Output is saved locally as transport stream (`.ts`) files. There is no authentication, background hosting, cloud synchronization, playback library, or recording guarantee.

## Next steps
Add tested TikTok-specific stream resolution, concurrent workers, a secure authenticated API, remote status and recording library, storage limits, and opt-in deployment. Never commit recordings or credentials.

Only record content you have rights or permission to save. Respect creators' privacy and TikTok terms. This code does not bypass paywalls or retrieve past streams.
