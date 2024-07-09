# Develop a smart home system using OOP principles that manages different types of smart devices. Each device type should have specific functionalities implemented as methods. 
# Use abstraction to define common properties and behaviors, while also ensuring specific device behaviors are handled appropriately.
# Components of the Exercise
# Abstract Smart Device Class
# This class should define the interface for all devices in the smart home system.
# It should include abstract methods like turn_on(), turn_off(), and status_report().
# Smart Light Class
# Inherits from the Smart Device class.
# Implements additional methods like dim() and change_color().
# Smart Thermostat Class
# Inherits from the Smart Device class.
# Implements methods to set temperature, and read current temperature.
# Smart Security Camera Class
# Inherits from the Smart Device class.
# Adds methods for starting and stopping recording, and motion detection.
# Smart Home Controller Class
# Manages a collection of devices.
# Can turn all devices on or off, and gather status reports from all devices.


from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_name, device_type):
        self.device_name = device_name
        self.device_type = device_type

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def status_report(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self, device_name, device_type, brightness, color):
        super().__init__(device_name, device_type)
        self.brightness = brightness
        self.color = color

    def turn_on(self):
        print(f'{self.device_name} is now on')

    def turn_off(self):
        print(f'{self.device_name} is now off')

    def status_report(self):
        print(f'{self.device_name} is a {self.device_type} with brightness level {self.brightness} and color {self.color}')

    def dim(self, brightness_level):
        self.brightness = brightness_level
        print(f'{self.device_name} brightness level is now {self.brightness}')

    def change_color(self, new_color):
        self.color = new_color
        print(f'{self.device_name} color is now {self.color}')

class SmartThermostat(SmartDevice):
    def __init__(self, device_name, device_type, current_temperature, set_temperature):
        super().__init__(device_name, device_type)
        self.current_temperature = current_temperature
        self.set_temperature = set_temperature

    def turn_on(self):
        print(f'{self.device_name} is now on')

    def turn_off(self):
        print(f'{self.device_name} is now off')

    def status_report(self):
        print(f'{self.device_name} is a {self.device_type} with current temperature {self.current_temperature} and set temperature {self.set_temperature}')

    def update_set_temperature(self, new_temperature):
        self.set_temperature = new_temperature
        print(f'{self.device_name} set temperature is now {self.set_temperature}')

    def read_current_temperature(self):
        print(f'{self.device_name} current temperature is {self.current_temperature}')

class SmartSecurityCamera(SmartDevice):
    def __init__(self, device_name, device_type, recording_status, motion_detection):
        super().__init__(device_name, device_type)
        self.recording_status = recording_status
        self.motion_detection = motion_detection

    def turn_on(self):
        print(f'{self.device_name} is now on')

    def turn_off(self):
        print(f'{self.device_name} is now off')

    def status_report(self):
        print(f'{self.device_name} is a {self.device_type} with recording status {self.recording_status} and motion detection {self.motion_detection}')

    def start_recording(self):
        self.recording_status = 'Recording'
        print(f'{self.device_name} is now recording')

    def stop_recording(self):
        self.recording_status = 'Not Recording'
        print(f'{self.device_name} is not recording')

    def motion_detected(self):
        self.motion_detection = 'Motion Detected'
        print(f'{self.device_name} detected motion')

class SmartHomeController:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_all_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()

    def status_report_all(self):
        for device in self.devices:
            device.status_report()



light = SmartLight('Living Room Light', 'Smart Light', '100%', 'White')
thermostat = SmartThermostat('Living Room Thermostat', 'Smart Thermostat', '70F', '72F')
camera = SmartSecurityCamera('Living Room Camera', 'Smart Security Camera', 'Not Recording', 'No Motion')

home = SmartHomeController()
home.add_device(light)
home.add_device(thermostat)
home.add_device(camera)

home.turn_all_on()
home.status_report_all()
home.turn_all_off()
home.status_report_all()
light.dim('50%')
light.change_color('Blue')
thermostat.update_set_temperature('75F')
thermostat.read_current_temperature()
camera.start_recording()
camera.motion_detected()
camera.stop_recording()
camera.motion_detected()


