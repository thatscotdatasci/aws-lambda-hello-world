from helloworld.core import Message


def lamdba_handler(event, context):
    my_hello_world = Message(event['first_name'], event['last_name'])
    return {'message': my_hello_world.message}
