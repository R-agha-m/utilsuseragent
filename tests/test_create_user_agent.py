import unittest
from unittest.mock import patch, MagicMock
from ...utilsuseragent import CreateUserAgent  # Replace 'your_module' with the actual module name


class TestCreateUserAgent(unittest.TestCase):

    @patch('...utilsuseragent.user_agent_parser.Parse')
    def test_parse(self, mock_parse):
        # Setup
        mock_parse.return_value = {
            'string': 'Mozilla/5.0',
            'user_agent': {'family': 'Firefox', 'major': '89', 'minor': '0', 'patch': '1'},
            'os': {'family': 'Windows', 'major': '10', 'minor': '0', 'patch': '0', 'patch_minor': None},
            'device': {'family': 'Desktop', 'brand': None, 'model': None}
        }
        user_agent_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

        # Execute
        parser = CreateUserAgent()
        result = parser._parse(user_agent_string)

        # Assert
        self.assertEqual(result['user_agent']['family'], 'Firefox')
        mock_parse.assert_called_once_with(user_agent_string)

    def test_extract_details(self):
        parsed = {
            'string': 'Mozilla/5.0 (Linux; Android 14; SM-S911B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.164 Mobile Safari/537.36',
            'user_agent': {'family': 'Firefox', 'major': '89', 'minor': '0', 'patch': '1'},
            'os': {'family': 'Windows', 'major': '10', 'minor': '0', 'patch': '0', 'patch_minor': None},
            'device': {'family': 'Desktop', 'brand': None, 'model': None}
        }

        # Execute
        parser = CreateUserAgent()
        details = parser._extract_details(parsed)

        # Assert
        expected_details = {
            'user_agent': 'Mozilla/5.0',
            'browser_family': 'Firefox',
            'browser_major': '89',
            'browser_minor': '0',
            'browser_patch': '1',
            'os_family': 'Windows',
            'os_major': '10',
            'os_minor': '0',
            'os_patch': '0',
            'os_patch_minor': None,
            'device_family': 'Desktop',
            'device_brand': None,
            'device_model': None,
        }
        self.assertEqual(details, expected_details)

    @patch('...utilsuseragent.connect')
    def test_insert_into_db(self, mock_connect):
        # Mock the database connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Mock the details
        details = {
            'user_agent': 'Mozilla/5.0',
            'browser_family': 'Firefox',
            'browser_major': '89',
            'browser_minor': '0',
            'browser_patch': '1',
            'os_family': 'Windows',
            'os_major': '10',
            'os_minor': '0',
            'os_patch': '0',
            'os_patch_minor': None,
            'device_family': 'Desktop',
            'device_brand': None,
            'device_model': None,
        }

        # Execute
        parser = CreateUserAgent()
        parser._insert_into_db(details)

        # Assert
        mock_connect.assert_called_once_with('user_agent.sqlite')
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            parser.create_insertion_query(details)
        )
        mock_connection.commit.assert_called_once()

    # Add more tests for other methods and edge cases


if __name__ == '__main__':
    unittest.main()
