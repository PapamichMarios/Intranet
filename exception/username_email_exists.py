class UsernameEmailExists(Exception):
    status_code = 409

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        self.success = False
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = self.status_code
        rv['message'] = self.message
        rv['success'] = False
        rv['type'] = "UsernameEmailExists"
        return rv
