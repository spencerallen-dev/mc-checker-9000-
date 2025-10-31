# Minecraft Server Status Checker 9000 🎮

A sleek web application to check if a Minecraft server is online and display detailed server information with Spencer's signature cyberpunk styling.

## Features

- ✅ Check Minecraft Java Edition server status
- 👥 View online player count and list
- 📦 Display server version and software
- 🌐 Show server hostname and IP information
- 📝 Read server MOTD (Message of the Day)
- 🎨 Cyberpunk-themed UI with animated particle background
- 📱 Fully responsive design
- ⚡ No backend required - runs entirely in the browser

## Live Demo

Open `index.html` in your web browser to use the application!

## Installation

1. Clone this repository:
```bash
git clone https://github.com/spencerallen-dev/mc-checker-9000-.git
cd mc-checker-9000-
```

2. Open `index.html` in your web browser:
```bash
# On macOS
open index.html

# On Linux
xdg-open index.html

# On Windows
start index.html
```

Or simply drag and drop `index.html` into your browser window.

## Usage

### How to Use

1. Enter a Minecraft server address in the input field (e.g., `mc.hypixel.net` or `play.example.com:25565`)
2. Click the "Check Status" button or press Enter
3. View the server information displayed in the results area

### Hosting

You can host this application on:
- GitHub Pages
- Any static web hosting service
- Your own web server

Just upload the three files (`index.html`, `style.css`, `script.js`) to your hosting service.

## Supported Server Types

This tool supports **Minecraft Java Edition** servers only. Bedrock Edition servers are not supported.

## Example Servers to Try

- `mc.hypixel.net` - Hypixel Network
- `play.cubecraft.net` - CubeCraft Games
- `us.mineplex.com` - Mineplex

## Technology Stack

- **HTML5** - Structure
- **CSS3** - Styling with animated particle background
- **JavaScript** - Client-side logic
- **mcsrvstat.us API** - Server status data

## Design

This application features Spencer Allen's signature cyberpunk aesthetic:
- Black background with cyan/turquoise accents (#00d4ff)
- Animated particle background
- Glowing text effects and smooth transitions
- Roboto font family
- Fully responsive design

## Troubleshooting

If you encounter issues:

- **Server shows as offline but it's running**: The server may be blocking status queries
- **API error**: The mcsrvstat.us API may be temporarily unavailable
- **No data shown**: Check your internet connection
- Make sure you're checking a Java Edition server (not Bedrock Edition)

## License

This project is open source and available for personal and educational use.
