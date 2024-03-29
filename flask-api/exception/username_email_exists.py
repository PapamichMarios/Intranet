class UsernameEmailExists(Exception):
    code = 409

    def __init__(self, message, code=None, payload=None, type=None):
        super().__init__()
        self.type = type
        self.message = message
        self.success = False
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type
        else:
            self.type = "UsernameEmailExistsException"
        self.payload = payload


    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = self.code
        rv['message'] = self.message
        rv['success'] = False
        rv['type'] = self.type
        return rv
