import requests

def get_dog_image():
    url_dog = 'https://random.dog/woof.json'
    respons = requests.get(url_dog)
    if respons.status_code == 200:
        return respons.json()['url']
    else:
        return respons.status_code
if __name__ == "__main__":
    print(get_dog_image())