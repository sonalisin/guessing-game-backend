import requests
import numpy as np

def get_random_character_id():
    return np.random.randint(1, 7438)
def get_character_appearances(data):
    media = []
    if(data["films"] or data["tvShows"]):
        media = [*data["films"], *data["tvShows"]]
        return media[0]
    else:
        raise Exception("No films or tv shows found.")

def create_character_question_data():
    id = get_random_character_id()
    character = get_character(id)
    media = get_character_appearances(character)
    return {
        "name": character["name"],
        "id": character["_id"],
        "img": character["imageUrl"],
        "appearance": media
    }

def get_character(id):
    url = f'https://api.disneyapi.dev/characters/{id}'
    try:
        res = requests.get(url)
        data = res.json()
        if(data["name"] and data["imageUrl"] ):
            return res.json()
    except:
        return get_character(get_random_character_id())