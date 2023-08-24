#!/usr/bin/python3
#Learning to use tkinter to create a basic GUI
import tkinter as tk 
import requests

def get_wan_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json") #Public API/JSON Reply Endpoint. Really neat in a browser too.
        if response.status_code == 200: # Healthy HTTP response
            data = response.json()
            return data['ip']
        else:
            return "Error: Unable to retrieve WAN IPv4."
    except requests.exceptions.RequestException as e: # Standard way to shrink and re-use the error. 
        return "Failure Reason: " + str(e) # Print the error code as a string to prevent any math or weird behavior.

def show_ip():
    global ip_label #Create 
    wan_ip = get_wan_ip() #Use the above function as a variable. I am not sure if this is best practice.
    ip_label.config(text="WANv4: " + wan_ip) #Output string to be called later.

def main():
    global ip_label  # Import the global variable defined earlier in the code.
    main_window = tk.Tk()
    main_window.title("BlueBotDDNS") #Window Name
    main_window.geometry("200x150") # Window Size
    main_window.configure(bg="grey") # Background Color

#This block will sit at the top of the window because it is defined first.
    ip_label = tk.Label(main_window, text="")
    ip_label.pack()
#This is the button below the output above. 
    ip_button = tk.Button(main_window, text="Get My WANv4", command=show_ip)
    ip_button.pack()

    main_window.mainloop()

main()
