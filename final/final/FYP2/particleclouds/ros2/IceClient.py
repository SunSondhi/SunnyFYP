"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WORKING!! PARTICLE CLOUDS ICE CLIENT 

"""


import rclpy
from geometry_msgs.msg import PoseArray, Pose
import Ice
import sys
Ice.loadSlice("ParticleCloudModule.ice")
import ParticleCloudModule

class ParticleCloudClient(Ice.Application):       

    def run(self,args):
        self.communicator = Ice.initialize(['--Ice.Config=ice.config'])
        rclpy.init()
        self.node = rclpy.create_node('particle_cloud_subscriber')
        self.publisher = self.node.create_publisher(PoseArray, '/fromICE/particlecloud', 10)
        
        proxy = self.communicator.stringToProxy("ParticleData:default -p 10060")
        particle_cloud_prx = ParticleCloudModule.ParticleCloudPrx.checkedCast(proxy)
        particle_cloud_prx.receiveParticleCloudData = self.receive_particle_cloud_data

        if not particle_cloud_prx:
            raise RuntimeError("Invalid proxy")

        rclpy.spin(self.node)  

    def receive_particle_cloud_data(self, data):
        pose_array_msg = PoseArray()
        pose_array_msg.header.seq = data.header.seq
        pose_array_msg.header.stamp.sec = data.header.stamp.secs
        pose_array_msg.header.stamp.nanosec = data.header.stamp.nsecs
        pose_array_msg.header.frame_id = data.header.frameid

        for pose_data in data.poses:
            pose_msg = Pose()
            pose_msg.position.x = pose_data.positionx
            pose_msg.position.y = pose_data.positiony
            pose_msg.position.z = pose_data.positionz
            pose_msg.orientation.x = pose_data.orientationx
            pose_msg.orientation.y = pose_data.orientationy
            pose_msg.orientation.z = pose_data.orientationz
            pose_msg.orientation.w = pose_data.orientationw
            pose_array_msg.poses.append(pose_msg)

        self.publisher.publish(pose_array_msg)

    def shutdown(self):
        self.communicator.destroy()
        self.node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    subscriber = ParticleCloudClient()
    try:
        subscriber.main(sys.argv)
    except KeyboardInterrupt:
        subscriber.shutdown()
