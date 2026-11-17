import os

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_movie_data_from_tmdb(title):
    tmdb_api_key = os.getenv("TMDB_API_KEY")
    urls = ["https://api.themoviedb.org/3/search/movie","https://api.themoviedb.org/3/search/TV"]
    params = {"api_key": tmdb_api_key, "query": title}

    for url in urls:
        try:
            response = requests.get(url, params=params,timeout=10)
            status_code = response.status_code
            if status_code == 200:
                data = response.json()
            else:
               continue
        except requests.exceptions.RequestException as e:
            print(e)
            continue
        results = data.get("results") or []
        if results:
            movie_info = results[0]
            return {"description": movie_info.get("overview")}
    return None

def fetch_anime_data_from_kitsu(title):
    url = "https://kitsu.io/api/edge/anime"
    params = {"filter[text]": title,"page[limit]": 1}
    headers = {"Accept": 'application/vnd.api+json'}

    try:
        response = requests.get(url,params=params,headers=headers, timeout=10,)
        response.raise_for_status()
        payload = response.json()
    except (requests.exceptions.RequestException,ValueError) as e:
        print(e)
        return None

    items = payload.get("data") or []
    if not items:
        return None
    return {"description": items[0].get("attributes").get("synopsis")}
















