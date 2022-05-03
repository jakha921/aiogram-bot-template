from environs import Env

env = Env()
env.read_env()

# .env 
BOT_TOKEN = env.str("BOT_TOKEN")  
ADMINS = env.list("ADMINS") 
IP = env.str("ip")  
PROVIDER_TOKEN = env.str("PROVIDER_TOKEN")
