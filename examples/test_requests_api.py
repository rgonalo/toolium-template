# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
import requests
from seleniumtid.test_cases import BasicTestCase


class RegisterUser(BasicTestCase):
    def test_successful_register(self):
        url = 'http://qacore01.hi.inet/sites/seleniumExamples/register.php'
        user = {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com',
                'place': 'Barcelona'}

        self.logger.debug("Registering a new user through the api")
        r = requests.post(url, user)
        self.assertEqual(r.status_code, 200)
        self.assertIn('The user has been registered', r.text)