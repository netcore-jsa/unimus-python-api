class Devices(BaseException):
    def __init__(self, unimus_con):
        self.unimus_con = unimus_con

    def get_device_by_id(self, id):
        return self.unimus_con.get('/devices/' + str(id))

    def get_device_by_ip(self, ip):
        return self.unimus_con.get('/devices/findByAddress/' + ip)

    def get_device_by_description(self, description):
        return self.unimus_con.get('/devices/findByDescription/' + description)

    def get_all_devices(self):
        return self.unimus_con.get('/devices')

    def create_new_devices(self, address, description, scheduleid):
        required_fields = {"address": address, "description": description, "scheduleId": str(scheduleid)}
        return self.unimus_con.post('/devices/', required_fields)

    def delete_device(self, id):
        return self.unimus_con.delete('/devices/', id)