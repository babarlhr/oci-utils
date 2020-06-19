# Copyright (c) 2020 Oracle and/or its affiliates. All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown
# at http://oss.oracle.com/licenses/upl.

import os
import subprocess
import unittest

from tools.oci_test_case import OciTestCase


class TestUpload(OciTestCase):
    """ Test image validate for migration.
    """
    def setUp(self):
        super(TestUpload, self).setUp()
        self.oci_migrate_image_path = self.properties.get_property('oci-image-migrate')
        if not os.path.exists(self.oci_migrate_image_path):
            raise unittest.SkipTest("%s not present" %
                                    self.oci_migrate_image_path)

    def test_display_help(self):
        """ Display help message.
        """
        try:
            _ = subprocess.check_output([self.oci_migrate_image_path, '--help'])
        except Exception as e:
            self.fail('Execution has failed: %s' % str(e))
