from sqlite3 import (
    connect,
    OperationalError,
    IntegrityError,
)

from aiosqlite import connect as async_connect
from ua_parser import user_agent_parser

from .table_creation_query import TABLE_CREATION_QUERY


class CreateUserAgent:

    def __init__(
            self,
            database_connection_string: str = 'user_agent.sqlite',
    ) -> None:
        self.database_connection_string = database_connection_string

    def perform(
            self,
            user_agent_string: str,
    ):
        parsed = self._parse(user_agent_string=user_agent_string)
        details = self._extract_details(parsed=parsed)
        self._insert_into_db(details=details)
        return details

    async def async_perform(
            self,
            user_agent_string: str,
    ):
        parsed = self._parse(user_agent_string=user_agent_string)
        details = self._extract_details(parsed=parsed)
        await self._async_insert_into_db(details=details)
        return details

    @staticmethod
    def _parse(user_agent_string: str) -> dict[str, str | dict]:
        return user_agent_parser.Parse(user_agent_string)

    @staticmethod
    def _extract_details(parsed: dict[str, str | dict]) -> dict[str, str | None]:
        return {
            'user_agent': parsed['string'],

            'browser_family': parsed['user_agent']['family'],
            'browser_major': parsed['user_agent']['major'],
            'browser_minor': parsed['user_agent']['minor'],
            'browser_patch': parsed['user_agent']['patch'],

            'os_family': parsed['os']['family'],
            'os_major': parsed['os']['major'],
            'os_minor': parsed['os']['minor'],
            'os_patch': parsed['os']['patch'],
            'os_patch_minor': parsed['os']['patch_minor'],

            'device_family': parsed['device']['family'],
            'device_brand': parsed['device']['brand'],
            'device_model': parsed['device']['model'],
        }

    async def _async_insert_into_db(
            self,
            details: dict[str, str | None]
    ) -> None:
        async with async_connect(self.database_connection_string) as connection:
            async with connection.cursor() as cursor:
                await self._async_create_table(cursor=cursor)
                await self._async_create_row(
                    cursor=cursor,
                    connection=connection,
                    details=details,
                )

    @staticmethod
    async def _async_create_table(cursor):
        try:
            await cursor.execute(TABLE_CREATION_QUERY)
        except OperationalError:
            pass

    async def _async_create_row(
            self,
            cursor,
            connection,
            details: dict[str, str | None]
    ):
        query = self.create_insertion_query(details=details)
        try:
            await cursor.execute(query)
            await connection.commit()
        except IntegrityError:
            pass

    def _insert_into_db(
            self,
            details: dict[str, str | None]
    ) -> None:
        with connect(self.database_connection_string) as connection:
            cursor = connection.cursor()

            self._create_table(cursor=cursor)
            self._create_row(
                cursor=cursor,
                connection=connection,
                details=details,
            )

    @staticmethod
    def _create_table(cursor):
        try:
            cursor.execute(TABLE_CREATION_QUERY)
        except OperationalError:
            pass

    def _create_row(
            self,
            cursor,
            connection,
            details: dict[str, str | None]
    ):
        query = self.create_insertion_query(details=details)
        try:
            cursor.execute(query)
            connection.commit()
        except IntegrityError:
            pass

    @staticmethod
    def create_insertion_query(details: dict[str, str | None]) -> str:
        columns_names = '"' + '", "'.join(details.keys()) + '"'
        columns_values = '"' + '", "'.join([i or "null" for i in details.values()]) + '"'

        return f"""
        INSERT INTO user_agent 
        ({columns_names}) 
        VALUES ({columns_values})
        """
