from pydantic import Field
from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str = Field(env="DB_HOST", default="127.0.0.1")
    port: int = Field(env="DB_PORT", default=5433)
    database_name: str = Field(env="DB_NAME", default="smart_scales")
    user: str = Field(env="DB_USER", default="postgres")
    password: str = Field(env="DB_PASSWORD", default="postgres")

    def get_connection_url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}"
