import pandas as kevpd
import seaborn as sb
import matplotlib.pyplot as kevplt
dataFrame = kevpd.read_csv(r'/home/kevin32/catkin_ws/src/lab2/data/good_static.csv')
kevplt.title("Stationary Data in Clear Environment(Good Data)")
sb.lineplot(data = dataFrame, x = ".UTM_easting", y = ".UTM_northing",hue=".Quality")
kevplt.xlabel("UTM-Easting (m)")
kevplt.ylabel("UTM-Northing (m)")
kevplt.show()

dataFrame2 = kevpd.read_csv(r'/home/kevin32/catkin_ws/src/lab2/data/bad_static.csv')
kevplt.title("Stationary Data in Obscure Environment(Bad Data)")
sb.scatterplot(data = dataFrame2, x = ".UTM_easting", y =".UTM_northing",hue=".Quality")
kevplt.xlabel("UTM-Easting (m)")
kevplt.ylabel("UTM-Northing (m)")
kevplt.show()

active_df = kevpd.read_csv(r'/home/kevin32/catkin_ws/src/lab2/data/good_moving.csv')
kevplt.title("Moving Data in Obscure Environment(Bad Data)")
sb.scatterplot(data = active_df, x = ".UTM_easting", y = ".UTM_northing",hue=".Quality")
kevplt.xlabel("UTM-Easting (m)")
kevplt.ylabel("UTM-Northing (m)")
kevplt.show()

active_df2 = kevpd.read_csv(r'/home/kevin32/catkin_ws/src/lab2/data/good_moving.csv')
kevplt.title("Moving Data in Obscure Environment(Bad Data)")
sb.scatterplot(data = active_df2, x = ".UTM_easting", y = ".UTM_northing",hue=".Quality")
kevplt.xlabel("UTM-Easting (m)")
kevplt.ylabel("UTM-Northing (m)")
kevplt.show()
