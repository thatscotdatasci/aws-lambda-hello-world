import unittest

from helloworld.message import Message


class MessageTestCase(unittest.TestCase):

    def test_message_success(self):
        first_name = 'John'
        last_name = 'Smith'
        my_message = Message(first_name, last_name)
        self.assertEqual(my_message.message, f'Hello-World! Nice to meet you {first_name} {last_name}!')
