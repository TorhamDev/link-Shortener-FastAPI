from os import getenv

# MySQL configs
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")

# Redis configs
REDIS_DB = getenv("REDIS_DB")
REDIS_DB_HOST = getenv("REDIS_DB_HOST")
REDIS_DB_PORT = getenv("REDIS_DB_PORT")

# Regex for link validation
WITH_HTTP = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
WITH_HTTPS = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]" +\
             "{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
