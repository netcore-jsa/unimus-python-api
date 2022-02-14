import unimus.connection as connection
import unimus.heath as health
import unimus.schedules as schedules
import unimus.devices as devices
import unimus.backups as backups
import unimus.tasks as tasks


class Unimus:

    def __init__(self, host, **kwargs):
        self.connection = connection.UnimusConnection(host=host, **kwargs)
        self.health = health.Health(self.connection)
        self.schedules = schedules.Schedules(self.connection)
        self.devices = devices.Devices(self.connection)
        self.backups = backups.Backups(self.connection)
        self.tasks = tasks.Tasks(self.connection)
