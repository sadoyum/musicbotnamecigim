from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQAsrFxLqwH6LyGQY3396pUv_jB_Sk66tscBFiDV7A5v5Ud1UNyxsbhxFqcCbCTb7caAgDHDWAV4jjZbcn72fFw5MQBXcIYwBKkTkSBgj61CHbzw56xZ47MEO6WjuWHHUlIvMeJ-anltYi00B1uH53xH2zTkVzlZqLF2E4i1oAsj1MqbPKyDWYOl3R2SZwzek5groV6NLfUPIy8Smn_86JB0cGcBaC21a7eZll7lbDTu5z3irF9JIkDkWcjf2ZtOh9XNoQCBtwLwJUqEfcvV7S7q6wVvopmmW7sbEtBvjoqJR43HHOxJTiQw-69fedfXkbxT7UCD9oZG9cSi4y9FhnO4AAAAAS6mjVwA")
BOT_TOKEN = getenv("BOT_TOKEN","6144599565:AAEQMVP95Af_RWJ4KrHS47JUNjxFcrRxVUA")
BOT_NAME = getenv("BOT_NAME", "Spotify Müzik") 
API_ID = int(getenv("API_ID","11919556"))
API_HASH = getenv("API_HASH","464b1d74248bed1c16a2f5f1243412fb")
BOT_USERNAME = getenv("BOT_USERNAME", "muzikdinleyicibot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
