import unittest

from napalm_fsos_ssh import fsos
from napalm.base.test.base import TestConfigNetworkDriver, TestGettersNetworkDriver


class TestConfigROSDriver(unittest.TestCase, TestConfigNetworkDriver):
    @classmethod
    def setUpClass(cls):
        """Executed when the class is instantiated."""
        cls.vendor = 'fsos'
        cls.device = fsos.FsosDriver(
            '127.0.0.1',
            'user',
            'password',
            timeout=60,
        )
        cls.device.open()
