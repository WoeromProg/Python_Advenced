import unittest
from task3 import BlockErrors

class TestBlockErrors(unittest.TestCase):
    def test_ignoreError(self):
        def test_case():
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            return True
        return self.assertTrue(test_case())

    def test_upLevel(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / '0'
        return True

    def test_ignore_in_out_errors(self):
        def test_case():
            outer_err_types={TypeError}
            with BlockErrors(outer_err_types):
                in_errr_types = {ZeroDivisionError}
                with BlockErrors(in_errr_types):
                    a = 1 / '0'
                return 'Внутренний блок: выполнено без ошибок'
            return 'Внешний блок: выполнено без ошибок'

    def test_exception(self):
        err_types = {Exception}
        with BlockErrors(err_types):
            a = 1 / '0'
        return True