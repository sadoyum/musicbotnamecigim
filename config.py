from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BABpWCOntkWil1VUhVfRvX3eh5eu2wlCL_XBzidvhu3HYeh-ZCkBXF-n81ZYWusjiUmS0Jtzfkhs7Fo7XoyYs3SO0jMIZhvD3EUtHfQ7MFWoU4HsDgbV5O82SLxCh_Af7rdZlRjymbR-mMcEAQsTNFJMgOSaYeggYvmt-XRoZa_p2RFdBdIuFGpcN4qSg2-EMm8YADRhSyvS1TubXuJtuq2uyS6c9shbHpzKY3pMLI3vZDH_h_qIA1cxdj0k9t3HHUbROWGlZ-tdxPuBnzayAwTGDw39t3kjhFCuwUnfdd5OfhdQqFCfsx7H4eradQZcMl9XbX8lP21a81gszkrAcsqbAAAAAUz8Jh0A")
BOT_TOKEN = getenv("BOT_TOKEN","6066378580:AAH4gTl9_mTcyHBxCMvJln0wrk_J-_zlJ8Q")
BOT_NAME = getenv("BOT_NAME", "Pulsar Music") 
API_ID = int(getenv("API_ID","26195299"))
API_HASH = getenv("API_HASH","a1f855a11d7d23af8a4869b07b57dde7")
BOT_USERNAME = getenv("BOT_USERNAME", "PulsarMusicBot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS","5072212654").split()))
