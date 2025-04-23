import os
from utils.config import app_config, env_config

# prints the config.json content
print(app_config)

# prints teh secret key - to check if env loaded successfully
# print(os.environ.get("GROQ_API_KEY"))
print(os.environ.get("APP_API_KEY"))

# check form env_config object
print(env_config.APP_API_KEY)