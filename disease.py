import health
list_of_reports = health.get_all_reports()
#print(list_of_reports)

#print(list_of_reports[0])

for row in list_of_reports:
    key = row ["disease"]
    #key1 = row ["year"]
    if key == "MEASLES":
        print(key,row["loc"], row["number"], row["population"], row["year"])

    
