import requests

def add_offer(access_token,offer_data):
    url = "https://www.zohoapis.ca/crm/v2/Offers"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
    }


    payload = {
            "data": [ offer_data ]
        }
    response = requests.post(url, headers=headers,json=payload)
    return response.json()



def update_Offer(access_token,data):
    url = f"https://www.zohoapis.ca/crm/v2/Offers"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
    }

    response = requests.put(url, headers=headers, json=data)

    return response.json()