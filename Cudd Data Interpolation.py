import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# import of job-data-30202.csv
import csv
with open('job-data-30202.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

# file definitions for deletion of rows
input_file = 'job-data-30202.csv'
output_file = 'updated-job-data-30202.csv'
weight_column = 'Weight'
depth_column = 'Depth'

# definitions of max, mins and start points
maxthreshold = 180000
minthreshold = -180000
start_depth = 0
modelmaxdepth = 23328

# read and filter the rows for the max and minimum thresholds
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    filtered_rows = [
        row for row in reader
        if minthreshold < float(row[weight_column]) < maxthreshold
        and float(row[depth_column]) >= start_depth
    ]

# write the filtered rows to a new CSV
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)


# setting values to relevant data from updated-job-data-30202.csv
df = pd.read_csv('updated-job-data-30202.csv')
a_data = df['Date Collected']
b_data = df['Weight']
c_data = df['Speed']
d_data = df['Depth']

# import of model.csv
import csv
with open('model.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

#setting values to relevant data from model.csv
df = pd.read_csv('model.csv')
e_data = df['Tubing Depth  (ft)']
f_data = df['Surface Weight RIH  (lbf)']


# plotting job-data-30202.csv with model.csv overlay
plt.scatter(b_data, d_data, label='Job Data', s = 0.1)
plt.plot(f_data, e_data, label='Model Data', c = 'red')
plt.axhline(y = modelmaxdepth, label='Max Model Depth', color='red', linestyle='--')

# inverts axis to max example image
plt.gca().invert_yaxis()

# sets labels for axis and legend
plt.title("Model vs. Data Visualization")
plt.xlabel('Weight')
plt.ylabel('Depth')
plt.legend(loc='upper right')
plt.show()


# plotting job-data-30202.csv for Speed
plt.scatter(c_data, d_data, label='Job Data', s = 0.1)
plt.axhline(y = modelmaxdepth, label='Max Model Depth', color='red', linestyle='--')

# inverts axis to max example image
plt.gca().invert_yaxis()

# sets labels for axis and legend, and plots the figures
plt.title("Model vs. Data Visualization")
plt.xlabel('Speed')
plt.ylabel('Depth')
plt.legend(loc='upper right')
plt.show()
