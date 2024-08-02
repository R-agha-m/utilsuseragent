from logging import Logger
from collections.abc import Sequence
from traceback import format_exc

from ..classes import DEFAULT_DATABASE_CONNECTION_STRING
from .create_user_agent_async_func import create_user_agent_async_func


async def create_user_agents_async_func(
        user_agents_strings: Sequence[str],
        database_connection_string: str = DEFAULT_DATABASE_CONNECTION_STRING,
        logger: Logger = None,
) -> list[str]:
    had_error = list()
    for index, user_agent_string in enumerate(user_agents_strings):
        if logger:
            logger.info("%s, %s", index, user_agent_string)
        try:
            await create_user_agent_async_func(
                database_connection_string=database_connection_string,
                user_agent_string=user_agent_string,
            )
        except Exception:
            if logger:
                logger.info(format_exc())
            had_error.append(user_agent_string)

    return had_error
