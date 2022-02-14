class Health(BaseException):
    def __init__(self, unimus_con):
        self.unimus_con = unimus_con

    def get_health(self):
        return self.unimus_con.get('/health')

