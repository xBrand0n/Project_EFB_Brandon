#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Name: <Brandon>
#Group Name: <EFB_Group>
#Class: <PN2004K>
#Date: <10 Feb>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  time_list = ["2006-2016","2004-2014","2000-2010",]
  region_list = ["1","2","3","4","5","6","7","8"]
  region_name =""
  visitor = []
  countries = []
  total_visitor = []
  visitor_dict = {}
  

  print("Select time period eg.(year-year)","\n","2006-2016","\n","2004-2014","\n","2000-2010","\n",
  )
  while True:
    
   time_period = input("select a time period:")

   if not time_period in time_list :
     print("Error!")

   elif time_period in time_list:
     break

  if time_period == "2006-2016":
       a=338
       a=int(a)
       b=470
       b=int(b)
  elif time_period == "2004-2014":
       a=314
       a=int(a)
       b=446
       b=int(b)
  elif time_period == "2000-2010":
       a=266
       a=int(a)
       b=398
       b=int(b)


  print("Select a region:",
  "\n","(1)South East Asia(SEA)",
  "\n","(2)Asia  Pacific(AP)",
  "\n","(3)Europe(EU)",)
  

  while True:
    
   region = input("Enter a region. Enter 1 for SEA or 2 for AP etc: ")
   region = str(region)

   if not region in region_list:
     print("Error!")
     
   elif region in region_list:
     break

  if region == "1":
    c = 2
    c =int(c)
    d = 9
    d =int(d)
    region_name = "South-East Asia"

  elif region == "2":
    c = 9
    c =int(c)
    d = 14
    d =int(d)
    region_name = "Asia Pacific"

  elif region == "3":
    c = 20
    c =int(c)
    d = 31
    d =int(d)
   
    region_name = "Europe"
  
   
  
    
  df= df.iloc[a:b,c:d]
  country_idx=d-c
  df.columns[0:int(country_idx)]
  
  for country in df.columns[0:int(country_idx)]:
    countries.append(country)
    
    for visitors in df[country]:
      visitor.append(visitors)
  
  for i in range(0,len(visitor)):
    if visitor[i]==" na ":
      visitor[i]=0
    else:
      visitor[i]=int(visitor[i])
    
    

  number_of_visitors = len(visitor)
  counter = number_of_visitors/len(countries)

  Index1 = 0
  Index2= int(counter)

  for i in range(0,(len(countries))):
    total_visitor.append(sum(visitor[Index1:Index2]))
    Index1=Index1+(int(counter))
    Index2=Index2+(int(counter))

  visitor_dict = {  countries[i]: total_visitor[i] for i in range(len(countries))}

  sort_visitor_dict = sorted(visitor_dict.items(), key=lambda x: x[1], reverse=True)

  visitor_dict=dict(sort_visitor_dict)

  df = pd.DataFrame(list(visitor_dict.items()),columns = ['Country','Visitors'])

  print(region_name,"visitors that travelled to Singapore listed in a table below in descending order:","\n",df)
  
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()
#########################################################################
#Main Branch: End of Code
#########################################################################