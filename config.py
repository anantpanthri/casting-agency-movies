import os

AUTH0_DOMAIN = 'fsnd007.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'view_movies_actors'

database_name = "casting_agency"
#   uncomment for local run
#   database_path = "postgres://{}/{}".format('localhost:5432', database_name)

database_path = os.environ.get('DATABASE_URL')

# for local run find tokens from readme
