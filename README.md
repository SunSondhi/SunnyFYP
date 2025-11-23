# Robot Receptionist — Sunny Sondhi
Aston University — 2023/24

A modular robot receptionist system built for the RB1 BASE robot and NVIDIA Jetson Orin. The system integrates ROS2-based navigation and control with ROS1 mapping/localization topics, voice command processing, and live visualization to guide guests around campus.

## Table of contents
- [Project overview](#project-overview)
- [Key features](#key-features)
- [Hardware & software](#hardware--software)
- [Architecture](#architecture)
- [Quick demo](#quick-demo)
- [Installation](#installation)
- [Usage](#usage)
- [Voice commands](#voice-commands)
- [Customization & extending](#customization--extending)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License & contact](#license--contact)

## Project overview
This project implements a receptionist robot that can:
- Accept spoken destination requests,
- Plan and follow safe paths on campus using ROS navigation stacks,
- Use existing ROS1 mapping/localization/laser data where required (via ROS1–ROS2 bridging),
- Provide visual feedback through RViz,
- Be deployed on an embedded Jetson-class compute node (NVIDIA Jetson Orin) attached to the RB1 BASE.

The repository contains code and configuration for the robot control stack, voice processing pipeline (speech-to-text), and integration with perception/localization pipelines.

## Key features
- Voice-activated navigation with natural command parsing
- ROS2-native control and node architecture
- Compatibility with ROS1 topics for legacy sensors/mappers
- RViz visualization for realtime state and map debugging
- Modular design so features (SLAM, obstacle avoidance, TTS, etc.) can be added independently

## Hardware & software
Recommended:
- Robot platform: RB1 BASE (university hardware)
- Compute: NVIDIA Jetson Orin (or equivalent Jetson device)
- OS: Ubuntu 22.04 LTS (or distro supported by your ROS version)
- ROS 2: Humble (or later) — adjust commands if you use a different ROS 2 distro
- (Optional) ROS 1: Noetic/Melodic — if you rely on ROS1 topics (requires ros1_bridge)
- Dependencies: colcon, Python 3.10+, speech-to-text runtime (e.g., Vosk, deepspeech, cloud STT), standard robotics libraries (navigation2, tf2, rclpy/rclcpp)

Note: Specific package versions and additional dependencies are defined in package manifests (package.xml) in the repository — install rosdep to resolve them automatically.

## Architecture
High-level components:
- Voice interface: Captures audio, does speech-to-text, and extracts navigation intents (e.g., "take me to the library").
- Command interpreter: Maps intent to named locations or coordinates and requests a navigation goal.
- Navigation stack: Global planner + local controller (ROS2 navigation2) that sends velocity commands to RB1 BASE.
- Perception & localization: Uses laser and localization topics (optionally coming from ROS1 nodes) for mapping and obstacle detection.
- Visualization: RViz for monitoring robot position, planned paths, sensor feeds, and active goals.

## Quick demo
1. Power on RB1 BASE and Jetson Orin; ensure network connectivity between them (ROS domain / IP setup).
2. On the Jetson (or machine running ROS2):
   - Source ROS 2 and workspace: `source /opt/ros/humble/setup.bash && source ~/ros2_ws/install/setup.bash`
   - Launch main stack (example): `ros2 launch robot_receptionist bringup.launch.py`
3. Use the voice interface or RViz to instruct the robot to go to a named location.
4. Monitor the robot's progress in RViz and on the console logs.

(The actual launch file names and node names vary by repository layout — replace the example with the real launch names in your repo.)

## Installation
1. Clone the repository:
   git clone https://github.com/SunSondhi/SunnyFYP.git
   cd SunnyFYP

2. Create and build a ROS 2 workspace (example for a catkin/colcon style workspace):
   ```
   # Ensure ROS2 environment is sourced first:
   source /opt/ros/humble/setup.bash

   # Create workspace (if not already in one)
   mkdir -p ~/ros2_ws/src
   cp -r <repo-packages> ~/ros2_ws/src/

   cd ~/ros2_ws
   rosdep install --from-paths src --ignore-src -r -y
   colcon build --symlink-install
   source install/setup.bash
   ```

3. Install speech-to-text backend and any hardware drivers required for RB1 BASE:
   - Example (Vosk): `pip install vosk`
   - GPU acceleration on Jetson: install CUDA / JetPack and follow speech library instructions.

4. If your setup uses ROS1 topics, install and configure ros1_bridge and source both ROS1 and ROS2 environments where needed.

## Usage examples
- Launch everything:
  `ros2 launch robot_receptionist bringup.launch.py`
- Send a navigation goal from command line:
  `ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{pose: {header: {frame_id: 'map'}, pose: {position: {x: 1.0, y: 2.0, z: 0.0}, orientation: {w: 1.0}}}}"`
- Start voice node (example):
  `ros2 run receptionist_voice voice_node --model /path/to/stt-model`

Replace node/launch names with actual names from this repository.

## Voice commands
Suggested command patterns the system recognizes:
- "Take me to [location name]" — go to a named waypoint.
- "Where is the [location]?" — provide directions or TTS feedback.
- "Stop" / "Cancel" — cancel current navigation goal and stop the robot.

You can add new named waypoints or synonyms in the waypoint config file (e.g., config/waypoints.yaml).

## Customization & extending
- Add new waypoints: update the waypoints config and reload the navigation params.
- Swap STT engine: replace the speech-to-text node with cloud or local engine; update launch files.
- Add behaviour: implement new ROS2 lifecycle nodes for greeting, question answering, or face recognition.

## Troubleshooting
- Robot not moving: check motor driver nodes and that cmd_vel topics are being published to the RB1 base.
- Localization drift: ensure correct TF frames are published and that the map is aligned with odometry.
- Voice not recognized: confirm microphone permissions, sampling rate, and correct STT model path.
- ROS1 topics missing: verify ros1_bridge is running and ROS1 nodes are reachable on network.

Enable debug logs:
`ros2 run <node_package> <node_executable> --ros-args --log-level debug`

## Contributing
Contributions welcome! To propose fixes or features:
1. Fork the repo and create a feature branch.
2. Add tests or a short demo showing the change.
3. Open a pull request with a clear description and motivation.

If you'd like, I can help open a pull request that updates README.md with this content.

## License
Specify a license (e.g., MIT). Add a LICENSE file to the repo to make the project open-source.

## Acknowledgements
- Aston University — project supervision and robot hardware
- ROS community — navigation2, rviz, ros1_bridge libraries
- Speech-to-text projects (Vosk, DeepSpeech, etc.) for voice components

---

If you want, I can:
- Replace the current README.md in the repository with this improved version (I can push it for you), or
- Tailor the README to use exact launch/file names and scripts from your repo — share the package/launch names or allow me to inspect the repository and I'll update the README to include precise commands and examples.
