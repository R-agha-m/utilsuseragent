from ..classes import DEFAULT_DATABASE_CONNECTION_STRING
from ..classes import FetchUserAgent


def fetch_user_agent_func(
        database_connection_string: str | None = DEFAULT_DATABASE_CONNECTION_STRING,
        **kwargs
) -> dict[str, str | None]:
    """
    Fetches a user agent record synchronously based on the provided filters.

    :param database_connection_string: Database connection string.
    :type user_agent: None | str
    :param user_agent: Filter for user agent.
    :type user_agent: None | str | Set
    :param browser_family: Filter for browser family.
    :type browser_family: None | str | Set
    :param browser_major: Filter for browser major version.
    :type browser_major: None | str | Set
    :param browser_minor: Filter for browser minor version.
    :type browser_minor: None | str | Set
    :param browser_patch: Filter for browser patch version.
    :type browser_patch: None | str | Set
    :param os_family: Filter for OS family.
    :type os_family: None | str | Set
    :param os_major: Filter for OS major version.
    :type os_major: None | str | Set
    :param os_minor: Filter for OS minor version.
    :type os_minor: None | str | Set
    :param os_patch: Filter for OS patch version.
    :type os_patch: None | str | Set
    :param os_patch_minor: Filter for OS patch minor version.
    :type os_patch_minor: None | str | Set
    :param device_family: Filter for device family.
    :type device_family: None | str | Set
    :param device_brand: Filter for device brand.
    :type device_brand: None | str | Set
    :param device_model: Filter for device model.
    :type device_model: None | str | Set

    :returns: A dictionary representing a user agent record.
    :rtype: dict[str, str | None]
    """
    fetch_user_agent_instance = FetchUserAgent(database_connection_string=database_connection_string)
    return fetch_user_agent_instance.perform(**kwargs)
