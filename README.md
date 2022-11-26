

# FamTube

FamTube enables you to fetch search results asynchronously.
You can use get and search api to enjoy results for query.

API fetches latest videos sorted in reverse chronological order of their publishing date-time from YouTube


## Features

- Fetches Youtube data asynchornously and stores data to sql databse
- Get api `/get_videos` to fetch paginated reults.
- Post api `/get_videos/search` to search results for query.
- Retry mechanism in case of esceptions or quota completion.



## Usage

GET API : /get_videos
```
Output: 
{
    "count": 750,
    "next": "http://127.0.0.1:8000/get_videos/?page=2",
    "previous": null,
    "results": [
        {
            "id": 75,
            "created_at": "2022-11-25T19:13:56.246753Z",
            "title": "India vs New Zealand ODI Match - Cricket 22 Live - RtxVivek",
            "description": "India vs New Zealand ODI Match - Cricket 22 Live - RtxVivek Myself RtxVivek, An Indian Cricket 22 Streamer/Content Creator ...",
            "publish_date_time": "2022-11-25T14:40:03Z",
            "thumbnail_url": "https://i.ytimg.com/vi/TLhvAVhn53o/default.jpg"
        },
    ]
}
```

POST API: /get_videos/search

```
Input: 
{
   "query": "india"
}

Output:
{
    "count": 258,
    "next": "http://127.0.0.1:8000/get_videos/search/?page=2",
    "previous": null,
    "results": [
        {
            "id": 75,
            "created_at": "2022-11-25T19:13:56.246753Z",
            "title": "India vs New Zealand ODI Match - Cricket 22 Live - RtxVivek",
            "description": "India vs New Zealand ODI Match - Cricket 22 Live - RtxVivek Myself RtxVivek, An Indian Cricket 22 Streamer/Content Creator ...",
            "publish_date_time": "2022-11-25T14:40:03Z",
            "thumbnail_url": "https://i.ytimg.com/vi/TLhvAVhn53o/default.jpg"
        }
    ]
}
```





## Installation

below setup works for Mac

Create Repo
```
cd ~
mkdir codebase
cd codebase
git clone https://github.com/gauravladdha12/famtube.git
```

Install requirements
```
 pip install -r requirements.txt
```

Setup local database
```
mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED BY 'YOUR_PASSWORD';
create database famtube;
```

Env file
```
Update values in env file
```

Run project
```
 ./manage.py runserver
```

