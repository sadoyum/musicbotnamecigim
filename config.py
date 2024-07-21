from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BADNvmIAwM1WBQ1zsiQtfzd8_QeSdQqgmGz8Rw68mSkbwtNpaOcCh-FCFdmp4iYR-QbeX1AkUMO6pxO42NU8FIcLikyoGUL-GZncIXgxYJpLKEUodsWAmREb7o_kN7chcqNqNuABHVIgpDN2-qUTibLf7kjXO48P7-78-ts5AHoLClP8VTaTooIPSglhgfln9CQXnyZ_Ca19yLRgTzCfQQ4Z7FE72JqOsowKCJQlXqU1H4827-DkDgMQZG1PyKxYUIjGF_6TuLaBj6VWmk8ucBcwYtlFtRik2CWeoe1C1E8LErfgrDjhZafMUhKnx4FPYr7L8MOGz6WaKEGY2Flw7r9qH-XcxwAAAAGW8GWeAA")
BOT_TOKEN = getenv("BOT_TOKEN","6806370617:AAEonEb8kA1WD74-8w63Kt953Xz44RjY8Y4")
BOT_NAME = getenv("BOT_NAME", "Taşıyıcı") 
API_ID = int(getenv("API_ID","28550420"))
API_HASH = getenv("API_HASH","c20e89efef71b9c6d971fc27c999f906")
BOT_USERNAME = getenv("BOT_USERNAME", "KitapTasiyanBot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS","5072212654").split()))
