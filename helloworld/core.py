from helloworld.message import Message


def my_handler(event, context):
    my_hello_world = Message(event['first_name'], event['last_name'])
    return {'message': my_hello_world.message}
