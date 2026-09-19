import rclpy
from rclpy.node import Node

import argparse
import sys
import os
import threading

from delta_cnc_interface.msg import Position, ConfirmationMessage

class Instruction:
    def __init__(self, line_of_command):
        for part in line_of_command.split():
            if part.startswith("("):
                self.type_of_instruction = "comment"
                break  # Ignore comments
            if part.startswith("T"):
                self.is_tool_change = True
                self.tool_number = int(part[1:])
                self.type_of_instruction = "tool_change"
                break
            elif part.startswith("F"):
                self.is_feedrate = True
                self.feedrate = float(part[1:])
                self.type_of_instruction = "feedrate"
                break
            elif part.startswith("G0") or part.startswith("G54") or part.startswith("G55") or part.startswith("G56"):
                self.is_coord_sys_command = True
                self.coord_sys_command = part[1:]
                self.type_of_instruction = "coord_sys_command"
                break
            elif part.startswith("S"):
                self.is_rotation_speed = True
                self.rotation_speed = float(part[1:])
                self.type_of_instruction = "rotation_speed"
                break
            elif part.startswith("X"):
                self.is_position = True
                self.x = float(part[1:])
                self.type_of_instruction = "position"
            elif part.startswith("Y"):
                self.is_position = True
                self.y = float(part[1:])
                self.type_of_instruction = "position"
            elif part.startswith("Z"):
                self.is_position = True
                self.z = float(part[1:])
                self.type_of_instruction = "position"
                break
            else:
                self.is_unknown_command = True
                self.type_of_instruction = "unknown"
    
    def __str__(self):
        return f"line of instruction of type:{self.type_of_instruction}"

class GCodeReader(Node):

    def __init__(self):
        super().__init__('gcode_reader')
        self.publisher_ = self.create_publisher(Position, 'gcode_position', 10)
        self.subscription = self.create_subscription(
            ConfirmationMessage,
            'gcode_position_confirmation_message',
            self.listener_callback,
            10)
        self.confirmation_event = threading.Event()
        self.subscription  # prevent unused variable warning
        self.tot_n_instructions = 0

    def listener_callback(self, msg):
        self.get_logger().info(f'Received confirmation: {msg.data}')
        if msg.data == "processed":
            self.confirmation_event.set()

    def read_gcode(self, file_path):
        with open(file_path, 'r') as file:
            gcode = file.read()
        return gcode

    def parse_gcode(self, gcode):
        for line in gcode.splitlines():
            instruction = Instruction(line)
            self.tot_n_instructions += 1
            if instruction.type_of_instruction == "position":
                self.publish_position(instruction)

    def publish_position(self, instruction):
        msg = Position()
        msg.pose.position.x = instruction.x if hasattr(instruction, 'x') else 0.0
        msg.pose.position.y = instruction.y if hasattr(instruction, 'y') else 0.0
        msg.pose.position.z = instruction.z if hasattr(instruction, 'z') else 0.0
        self.confirmation_event.clear()
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing position: x={msg.pose.position.x}, y={msg.pose.position.y}, z={msg.pose.position.z}')
        # Wait for confirmation before proceeding
        if not self.confirmation_event.wait(timeout=60):
            self.get_logger().warn('No confirmation received within timeout period.')

def main(args=None):
    rclpy.init(args=args)

    parser = argparse.ArgumentParser(description='GCode Reader')
    parser.add_argument('file_path', type=str, help='Path to the GCode file')
    args = parser.parse_args()

    gcode_reader = GCodeReader()
    
    gcode_reader = GCodeReader()
    gcode = gcode_reader.read_gcode(args.file_path)

    parse_thread = threading.Thread(target=gcode_reader.parse_gcode, args=(gcode,))
    parse_thread.start()

    rclpy.spin(gcode_reader)

    parse_thread.join()
    gcode_reader.destroy_node()
    rclpy.shutdown()