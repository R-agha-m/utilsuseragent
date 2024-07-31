from ..classes.fetch_user_agent import FetchUserAgent


async def fetch_user_agent_async_func(**kwargs) -> dict[str, str | None]:
    fetch_user_agent_instance = FetchUserAgent(database_connection_string=kwargs.get("database_connection_string"))
    return await fetch_user_agent_instance.async_perform(**kwargs)
