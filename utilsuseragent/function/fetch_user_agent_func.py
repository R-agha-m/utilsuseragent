from .fetch_user_agent import (
    FetchUserAgent,
    Sentinel,
)


def fetch_user_agent_func(
        database_connection_string: str = 'user_agent.sqlite',
        browser_family: str = Sentinel,
        browser_major: int = Sentinel,
        browser_minor: int = Sentinel,
        browser_patch: int = Sentinel,
        os_family: str = Sentinel,
        os_major: int = Sentinel,
        os_minor: int = Sentinel,
        os_patch: int = Sentinel,
        os_patch_minor: int = Sentinel,
        device_family: str = Sentinel,
        device_brand: str = Sentinel,
        device_model: str = Sentinel,
):
    fetch_user_agent_instance = FetchUserAgent(database_connection_string=database_connection_string)
    return fetch_user_agent_instance(
        browser_family=browser_family,
        browser_major=browser_major,
        browser_minor=browser_minor,
        browser_patch=browser_patch,
        os_family=os_family,
        os_major=os_major,
        os_minor=os_minor,
        os_patch=os_patch,
        os_patch_minor=os_patch_minor,
        device_family=device_family,
        device_brand=device_brand,
        device_model=device_model,
    )
