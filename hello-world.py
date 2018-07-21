def my_handler(event, context):
    message = f'Hello-World! Nice to meet you {event["first_name"]} {event["last_name"]}!'
    return {'message': message}
