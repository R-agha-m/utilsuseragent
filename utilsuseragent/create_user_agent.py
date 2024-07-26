from sqlite3 import (
    connect,
    OperationalError,
)

from ua_parser import user_agent_parser

TABLE_CREATION_QUERY = '''
                        CREATE TABLE user_agent (
                            user_agent TEXT PRIMARY KEY NOT NULL UNIQUE,
                            browser_family TEXT,
                            browser_major INTEGER,
                            browser_minor INTEGER,
                            browser_patch INTEGER,
                            os_family TEXT,
                            os_major INTEGER,
                            os_minor INTEGER,
                            os_patch INTEGER,
                            os_patch_minor INTEGER,
                            device_family TEXT,
                            device_brand TEXT,
                            device_model TEXT
                        )
                    '''


class CreateUserAgent:

    def __init__(
            self,
            database_connection_string: str = 'user_agent.sqlite',
    ) -> None:
        self.database_connection_string = database_connection_string

    def __call__(
            self,
            user_agent_string: str,
    ) -> dict[str, str | None]:
        parsed = self._parse(user_agent_string=user_agent_string)
        details = self._extract_details(parsed=parsed)
        self._insert_into_db(details=details)
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

    def _insert_into_db(
            self,
            details: dict[str, str | None]
    ) -> None:
        with connect(self.database_connection_string) as connection:
            cursor = connection.cursor()

            self._create_table(cursor=cursor)
            self._insert_into_db_core(
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

    @staticmethod
    def _insert_into_db_core(
            cursor,
            connection,
            details: dict[str, str | None]
    ):
        columns_names = '"' + '", "'.join(details.keys()) + '"'
        columns_values = '"' + '", "'.join([i or "null" for i in details.values()]) + '"'

        query = f"""
        INSERT INTO user_agent 
        ({columns_names}) 
        VALUES ({columns_values})
        """

        cursor.execute(query)
        connection.commit()


def create_user_agent(
        user_agent_string: str,
        database_connection_string: str = 'user_agent.sqlite',
):
    create_user_agent_instance = CreateUserAgent(database_connection_string=database_connection_string)
    return create_user_agent_instance(
        user_agent_string=user_agent_string,
    )


if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    create_user_agent_instance_2 = CreateUserAgent()
    result = create_user_agent_instance_2(
        user_agent_string="Mozilla/5.0 (Linux; Android 14; SM-S911B Build/UP1A.231005.007; wv) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.164 Mobile Safari/537.3",
    )

    pp.pprint(result)
