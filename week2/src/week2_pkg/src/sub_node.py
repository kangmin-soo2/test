#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    # 수신된 메시지 로그 출력
    rospy.loginfo("I heard: %s", data.data)

def subscriber():
    # 노드 초기화: 이름은 'listener'로 지정
    rospy.init_node('listener', anonymous=True)
    
    # Subscriber 설정: 'chatter' 토픽 구독, 메시지 수신 시 callback 함수 실행
    rospy.Subscriber('chatter', String, callback)
    
    # 콜백 함수를 계속해서 기다리도록 spin
    rospy.spin()

if __name__ == '__main__':
    subscriber()

