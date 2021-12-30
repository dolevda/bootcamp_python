import pytest


class Test_PyTest:

    @classmethod
    def setup_class(cls):
        print("Before Test Class")

    @classmethod
    def teardown_class(cls):
        print("After Test Class")

    # def setup_method(self):
    #     print("Before test")
    #
    # def teardown_method(self):
    #     print("Before test")

    @pytest.fixture(autouse=True)
    def setup(self):
        print("This is setup")
        yield
        print("This is tearDown")

    def test_1(setup):
        print("Test case 1")

    def test_2(setup):
        print("Test case 1")
