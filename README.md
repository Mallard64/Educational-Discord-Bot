# Educational Discord Bot

A Discord chat-game bot: a small collect-and-battle RPG built around "Pepe"
characters, plus a handful of server utility commands. Players catch
characters, level them up and evolve them, battle an AI or each other, and
spend the credits they win in a shop. All progress is saved to JSON files.

Learning project to get hands-on with the Discord API,
asynchronous event handling, and persisting state across restarts.

## Tech stack

- **Python 3.9** (targets the `discord.py` 1.x API)
- **discord.py** for the bot and command framework
- **Flask** — a tiny keep-alive web server (`keep_alive.py`) so the bot stays
  up on always-on free hosts like Replit
- **python-dotenv** for loading the bot token from the environment

## Running it locally

1. Create a bot application and token at the
   [Discord Developer Portal](https://discord.com/developers/applications).
2. Install dependencies (a virtual environment is recommended):

   ```bash
   pip install -r requirements.txt
   ```

3. Provide your token. Copy the example env file and edit it:

   ```bash
   cp .env.example .env
   # then set DISCORD_TOKEN=... in .env
   ```

4. Run the bot:

   ```bash
   python main.py
   ```

Invite the bot to a server, then use the `pepe ` command prefix (e.g.
`pepe start`).

## Commands

The command prefix is `pepe `.

| Command | What it does |
| --- | --- |
| `pepe start` | Create your save and get a starter character. Run this first. |
| `pepe search` | Hunt for a new character (rarity is random; a Lucky-Charm improves odds). |
| `pepe box [user]` | List your characters (or another user's). |
| `pepe select <character>` | Choose your active character. |
| `pepe info <character>` | Show a character's HP / Def / Atk. |
| `pepe battle` | Fight a random AI opponent; win credits. |
| `pepe pvpbattle <@user>` | Challenge another player (work in progress). |
| `pepe shop` | Buy characters and items, level up, and evolve. |
| `pepe bal` | Check your credit balance. |
| `pepe items` | List your items. |
| `pepe save` | Persist your progress to disk. |
| `pepe magic8 <question>` | Magic 8-ball. |
| `pepe roll <sides>` | Roll a die. |
| `pepe text_channel [name]` / `pepe voice_channel [name]` | Create a channel. |
| `pepe ping <text> <count>` | Repeat a message. |

## How state is stored

Each command reads and writes small JSON files keyed by Discord user ID:

| File | Contents |
| --- | --- |
| `OwO.json` | Characters each user owns |
| `bal.json` | Credit balances |
| `items.json` | Items each user holds |
| `levels.json` | Per-character levels |
| `select.json` | Each user's active character |
| `moves.json` | Per-character move sets |

`globals.py` holds the static `stats` table (HP / Def / Atk per character).
Character art is the bundled image files referenced by `icondata` in
`main.py`. These files are committed empty (`{}`) and the bot populates them
as people play.

## Status and known limitations

This is an early personal project, not production software. Known rough edges:

- The PvP battle (`pepe pvpbattle`) is incomplete.
- The member-join role assignment uses an older discord.py API and would need
  updating for current library versions.
- There are no per-user write locks, so heavy concurrent play could race on
  the JSON files.

## Tests

```bash
pip install pytest
pytest
```

`test_smoke.py` checks that the data files load and the stats table is
well-formed. CI (GitHub Actions) runs flake8 and these tests on every push.
