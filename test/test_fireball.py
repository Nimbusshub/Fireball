#!/usr/bin/python3

"""Fireball console unittest"""

import os
import sys
from io import StringIO
import unittest
from unittest.mock import patch
from fireball import FireballPrompt


class TestFireball(unittest.TestCase):
    """Unitest for testing prompt of fireball console"""

    def test_prompt_string(self):
        self.assertEqual("<FireB>  ", FireballPrompt.prompt)

    def test_exit(self):
        """Test exit"""
        msg = "Thank you for using fireball"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(FireballPrompt().onecmd("exit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_man(self):
        """Test exit"""
        msg = "Type 'man fireball' to see the usage"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("man"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_wrong_man(self):
        """Test exit"""
        cmds = ['scan', 'listen', 'anything']
        for cmd in cmds:
            msg = "No manual entry for {}".format(cmd)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(FireballPrompt().onecmd("man {}".format(cmd)))
                self.assertEqual(msg, output.getvalue().strip())

    # def test_scan(self):
    #     """Test exit"""
    #     localhost = "127.0.0.1"
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertTrue(FireballPrompt().onecmd(
    #             "scan 127.0.0.1"))


class TestFireballHelp(unittest.TestCase):
    """UNittest for testing fireball help"""

    def test_help_exit(self):
        """Test exit help msg"""
        msg = "Exits the console"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help exit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_man(self):
        """Test man help msg"""
        msg = "Shows the man page"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help man"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_eof(self):
        """Test EOF help msg"""
        msg = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help EOF"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_clear(self):
        """Test clear help msg"""
        msg = "Clear all the outputs on the console"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help clear"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_scan(self):
        """Test scan help msg"""
        msg = "Scans for open ports"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help scan"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_listen(self):
        """Test listen help msg"""
        msg = "Listens for connection"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(FireballPrompt().onecmd("help listen"))
            self.assertEqual(msg, output.getvalue().strip())
