import pytest
from utilsuseragent import CreateUserAgent


def test_perform():
    # TODO: clean db after test
    create_user_agent_obj = CreateUserAgent(database_connection_string='user_agent_test.sqlite')

    result = create_user_agent_obj.perform(user_agent_string='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                             'Chrome/91.0.4472.124 Safari/537.36')

    assert {
               'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                             'Chrome/91.0.4472.124 Safari/537.36',
               'browser_family': 'Chrome',
               'browser_major': '91',
               'browser_minor': '0',
               'browser_patch': '4472',
               'os_family': 'Windows',
               'os_major': '10',
               'os_minor': None,
               'os_patch': None,
               'os_patch_minor': None,
               'device_family': 'Other',
               'device_brand': None,
               'device_model': None,
           } == result


@pytest.mark.asyncio
async def test_async_perform():
    create_user_agent_obj = CreateUserAgent(database_connection_string='user_agent_test.sqlite')

    result = await create_user_agent_obj.async_perform(user_agent_string='Mozilla/5.0 (Linux; Android 10; K) '
                                                                         'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                                         'SamsungBrowser/25.0 Chrome/121.0.0.0 ' \
                                                                         'Mobile Safari/537.36')

    assert {
               'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                             'SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.36',
               'browser_family': 'Samsung Internet',
               'browser_major': '25',
               'browser_minor': '0',
               'browser_patch': None,
               'os_family': 'Android',
               'os_major': '10',
               'os_minor': None,
               'os_patch': None,
               'os_patch_minor': None,
               'device_family': 'K',
               'device_brand': 'Generic_Android',
               'device_model': 'K'
           } == result


# Run the tests
if __name__ == "__main__":
    pytest.main()
