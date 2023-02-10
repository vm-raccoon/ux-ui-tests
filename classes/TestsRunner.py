from glob import glob
from os import walk, path
from os.path import basename
from importlib import import_module
from classes.BaseTest import BaseTest


class TestsRunner:

    @staticmethod
    def get_test_files_list(tests_path):
        return [y for x in walk(tests_path) for y in glob(path.join(x[0], '*.py'))]

    @staticmethod
    def get_module_path(filename):
        return filename.replace('.py', '').replace('\\', '.').replace('/', '.')

    @staticmethod
    def get_class_name(filename):
        return basename(filename).replace('.py', '')

    @staticmethod
    def process_test_file(filename):
        module_path = TestsRunner.get_module_path(filename)
        class_name = TestsRunner.get_class_name(filename)
        module_test = import_module(module_path)
        class_test = getattr(module_test, class_name)
        if issubclass(class_test, BaseTest):
            if class_test.active:
                class_test().run()

    @staticmethod
    def run_tests(tests_path):
        tests_path = basename(tests_path)
        test_files = TestsRunner.get_test_files_list(tests_path)
        for file in test_files:
            TestsRunner.process_test_file(file)
