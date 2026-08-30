
import requests
import matplotlib.pyplot as plt
import pandas as pd

while True:
# create a variable(c_name)
    c_name=input("enter country name:").lower().strip()
    
# program closed
    if c_name=="exit":
        print("program closed")
        break
    
# taking data from api
    url =f"https://disease.sh/v3/covid-19/countries/{c_name}"

    data= requests.get(url).json()

# ERROR HANDLING
    if "message" in data:
        print("invalid country name, try again\n")
        continue
    
# covert json data into table form
    df =pd.DataFrame([{'country': data['country'], 'cases': data['cases'],'deaths': data['deaths'], 
                   'recovered': data['recovered'],'today_cases': data['todayCases'], 'today_deaths':data['todayDeaths'],
                   'critical': data['critical'],'active':data['active']}])
    print(df)
    
# create graph using matplotlib
    print("visualization output")
    labels=['cases','deaths','recovered','today_cases', 'today_deaths', 'critical', 'active']

    values=[data['cases'],data['deaths'],data['recovered'],data['todayCases'],data['todayDeaths'],data['critical'],data['active']]

    plt.bar(labels,values )

    plt.title(f"COVID-19 Data Visualization  {data['country']}",color="red")

    plt.xlabel('TYPE', color='red')

    plt.ylabel('COUNT', color='purple')
    plt.show()


