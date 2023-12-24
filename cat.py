import requests

def get_cat_image():
    base_url = "https://api.thecatapi.com/v1/images/search"
    respons = requests.get(url=base_url)
    if respons.status_code == 200:
        return respons.json()[0]['url']
    else:
        return respons.status_code
if __name__ == "__main__":
    print(get_cat_image())