from pydantic import BaseSettings

class EnvSettings(BaseSettings):
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_HOSTNAME: str
    SECRET_KEY: str 
    ALGORITHM: str
    
    class Config:
        env_file = '../../.env'
        

env = EnvSettings()