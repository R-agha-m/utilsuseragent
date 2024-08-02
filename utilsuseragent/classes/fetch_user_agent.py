from typing import (
    Any, 
    Set,
)
from collections.abc import Set
from sqlite3 import connect, Row

from aiosqlite import connect as async_connect

from .default_connection_string import DEFAULT_DATABASE_CONNECTION_STRING


class FetchUserAgent:
    """
    A class to fetch user agent data from a SQLite database.

    This class provides both synchronous and asynchronous methods to fetch user agent
    records based on dynamic filters.

    Attributes
    ----------
    database_connection_string : str
        The connection string for the SQLite database.
    """

    def __init__(
            self,
            database_connection_string: str | None = DEFAULT_DATABASE_CONNECTION_STRING,
    ) -> None:
        """
        Initializes the FetchUserAgent instance.

        :param database_connection_string: Database connection string.
        :type database_connection_string: None | str
        """
        self.database_connection_string = database_connection_string or DEFAULT_DATABASE_CONNECTION_STRING

    def perform(
            self,
            **kwargs,
    ) -> dict[str, str | None]:
        """
        Fetches a user agent record synchronously based on the provided filters.

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
        filter_ = self._create_filter(inputs=kwargs)
        query = self._create_query(filter_=filter_)
        return self._fetch(query=query)

    async def async_perform(
            self,
            **kwargs,
    ) -> dict[str, str | None]:
        """
        Fetches a user agent record asynchronously based on the provided filters.

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
        filter_ = self._create_filter(inputs=kwargs)
        query = self._create_query(filter_=filter_)
        return await self._async_fetch(query=query)

    @staticmethod
    def _create_filter(inputs: dict[str, Any]) -> str:
        """
        Creates a SQL filter string based on the provided input dictionary.

        :param inputs: A dictionary of filter criteria.
        :type inputs: dict[str, Any]

        :returns: A SQL filter string.
        :rtype: str
        """
        filter_ = list()
        for key, value in inputs.items():
            if value is None:
                filter_.append(f"{key} IN ('null')")

            elif isinstance(value, str):
                filter_.append(f"{key} IN ('{value}')")

            elif isinstance(value, Set):
                prepared_value = [f"'{i}'" for i in value]
                filter_.append(f"{key} IN ({', '.join(prepared_value)})")

        return ' AND '.join(filter_)

    @staticmethod
    def _create_query(filter_: str) -> str:
        """
        Creates a SQL query string based on the provided filter string.

        :param filter_: A SQL filter string.
        :type filter_: str

        :returns: A SQL query string.
        :rtype: str
        """
        if filter_:
            return f"""
            SELECT * 
            FROM user_agent 
            WHERE {filter_}
            ORDER BY RANDOM() LIMIT 1;
            """
        else:
            return f"""
            SELECT * 
            FROM user_agent 
            ORDER BY RANDOM() LIMIT 1;
            """

    def _fetch(
            self,
            query: str,
    ) -> dict[str, str | None]:
        """
        Executes the provided SQL query synchronously and returns the result as a dictionary.

        :param query: A SQL query string.
        :type query: str

        :returns: A dictionary representing a user agent record.
        :rtype: dict[str, str | None]
        """
        with connect(self.database_connection_string) as connection:
            connection.row_factory = Row
            cursor = connection.cursor()
            cursor.execute(query)

            row = cursor.fetchone()
            return dict(row)

    async def _async_fetch(
            self,
            query: str,
    ) -> dict[str, str | None]:
        """
        Executes the provided SQL query asynchronously and returns the result as a dictionary.

        :param query: A SQL query string.
        :type query: str

        :returns: A dictionary representing a user agent record.
        :rtype: dict[str, str | None]
        """
        async with async_connect(self.database_connection_string) as connection:
            connection.row_factory = Row
            cursor = await connection.cursor()
            await cursor.execute(query)

            row = await cursor.fetchone()
            return dict(row)