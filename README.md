# Minecraft Server Status Checker 9000 🎮

A simple Python GUI application to check if a Minecraft server is online and display detailed server information.

## Features

- ✅ Check Minecraft Java Edition server status
- 👥 View online player count and list
- 📦 Display server version and protocol
- ⚡ Show server latency/ping
- 📝 Read server MOTD (Message of the Day)
- 🎨 Clean and user-friendly GUI interface

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/spencerallen-dev/mc-checker-9000-.git
cd mc-checker-9000-
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python3 mc_checker.py
```

Or make it executable and run directly:
```bash
chmod +x mc_checker.py
./mc_checker.py
```

### How to Use

1. Enter a Minecraft server address in the input field (e.g., `mc.hypixel.net` or `play.example.com:25565`)
2. Click the "Check Status" button or press Enter
3. View the server information displayed in the results area

## Supported Server Types

This tool supports **Minecraft Java Edition** servers only. Bedrock Edition servers are not supported.

## Example Servers to Try

- `mc.hypixel.net` - Hypixel Network
- `play.cubecraft.net` - CubeCraft Games
- `us.mineplex.com` - Mineplex

## Troubleshooting

If you encounter issues:

- **"No address associated with hostname"**: The server address is invalid or the server doesn't exist
- **"Connection refused"**: The server is offline or not accepting connections
- **"Timeout"**: The server is unreachable or taking too long to respond
- Make sure you're checking a Java Edition server (not Bedrock Edition)

## License

This project is open source and available for personal and educational use.
