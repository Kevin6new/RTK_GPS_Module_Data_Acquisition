import rospy
import serial
import sys
import time
import utm
import datetime
from lab2.msg import rtk_gps

def rtk_driver(port_id):
        rtk_msg= rtk_gps()
        if line.startswith(b"$GNGGA"):
        	data = line.split(b',')
        	print(data)

        if len(data) >= 10:
            lat_val,long_val,alt=0.0
            quality=0
            lat_val= float(lat_val[0:2]) + (float(lat_val[2:]) / 60)
            long_val = float(long_val[0:3]) + (float(long_val[3:]) / 60)
            lon_dir = lon_dir.decode("utf-8")
            lat_dir = lat_dir.decode("utf-8")
            alt = float(data(9))
      

            if lat_dir == "S":
                lat_val = -1 * lat_val

            if lon_dir == "W":
                long_val = -1 * long_val
                
            rtk_msg.header.stamp = rospy.Time.now()
            rtk_msg.header.seq += 1
            utm_data = utm.from_latlon(lat_val, long_val)
            rtk_msg.latitude = lat_val
            rtk_msg.longitude = long_val
            rtk_msg.altitude = alt
            rtk_msg.utm_easting = utm_data[0]
            rtk_msg.utm_northing = utm_data[1]
            rtk_msg.zone_num = utm_data[2]
            rtk_msg.zone_letter = utm_data[3]
            rtk_msg.quality = quality
            gps_pub.publish(rtk_msg)
        else:
            pass

if __name__ == '_main_':
     SENSOR_NAME = "RTK GPS"
     serial_port = rospy.get_param('~port','/dev/ttyACM0')
     serial_baud = rospy.get_param('~baudrate',57600)
     port = serial.Serial(serial_port, serial_baud, timeout=3.)
     gps_pub = rospy.Publisher('/gps', rtk_gps, queue_size=10)
     rospy.init_node('driver', anonymous=True)
     line = port.readline()
     while not rospy.is_shutdown():

        if line == '':
                rospy.logwarn("DEPTH: No data")

        else:
             rtk_driver(line)

     try:
        rtk_driver(sys.argv[1])
     except rospy.ROSInterruptException:
        port.close()
