# URL Shortener - Django

This is a simple backend application that shortens URL links. The application uses an in-memory 

## Requirements
- An A anonymous user can input a URL and receive a shortened URL in return.
- A user should be able to view basic analytics for their links

## Running the application

1. Install dependencies
```python
pip install -r requirements.txt
```

2. Run migrations
```python
 python manage.py makemigrations

 python manage.py migrate
```

3. Start the application
```python
 python manage.py runserver
```

## Endpoints exposed

Refer to the postman collection `url_shortener.postman_collection.json` for sample endpoints used in this app.

### `/shorten/`
Takes in a URL string in the POST body and returns a shorten link and usage stats of the URL. 

Sample output:
```json
{
    "full_url": "https://towardsdatascience.com/best-apis-for-url-shortening-using-python-2db09d1f86f0/",
    "url_hash": "da0df0698f",
    "clicks": 7,
    "created_at": "2021-07-18T16:22:31.558357Z"
}
```

### `/url/<str:url_hash>/`
Retrieves a previously decoded url hash and it's usage stats. 

Sample call: `http://localhost:8000/url/da0df0698f/`

Sample output:
```json
{
    "full_url": "https://towardsdatascience.com/best-apis-for-url-shortening-using-python-2db09d1f86f0/",
    "url_hash": "da0df0698f",
    "clicks": 7,
    "created_at": "2021-07-18T16:22:31.558357Z"
}
```

## Deployment

The project comes with a Dockerfile that packages the application code and runtime packages. This is a convenient point of departure as it allows the application to be hosted on a variety of hosted solutions such as Kubernetes or managed PaaS solutions like (ECS, Heroku, Cloud Run). The Docker approach also makes it easy to accommodate several deployment options and scaling considerations. 