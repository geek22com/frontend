# configuration
MIN_POOL = 5
MAX_POOL = 4000
HOST = '127.0.0.1'
DATABASE = 'social_sampler'
DEBUG = True
DB_USER = 'qa'
DB_PASSWORD = 'appatit'
DB_PORT = 5432
DB_CHARSET = 'utf8'
SECRET_KEY = 'lola pola_mola_cola'
RESTAPI_SERVER = 'http://localhost:5468'
USE_DATABASE = False

STATIC_PATH = "/usr/share/nginx/www/static"

APP_ID = "196817947051588"
APP_SECRET = "3ca1d75b952eeef29625ffc42df61ddf"
DEVELOPER_SECRET_KEY = "3ca2a85b953ffef29625ffc11df61eee"

#Facebook parameters
FACEBOOK_SERVICE_URL = "http://www.facebook.com"
FACEBOOK_GRAPH_URL = "https://graph.facebook.com"
FACEBOOK_APP_DOMAIN = "http://heymoose.com:8080"
FACEBOOK_SECURE_APP_DOMAIN = "https://heymoose.com"

FACEBOOK_APP_URL = "http://apps.facebook.com/heymoose/"
FACEBOOK_SECURE_APP_URL = "https://apps.facebook.com/heymoose/"

FACEBOOK_AUTH_SCOPE = "publish_stream,email,create_event,sms,publish_actions,user_likes,user_about_me"
BACKEND_PRIVATE_URL = "http://localhost"
BACKEND_PRIVATE_PORT = 1234

#Mongo parameters
MONGOALCHEMY_SERVER_AUTH = False
MONGOALCHEMY_DATABASE = 'facebook'

print "ATTENTION!! DEBUG CONFIG IS USED"
