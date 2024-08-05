from openai import OpenAI


class ImageCaptionTool:

    def __init__(self) -> None:
        self.client = OpenAI()

    def caption(self, url, query="What's in this Image?"):
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": query},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content


# # Getting the base64 string
