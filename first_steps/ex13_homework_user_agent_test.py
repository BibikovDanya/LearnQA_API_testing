import requests
import pytest
from environment import default_url
from lib.base_case import BaseCase


class TestUserAgent(BaseCase):
    dataprovider = [
        {
            "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) "
                          "AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "platform": "Mobile",
            "browser": "No",
            "device": "Android"
        },
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) "
                          "AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "No",
            "device": "iOS"
        },
        {
            "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "platform": "Unknown",
            "browser": "Unknown",
            "device": "Unknown"
        },
        {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "platform": "Web",
            "browser": "Chrome",
            "device": "No"
        },
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "No",
            "device": "Unknown"
        }
    ]

    @pytest.mark.parametrize('dataprovider', dataprovider)
    def test_user_agent(self, dataprovider):
        self.user_agent = dataprovider["user_agent"]
        response = requests.get(f"{default_url}/user_agent_check", headers={"User-Agent": self.user_agent})

        self.actual_platform = self.get_json_value(response, 'platform')
        self.actual_browser = self.get_json_value(response, 'browser')
        self.actual_device = self.get_json_value(response, 'device')

        self.expected_platform = dataprovider['platform']
        self.expected_browser = dataprovider['browser']
        self.expected_device = dataprovider['device']

        assert self.actual_platform == self.expected_platform, \
            f"UserAgent: {self.user_agent} \n " \
            f"Actual platform: '{self.actual_platform}', expected platform: '{self.expected_platform}' "
        assert self.actual_browser == self.expected_browser, \
            f"UserAgent: {self.user_agent} \n " \
            f"Actual browser: '{self.actual_browser}', expected browser: '{self.expected_browser}' "
        assert self.actual_device == self.expected_device, \
            f"UserAgent: {self.user_agent} \n " \
            f"Actual device: '{self.actual_device}', expected device: '{self.expected_device}' "
