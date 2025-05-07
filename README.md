# **This is a recreation of figures as an exercise for Cudd Pressure Control.**

Data was given and a python code interpreting the data was to be written following the instruction in the README file within the OrigionalFiles.zip.

## Cudd Data Interpolation

Following the instructions of the README, I was tasked with taking a CSV file from a time-series field data collection. From the CSV, I was tasked with recreating the given figure while also editing the CSV file to exclude weight values greater than 180,000 and less than -180,000. Along with plotting these values, I was instructed to overlay a model data set to demonstrate the actualization of the model. 

Following these directions, the code Cudd Data Interpolation.py was created. The code operates by importing the CSV file and reading the contents. From there, file definitions were set for eliminations of data that falls outside of the weight range. Then, maxes, mins and start points were defined for the weight and depth. The code then reads the file, determines where the the values are outside of the limits and eleiminates the rows from the CSV and rewrites as updated-job-data-30202.csv. This file is then used to plot the figure. The file CuddWeightVsDepthPlot.png was produced from the code and saved to match. The overlay was included in the data as well as the dashed line for the max model depth as seen. The figure CuddSpeedVsDepthPlot.png was created as well to show the speed at increasing depth with a similar max depth line. 

## Cudd Data Interpolation Experimental

Lastly, the data was run exactly the same as the previous iteration, but was changed due to discrepancies in the code. The requirement was to eliminate any rows outside of the max weight, but the values do not exceed out of the limits. Therefore, the limits were reset to a max of 20,000 and -10,000 so illustrate the elimination of rows in the code and its effectiveness. The plots were then created in the same way and shown in CuddWeightVsDepthPlotExperimental.png and CuddSpeedVsDepthPlotExperimental.png. The figures illustrate the changes and deletion of the data in a more severe manner to show the effectiveness of the code.
