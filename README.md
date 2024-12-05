
# Horoscope Bot 🤖✨

A fun and simple Telegram bot that gives you daily horoscopes based on your zodiac sign. You can get your horoscope for *today*, *tomorrow*, *yesterday*, or any specific date.

## Features
- Get daily horoscopes for all zodiac signs.
- Options to check:
  - **Today**
  - **Tomorrow**
  - **Yesterday**
  - Any specific date (e.g., `2024-12-05`).
- Easy-to-use interface.
- Powered by the [Horoscope App API](https://horoscope-app-api.vercel.app/).

## Setup

### Prerequisites
- Python 3.8 or later
- A [Telegram bot token](https://core.telegram.org/bots#botfather)
- `pip` for installing dependencies
- A `.env` file to store your bot token securely

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/horoscope-bot.git
   cd horoscope-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your bot token:
   ```env
   BOT_TOKEN=your-telegram-bot-token
   ```

4. Start the bot:
   ```bash
   python bot.py
   ```

### Using the Bot

1. Start the bot by typing `/start` or `/hello`.
2. Begin by typing `/horoscope`.
3. Enter your zodiac sign (e.g., `Aries`, `Leo`, `Pisces`).
4. Choose the date you want the horoscope for:
   - `TODAY`
   - `TOMORROW`
   - `YESTERDAY`
   - A specific date (`YYYY-MM-DD`)

The bot will send your daily horoscope!

## Project Structure

```
horoscope-bot/
├── bot.py             # Bot logic
├── requirements.txt   # Dependencies
├── .env               # Your bot token (not in the repo)
└── README.md          # Documentation
```

## API Details

This bot uses the [Horoscope App API](https://horoscope-app-api.vercel.app/) to fetch horoscope data.

**Endpoint:**  
`https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily`

**Parameters:**
- `sign`: The zodiac sign (e.g., `Aries`, `Taurus`).
- `day`: The date (`TODAY`, `TOMORROW`, `YESTERDAY`, or `YYYY-MM-DD`).

## Technologies

- Python
- PyTelegramBotAPI
- dotenv

## Contributing

Want to contribute? Fork the repo and submit a pull request! 🎉

1. Fork the repository
2. Create your branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Let’s bring the stars closer! 🌌
