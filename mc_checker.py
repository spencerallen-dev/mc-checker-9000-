#!/usr/bin/env python3
"""
Minecraft Server Status Checker
A simple GUI application to check Minecraft server status
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from mcstatus import JavaServer
import threading


class MinecraftServerChecker:
    """Main application class for Minecraft Server Status Checker"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Server Status Checker 9000")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        self.setup_styles()
        
        # Create UI elements
        self.create_widgets()
        
    def setup_styles(self):
        """Configure ttk styles for better appearance"""
        style = ttk.Style()
        style.theme_use('clam')
        
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="🎮 Minecraft Server Checker 9000",
            font=('Helvetica', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Server address input
        ttk.Label(main_frame, text="Server Address:", font=('Helvetica', 10)).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        
        self.server_entry = ttk.Entry(main_frame, width=40, font=('Helvetica', 10))
        self.server_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 5))
        self.server_entry.insert(0, "mc.hypixel.net")
        self.server_entry.bind('<Return>', lambda e: self.check_server())
        
        # Check button
        self.check_button = ttk.Button(
            main_frame, 
            text="Check Status", 
            command=self.check_server
        )
        self.check_button.grid(row=1, column=2, pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame, 
            mode='indeterminate', 
            length=200
        )
        self.progress.grid(row=2, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        # Status label
        self.status_label = ttk.Label(
            main_frame, 
            text="Enter a server address and click 'Check Status'",
            font=('Helvetica', 9),
            foreground='gray'
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=5)
        
        # Results text area
        results_frame = ttk.LabelFrame(main_frame, text="Server Information", padding="10")
        results_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            width=60,
            height=15,
            font=('Courier', 9),
            wrap=tk.WORD,
            state='disabled'
        )
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure text tags for colored output
        self.results_text.tag_configure('header', font=('Courier', 9, 'bold'), foreground='#2196F3')
        self.results_text.tag_configure('success', foreground='#4CAF50')
        self.results_text.tag_configure('error', foreground='#F44336')
        self.results_text.tag_configure('info', foreground='#333333')
        
    def update_results(self, text, tag='info', clear=False):
        """Update the results text area"""
        self.results_text.config(state='normal')
        if clear:
            self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, text, tag)
        self.results_text.config(state='disabled')
        self.results_text.see(tk.END)
        
    def check_server(self):
        """Check the Minecraft server status in a separate thread"""
        server_address = self.server_entry.get().strip()
        
        if not server_address:
            messagebox.showwarning("Input Error", "Please enter a server address!")
            return
            
        # Disable button and start progress bar
        self.check_button.config(state='disabled')
        self.progress.start(10)
        self.status_label.config(text=f"Checking {server_address}...", foreground='blue')
        self.update_results("", clear=True)
        
        # Run the check in a separate thread to prevent GUI freezing
        thread = threading.Thread(target=self._check_server_thread, args=(server_address,))
        thread.daemon = True
        thread.start()
        
    def _check_server_thread(self, server_address):
        """Perform the actual server check (runs in separate thread)"""
        try:
            # Parse server address (handle port if provided)
            server = JavaServer.lookup(server_address)
            
            # Get server status
            status = server.status()
            
            # Format the results
            result_text = "═" * 60 + "\n"
            result_text += f"  SERVER: {server_address}\n"
            result_text += "═" * 60 + "\n\n"
            
            # Online status
            result_text += "🟢 SERVER IS ONLINE\n\n"
            
            # Version information
            result_text += f"📦 Version: {status.version.name}\n"
            result_text += f"   Protocol: {status.version.protocol}\n\n"
            
            # Player information
            result_text += f"👥 Players: {status.players.online}/{status.players.max}\n"
            
            if status.players.sample:
                result_text += "   Online players:\n"
                for player in status.players.sample[:10]:  # Show max 10 players
                    result_text += f"   • {player.name}\n"
                if len(status.players.sample) > 10:
                    result_text += f"   ... and {len(status.players.sample) - 10} more\n"
            result_text += "\n"
            
            # Latency
            result_text += f"⚡ Latency: {status.latency:.2f} ms\n\n"
            
            # MOTD (Message of the Day)
            result_text += "📝 MOTD:\n"
            # Clean MOTD (remove formatting codes)
            motd = status.description
            if isinstance(motd, dict):
                motd_text = motd.get('text', str(motd))
            else:
                motd_text = str(motd)
            
            # Remove common Minecraft color codes
            import re
            motd_clean = re.sub(r'§[0-9a-fk-or]', '', motd_text)
            result_text += f"   {motd_clean}\n"
            
            result_text += "\n" + "─" * 60 + "\n"
            
            # Update GUI in main thread
            self.root.after(0, self._update_success, result_text)
            
        except Exception as e:
            error_msg = f"❌ Error checking server:\n\n{str(e)}\n\n"
            error_msg += "Possible reasons:\n"
            error_msg += "• Server is offline or unreachable\n"
            error_msg += "• Invalid server address\n"
            error_msg += "• Network connectivity issues\n"
            error_msg += "• Server may be a Bedrock edition server (this tool is for Java edition)\n"
            
            # Update GUI in main thread
            self.root.after(0, self._update_error, error_msg, str(e))
            
    def _update_success(self, result_text):
        """Update GUI with success results (must run in main thread)"""
        self.progress.stop()
        self.check_button.config(state='normal')
        self.status_label.config(text="✓ Server check complete!", foreground='green')
        self.update_results(result_text, 'success', clear=True)
        
    def _update_error(self, error_msg, short_error):
        """Update GUI with error results (must run in main thread)"""
        self.progress.stop()
        self.check_button.config(state='normal')
        self.status_label.config(text=f"✗ Failed to check server", foreground='red')
        self.update_results(error_msg, 'error', clear=True)


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = MinecraftServerChecker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
