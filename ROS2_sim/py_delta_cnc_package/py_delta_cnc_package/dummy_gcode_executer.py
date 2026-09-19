#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from delta_cnc_interface.msg import ConfirmationMessage
from ros_gz_interfaces.msg import Entity
from ros_gz_interfaces.srv import SetEntityPose

class DummyGCodeExecuter(Node):

    def __init__(self):
        super().__init__('dummy_gcode_executer')
        self.subscription = self.create_subscription(
            Pose,
            'gcode_position',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(ConfirmationMessage, 'gcode_position_confirmation_message', 10)
        self.set_pose_client = self.create_client(SetEntityPose, '/world/cnc_world/set_pose')
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received position: x={msg.position.x}, y={msg.position.y}, z={msg.position.z}')

        time.sleep(0.5)
        if not self.set_pose_client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error('/world/cnc_world/set_pose service not available')
            self.send_confirmation()
            return

        request = SetEntityPose.Request()
        request.entity.name = 'cnc_sphere'
        request.entity.type = Entity.MODEL
        request.pose = msg

        future = self.set_pose_client.call_async(request)
        future.add_done_callback(self.set_pose_done_callback)

    def set_pose_done_callback(self, future):
        try:
            response = future.result()
            if not response.success:
                self.get_logger().warn('set_pose service reported failure')
        except Exception as e:
            self.get_logger().error(f'set_pose service call failed: {e}')
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