# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from nose.tools import assert_in

from toolium_template.pageobjects.login import LoginPageObject
from toolium_template.test_cases import SeleniumTestCase


class Login(SeleniumTestCase):
    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Login and check welcome message
        secure_area = LoginPageObject().open().login(user)
        assert_in(expected_login_message, secure_area.message.get_message())
        self.assert_full_screenshot('login_secure_area')

        # Logout and check logout message
        login_page = secure_area.logout()
        assert_in(expected_logout_message, login_page.message.get_message())
        self.assert_full_screenshot('login_logout')

    def test_wrong_login(self):
        user = {'username': 'peter', 'password': 'pass'}
        expected_message = "Your username is invalid!"

        # Try to login and check error message
        login_page = LoginPageObject()
        login_page.open().login(user)
        assert_in(expected_message, login_page.message.get_message())
        self.assert_full_screenshot('login_wrong_full')
