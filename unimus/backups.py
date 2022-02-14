class Backups(BaseException):
    def __init__(self, unimus_con):
        self.unimus_con = unimus_con

    def get_device_backup(self, id):
        return self.unimus_con.get('/devices/' + str(id) + '/backups/')

    def get_device_latest_backup(self, id):
        return self.unimus_con.get('/devices/' + str(id) + '/backups/latest')
    