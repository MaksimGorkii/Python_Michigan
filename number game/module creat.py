import requests
def get_location_info():
    return requests.get("http://freegeoip.net/json/").json()


