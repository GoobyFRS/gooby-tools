import tkinter as tk
import requests

def get_wan_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            return data['ip']
        else:
            return 'Error: Unable to retrieve WAN IP.'
    except requests.exceptions.RequestException as e: 
        return 'Error: ' + str(e)

def show_ip():
    global ip_label  # Declare ip_label as a global variable
    wan_ip = get_wan_ip()
    ip_label.config(text="WAN IP Address: " + wan_ip)

def create_window():
    global ip_label  # Declare ip_label as a global variable
    main_window = tk.Tk()
    main_window.title("BlueBotCDN")
    main_window.geometry("400x300")
    main_window.configure(bg="grey")

    ip_button = tk.Button(main_window, text="Get WANv4 Address", command=show_ip)
    ip_button.pack()

    ip_label = tk.Label(main_window, text="")
    ip_label.pack()

    main_window.mainloop()

create_window()
