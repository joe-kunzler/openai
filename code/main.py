import os
import openai
openai.organization = os.environ["OPENAI_ORG"]
openai.api_key = os.environ["OPENAI_API_KEY"]
#openai.Model.list()

response = openai.Image.create(
  prompt="7 wonders of the world",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)