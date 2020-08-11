## Content

1. [Motivation](#motivation)
2. [Local Setup](#local_setup)
3. [API endpoints](#api_endpoints)
4. [Authentication](#authentication)
5. [Deployment](#deployment)


<a name="motivation"></a>
## Motivation
1. Architect relational database models in Python
2. Utilize SQLAlchemy to conduct database queries
3. Follow REST ful principles of API development
4. Structure endpoints to respond to four HTTP methods, including error handling
5. Enable Role Based Authentication and roles-based access control (RBAC) in a Flask application
6. Application is hosted live on heroku


<a name="local_setup"></a>
## Local setup
1. To start locally checkout the file named requirements.txt
`$ pip install -r requirements.txt`
2. To execute test go to capstone/completed
```
completed % python test_app.py
/Users/anantpanthri/PycharmProjects/FSND/projects/capstone/venv/lib/python3.8/site-packages/jose/backends/cryptography_backend.py:187: CryptographyDeprecationWarning: signer and verifier have been deprecated. Please use sign and verify instead.
  verifier = self.prepared_key.verifier(
....................
----------------------------------------------------------------------
Ran 20 tests in 23.261s

OK

```
3. To setup Auth0 for authentication and authorization
go to config.py that also contains the bearer token 

```
AUTH0_DOMAIN = 'fsnd007.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'view_movies_actors'
```

4. DB migrations

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```

5. Flask run

```
export FLASK_APP=app.py;
flask run --reload
```

<a name="api_endpoints"></a>
## API Endpoints
### [Actors]
The below endpoint will query all the actors in the database
##### End Point
 LIVE URL endpoint 
 ```
 https://casting-agency-movies.herokuapp.com/actors
```
 local  
 ```
 http://localhost:5000/actors
```
#### GET
```
{
    "actors": [
        {
            "age": 29,
            "gender": "Male",
            "id": 1,
            "name": "Anant"
        }
        ],
    "success": true
}
```
#### Create Actor
The below endpoint will create an actor in the database

##### End Point
 LIVE URL endpoint 
 ```
 https://casting-agency-movies.herokuapp.com/actors
```
 local 
 ```
 http://localhost:5000/actors
```
##### POST
```
        {
            "age": 30,
            "gender": "Female",
            "name": "Anjelina"
        }
 ```
##### OUTPUT
```
{
    "created": 6,
    "success": true
}
```
#### Update Actor

The below endpoint will update an actor in the database

##### End Point
 LIVE URL endpoint 
 ```
 https://casting-agency-movies.herokuapp.com/actors/2
```
 local 
 ```
 http://localhost:5000/actors/2
```
##### PATCH
```
        {
            "age": 50,
            "gender": "Male",
            "name": "SRK"
        }
  ```
##### OUTPUT
```
{
    "actor": [
        {
            "age": 50,
            "gender": "Male",
            "id": 2,
            "name": "SRK"
        }
    ],
    "success": true,
    "updated": "SRK"
}
```

#### Delete Actor
The below endpoint will delete an actor in the database

##### End Point
LIVE URL endpoint 
```
https://casting-agency-movies.herokuapp.com/actors/2
```
local  
```
http://localhost:5000/actors/2
```
##### DELETE
##### OUTPUT
```
{
    "deleted": "2",
    "success": true
}
```

### [Movies]
#### Get 
The below endpoint will query all the movies in the database

##### End Point
LIVE URL endpoint 
```
https://casting-agency-movies.herokuapp.com/movies
```
localhost 
```
http://localhost:5000/movies
```
##### Output
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 10 Aug 2020 00:00:00 GMT",
            "title": "Steps to code"
        }
    ],
    "success": true
}
```
#### Create Movies
The below endpoint will create a movie in the database

##### End Point
LIVE URL endpoint 
```
https://casting-agency-movies.herokuapp.com/movies
```
localhost  
```
http://localhost:5000/movies
```
##### POST
```
        {
            "release_date": "Mon, 10 Aug 2020 00:00:00 GMT",
            "title": "Hello brother!!!"
        }
  ```
##### OUTPUT
```
{
    "created": "Hello brother!!!",
    "success": true
}
```
#### Delete Movies
The below endpoint will delete a movie in the database

##### End Point
LIVE URL endpoint 
```
https://casting-agency-movies.herokuapp.com/movies/7
```
localhost  
```
http://localhost:5000/movies/7
```
##### DELETE
##### OUTPUT
```
{
    "deleted": "7",
    "success": true
}
```

#### Update Movies
The below endpoint will update a movie in the database

##### End Point
LIVE URL endpoint 
```
https://casting-agency-movies.herokuapp.com/movies/10
```
localhost  
```
http://localhost:5000/movies/10
```
##### PATCH
```
        {
            "release_date": "Mon, 10 Aug 2020 00:00:00 GMT",
            "title": "Stigma in society"
        }
  ```
##### OUTPUT
```
{
    "edited": 10,
    "movie": [
        {
            "id": 10,
            "release_date": "Mon, 10 Aug 2020 00:00:00 GMT",
            "title": "Stigma in society"
        }
    ],
    "success": true
}
```
<a name="authentication"></a>
## Authentication
An error occurs if:
1. the token is expired
2. the claims are invalid permissions are not present in token
3. the token is invalid or not provided
4. the JWT doesn’t contain the proper action

The tokens w.r.t to role are
```
tokens = {
    "casting_assistant": "Bearer  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNMTZNRzE4WFRaVjgxa3U0T0x2dyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQwMDcudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMjVhYzI1MzJjZWEzMDIyMTE0Mjk3OSIsImF1ZCI6InZpZXdfbW92aWVzX2FjdG9ycyIsImlhdCI6MTU5NzE2MzcxNSwiZXhwIjoxNTk3MjUwMTEzLCJhenAiOiJwY2p0aDhCOUcxNlJGc25oUDg5bUJMbEx4d3VKTDJEUiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.H9_CzXburmYX7M6eTddAG6RC2ln_KJhA1hwCafVw7l0BC5hcIyS8v1pduJV5Knxo3FYisvt7hDbe9_fC4G17qJIe8JJ7eAr1n4IuGAKATD99SJbjQEUzTd06CtvX0kyLIx6nGEfmqCxTF0Qz_3T2wFDVPdlcQCQHq00z3AX9_RVXhDUkvkqOrRpqUX8YE015h32WALKW9uQBJH5aunTB8VRMhOGYS_xxPxs49e7sg8lbdmLQEwQvIJBqW8PrCC9YkWBPzVhiozTDytryxyx9Fgy0Jz2eNMIHumckf5_Xm1_jA9id4T-eTY0IHHlRvNzSgKztRfmi_ZC-hFz6oOebnA",
    "executive_producer": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNMTZNRzE4WFRaVjgxa3U0T0x2dyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQwMDcudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzE2MjNiNjhkZTk5MDAzNzQ2ZjYzNCIsImF1ZCI6InZpZXdfbW92aWVzX2FjdG9ycyIsImlhdCI6MTU5NzA4MTU5MSwiZXhwIjoxNTk3MTY3OTg5LCJhenAiOiJwY2p0aDhCOUcxNlJGc25oUDg5bUJMbEx4d3VKTDJEUiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImNyZWF0ZTptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.G-hkd2HEHDdq3axgon9Ykcy5AriDtOxbQ_DrxiTBq25cl5A6AL-eOQs64Kh0vPJgLDkecV1wJxSNwIgz8-a_bJXb-KhZZkLMB3INSG3W5ap8wAOyiaoMEo_KFVQ6wF-eKlBM0rNJJ0ae2p2RQJyMXLNyr_rEZY53XCCWlH-ZCGWpljxG2Xtp2e8aAdUQNKL86h8RBLUlbGhZcXfJ9xH9zrySxyxhtIHt5pxX8cvLKpd6CN6Nc3WfMXaHKnOtXTm7ocVyu0dmFoV7m1QqcqhFyRsLivuJ9CcYodpqv5ygh01oGnXEI0M0RZFx1aA1jy6tPJVvomO1VTzlO9U-d84tYw",
    "casting_director": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNMTZNRzE4WFRaVjgxa3U0T0x2dyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQwMDcudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzE2MjNiNjhkZTk5MDAzNzQ2ZjYzNCIsImF1ZCI6InZpZXdfbW92aWVzX2FjdG9ycyIsImlhdCI6MTU5NzE2NDAwOCwiZXhwIjoxNTk3MjUwNDA2LCJhenAiOiJwY2p0aDhCOUcxNlJGc25oUDg5bUJMbEx4d3VKTDJEUiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImNyZWF0ZTptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.HSapZyZOuNP2yg0MVIBuDqhZTw47dro4fcHxvFCpWMqRvBeI4c49kwfqB-6BTQSRIS1f2MLdbX0YWF5xqBM76PrPDlAYol4X6tZr4hNJJuPbJIozj9Ha_sTOibFhhw-4TUmPZWmLVqX6ZLiVGBAzjq6g86TVugqhEBFNUwKDIf9gZnDQWg44PVx7ie5cgwW6k7GNhn41rjQjmtCrZW7orbIROiY5igKFqSCpvHkdR6GO2omkIj6pnd-f2yQxCKbs1drh5zBOrscIvLWKdAAYLGGgAAUm7ZE9bjBFsNUNNco89Rwc8v_y0avqkTJtImlnsLb8PT6Aa1yl8RTcXcDIbQ
}
```
### Example of getting tokens
```
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```
tokens used

```
https://fsnd007.us.auth0.com/authorize?audience=view_movies_actors&response_type=token&client_id=pcjth8B9G16RFsnhP89mBLlLxwuJL2DR&redirect_uri=http://localhost:5000/

```

### Permissions
```
1. Casting Assistant
    - Can view actors and movies
2. Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
3. Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database
```

<a name="deployment"></a>
## Deployment
1. Deployment was on heroku
2. The app contains postgres sql initialized with some data
3. The app is provided with an environment variable DATABASE_URL fetched from heroku
4. db_reboot and db_create_all have been uncommented as the tables have been created
```
database_path = os.environ.get('DATABASE_URL')
```
3. to check the health of the app go on the browser
```
https://casting-agency-movies.herokuapp.com/health
```

Output
```
{
    "health":"APP is up",
    "success":true
}
```
### URL
 `https://casting-agency-movies.herokuapp.com/`
 
