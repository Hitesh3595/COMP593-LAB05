import requests

DEV_KEY = "4M8RGgS3vuAOB5gO2NK-Le-9lB_Lhi65"
USER_KEY = "d53199be16b278b7fd7a9b853b9a74fc"
USER_NAME = "Hitesh3178"
PASSWORD = ""

LOGIN_URL = "https://pastebin.com/api/api_login.php"
CREATE_URL = "https://pastebin.com/api/api_post.php"


def login():

    response = requests.post(
        LOGIN_URL,
        data={
            "api_dev_key": DEV_KEY,
            "api_user_name": USER_NAME,
            "api_user_password": PASSWORD,
        }
    )
    user_key = None
    if response.status_code == 200:
        user_key = response.text

    return user_key


def create_paste(title, body, expiration_period="10M", is_public=True):
    """
    Creates a new PasteBin paste

    Args:
        title (str): title of new paste
        body (str): body text of new paste
        expiration (str, optional): Expiration date of paste
        is_public (bool, optional): whether paste is public listed or not
    
    Return:
        if paste is created:
            url of paste
        if paste is not created:
            None
    """
    url = None
    print("Posting new paste to PasteBin...",end="")

    response = requests.post(
        CREATE_URL,
        data={
            "api_user_key": USER_KEY,
            "api_dev_key": DEV_KEY,
            "api_option": "paste",
            "api_paste_name": title,
            "api_paste_code": body,
            "api_paste_private": 0 if is_public else 1,
            "api_paste_expire_date": expiration_period,
        }
    )
    if response.status_code == 200:
        url = response.text
        print("success")
        print(url)
    else:
        print("failure")
        print(f"Response code: {response.status_code} ({response.reason})")
        print(response.text)
    return url
