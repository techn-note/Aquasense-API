import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = "mongodb+srv://ambiente-teste:1452@aquasense.fgtzuhv.mongodb.net/aquasense?retryWrites=true&w=majority&appName=Aquasense"
    JWT_SECRET_KEY = "minha_senha_super_secreta"

