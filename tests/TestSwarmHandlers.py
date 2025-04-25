import unittest
import os
import logging
from tests import TestTools
from SwarmManagement import SwarmConfigs
from SwarmManagement import SwarmSecrets
from SwarmManagement import SwarmVolumes
from SwarmManagement import SwarmNetworks
from SwarmManagement import SwarmStacks
from SwarmManagement import SwarmManager

log = logging.getLogger(__name__)


class TestSwarmHandlers(unittest.TestCase):

    def test_a_config(self):
        log.info('EXECUTING SWARM CONFIG TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-config', '-create', 'all']
        SwarmConfigs.HandleConfigs(arguments)
        arguments = ['-config', '-rm', 'all']
        SwarmConfigs.HandleConfigs(arguments)
        arguments = ['-config', '-create', 'site.conf']
        SwarmConfigs.HandleConfigs(arguments)
        arguments = ['-config', '-rm', 'site.conf']
        SwarmConfigs.HandleConfigs(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM CONFIG TEST')

    def test_b_secret(self):
        log.info('EXECUTING SWARM SECRET TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-secret', '-create', 'all']
        SwarmSecrets.HandleSecrets(arguments)
        arguments = ['-secret', '-rm', 'all']
        SwarmSecrets.HandleSecrets(arguments)
        arguments = ['-secret', '-create', 'site.key']
        SwarmSecrets.HandleSecrets(arguments)
        arguments = ['-secret', '-rm', 'site.key']
        SwarmSecrets.HandleSecrets(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM SECRET TEST')

    def test_c_networks(self):
        log.info('EXECUTING SWARM NETWORK TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-network', '-create', 'all']
        SwarmNetworks.HandleNetworks(arguments)
        arguments = ['-network', '-rm', 'all']
        SwarmNetworks.HandleNetworks(arguments)
        arguments = ['-network', '-create', 'frontend_network']
        SwarmNetworks.HandleNetworks(arguments)
        arguments = ['-network', '-rm', 'frontend_network']
        SwarmNetworks.HandleNetworks(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM NETWORK TEST')

    def test_d_volumes(self):
        log.info('EXECUTING SWARM VOLUMES TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-volume', '-create', 'all']
        SwarmVolumes.HandleVolumes(arguments)
        arguments = ['-volume', '-rm', 'all']
        SwarmVolumes.HandleVolumes(arguments)
        arguments = ['-volume', '-create', 'first_volume']
        SwarmVolumes.HandleVolumes(arguments)
        arguments = ['-volume', '-rm', 'first_volume']
        SwarmVolumes.HandleVolumes(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM VOLUMES TEST')

    def test_e_manager(self):
        log.info('EXECUTING SWARM MANAGER TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-start']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-restart', '2']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-restart']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-wait', '10']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-wait', '3', 'ssl_proxy_ssl-proxy-web']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-stop']
        SwarmManager.HandleManagement(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM MANAGER TEST')

    def test_f_stacks(self):
        log.info('EXECUTING SWARM STACKS TEST')
        cwd = TestTools.ChangeToSampleFolderAndGetCwd()
        arguments = ['-start']
        SwarmManager.HandleManagement(arguments)
        arguments = ['-stack', '-deploy', 'all']
        SwarmStacks.HandleStacks(arguments)
        arguments = ['-stack', '-rm', 'all']
        SwarmStacks.HandleStacks(arguments)
        arguments = ['-stack', '-deploy', 'ssl_proxy']
        SwarmStacks.HandleStacks(arguments)
        arguments = ['-stack', '-rm', 'ssl_proxy']
        SwarmStacks.HandleStacks(arguments)
        arguments = ['-stop']
        SwarmManager.HandleManagement(arguments)
        os.chdir(cwd)
        log.info('DONE EXECUTING SWARM STACKS TEST')

if __name__ == '__main__':
    unittest.main()