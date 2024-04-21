#!/usr/bin/env python

import rospy
import tf2_ros
import Ice
import sys
import TFModule
import yaml

class TransformPublisherI(TFModule.TransformSender):
    def __init__(self):
        self.node_name = 'transform_publisher'
        rospy.init_node(self.node_name)
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

    def sendTransformData(self, data, current=None):
        for transform in self.tf_buffer.all_frames_as_yaml().split('\n---\n'):
            if not transform:
                continue
            transform_data = TFModule.TransformData()
            tf_data = yaml.load(transform)
            transform_data.frame_id = tf_data['frame_id']
            transform_data.child_frame_id = tf_data['child_frame_id']
            transform_data.translation_x = tf_data['transform']['translation']['x']
            transform_data.translation_y = tf_data['transform']['translation']['y']
            transform_data.translation_z = tf_data['transform']['translation']['z']
            transform_data.rotation_x = tf_data['transform']['rotation']['x']
            transform_data.rotation_y = tf_data['transform']['rotation']['y']
            transform_data.rotation_z = tf_data['transform']['rotation']['z']
            transform_data.rotation_w = tf_data['transform']['rotation']['w']
            self.send_transform(transform_data)

    def send_transform(self, transform_data):
        try:
            # Assuming the receiver is running on the client side
            base = self.communicator().stringToProxy("receiver:default -p 10040")
            receiver = TFModule.TransformReceiverPrx.checkedCast(base)
            if not receiver:
                raise RuntimeError("Invalid proxy")
            receiver.receiveTransformData(transform_data)
        except Ice.Exception as ex:
            print("Error sending transform data:", ex)

class Server(Ice.Application):
    def run(self, argv):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("MovementAdapter", "default -p 10040")
            sender = TransformPublisherI()
            adapter.add(sender, communicator.stringToIdentity("transform_publisher"))
            adapter.activate()
            print("Server started...")
            communicator.waitForShutdown()
        return 0

if __name__ == '__main__':
    transform_server = Server()
    sys.exit(transform_server.main(sys.argv))
