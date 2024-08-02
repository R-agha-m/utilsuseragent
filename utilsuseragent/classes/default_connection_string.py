from pathlib import Path

BASE_DIR_PATH = Path(__file__).resolve().parent.parent

DEFAULT_DATABASE_CONNECTION_STRING = str(BASE_DIR_PATH.joinpath("user_agent.sqlite"))


