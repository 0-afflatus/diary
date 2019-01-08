#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Host/diary - tests.py

AR Event Organiser
"""

__version__ = 0.1
__maintainer__ = "tim@assemblyrooms.org.uk"

# Modules

from django.contrib.auth.models import User
from django.test import TestCase

class RealmsViewsTest(TestCase):
    
    fixtures = ['test_data.json']
    
    # Event list view /
    def test_event_list(self):
        resp = self.client.get('/')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('events' in resp.context)
    
    # Event detail view
    
    def test_bad_event_view(self):
        resp = self.client.get('/event/0')
        # Should Fail [404]
        self.assertEqual(resp.status_code, 404)
    
    def test_good_event_view(self):
        resp = self.client.get('/event/1')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
        
    # def test_public_filter
    # def test_provisional_filter
    # def test_export
    def test_export_list(self):
        resp = self.client.get('/export/')
        # Should be OK [200]
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('events' in resp.context)
    
    # Event edit view
    