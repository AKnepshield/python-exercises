planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")


planet_list.extend(["Uranus", "Neptune"])
planet_list.extend(["Uranus", "Neptune"])


planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")


planet_list.append("Pluto")

gassy_planets = [
    "Mercury",
    "Venus, Earth",
    "Mars",
    "Jupiter, Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
]
rocky_planets = gassy_planets.__getitem__(slice(4, 8))

del rocky_planets[2]

spacecraft = [
    ("Pioneer", "Jupiter"),
    ("Voyager", "Saturn"),
    ("Galileo", "Jupiter"),
    ("Voyager2", "Neptune"),
    ("Pioneer11", "Saturn"),
]

for planet in planet_list:
    visited_by = []

    for craft, visited_planet in spacecraft:
        if visited_planet == planet:
            visited_by.append(craft)

            print(f"{planet} was visited by {','.join(visited_by)}")
