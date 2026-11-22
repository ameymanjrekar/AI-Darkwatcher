# AI DarkWatch™ - Global AI Threat, Rogue Agent & Harm Observatory

> **Real-time telemetry tracking AI security hacks, runaway autonomous agent behaviors, model culpability rankings, and emerging safety solutions in plain English.**

---

## 🚀 Key Features

- **📈 Live Public Trust Wave**: Real-time moving telemetry graph tracking global sentiment and AI reliability.
- **🚩 Red-Flag Anomaly Spikes**: Instant visual alerts and spike animations whenever a major exploit or safety violation occurs.
- **🤖 Autonomous AI Agent Monitor**: Tracks what unmonitored AI bots and coding agents are doing in the wild (sandbox breakouts, runaway loops).
- **🏢 Culprit Scoreboard**: Transparent rankings of which AI models and architectures are causing the highest number of safety incidents.
- **🛡️ Solutions & Defenses**: Plain-English explanations of emerging fixes (C2PA digital fingerprints, microVM jails, dual-guard checkpoints).
- **💬 1-Click WhatsApp Sharing**: Instant mobile dispatch button to send concise safety alerts to team members or family.
- **⚙️ Automated GitHub Ingestion Workflow**: Scheduled GitHub Actions pipeline (`.github/workflows/update_incidents.yml`) syncing fresh threat data automatically.

---

## 🛠️ Quick Setup: Publishing to GitHub & GitHub Pages

To link this project to your GitHub account and host it free forever on GitHub Pages:

### 1. Initialize Git in this directory
```bash
cd C:\Users\ameym\.gemini\antigravity\scratch\ai-darkwatch
git init
git add .
git commit -m "feat: initial release of AI DarkWatch observatory"
```

### 2. Connect to your GitHub repository
Create a new public repository named `ai-darkwatch` on GitHub, then link it:
```bash
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/ai-darkwatch.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages
1. Go to your repository **Settings** > **Pages**.
2. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then click **Save**.
4. Your site will be live instantly at:
   `https://<YOUR_GITHUB_USERNAME>.github.io/ai-darkwatch/`

---

## 🤖 Automated Cron Updates
The workflow at `.github/workflows/update_incidents.yml` runs every 6 hours (and on manual trigger) to refresh `data/incidents.json` and keep your live site continuously updated!
