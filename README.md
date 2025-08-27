# My_OFM_bot - V1 (MVP)

My_OFM_bot V1 is a minimal Telegram bot intended to run from Termux (Android) or any Python environment.
This V1 is the skeleton (MVP) with a /start menu and placeholders for future features (image generation, faceswap, model management).

## What's inside (V1)
- `bot.py` : main bot code (menu + handlers).
- `config.py` : sample config file to store your Telegram token (EDIT THIS).
- `requirements.txt` : Python packages to install.
- `README.md` : this file.

## Quick start (Termux)
1. Install Termux and allow storage access: `termux-setup-storage`.
2. Install packages: `pkg update && pkg install git python -y`.
3. Clone this repo or copy files into a directory.
4. Create `config.py` and set `API_TOKEN` to your BotFather token.
5. Install Python dependencies: `pip install -r requirements.txt`.
6. Run the bot: `python bot.py`.
7. Open Telegram and send `/start` to your bot.

## Next steps (V2+)
- V2: integrate image generation via Hugging Face or other API.
- V3: per-user model storage and generation history.
- V4: faceswap workflow (Colab / server-side).
- V5: production deployment on Render/Railway and monetization features.

## Security
- Do NOT commit `config.py` with a real token to a public repo.
- Use `.gitignore` to exclude credentials and generated media.
