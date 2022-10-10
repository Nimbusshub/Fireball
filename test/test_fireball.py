#!/usr/bin/python3

"""Fireball console unittest"""

import os
import sys
import unittest
from unittest.mock import patch
from models import listener, portScanner
from fireball import FireballPrompt


class TestFireballCommandPromp(unittest.TestCase):
    """Unitest for testing prompt of fireball console"""

    def test_prompt_string(self):
        self.assertEqual("<FireB>  ", FireballPrompt.prompt)


class TestFireball_EOF(self):
    """Test EOF"""
    self.assertEqual("")
