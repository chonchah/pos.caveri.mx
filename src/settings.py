# settings.py
import settings
import os
from pymongo import MongoClient
from pathlib import Path  # Python 3.6+ only
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db_usr, db_host, db_pass, db_port, db_name = os.getenv(
    'DB_USER'), os.getenv('DB_HOST'), os.getenv('DB_PASS'), os.getenv('DB_PORT'), os.getenv('DB_NAME')
uri_conection = "mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority" % (
    db_usr, db_pass, db_host, db_name)
print(uri_conection)
mongo_client = MongoClient(host=db_host, port=int(db_port),
                           username=db_usr, password=db_pass, authSource=db_name)
