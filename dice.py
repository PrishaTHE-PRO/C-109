import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 

dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

first_sd_start,first_sd_end=mean-std_deviation,mean+std_deviation
second_sd_start,second_sd_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_sd_start,third_sd_end=mean-(3*std_deviation),mean+(3*std_deviation)

fig=ff.create_distplot([dice_result],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
fig.show()

list_of_data_within_1_sd=[result for result in dice_result if result > first_sd_start and result < first_sd_end]
list_of_data_within_2_sd=[result for result in dice_result if result > second_sd_start and result < second_sd_end]
list_of_data_within_3_sd=[result for result in dice_result if result > third_sd_start and result < third_sd_end]


print('mean of this data is =>',mean)
print('standard deviation of this data is =>', std_deviation)
print('the median of the is data is =>', median)
print('the mode of the data is =>', mode)

print('{}% of data lies with in 1 standard deviation'.format(len(list_of_data_within_1_sd)*100.0/len(dice_result)))
print('{}% of data lies with in 2 standard deviation'.format(len(list_of_data_within_2_sd)*100.0/len(dice_result)))
print('{}% of data lies with in 3 standard deviation'.format(len(list_of_data_within_3_sd)*100.0/len(dice_result)))

