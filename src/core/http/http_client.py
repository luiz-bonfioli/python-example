import httpx


def get_posts(params=None):
    if params:
        return httpx.get('https://jsonplaceholder.typicode.com/posts', params=params).json()

    return httpx.get('https://jsonplaceholder.typicode.com/posts').json()
