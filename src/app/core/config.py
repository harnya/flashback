import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

# DOTENV = os.path.join(os.path.dirname(__file__), ".env")

class Settings(BaseSettings):
    PGHOST: str
    PGUSER: str
    PGDATABASE: str
    PGPASSWORD: str
    model_config = SettingsConfigDict(case_sensitive=True)

class GSettings(BaseSettings):
    G_CLIENT_ID: str
    G_CLIENT_SECRET: str
    model_config = SettingsConfigDict(case_sensitive=True)

gsettings = GSettings()

settings = Settings()
