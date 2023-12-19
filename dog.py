import requests

def get_dog_image():
    url_dog = 'https://random.dog/woof.json'
    response = requests.get(url_dog)

    if response.status_code == 200:
        return response.json()['url']
    
    return response.status_code
if __name__ == "__main__":
    print(get_dog_image())