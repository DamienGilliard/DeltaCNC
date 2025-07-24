"""
This is a dummy GCode executor for testing purposes.
It replaces a motor controller with a simple print statement.
"""
import time
import rclpy
from rclpy.node import Node
from delta_cnc_interface.msg import Position, ConfirmationMessage

class DummyGCodeExecuter(Node):

    def __init__(self):
        super().__init__('dummy_gcode_executer')
        self.subscription = self.create_subscription(
            Position,
            'gcode_position',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(ConfirmationMessage, 'gcode_position_confirmation_message', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received position: x={msg.pose.position.x}, y={msg.pose.position.y}, z={msg.pose.position.z}')
        time.sleep(1)  # Simulate processing time
        self.send_confirmation()

    def send_confirmation(self):
        msg = ConfirmationMessage()
        msg.data = "processed"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing confirmation: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    dummy_gcode_executer = DummyGCodeExecuter()

    rclpy.spin(dummy_gcode_executer)

    dummy_gcode_executer.destroy_node()
    rclpy.shutdown()