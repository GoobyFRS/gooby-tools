import tkinter as tk
import requests

def get_wan_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    wan_ip = data['ip']
    ip_textbox.delete('1.0', tk.END)  # Clear previous text
    ip_textbox.insert(tk.END, wan_ip)

# Create the main window
window = tk.Tk()
window.title("BlueBotDNS")
window.geometry("400x300")
window.configure(bg="grey")

# Create the first button
button1 = tk.Button(window, text="Get WAN IP", command=get_wan_ip)
button1.pack()

# Create the first text box
ip_textbox = tk.Text(window, height=1, width=20)
ip_textbox.pack()

# Run the GUI event loop
window.mainloop()
