import json
import requests

from .constants import SERVER_URL

class Exam:
    ENDPOINT = "/candidates/"

    def __init__(self, name=None, post=None, candidate_class=None, id_session=None, candidate_id=None) -> None:
        self.candidate_id = candidate_id
        self.name = name
        self.post = post
        self.candidate_class = candidate_class
        self.id_session = id_session
        self.files = []

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'name': self.name,
        'post': self.post,
        'candidate_class': self.candidate_class,
        'id_session': self.id_session}
        #files=[
       # ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        #('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        #]
        #headers = {}

        #response = requests.request("POST", url, headers=headers, data=payload, files=files)

        #data = json.loads(response.text)
        #self.id = data['id']

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += candidate_id if candidate_id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if id:
            candidate = __class__(**response)
            return candidate
        else:
            candidates = []

            for result in response:
                candidate = __class__(**result)
                exams.append(candidate)
            
            return candidate  

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.candidate_id = None
        except Exception:
            raise exception