import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28978038'))
API_HASH = environ.get('API_HASH', 'dd7fa173882b6e3d3ccb0c70ccf6d626')
BOT_TOKEN = environ.get('BOT_TOKEN', '7637309577:AAH2UHaMqnQyJfoXy5Sy9Azqa0IYlIZewXA')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7404203924').split()]
USERNAME = environ.get('USERNAME', "RDX1444") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002580632118'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/MC_MOVIES_PVT')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', ' -1002598175852').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://RDX:RDX@cluster0.ckt1p.mongodb.net/RDX?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "RDX")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002727969724'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL',' -1002878005579'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '-1002694665484')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002718911113')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002718911113'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/MC_MOVIES_PVT') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', False)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Stark_Network07")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "fa7b06fadcb10ca159f29be425adcbae662469b5")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'gplinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "fa7b06fadcb10ca159f29be425adcbae662469b5")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'gplinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "fa7b06fadcb10ca159f29be425adcbae662469b5")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'gplinks.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 3000
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://graph.org/file/6b3d2e2b0554abf816174-8254b0f8e1878b7f14.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://graph.org/file/84b250fbdf2cf62272057-a03b878fd6125bcf4c.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/6ba05f3a66646e9d78c37-0cee0a01b9d84aa1af.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 900))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "sharp-april-zishananis-cb465703.koyeb.app")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
