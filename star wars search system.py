import requests, time, json
from apihelper import callStarwarsApi

print("Welcome to the Star Wars search engine")
time.sleep(0.5)
print("(films/characters/planets/species/starships/vehicles)")
selection = input("What do you want to search for? : ")

if selection.lower().strip() == "planets":
    search = input("Search a Star Wars planet: ")
    json_data = callStarwarsApi("planets", search)
    for planet in json_data["results"]:
        print("planet name: " + planet["name"])
        print("rotation period: " + planet["rotation_period"])
        print("orbital period: " + planet["orbital_period"])
        print("diameter: " + planet["diameter"])
        print("climate: " + planet["climate"])
        print("gravity: " + planet["gravity"])
        print("terrain: " + planet["terrain"])
        print("surface water: " + planet["surface_water"])
        print("population: " + planet["population"])
        # print("residents: " + planet["residents"])
        # print("films: " + planet["films"])
        print("created: " + planet["created"])
        print("edited: " + planet["edited"])
        print("------------------------------------------------------------------------------------------------------------------------------------")

elif selection.lower().strip() == "characters":
    search = input("Search a Star Wars character: ")
    json_data = callStarwarsApi("people", search)
    for person in json_data["results"]:
        print("character name: " + person["name"])
        print("height: " + person["height"])
        print("mass: " + person["mass"])
        print("hair color: " + person["hair_color"])
        print("skin color: " + person["skin_color"])
        print("eye color: " + person["eye_color"])
        print("birth year: " + person["birth_year"])
        print("gender: " + person["gender"])
        # print("homeworld: " + person["homeworld"])
        # print("films: " + person["films"])
        # print("species: " + person["species"])
        # print("vehicles: " + person["vehicles"])
        # print("starship: " + person["starship"])
        print("created: " + person["created"])
        print("edited: " + person["edited"])
        print("--------------------------------------------------------------------------------------------------------------------------------------")

elif selection.lower().strip() == "films":
    search = input("Search a Star Wars film: ")
    json_data = callStarwarsApi("films", search)
    for films in json_data["results"]:
        print("title: " + films["title"])
        # print("episode id: " + films["episode_id"])
        print("opening crawl: " + films["opening_crawl"])
        print("director: " + films["director"])
        print("producer: " + films["producer"])
        print("release date: " + films["release_date"])
        # print("characters: " + films["characters"])
        # print("planets: " + films["planets"])
        # print("starships: " + films["starships"])
        # print("vehicles: " + films["vehicles"])
        # print("species: " + films["species"])
        print("created: " + films["created"])
        print("edited: " + films["edited"])
        print("--------------------------------------------------------------------------------------------------------------------------------------")

elif selection.lower().strip() == "species":
    search = input("Search a Star Wars species: ")
    json_data = callStarwarsApi("species", search)
    for species in json_data["results"]:
        print("name: " + species["name"])
        print("classification: " + species["classification"])
        print("designation: " + species["designation"])
        print("average height: " + species["average_height"])
        print("skin colors: " + species["skin_colors"])
        print("hair colors: " + species["hair_colors"])
        print("eye colors: " + species["eye_colors"])
        print("average lifespan: " + species["average_lifespan"])
        # print("homeworld: " + species["homeworld"])
        print("language: " + species["language"])
        # print("people: " + species["people"])
        # print("films: " + species["films"])
        print("created: " + species["created"])
        print("edited: " + species["edited"])
        print("--------------------------------------------------------------------------------------------------------------------------------------")

elif selection.lower().strip() == "starships":
    search = input("Search a Star Wars starship: ")
    json_data = callStarwarsApi("starships", search)
    for starships in json_data["results"]:
        print("name: " + starships["name"])
        print("model: " + starships["model"])
        print("manufacturer: " + starships["manufacturer"])
        print("cost in credits: " + starships["cost_in_credits"])
        print("length: " + starships["length"])
        print("max atmosphering speed: " + starships["max_atmosphering_speed"])
        print("crew: " + starships["crew"])
        print("passengers: " + starships["passengers"])
        print("cargo capacity: " + starships["cargo_capacity"])
        print("consumables: " + starships["consumables"])
        print("hyperdrive rating: " + starships["hyperdrive_rating"])
        print("MGLT: " + starships["MGLT"])
        print("starship_class: " + starships["starship_class"])
        # print("pilots: " + starships["pilots"])
        # print("films: " + starships["films"])
        print("created: " + starships["created"])
        print("edited: " + starships["edited"])
        print("--------------------------------------------------------------------------------------------------------------------------------------")

elif selection.lower().strip() == "vehicles":
    search = input("Search a Star Wars vehicle: ")
    json_data = callStarwarsApi("vehicles", search)
    for vehicles in json_data["results"]:
        print("name: " + vehicles["name"])
        print("model: " + vehicles["model"])
        print("manufacturer: " + vehicles["manufacturer"])
        print("cost in credits: " + vehicles["cost_in_credits"])
        print("length: " + vehicles["length"])
        print("max atmosphering speed: " + vehicles["max_atmosphering_speed"])
        print("crew: " + vehicles["crew"])
        print("passengers: " + vehicles["passengers"])
        print("cargo capacity: " + vehicles["cargo_capacity"])
        print("consumables: " + vehicles["consumables"])
        print("vehicle class: " + vehicles["vehicle_class"])
        # print("pilots: " + vehicles["pilots"])
        # print("films: " + vehicles["films"])
        print("created: " + vehicles["created"])
        print("edited: " + vehicles["edited"])
        print("--------------------------------------------------------------------------------------------------------------------------------------")


else:
    print("Invalid selection")
