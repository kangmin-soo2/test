#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def publisher():
    # 노드 초기화: 이름은 'talker'로 지정
    rospy.init_node('talker', anonymous=True)
    
    # Publisher 설정: 'chatter' 토픽에 String 타입 메시지 전송
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # 1초에 1번씩 발행하도록 Rate 설정
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        # 메시지 생성
        hello_str = "hello world %s" % rospy.get_time()
        
        # 로그 출력
        rospy.loginfo("Publishing: %s", hello_str)
        
        # 실제 발행
        pub.publish(hello_str)
        
        # 설정된 주기에 맞춰 sleep
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

