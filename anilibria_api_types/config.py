from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class MainSettings(BaseSettings):
    FOLDER_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="MAIN_", extra="ignore"
    )


main_settings = MainSettings()