import unittest
import os
import json


class TestProjectStructure(unittest.TestCase):
    """Test that the project structure is correct."""

    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"))

    def test_license_exists(self):
        self.assertTrue(os.path.exists("LICENSE"))

    def test_contributing_exists(self):
        self.assertTrue(os.path.exists("CONTRIBUTING.md"))

    def test_requirements_exists(self):
        self.assertTrue(os.path.exists("requirements.txt"))

    def test_src_directory_exists(self):
        self.assertTrue(os.path.isdir("src"))

    def test_configs_directory_exists(self):
        self.assertTrue(os.path.isdir("configs"))


class TestSourceCode(unittest.TestCase):
    """Test that source code files are valid Python."""

    def test_src_files_importable(self):
        src_dir = "src"
        if os.path.isdir(src_dir):
            for f in os.listdir(src_dir):
                if f.endswith(".py"):
                    filepath = os.path.join(src_dir, f)
                    with open(filepath, "r") as fh:
                        source = fh.read()
                    # Check it compiles without syntax errors
                    try:
                        compile(source, filepath, "exec")
                        compiled = True
                    except SyntaxError:
                        compiled = False
                    self.assertTrue(compiled, f"Syntax error in {filepath}")


class TestConfigs(unittest.TestCase):
    """Test that config files are valid."""

    def test_config_files_valid(self):
        configs_dir = "configs"
        if os.path.isdir(configs_dir):
            for f in os.listdir(configs_dir):
                if f.endswith(".json"):
                    filepath = os.path.join(configs_dir, f)
                    with open(filepath, "r") as fh:
                        try:
                            json.load(fh)
                            valid = True
                        except json.JSONDecodeError:
                            valid = False
                    self.assertTrue(valid, f"Invalid JSON in {filepath}")


if __name__ == "__main__":
    unittest.main()
