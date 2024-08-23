import requests

def add_watchlist(access_token,data):
    url = "https://www.zohoapis.ca/crm/v2/Watchlist"
    

    # Authorization header
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "data": [
            data
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    except Exception as e:
        return {"status":"Failed","Error":str(e)}
    

def update_watchlist(access_token,payload):
    url = f"https://www.zohoapis.ca/crm/v2/Watchlist"
    

    # Authorization header
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.put(url, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"status":"Failed","Error":str(e)}
