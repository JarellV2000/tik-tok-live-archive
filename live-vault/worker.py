"""LIVE VAULT: simple public TikTok LIVE monitor and recorder.
Requires streamlink and ffmpeg installed separately. No login, scraping bypass, or private streams.
"""
import argparse
import json
import re
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

VALID = re.compile(r"^[a-zA-Z0-9._]{2,40}$")

def load_names(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    names = data.get("usernames", [])
    if not isinstance(names, list):
        raise ValueError("usernames must be a list")
    result = []
    for name in names:
        if not isinstance(name, str) or not VALID.fullmatch(name):
            raise ValueError("Invalid username in watchlist")
        if name.lower() not in [x.lower() for x in result]:
            result.append(name)
    return result

def record_one(name, output):
    url = f"https://www.tiktok.com/@{name}/live"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = output / f"{name}-{stamp}.ts"
    # Streamlink handles public streams where supported; it may stop working as TikTok changes.
    cmd = ["streamlink", "--output", str(target), url, "best"]
    print(f"Checking @{name}", flush=True)
    try:
        result = subprocess.run(cmd, timeout=4 * 60 * 60, check=False)
        if result.returncode != 0:
            print(f"@{name}: offline, unavailable, or recording failed (exit {result.returncode})", flush=True)
            if target.exists() and target.stat().st_size == 0:
                target.unlink()
    except subprocess.TimeoutExpired:
        print(f"@{name}: recording time limit reached; will retry next cycle", flush=True)

def main():
    parser = argparse.ArgumentParser(description="Record public TikTok LIVE streams when available")
    parser.add_argument("--watchlist", default="live-vault-watchlist.json")
    parser.add_argument("--output", default="recordings")
    parser.add_argument("--interval", type=int, default=120)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    if shutil.which("streamlink") is None:
        parser.error("streamlink is required: python -m pip install streamlink")
    if args.interval < 30:
        parser.error("interval must be at least 30 seconds")
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    while True:
        names = load_names(args.watchlist)
        for name in names:
            record_one(name, output)
        if args.once:
            break
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
