import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

def analysis(csv):
	fixed_df = pd.read_csv(csv)
	northing_array = fixed_df[[".UTM_northing"]].to_numpy()
	easting_array = fixed_df[[".UTM_easting"]].to_numpy()
	n=np.size(easting_array)
	altitude_array = fixed_df[[".Altitude"]].to_numpy()
	fixed_array = fixed_df[[".Quality"]].to_numpy()
	northing_array_rel = northing_array - northing_array[0]
	easting_array_rel = easting_array - easting_array[0]
	sb.set_theme(style="darkgrid")
	northing_array_rel = np.array(northing_array_rel).flatten()
	easting_array_rel = np.array(easting_array_rel).flatten()
	altitude_array = np.array(altitude_array).flatten()
	fixed_array = np.array(fixed_array).flatten()
	print("\n")
	print("               Analysis Data				")
	print("======================================================")
	mean_east = np.mean(easting_array_rel)
	print('Mean of all UTM East terms %f' % mean_east)
	mean_north = np.mean(northing_array_rel)
	print('Mean of all UTM North terms %f' % mean_north)
	stddev_north = np.std(northing_array_rel)
	print('Std dev of all UTM North terms %f' % stddev_north)
	utm_east_var = mean_east - easting_array_rel
	utm_north_var = mean_north - northing_array_rel
	mean_east = np.mean(easting_array_rel)
	print('Mean of all UTM East terms %f' % mean_east)
	stddev_east = np.std(easting_array_rel)
	print('Std dev of all UTM East terms %f' % stddev_east)
	sem_data = stddev_east / np.sqrt(n)
	print("Mean error is %f" % sem_data)
	rmse = np.linalg.norm(easting_array_rel) / np.sqrt(n)
	print("Root Mean Square error is %f" % rmse)
	print("======================================================")
	print("\n")
	alt_data = np.linspace(1,len(altitude_array), num=len(altitude_array))
	sb.scatterplot(data = fixed_df, x =alt_data, y = ".Altitude",hue=".Quality",palette="flare")
	plt.xlabel("Sample Data")
	plt.ylabel("Altitude (m)")
	plt.title("Altitude of Good Moving Data")
	plt.show()
if __name__=="__main__":

	csv=[r'/home/kevin32/catkin_ws/src/lab2/data/bad_static.csv',
	r'/home/kevin32/catkin_ws/src/lab2/data/good_static.csv',
	r'/home/kevin32/catkin_ws/src/lab2/data/bad_moving.csv',
	r'/home/kevin32/catkin_ws/src/lab2/data/good_moving.csv']
	
	for i in csv:
		analysis(i)
	 
