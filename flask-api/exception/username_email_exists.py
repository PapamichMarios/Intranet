class UsernameEmailExists(Exception):
    code = 409

    def __init__(self, message, code=None, payload=None):
        super().__init__()
        self.message = message
        self.success = False
        if code is not None:
            self.code = code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = self.code
        rv['message'] = self.message
        rv['success'] = False
        rv['type'] = "UsernameEmailExistsException"
        return rv
