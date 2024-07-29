from utilscommon.utilscommon import base_dir_path_finder

BASE_DIR_PATH = base_dir_path_finder(
    file_path=__file__,
    number_of_going_up=2,
)
DEFAULT_DATABASE_CONNECTION_STRING = BASE_DIR_PATH.joinpath("user_agent.sqlite")

