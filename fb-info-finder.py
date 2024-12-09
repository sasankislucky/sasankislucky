import requests

def get_facebook_account_info(access_token):
    url = "https://graph.facebook.com/me"
    params = {
        'fields': 'id,name,email,phone',
        'access_token': access_token
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}

# Example usage
if __name__ == "__main__":
    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your actual access token
    account_info = get_facebook_account_info(access_token)
    print(account_info)

