import os
import openai
openai.organization = "org-26MZrYGH1VczLYfeJkoCXzKY"
openai.api_key = "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"
#openai.Model.list()

response = openai.Image.create(
  prompt="Chicago Illinois",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)