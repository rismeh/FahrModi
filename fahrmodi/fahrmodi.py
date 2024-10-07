import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
import time

class MarkerPublisher(Node):
    def __init__(self):
        super().__init__('marker_publisher')
        self.publisher = self.create_publisher(Marker, 'fahrmodi', 10)
        self.timer = self.create_timer(1.0, self.publish_marker)

    def publish_marker(self):
        marker_msg = Marker()
        marker_msg.header.frame_id = 'map'
        marker_msg.header.stamp = self.get_clock().now().to_msg()
        marker_msg.ns = 'text_markers'
        marker_msg.id = 63
        marker_msg.type = Marker.TEXT_VIEW_FACING
        marker_msg.action = Marker.ADD
        marker_msg.pose.position.x = 0.0
        marker_msg.pose.position.y = 0.0
        marker_msg.pose.position.z = 1.0
        marker_msg.pose.orientation.x = 0.0
        marker_msg.pose.orientation.y = 0.0
        marker_msg.pose.orientation.z = 0.0
        marker_msg.pose.orientation.w = 1.0
        marker_msg.scale.x = 0.2
        marker_msg.scale.y = 0.2
        marker_msg.scale.z = 0.2
        marker_msg.color.r = 1.0
        marker_msg.color.g = 1.0
        marker_msg.color.b = 0.0
        marker_msg.color.a = 1.0
        marker_msg.text = 'Jetracer modus'
        self.publisher.publish(marker_msg)
    
    def speed(self):
        if time > 10:
                    marker_msg.text = 'Jetracer modus'
        else:
                    marker_msg.text = 'NO modus'
        self.publisher.publish(marker_msg)

def main(args=None):
    rclpy.init(args=args)
    marker_publisher = MarkerPublisher()
    rclpy.spin(marker_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
