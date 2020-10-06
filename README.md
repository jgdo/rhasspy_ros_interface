# rhasspy_ros_interface
ROS interface node to act as [Rhasspy](https://rhasspy.readthedocs.io/) intent handler.

Listens on port 1337 for JSON messages. Can be registered in Rhasspy as [remote HTTP server intent handler](https://rhasspy.readthedocs.io/en/latest/intent-handling/#remote-server). Upon receiving an intent from rhasspy, an intent message containing the slot values is published over ROS.

    rosrun rhasspy_ros_interface rhasspy_ros_node.py
