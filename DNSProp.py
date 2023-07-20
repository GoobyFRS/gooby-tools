import tkinter as tk
import subprocess

def perform_dns_check():
    domain = domain_textbox.get("1.0", tk.END).strip()
    dns_servers = [
        "8.8.8.8",      # Google DNS
        "1.1.1.1",      # Cloudflare DNS
        "208.67.222.222",  # OpenDNS
        "9.9.9.9",      # Quad9 DNS
        "64.6.64.6",    # Verisign DNS
        "185.228.168.168"  # CleanBrowsing DNS
    ]
    results_textbox.delete("1.0", tk.END)  # Clear previous results

    for dns_server in dns_servers:
        command = f"nslookup {domain} {dns_server}"
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        results_textbox.insert(tk.END, f"DNS Server: {dns_server}\n")
        results_textbox.insert(tk.END, output)
        results_textbox.insert(tk.END, "\n")

# Create the main window
window = tk.Tk()

# Create the domain input text box
domain_textbox = tk.Text(window, height=1, width=30)
domain_textbox.pack()

# Create the DNSCheck button
dns_check_button = tk.Button(window, text="DNSCheck", command=perform_dns_check)
dns_check_button.pack()

# Create the results text box
results_textbox = tk.Text(window, height=10, width=50)
results_textbox.pack()

# Run the GUI event loop
window.mainloop()
