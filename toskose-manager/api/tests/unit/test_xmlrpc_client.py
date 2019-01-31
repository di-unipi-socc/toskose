import unittest
from app.client.impl.xmlrpc_client import ToskoseXMLRPCclient


class TestXMLRPCclient(unittest.TestCase):

    def setUp(self):
        self.client = ToskoseXMLRPCclient(
            host='localhost',
            port='9001',
            username='admin',
            password='admin'
        )
        self.log_offset = 0
        self.log_length = 0
        self.process_name = 'test-1'

    """ Testing Supervisord Process Management """

    def test_api_version(self):
        print(self.client.get_api_version())

    def test_supervisor_version(self):
        print(self.client.get_supervisor_version())

    def test_identification(self):
        print(self.client.get_identification())

    def test_state(self):
        print(self.client.get_state())

    def test_pid(self):
        print(self.client.get_pid())

    def test_read_log(self):
        print(self.client.read_log(self.log_offset, self.log_length))

    def test_clear_log(self):
        res = self.client.clear_log()
        if res:
            print('log cleared')
        else:
            print('failed')

    def test_shutdown(self):
        down = self.client.shutdown()
        if down:
            print('supervisor shutted down')
        else:
            print('failed')

    def test_restart(self):
        re = self.client.restart()
        if re:
            print('supervisor restarted')
        else:
            print('failed')

    """ Testing Supervisord Subprocesses Management """

    def test_get_process_info(self):
        process_info = self.client.get_process_info(self.process_name)

    def test_get_all_process_info(self):
        processes_info = self.client.get_all_process_info()
        print(processes_info)



if __name__ == '__main__':
    unittest.main()
