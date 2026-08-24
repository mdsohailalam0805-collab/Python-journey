if n%2!=0:
        print("Weird")
        if n%2==0 and 2<=n<=5:
            print("Not Weird")
            if n%2==0 and 6<=n<=20:
                print("Weird")
                if n%2==0 and n>20:
                    print(" Not Weird")
                    
                    
                    


# df = pd.DataFrame([{
#     'country': data['country'],
#     'cases': data['cases'],
#     'today_cases': data['todayCases'],
#     'deaths': data['deaths'],
#     'today_deaths': data['todayDeaths'],
#     'recovered': data['recovered'],
#     'active': data['active'],
#     'critical': data['critical']
# }])



# plt.pie(values, labels=labels, autopct='%1.1f%%')
# plt.title(f"COVID Distribution in {data['country']}")
# plt.show()

