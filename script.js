// Particle background animation
const canvas = document.getElementById('bg');
const ctx = canvas.getContext('2d');
let particles = [];
let w, h;

function resize() {
  w = canvas.width = window.innerWidth;
  h = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

class Particle {
  constructor() {
    this.reset();
  }
  reset() {
    this.x = Math.random() * w;
    this.y = Math.random() * h;
    this.vx = (Math.random() - 0.5) * 0.5;
    this.vy = (Math.random() - 0.5) * 0.5;
    this.size = Math.random() * 2 + 1;
  }
  update() {
    this.x += this.vx;
    this.y += this.vy;
    if (this.x < 0 || this.x > w || this.y < 0 || this.y > h) this.reset();
  }
  draw() {
    ctx.fillStyle = '#00d4ff';
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

for (let i = 0; i < 100; i++) particles.push(new Particle());

function animate() {
  ctx.clearRect(0, 0, w, h);
  particles.forEach(p => { p.update(); p.draw(); });
  requestAnimationFrame(animate);
}
animate();

// Enter key support
document.getElementById('serverInput').addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    checkServer();
  }
});

// Check server function
async function checkServer() {
  const serverInput = document.getElementById('serverInput');
  const checkBtn = document.getElementById('checkBtn');
  const progressBar = document.getElementById('progressBar');
  const statusMessage = document.getElementById('statusMessage');
  const resultsText = document.getElementById('resultsText');

  const serverAddress = serverInput.value.trim();

  if (!serverAddress) {
    statusMessage.className = 'status-message error';
    statusMessage.textContent = '❌ Please enter a server address!';
    return;
  }

  // Disable button and show progress
  checkBtn.disabled = true;
  progressBar.classList.add('active');
  statusMessage.className = 'status-message loading';
  statusMessage.textContent = `Checking ${serverAddress}...`;
  resultsText.textContent = 'Querying server... Please wait.';

  try {
    // Use Minecraft Server Status API
    const response = await fetch(`https://api.mcsrvstat.us/3/${serverAddress}`);
    const data = await response.json();

    if (data.online) {
      displaySuccess(data, serverAddress);
    } else {
      displayOffline(serverAddress);
    }
  } catch (error) {
    displayError(error, serverAddress);
  } finally {
    checkBtn.disabled = false;
    progressBar.classList.remove('active');
  }
}

function displaySuccess(data, serverAddress) {
  const statusMessage = document.getElementById('statusMessage');
  const resultsText = document.getElementById('resultsText');

  statusMessage.className = 'status-message success';
  statusMessage.textContent = '✓ Server check complete!';

  let result = '═'.repeat(60) + '\n';
  result += `  SERVER: ${serverAddress}\n`;
  result += '═'.repeat(60) + '\n\n';

  result += '🟢 SERVER IS ONLINE\n\n';

  // Version
  if (data.version) {
    result += `📦 Version: ${data.version}\n`;
  }

  // Players
  if (data.players) {
    result += `👥 Players: ${data.players.online || 0}/${data.players.max || 'Unknown'}\n`;
    
    if (data.players.list && data.players.list.length > 0) {
      result += '   Online players:\n';
      const playerList = data.players.list.slice(0, 10);
      playerList.forEach(player => {
        result += `   • ${player}\n`;
      });
      if (data.players.list.length > 10) {
        result += `   ... and ${data.players.list.length - 10} more\n`;
      }
    }
    result += '\n';
  }

  // MOTD (Message of the Day)
  if (data.motd && data.motd.clean) {
    result += '📝 MOTD:\n';
    data.motd.clean.forEach(line => {
      result += `   ${line}\n`;
    });
    result += '\n';
  }

  // Server info
  if (data.hostname) {
    result += `🌐 Hostname: ${data.hostname}\n`;
  }
  if (data.port) {
    result += `🔌 Port: ${data.port}\n`;
  }
  if (data.ip) {
    result += `📍 IP: ${data.ip}\n`;
  }

  // Software
  if (data.software) {
    result += `⚙️  Software: ${data.software}\n`;
  }

  // Mods/Plugins
  if (data.mods && data.mods.length > 0) {
    result += `🔧 Mods: ${data.mods.length} installed\n`;
  }
  if (data.plugins && data.plugins.length > 0) {
    result += `🔌 Plugins: ${data.plugins.length} installed\n`;
  }

  result += '\n' + '─'.repeat(60) + '\n';
  result += 'Data provided by mcsrvstat.us API\n';

  resultsText.textContent = result;
  resultsText.className = 'server-online';
}

function displayOffline(serverAddress) {
  const statusMessage = document.getElementById('statusMessage');
  const resultsText = document.getElementById('resultsText');

  statusMessage.className = 'status-message error';
  statusMessage.textContent = '✗ Server is offline or unreachable';

  let result = '═'.repeat(60) + '\n';
  result += `  SERVER: ${serverAddress}\n`;
  result += '═'.repeat(60) + '\n\n';

  result += '🔴 SERVER IS OFFLINE\n\n';
  result += 'Possible reasons:\n';
  result += '• Server is offline or not running\n';
  result += '• Invalid server address\n';
  result += '• Network connectivity issues\n';
  result += '• Server may be a Bedrock edition server\n';
  result += '  (this tool only works with Java edition)\n\n';
  result += '─'.repeat(60) + '\n';

  resultsText.textContent = result;
  resultsText.className = 'server-offline';
}

function displayError(error, serverAddress) {
  const statusMessage = document.getElementById('statusMessage');
  const resultsText = document.getElementById('resultsText');

  statusMessage.className = 'status-message error';
  statusMessage.textContent = '✗ Error checking server';

  let result = '═'.repeat(60) + '\n';
  result += `  SERVER: ${serverAddress}\n`;
  result += '═'.repeat(60) + '\n\n';

  result += '❌ ERROR CHECKING SERVER\n\n';
  result += `Error: ${error.message}\n\n`;
  result += 'Possible reasons:\n';
  result += '• Network connectivity issues\n';
  result += '• API service temporarily unavailable\n';
  result += '• Invalid server address format\n\n';
  result += '─'.repeat(60) + '\n';

  resultsText.textContent = result;
  resultsText.className = 'server-offline';
}
