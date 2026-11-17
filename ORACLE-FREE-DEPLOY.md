# Free Oracle Cloud deployment (manual account setup required)

This project is **not yet deployed**. Oracle Always Free is subject to account eligibility, available capacity, and idle VM reclamation. Never enable paid resources without checking the cost estimate.

## 1. Provision
1. Sign up at https://www.oracle.com/cloud/free/ from your iPhone. Oracle may require identity/payment verification.
2. In the Oracle console, create an **Always Free eligible** Ubuntu VM in your home region. An Ampere A1 shape may be available, but capacity varies. Select an appropriate boot disk within free limits.
3. Add your SSH public key during creation. Do not paste private keys, credentials, or TikTok cookies into GitHub.
4. Allow outbound HTTPS; **do not expose the recordings directory or Docker daemon to the internet**.

## 2. Install and launch
Connect to the VM with SSH, then install Docker Engine and the Compose plugin following https://docs.docker.com/engine/install/ubuntu/ . Clone your repository and start the recorder:

```bash
git clone https://github.com/JarellV2000/tik-tok-live-archive.git
cd tik-tok-live-archive
git checkout feature/live-dashboard
cp .env.example .env
mkdir -p recordings
chmod 700 recordings
docker compose up -d
docker compose logs --tail=100 recorder
```

For a private repository, GitHub authentication is needed to clone. The supplied compose file checks the selected account approximately once a minute; the application may need cookies and may not work from some datacenter IP addresses.

## 3. Private storage and iPhone retrieval
The Docker bind mount saves videos in `recordings/` on the VM. This directory is ignored by Git and must **never** be committed. To retrieve a file, use an SFTP client on your iPhone over SSH. Use SSH keys, keep the SSH port restricted when possible, and back up important files: free VM storage is not a durable archive guarantee.

## 4. Website
The static `index.html` is a dashboard shell only. GitHub Pages cannot run the recorder or browse private VM files. A future authenticated backend is needed to list and stream saved recordings securely. Do not make a public recording index.

## 5. Validation
Run `docker compose ps` and `docker compose logs -f recorder`. A running container does **not** guarantee the selected TikTok account has been successfully monitored or recorded. Verify an actual public LIVE and a completed video file before relying on it.

Official Oracle free resources: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
