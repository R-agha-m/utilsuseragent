from typing import Any
from collections.abc import Sequence
from sqlite3 import connect, Row

from aiosqlite import connect as async_connect

from .default_connection_string import DEFAULT_DATABASE_CONNECTION_STRING


class FetchUserAgent:

    def __init__(
            self,
            database_connection_string: str | None = DEFAULT_DATABASE_CONNECTION_STRING,
    ) -> None:
        self.database_connection_string = database_connection_string or DEFAULT_DATABASE_CONNECTION_STRING

    def perform(
            self,
            **kwargs,
    ) -> dict[str, str | None]:
        filter_ = self._create_filter(inputs=kwargs)
        query = self._create_query(filter_=filter_)
        return self._fetch(query=query)

    async def async_perform(
            self,
            **kwargs,
    ) -> dict[str, str | None]:
        filter_ = self._create_filter(inputs=kwargs)
        query = self._create_query(filter_=filter_)
        return await self._async_fetch(query=query)

    @staticmethod
    def _create_filter(inputs: dict[str, Any]) -> str:
        filter_ = list()
        for key, value in inputs.items():
            if value is None:
                filter_.append(f"{key} IN ('null')")

            elif isinstance(value, str):
                filter_.append(f"{key} IN ('{value}')")

            elif isinstance(value, Sequence):
                prepared_value = [f"'{i}'" for i in value]
                filter_.append(f"{key} IN ({', '.join(prepared_value)})")

        return ' AND '.join(filter_)

    @staticmethod
    def _create_query(filter_: str) -> str:
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
        async with async_connect(self.database_connection_string) as connection:
            connection.row_factory = Row
            cursor = await connection.cursor()
            await cursor.execute(query)

            row = await cursor.fetchone()
            return dict(row)
