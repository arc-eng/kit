# coding: utf-8

"""
    Arcane Engine API

    API for creating Arcane Engine tasks

    The version of the OpenAPI document: 1.13.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arcane.models.installation_status import InstallationStatus

class TestInstallationStatus(unittest.TestCase):
    """InstallationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstallationStatus:
        """Test InstallationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallationStatus`
        """
        model = InstallationStatus()
        if include_optional:
            return InstallationStatus(
                installed = True
            )
        else:
            return InstallationStatus(
                installed = True,
        )
        """

    def testInstallationStatus(self):
        """Test InstallationStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
