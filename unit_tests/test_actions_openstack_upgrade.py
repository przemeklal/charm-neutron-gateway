from unittest.mock import patch
import os

from test_utils import (
    CharmTestCase
)

os.environ['JUJU_UNIT_NAME'] = 'neutron-gateway'

import openstack_upgrade

TO_PATCH = [
    'do_openstack_upgrade',
    'config_changed',
    'charmhelpers.core.hookenv.log',
    'charmhelpers.contrib.openstack.utils.juju_log',
    'resolve_CONFIGS',
]


class TestNeutronGWUpgradeActions(CharmTestCase):

    def setUp(self):
        super(TestNeutronGWUpgradeActions, self).setUp(openstack_upgrade,
                                                       TO_PATCH)

    @patch('charmhelpers.contrib.openstack.utils.config')
    @patch('charmhelpers.contrib.openstack.utils.action_set')
    @patch('charmhelpers.contrib.openstack.utils.openstack_upgrade_available')
    def test_openstack_upgrade_true(self, upgrade_avail,
                                    action_set, config):
        upgrade_avail.return_value = True
        config.return_value = True

        openstack_upgrade.openstack_upgrade()

        self.assertTrue(self.do_openstack_upgrade.called)
        self.assertTrue(self.config_changed.called)

    @patch('charmhelpers.contrib.openstack.utils.config')
    @patch('charmhelpers.contrib.openstack.utils.action_set')
    @patch('charmhelpers.contrib.openstack.utils.openstack_upgrade_available')
    def test_openstack_upgrade_false(self, upgrade_avail,
                                     action_set, config):
        upgrade_avail.return_value = True
        config.return_value = False

        openstack_upgrade.openstack_upgrade()

        self.assertFalse(self.do_openstack_upgrade.called)
        self.assertFalse(self.config_changed.called)
