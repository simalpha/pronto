#!/usr/bin/python
import os,sys
import lcm
from lcm import LCM

from bot_core.pose_t import pose_t
from bot_core.rigid_transform_t import rigid_transform_t

def on_pose(channel, data):
  m = pose_t.decode(data)
  o = rigid_transform_t()
  o.utime = m.utime
  o.trans = m.pos
  o.quat = m.orientation
  lc.publish("VICON_TO_LOCAL",o.encode())

lc = lcm.LCM()
print "started"
lc.subscribe("POSE_VICON", on_pose)
while True:
  lc.handle()
