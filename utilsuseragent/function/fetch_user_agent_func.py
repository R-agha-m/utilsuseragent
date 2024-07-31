from ..classes.fetch_user_agent import FetchUserAgent


def fetch_user_agent_func(
        database_connection_string: str = 'user_agent.sqlite',
        **kwargs
) -> dict[str, str | None]:
    fetch_user_agent_instance = FetchUserAgent(database_connection_string=database_connection_string)
    return fetch_user_agent_instance.perform(**kwargs)
