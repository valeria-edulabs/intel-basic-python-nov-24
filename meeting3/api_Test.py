import requests

api_key = 'acc_59cce29b859c22a'
api_secret = 'e12d31e891c1e56f9111f72508dc5846'
image_url = 'https://random.dog/29442e1e-4078-4d74-b06c-f0b4c054c8f0.png'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

print(response.json())