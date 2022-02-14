class Schedules(BaseException):
    def __init__(self, unimus_con):
        self.unimus_con = unimus_con

    def get_schedule(self, schedule_id):
        return self.unimus_con.get('/schedules/' + str(schedule_id))

    def get_all_sechdules(self):
        return self.unimus_con.get('/schedules')
