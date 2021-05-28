
# Youbot_description

Robot description in form of URDF files and meshes

```
robot name is: youbot
---------- Successfully Parsed XML ---------------
root Link: world has 1 child(ren)
    child(1):  base_footprint
        child(1):  base_link
            child(1):  arm_link_0
                child(1):  arm_link_1
                    child(1):  arm_link_2
                        child(1):  arm_link_3
                            child(1):  arm_link_4
                                child(1):  arm_link_5
                                    child(1):  pen
            child(2):  base_laser_front_link
            child(3):  caster_link_bl
                child(1):  wheel_link_bl
            child(4):  caster_link_br
                child(1):  wheel_link_br
            child(5):  caster_link_fl
                child(1):  wheel_link_fl
            child(6):  caster_link_fr
                child(1):  wheel_link_fr
            child(7):  plate_link

```

This Youbot robot is a modified version of the [Youbot](http://www.youbot-store.com/) sold by Kuka until 2016 as part of an internship with the University of [Ostfalia](https://www.ostfalia.de/cms/de/i/), Wolfenbüttel.


![](misc/youbot.png)


## Launch Rviz
```sh
cd youbot_description
colcon build
ros2 launch youbot_description rviz.launch.py
```

## Launch Gazebo
```sh
cd youbot_description
colcon build
export GAZEBO_MODEL_PATH=$PWD/sdf
ros2 launch youbot_description gazebo.py
```

## Examples
### Move joint (Gazebo)
```sh
# launch gazebo
ros2 topic pub /youbot/set_joint_trajectory trajectory_msgs/msg/JointTrajectory "{header: {frame_id: world}, joint_names: {youbot::arm_joint_2}, points: [{positions: {1.0}}]}"
```

