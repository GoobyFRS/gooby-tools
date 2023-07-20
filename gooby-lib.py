import requests

def get_wan_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            return data['ip']
        else:
            print('Error: Unable to retrieve WAN IP.')
    except requests.exceptions.RequestException as e:
        print('Error:', e)

# Example usage below
wan_ip = get_wan_ip()
print('WAN IP Address:', wan_ip)