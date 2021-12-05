travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited,times_visited,cities_visited):
    new_dictionary={}
    new_dictionary["country"]= country_visited
    new_dictionary["visits"]= times_visited
    new_dictionary["cities"]=cities_visited
    
    travel_log.append() =new_dictionary

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



