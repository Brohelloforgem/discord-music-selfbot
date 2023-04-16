# Discord Music Selfbot
This Discord selfbot allows you to play music in a voice channel. With this selfbot, you can do many things, but it is currently in development.

## Commands
- `play <url or query>` — bot joins your channel and starts playing music from a URL or query on YouTube!
- `pause` or `unpause` — commands for pausing and unpausing music!
- `skip` — skip currently playing track and start playing the next one in the queue!
- `clear` — bot clears queue and leaves your channel!
- `bassboost` — BASSBOOST your music!
- `queue` — command for showing your current queue!

## Installation
1. [Download](https://github.com/atikiNBTW/discord-music-selfbot/archive/refs/heads/main.zip) or clone this repository.
2. Create a new virtual environment and install the required packages: `pip install discord.py-self ffmpeg asyncio yt_dlp`.
4. Modify the `token` and `prefix` fields in the [config.json](https://github.com/atikiNBTW/discord-music-selfbot/blob/main/config.json) file.
5. Start the selfbot: `python main.py`

> **WARNING: If you are using the standard discord.py library for anything else, please create another environment and install all packages there to avoid errors!**

## Contributing
If you find a bug or have a suggestion, please open an issue on this repository. To contribute code, documentation, or tests, please follow these guidelines:
```
1. Fork the repository and create a new branch
2. Make changes and test thoroughly
3. Submit a pull request
```

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
