import pytest
from utilsuseragent import (
    CreateUserAgent,
    FetchUserAgent,
)


def test_perform():
    # TODO: clean db after test
    create_user_agent_obj = CreateUserAgent(database_connection_string='user_agent_test.sqlite')

    create_user_agent_obj.perform(user_agent_string='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                    'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                    'Chrome/91.0.4472.124 Safari/537.36')

    fetch_user_agent_obj = FetchUserAgent(database_connection_string='user_agent_test.sqlite')
    result = fetch_user_agent_obj.perform()

    assert list(result.keys()) == [
        'user_agent',
        'browser_family',
        'browser_major',
        'browser_minor',
        'browser_patch',
        'os_family',
        'os_major',
        'os_minor',
        'os_patch',
        'os_patch_minor',
        'device_family',
        'device_brand',
        'device_model',
    ]


@pytest.mark.asyncio
async def test_async_perform():
    create_user_agent_obj = CreateUserAgent(database_connection_string='user_agent_test.sqlite')

    await create_user_agent_obj.async_perform(
        user_agent_string='Mozilla/5.0 (Linux; Android 10; K) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'SamsungBrowser/25.0 Chrome/121.0.0.0 ' \
                          'Mobile Safari/537.36'
    )

    fetch_user_agent_obj = FetchUserAgent(database_connection_string='user_agent_test.sqlite')
    result = await fetch_user_agent_obj.async_perform()

    assert list(result.keys()) == [
        'user_agent',
        'browser_family',
        'browser_major',
        'browser_minor',
        'browser_patch',
        'os_family',
        'os_major',
        'os_minor',
        'os_patch',
        'os_patch_minor',
        'device_family',
        'device_brand',
        'device_model',
    ]


if __name__ == "__main__":
    pytest.main()
