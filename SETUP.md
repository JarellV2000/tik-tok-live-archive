# LIVE Vault setup

This is a static GitHub Pages dashboard plus a **separate** Docker recording worker. GitHub Pages cannot execute Python or Docker, and GitHub Actions should not be used as a persistent 24/7 recorder.

## Run the recorder on a Linux cloud server
1. Install Docker Engine and Docker Compose plugin on a server you control.
2. Clone this repository and change into its directory.
3. Copy `.env.example` to `.env`, then edit USERNAME as needed.
4. Run `docker compose up -d`.
5. Check `docker compose logs -f recorder` for errors.
6. Recordings are saved to `./recordings` on that server. Download using a secure transfer method (such as SFTP). Do not expose this folder publicly.

The upstream recorder is at https://github.com/Michele0303/tiktok-live-recorder . Its flags and behavior may change; check upstream documentation before deployment. A server must remain running for continuous monitoring. TikTok may block datacenter IPs, and the recorder may fail due to upstream changes.

## Dashboard
Enable GitHub Pages from repository Settings > Pages > Deploy from a branch. Select the branch you want to publish and root folder. The dashboard is not connected to a live backend and does not claim real-time recording status. Its archive links point to independent services; old recordings are not guaranteed.

## Privacy
Keep the repo private until you deliberately choose to publish a dashboard. GitHub Pages site visibility depends on your plan and settings; do not put secrets or private videos in the published site. Respect creators' rights and applicable laws.
