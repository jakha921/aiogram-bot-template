import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com",
	"X-RapidAPI-Key": "69bc405e5bmsh2f4565ba236cd4bp1ea962jsne4eb459bbc5c"
}

async def remove_background(img_ulr):
    payload = f"image_url={img_ulr}"
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['response']['image_url']

if __name__ == '__main__':
    print(remove_background('http://telegra.ph//file/cd6867e8be3749ed09cfb.jpg'))