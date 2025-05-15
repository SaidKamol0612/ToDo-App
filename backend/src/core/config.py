from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    title: str = "Postgres ToDo API"
    description: str = "ToDo API with Postgres DB"
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn | str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
    
class JWTAuth(BaseModel):
    private_key_path: Path
    public_key_path: Path
    lifetime_seconds: int = 3600
    algorithm: str = "RS256"
    secret: str
    
    reset_password_token_secret: str
    verification_token_secret: str
    
class MediaSettings(BaseModel):
    path_or_url: str    

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    
    run: RunConfig = RunConfig()    
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    # jwt_auth: JWTAuth
    media: MediaSettings

settings = Settings()
