# myapp/tasks.py
from celery import shared_task
from time import sleep
import requests

@shared_task
def texttoimage(prompt):

    for i in prompt:
        response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
            headers={
                "authorization": f"Bearer sk-<YOUR API KEY>",
                "accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": i,
                "output_format": "webp",
            },
        )

        if response.status_code == 200:
            first_letters = [word for word in i.split()]
            result = ''.join(first_letters)
            with open(f"./{result}.webp", 'wb') as file:
                file.write(response.content)
        else:
            raise Exception(str(response.json()))
    sleep(10)  # Simulate a long-running task
    return 
