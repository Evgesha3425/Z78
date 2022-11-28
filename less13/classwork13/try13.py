distance = {
    "Minsk": [["Warsaw", 476], ["Kiev", 417]],
    "Warsaw": [["Minsk", 476], ["Kiev", 690]],
    "Kiev": [["Minsk", 417], ["Warsaw", 690]]
}

departure = "Minsk"
target = "Kiev"

def check_city(city1, city2):
    for c1 in distance:
        if c1 == city1:
            for c2 in distance[c1]:
                if c2[0] == city2:
                    return c2[1]


check_city("Minsk", "Kiev")