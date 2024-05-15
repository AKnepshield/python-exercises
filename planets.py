planet_list = ["Mercury", "Mars"]
print(planet_list)
planet_list.append("Jupiter")
print(planet_list)
planet_list.append("Saturn")
print(planet_list)
extended_list = ["Uranus", "Neptune"]
planet_list.extend(extended_list)
print(planet_list)
planet_list.insert(1, "Venus")
index_of_venus = planet_list.index("Venus")
planet_list.insert(index_of_venus + 1, "Earth")
print(planet_list)
planet_list.append("Pluto")
print(planet_list)
start_index = 0
end_index = 4

gas_planets = planet_list[end_index:]
planet_list = planet_list[start_index:end_index]

print("Rocky Planets: ", planet_list)
print("Gas Planets: ", gas_planets)
