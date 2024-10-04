import pydobot
import math
import struct

from pydobot.message import Message

PORT_GP1 = 0x00
PORT_GP2 = 0x01
PORT_GP4 = 0x02
PORT_GP5 = 0x03

class Dobot(pydobot.Dobot):
    def conveyor_belt_distance(self, speed_mm_per_sec, distance_mm, direction=1, interface=0):
        if speed_mm_per_sec > 100:
            raise pydobot.dobot.DobotException("Speed must be <= 100 mm/s")

        MM_PER_REV = 34 * math.pi  # Seems to actually be closer to 36mm when measured but 34 works better
        STEP_ANGLE_DEG = 1.8
        STEPS_PER_REV = 360.0 / STEP_ANGLE_DEG * 10.0 * 16.0 / 2.0  # Spec sheet says that it can do 1.8deg increments, no idea what the 10 * 16 / 2 fudge factor is....
        distance_steps = distance_mm / MM_PER_REV * STEPS_PER_REV
        speed_steps_per_sec = speed_mm_per_sec / MM_PER_REV * STEPS_PER_REV * direction
        return self._extract_cmd_index(self._set_stepper_motor_distance(int(speed_steps_per_sec), int(distance_steps), interface))

    def set_color(self, enable=True, port=PORT_GP2, version=0x1):
        msg = Message()
        msg.id = 137
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray([int(enable)]))
        msg.params.extend(bytearray([port]))
        msg.params.extend(bytearray([version]))  # Version1=0, Version2=1
        return self._extract_cmd_index(self._send_command(msg))

    def get_color(self, port=PORT_GP2, version=0x1):
        msg = Message()
        msg.id = 137
        msg.ctrl = 0x00
        msg.params = bytearray([])
        msg.params.extend(bytearray([port]))
        msg.params.extend(bytearray([0x01]))
        msg.params.extend(bytearray([version]))  # Version1=0, Version2=1
        response = self._send_command(msg)
        print(response)
        r = struct.unpack_from('?', response.params, 0)[0]
        g = struct.unpack_from('?', response.params, 1)[0]
        b = struct.unpack_from('?', response.params, 2)[0]
        return [r, g, b]