import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import Ice
import TFModule
import sys

class TransformSubscriber(Node):
    def __init__(self):
        super().__init__('transform_subscriber')
        self.tf_broadcaster = TransformBroadcaster(self)

    def receive_transform_data(self, data):
        transform_msg = TransformStamped()
        transform_msg.header.stamp = self.get_clock().now().to_msg()
        transform_msg.header.frame_id = data.frame_id
        transform_msg.child_frame_id = data.child_frame_id
        transform_msg.transform.translation.x = data.translation_x
        transform_msg.transform.translation.y = data.translation_y
        transform_msg.transform.translation.z = data.translation_z
        transform_msg.transform.rotation.x = data.rotation_x
        transform_msg.transform.rotation.y = data.rotation_y
        transform_msg.transform.rotation.z = data.rotation_z
        transform_msg.transform.rotation.w = data.rotation_w
        self.tf_broadcaster.sendTransform(transform_msg)

def main(args=None):
    rclpy.init(args=args)
    transform_subscriber = TransformSubscriber()

    try:
        # Initialize Ice communicator
        communicator = Ice.initialize(sys.argv)
        if not communicator:
            raise RuntimeError("Failed to initialize Ice communicator")

        base = communicator.stringToProxy("transform_publisher:default -h 127.0.0.1 -p 10040")  # Adjust endpoint as needed
        sender = TFModule.TransformSenderPrx.checkedCast(base)
        if not sender:
            raise RuntimeError("Invalid proxy")

        # Continuously receive Ice data
        while rclpy.ok():
            try:
                transform_data = sender.receiveTransformData()
                transform_subscriber.receive_transform_data(transform_data)
            except Ice.OperationNotExistException:
                # Handle exception if the receiveTransformData operation does not exist
                print("Operation receiveTransformData does not exist")
    except Exception as e:
        print("Error:", e)
        raise e  # Reraise the exception for further analysis
    finally:
        if communicator:
            try:
                communicator.destroy()
            except:
                pass

    rclpy.shutdown()

if __name__ == '__main__':
    main()
