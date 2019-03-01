#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `juritagger` package."""


import unittest
from click.testing import CliRunner

from juritagger import display_entities
from juritagger import cli


class TestDisplay(unittest.TestCase):
    """Tests for `juritagger` package."""
    def test_convert_match(self):
        match = ("label", 12, 28)
        converted_match = display_entities.convert_match(match)
        self.assertIsInstance(converted_match, dict)
        self.assertIsNotNone(converted_match)
        self.assertEqual(len(converted_match), 3)
        self.assertIn("label", converted_match)
        self.assertIn("start", converted_match)
        self.assertIn("end", converted_match)
    
    def test_check_overlap(self):
        entity_range = [{61},
                        {66},
                        {68},
                        {68, 69},
                        {78},
                        {85, 86, 87},
                        {87},
                        {87, 88}]
        overlaps = display_entities.check_overlap(6 , entity_range)
        self.assertEqual(overlaps, [5, 7])
        self.assertIn(overlaps[0], range(len(entity_range)))
        overlaps2 = display_entities.check_overlap(1 ,entity_range)
        self.assertEqual(overlaps2, [])

    def test_keep_longer_match(self):
        matches = [('JUR', 17, 18),
                    ('JUR', 33, 36),
                    ('JUR', 35, 36)]
        expected_res = [('JUR', 17, 18),
                        ('JUR', 33, 36)]
        new_matches = display_entities.keep_longer_match(matches)
        self.assertEqual(new_matches, expected_res)
        
if __name__ == "__main__":
    unittest.main()
