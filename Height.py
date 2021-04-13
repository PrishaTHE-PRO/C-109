import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import csv
import pandas as pd

df=pd.read_csv('data.csv')
height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_first_sd_start,height_first_sd_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_second_sd_start,height_second_sd_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_sd_start,height_third_sd_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)
weight_first_sd_start,weight_first_sd_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_sd_start,weight_second_sd_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_sd_start,weight_third_sd_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)

# fig=ff.create_distplot([dice_result],['Result'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
# fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
# fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
# fig.show()

height_list_of_data_within_1_sd=[result for result in height_list if result > height_first_sd_start and result < height_first_sd_end]
height_list_of_data_within_2_sd=[result for result in height_list if result > height_second_sd_start and result < height_second_sd_end]
height_list_of_data_within_3_sd=[result for result in height_list if result > height_third_sd_start and result < height_third_sd_end]
weight_list_of_data_within_1_sd=[result for result in weight_list if result > weight_first_sd_start and result < weight_first_sd_end]
weight_list_of_data_within_2_sd=[result for result in weight_list if result > weight_second_sd_start and result < weight_second_sd_end]
weight_list_of_data_within_3_sd=[result for result in weight_list if result > weight_third_sd_start and result < weight_third_sd_end]


print('mean,median,and mode of height is{},{},and{}respectivly'.format(height_mean,height_median,height_mode))
print('mean,median,and mode of weight is{},{},and{}respectivly'.format(weight_mean,weight_median,weight_mode))

print('{}% of data lies with in 1 standard deviation'.format(len(height_list_of_data_within_1_sd)*100.0/len(height_list)))
print('{}% of data lies with in 2 standard deviation'.format(len(height_list_of_data_within_2_sd)*100.0/len(height_list)))
print('{}% of data lies with in 3 standard deviation'.format(len(height_list_of_data_within_3_sd)*100.0/len(height_list)))
print('{}% of data lies with in 1 standard deviation'.format(len(weight_list_of_data_within_1_sd)*100.0/len(weight_list)))
print('{}% of data lies with in 2 standard deviation'.format(len(weight_list_of_data_within_2_sd)*100.0/len(weight_list)))
print('{}% of data lies with in 3 standard deviation'.format(len(weight_list_of_data_within_3_sd)*100.0/len(weight_list)))

