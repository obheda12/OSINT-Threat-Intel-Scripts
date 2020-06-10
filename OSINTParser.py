#import necessary libraries
import pandas as pd
import os
import csv
import glob
import xlsxwriter

#path to parse to and read files from
path = "/Users/Omar/Documents/Scripts/OSINT Parser/"

#all files ending in .csv
all_files = glob.glob(os.path.join(path, "*.csv"))

#read data from each file
df_from_each_file = (pd.read_csv(f) for f in all_files)

#initialize writer
writer = pd.ExcelWriter('ParsedOSINT.xlsx', engine='xlsxwriter')

#write all files into excel
for f in all_files:
    df = pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.basename(f))



#save written files
writer.save()

print("Parsing Complete")






































#random number output
num = 5

for i in range(num):
    square = num*num
    print(square)
    num = num-1
