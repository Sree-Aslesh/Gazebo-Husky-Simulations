import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.msg import ModelState

data_husky = ModelState()

def sub_callback(data):
    global data_husky
    data_husky.model_name = data.name[1]
    data_husky.pose = data.pose[1]
    data_husky.twist = data.twist[1]
    husky_pose_x = data_husky.pose.position.x
    husky_pose_y = data_husky.pose.position.y
    husky_twist_linear_x = data_husky.twist.linear.x
    husky_twist_linear_y = data_husky.twist.linear.y
    husky_twist_linear_z = data_husky.twist.linear.z
    husky_twist_angular_x = data_husky.twist.angular.x
    husky_twist_angular_y = data_husky.twist.angular.y
    husky_twist_angular_z = data_husky.twist.angular.z

def talker():
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
    sub = rospy.Subscriber('/gazebo/model_states', ModelStates , sub_callback)
    rospy.init_node('husky', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    pub_msg = ModelState()
    while not rospy.is_shutdown():
        if data_husky.pose:
            pub_msg.model_name = 'husky_sim'
            pub_msg.pose = data_husky.pose
            pub_msg.twist = data_husky.twist
            pub_msg.twist.linear.x = pub_msg.twist.linear.x + 0.11
        pub.publish(pub_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
