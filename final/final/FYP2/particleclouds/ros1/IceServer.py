"""
SUNNY SONDHI (210097072)

ASTON UNIVERSITY

2024

!!WORKING!! PARTICLE CLOUDS ICE SERVER 

"""

import rospy
from nav_msgs.msg import Odometry
import Ice
import sys

Ice.loadSlice("ParticleCloudModule.ice")
import ParticleCloudModule


class ParticleCloudServer:
    def __init__(self):
        self.communicator = Ice.initialize(sys.argv)
        adapter = self.communicator.createObjectAdapterWithEndpoints("ParticlesCloud", "default -p 10060")
        self.particle_cloud_impl = ParticleCloudI()
        adapter.add(self.particle_cloud_impl, self.communicator.stringToIdentity("ParticleData"))
        adapter.activate()

    def shutdown(self):
        print("Shutting down...")
        self.communicator.shutdown()

class ParticleCloudI(ParticleCloudModule.ParticleCloud):

    def particlecloud_callback(msg, particle_cloud_impl):
        ice_data = ParticleCloudModule.ParticleCloudData()
        ice_data.header.seq = msg.header.seq
        ice_data.header.stamp.secs = msg.header.stamp.secs
        ice_data.header.stamp.nsecs = msg.header.stamp.nsecs
        ice_data.header.frameid = msg.header.frame_id

        for pose in msg.poses:
            ice_pose = ParticleCloudModule.Pose()
            ice_pose.positionx = pose.position.x
            ice_pose.positiony = pose.position.y
            ice_pose.positionz = pose.position.z
            ice_pose.orientationx = pose.orientation.x
            ice_pose.orientationy = pose.orientation.y
            ice_pose.orientationz = pose.orientation.z
            ice_pose.orientationw = pose.orientation.w
            ice_data.poses.append(ice_pose)

        particle_cloud_impl.receiveParticleCloudData(ice_data)

    


if __name__ == '__main__':
    rospy.init_node('particlecloud_publisher')
    particle_cloud_server = ParticleCloudServer()

    def shutdown_hook():
        particle_cloud_server.shutdown()

    rospy.on_shutdown(shutdown_hook)

    rospy.Subscriber('/robot/particlecloud', Odometry, lambda msg: particlecloud_callback(msg, particle_cloud_server.particle_cloud_impl))
    rospy.spin()
