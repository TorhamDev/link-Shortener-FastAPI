# MySQL configs
DB_NAME = "shortener_link"
DB_USER = "root"
DB_PASSWORD = "mysql"
DB_HOST = "localhost"
DB_PORT = 3306

# Redis configs
REDIS_DB = 0
REDIS_DB_HOST = "localhost"
REDIS_DB_PORT = 6379

# Regex for link validation
WITH_HTTP = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
WITH_HTTPS = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

