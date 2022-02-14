class Tasks:
    def __init__(self, unimus_con):
        self.unimus_con = unimus_con

    def discover_device(self):
        return self.unimus_con.patch('/jobs/discovery')

    def discover_undiscovered_devices(self):
        return self.unimus_con.patch('jobs/discovery/undiscovered')
