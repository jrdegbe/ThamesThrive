class ThamesThriveException(Exception):
    pass


class StorageException(ThamesThriveException):

    def __init__(self, *args, message=None, details=None):
        ThamesThriveException.__init__(self, *args)
        self.message = message
        self.details = details


class FieldTypeConflictException(ThamesThriveException):

    def __init__(self, *args, rows=None):
        ThamesThriveException.__init__(self, *args)
        if isinstance(rows, list):
            self.details = [row['index']['error']['reason'] for row in rows]
        elif isinstance(rows, str):
            self.details = rows
        else:
            self.details = "Unknown"

    def explain(self):
        if isinstance(self.details, str):
            return self.details
        return ",".join(self.details)


class ExpiredException(ThamesThriveException):
    pass


class UnauthorizedException(ThamesThriveException):
    pass


class WorkflowException(Exception):
    pass


class ConnectionException(ThamesThriveException):

    def __init__(self, *args, response=None):
        ThamesThriveException.__init__(self, *args)
        self.response = response


class LoginException(ThamesThriveException):
    pass


class EventValidationException(ThamesThriveException):
    pass


class DuplicatedRecordException(ThamesThriveException):
    pass
