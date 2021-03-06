import unittest
import time
import pathlib
import os

from utils.create_project import *

class TestCreateProject(unittest.TestCase):
    def test_create_file(self):
        root_path = "./tests/work"
        file_path = "test_create_file.txt"

        create_file(root_path, file_path)

        file_path_actual = pathlib.Path(root_path + "/" + file_path)
        self.assertTrue(file_path_actual.exists())

    def test_git_init_project(self):
        root_path = "./tests/work"
        git_init_project(root_path)
        file_list = os.listdir(root_path)
        actual = ".git" in file_list
        self.assertTrue(actual)

    def test_create_file_already_exists(self):
        """test create_file_false case when already file exists.
        """
        root_path = "./tests/work"
        file_path = "test_create_file.txt"

        actual = create_file(root_path, file_path)

        self.assertFalse(actual)

