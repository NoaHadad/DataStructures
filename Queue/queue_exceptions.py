class EmptyQueueException(Exception):

    def __init__(self, message='queue is empty'):
        super().__init__(message)


