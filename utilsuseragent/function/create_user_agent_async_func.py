from ..classes import DEFAULT_DATABASE_CONNECTION_STRING
from ..classes import CreateUserAgent


async def create_user_agent_async_func(
        user_agent_string: str,
        database_connection_string: str = DEFAULT_DATABASE_CONNECTION_STRING,
):
    create_user_agent_instance = CreateUserAgent(database_connection_string=database_connection_string)
    return await create_user_agent_instance.async_perform(
        user_agent_string=user_agent_string,
    )
