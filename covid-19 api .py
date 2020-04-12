import requests, sys
from apihelper import callApi


print("Welcome to the covid-19 search system")


selected_country = input("enter a country: ")
selected_country_data = None


results = callApi("https://api.covid19api.com/summary")

for country_item in results["Countries"]:
    if country_item["Country"] == selected_country:
        selected_country_data = country_item
        print("new confirmed: " + str(selected_country_data["NewConfirmed"]))
        print("total confirmed: " + str(selected_country_data["TotalConfirmed"]))
        print("new deaths: " + str(selected_country_data["NewDeaths"]))
        print("total deaths: " + str(selected_country_data["TotalDeaths"]))
        print("new recovered: " + str(selected_country_data["NewRecovered"]))
        print("total recovered: " + str(selected_country_data["TotalRecovered"]))
        sys.exit(0)

else:
    print("invalid selection")
