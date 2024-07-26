from typing import Any
from collections.abc import Sequence
from sqlite3 import connect


class Sentinel: pass


class FetchUserAgent:

    def __init__(
            self,
            database_connection_string: str = 'user_agent.sqlite',
    ) -> None:
        self.database_connection_string = database_connection_string

    def __call__(
            self,
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
    ) -> tuple[str]:
        inputs = {
            'browser_family': browser_family,
            'browser_major': browser_major,
            'browser_minor': browser_minor,
            'browser_patch': browser_patch,
            'os_family': os_family,
            'os_major': os_major,
            'os_minor': os_minor,
            'os_patch': os_patch,
            'os_patch_minor': os_patch_minor,
            'device_family': device_family,
            'device_brand': device_brand,
            'device_model': device_model,
        }

        filter_ = self._create_filter(inputs=inputs)
        return self._fetch(filter_=filter_)

    @staticmethod
    def _create_filter(inputs: dict[str, Any]) -> str:
        filter_ = list()
        for key, value in inputs.items():
            if value is not Sentinel:
                if value is None:
                    filter_.append(f"{key} IN ('null')")

                elif isinstance(value, str):
                    filter_.append(f"{key} IN ('{value}')")

                elif isinstance(value, Sequence):
                    prepared_value = [f"'{i}'" for i in value]
                    filter_.append(f"{key} IN ({', '.join(prepared_value)})")

        return ' AND '.join(filter_)

    def _fetch(
            self,
            filter_: str,
    ) -> tuple[str]:
        query = f"""
        SELECT * 
        FROM user_agent 
        WHERE {filter_}
        ORDER BY RANDOM() LIMIT 1;
        """

        with connect(self.database_connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(query)

            return cursor.fetchone()


#
# def create_user_agent(
#         user_agent_string: str,
#         database_connection_string: str = 'user_agent.sqlite',
# ):
#     create_user_agent_instance = CreateUserAgent(database_connection_string=database_connection_string)
#     return create_user_agent_instance(
#         user_agent_string=user_agent_string,
#     )


if __name__ == "__main__":
    fetch_user_agent_instance_2 = FetchUserAgent()
    result = fetch_user_agent_instance_2(
        browser_family='Chrome',
        # browser_major= None,
        # browser_minor= ,
        # browser_patch= ,
        os_family=('Windows','Android'),
        # os_major= ,
        os_minor= None,
        # os_patch= ,
        # os_patch_minor= ,
        # device_family= None,
        # device_brand= ,
        # device_model= ,
    )

    print(result)
