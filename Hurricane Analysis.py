# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah',
         'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September',
          'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005,
         2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
                       165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'],
                  ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B',
           '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B',
           '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
# changes the damages from strings to floats for numbers, preserves "Damages not recorded".
def convert_damages(damages_list):
    updated_damages = []
    conversion = {"M": 1000000, "B": 1000000000}
    for index in damages_list:
        for key, value in conversion.items():
            if index[-1] == key:
                float_value = float(index[:-1]) * value
                updated_damages.append(float_value)
        if index == "Damages not recorded":
            updated_damages.append(index)
    return updated_damages


# write your construct hurricane dictionary function here:
# creates a dictionary of hurricanes and all their info
def construct_dict(names, months, years, max_winds, areas, damages, deaths):
    hurricane_dictionary = {}
    for index in range(len(names)):
        hurricane_dictionary.update({names[index]: {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Winds": max_winds[index],
                                                    "Areas Affected": areas[index], "Damage": convert_damages(damages)[index], "Deaths": deaths[index]}})
    return hurricane_dictionary


# write your construct hurricane by year dictionary function here:

# constructs a new dictionary from all the previous lists from scratch
def construct_years_dict(names, months, years, max_winds, areas, damages, deaths):
    hurricane_years_dict = {}
    for index in range(len(years)):
        current_hurricane = names[index]
        current_year = years[index]
        if hurricane_years_dict.get(current_year, None) == None:
            hurricane_years_dict.update({current_year: [
                {"Name": current_hurricane, "Month": months[index], "Year": years[index], "Max Sustained Winds": max_winds[index], "Areas Affected": areas[index],
                 "Damages": convert_damages(damages)[index], "Deaths": deaths[index]}]})
        elif hurricane_years_dict.get(current_year, None) != None:
            for key, value in hurricane_years_dict.items():
                if key == current_year:
                    value.append(
                        {"Name": current_hurricane, "Month": months[index], "Year": years[index], "Max Sustained Winds": max_winds[index], "Areas Affected": areas[index],
                         "Damages": convert_damages(damages)[index], "Deaths": deaths[index]})
    return hurricane_years_dict


# converts the dictionary keys from the names of the hurricanes to the years of the hurricanes.
def convert_to_years(dictionary):
    years_dict = {}
    for hurricane, info in dictionary.items():
        for key, value in info.items():
            if key == "Year":
                current_year = value
                current_hurricane = hurricane
                if years_dict.get(current_year, None) == None:
                    years_dict.update({current_year: [info]})
                elif years_dict.get(current_year, None) != None:
                    for key, value in years_dict.items():
                        if key == current_year:
                            value.append(info)
    return years_dict


# write your count affected areas function here:

# use this function if you want to pass in a dictionary full of all the hurricane information and return a dictionary with a key: value pair of location:number of times it was hit by a hurricane.
def count_affected_areas(dictionary):
    count_list = []
    count_dictionary = {}
    for values in dictionary.values():
        for key, info in values.items():
            if key == "Areas Affected":
                for affected_areas in info:
                    count_list.append(affected_areas)
    for index in count_list:
        count = count_list.count(index)
        count_dictionary[index] = count
    return count_dictionary


# Use this function if you want to take a LIST of places and convert it to a dictionary with a key:value pair of location: number of times it had hurricanes
def areas_list_to_dict(list):
    affected_areas = []
    hurricane_dictionary = {}
    for nested_list in list:
        for location in nested_list:
            affected_areas.append(location)
    for area in affected_areas:
        count = affected_areas.count(area)
        hurricane_dictionary[area] = count
    return hurricane_dictionary


# Function to find the area(s) hit with the most hurricanes. prints a list (if multiple) and returns a dictionary or prints a name and returns a dictionary
def area_most_affected(dictionary):
    greatest_value = 0
    greatest_area = ""
    equal_values = {}
    for area, num_hurricanes in dictionary.items():
        if num_hurricanes > greatest_value:
            greatest_value = num_hurricanes
            greatest_area = area
        elif num_hurricanes == greatest_value:
            equal_values.update({greatest_area: num_hurricanes, area: num_hurricanes})
    if len(equal_values) > 0:
        max_dict_value = max(value for value in equal_values.values())
    else:
        max_dict_value = 0
    if max_dict_value == greatest_value:
        print("The following areas are all equally affected by hurricanes, with a total of {number} hurricanes each: {areas}".format(number=greatest_value,
                                                                                                                                     areas=[key for key in equal_values.keys()
                                                                                                                                            if equal_values.get(
                                                                                                                                             key) == greatest_value]))
        return {key: value for key, value in equal_values.items() if equal_values.get(key) == greatest_value}
    else:
        print("The area most affected is {greatest_area}, with {number} hurricanes.".format(greatest_area=greatest_area, number=greatest_value))
        return {greatest_area: greatest_value}

    # write your greatest number of deaths function here:


# creates a dictionary of names and deaths from a dictionary created from the construct_dict() function use this before passing in a dictionary on the most_deaths() function.
def death_dict(dictionary):
    death_count_list = []
    death_names_list = []
    death_dictionary = {}
    for values in dictionary.values():
        for key, death_toll in values.items():
            if key == "Deaths":
                death_count_list.append(death_toll)
        for key, name in values.items():
            if key == "Name":
                death_names_list.append(name)
    for index in range(len(death_names_list)):
        death_dictionary.update({death_names_list[index]: death_count_list[index]})
    return death_dictionary


# creates a name/death list from the list of names and the list of deaths. Use this if you don't already have a dictionary of hurricane information, then pass the result into most deaths.
def death_list_to_dict(names, deaths):
    death_dictionary = {}
    for index in range(len(names)):
        death_dictionary.update({names[index]: deaths[index]})
    return death_dictionary


# This requires a dictionary of just names and total deaths as key: value pairs. pass in the dictionary returned from death dict or death_list_to_dict function as the argument for this function
def most_deaths(death_dictionary):
    most_deaths = 0
    location_most_deaths = ""
    equal_values = {}
    for location, num_deaths in death_dictionary.items():
        if num_deaths > most_deaths:
            most_deaths = num_deaths
            location_most_deaths = location
        elif num_deaths == most_deaths:
            equal_values.update({location_most_deaths: num_deaths, location: num_deaths})
    if len(equal_values) > 0:
        max_dict_value = max(value for value in equal_values.values())
    else:
        max_dict_value = 0
    if max_dict_value == most_deaths:
        print("The following hurricanes had an equal number of deaths, with a total of {number} deaths each: {location}.".format(number=most_deaths,
                                                                                                                                 location=[key for key in equal_values.keys()
                                                                                                                                           if equal_values.get(
                                                                                                                                         key) == most_deaths]))
        return {key: value for key, value in equal_values.items() if equal_values.get(key) == most_deaths}
    else:
        print("The hurricane with the most deaths is {location}, with {number} deaths.".format(location=location_most_deaths, number=most_deaths))
        return {location_most_deaths: most_deaths}

    # write your catgeorize by mortality function here:


# This function takes a dictionary of names:deaths and returned a dictionary mortality scale. Pass in the dictionary returned from death_dict() or death_list_to_dict(), not the full dictionary from the construct_dict() function
def hurricane_mortality(dictionary):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane, deaths in dictionary.items():
        if mortality_scale[0] == deaths:
            hurricane_mortality[0].append(hurricane)
        elif mortality_scale[0] < deaths <= mortality_scale[1]:
            hurricane_mortality[1].append(hurricane)
        elif mortality_scale[1] < deaths <= mortality_scale[2]:
            hurricane_mortality[2].append(hurricane)
        elif mortality_scale[2] < deaths <= mortality_scale[3]:
            hurricane_mortality[3].append(hurricane)
        elif mortality_scale[3] < deaths <= mortality_scale[4]:
            hurricane_mortality[4].append(hurricane)
        else:
            hurricane_mortality[5].append(hurricane)
    return hurricane_mortality


# write your greatest damage function here:
# creates a dictionary of names and damages to pass into most_damage() function. takes the original dictionary as an argument
def damage_dict(dictionary):
    damage_value_list = []
    damage_names_list = []
    damage_dictionary = {}
    for values in dictionary.values():
        for key, damage in values.items():
            if key == "Damage":
                damage_value_list.append(damage)
        for key, name in values.items():
            if key == "Name":
                damage_names_list.append(name)
    for index in range(len(damage_names_list)):
        damage_dictionary.update({damage_names_list[index]: damage_value_list[index]})
    return damage_dictionary


# creates a dictionary of names:damages from the original lists of names and damages, pass the results into the most_damage() function
def damage_list_to_dict(names, damages):
    damage_dictionary = {}
    for index in range(len(names)):
        damage_dictionary.update({names[index]: convert_damages(damages)[index]})
    return damage_dictionary


# determines which hurricane caused the most damages
def most_damage(damage_dictionary):
    most_damage = 0
    location_most_damage = ""
    equal_values = {}
    for location, damage_total in damage_dictionary.items():
        if damage_total == "Damages not recorded":
            pass
        elif damage_total > most_damage:
            most_damage = damage_total
            location_most_damage = location
        elif damage_total == most_damage:
            equal_values.update({location_most_damage: damage_total, location: damage_total})
    if len(equal_values) > 0:
        max_dict_value = max(value for value in equal_values.values())
    else:
        max_dict_value = 0
    if most_damage == 0:
        print("No damages were recorded for any hurricanes.")
        return damage_dictionary
    elif max_dict_value == most_damage:
        print("The following hurricanes had an equal amount of damages, with a total of ${number} worth of damage each: {location}.".format(number=most_damage,
                                                                                                                                            location=[key for key in
                                                                                                                                                      equal_values.keys() if
                                                                                                                                                      equal_values.get(
                                                                                                                                                          key) == most_damage]))
        return {key: value for key, value in equal_values.items() if equal_values.get(key) == most_damage}
    else:
        print("The hurricane with the most damage is {location}, with ${number} worth of damage.".format(location=location_most_damage, number=most_damage))
        return {location_most_damage: most_damage}


# write your catgeorize by damage function here:
# creates a dictionary of damage rating:list of hurricane names
def damage_scale(dictionary):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000, "Damages not recorded": []}
    damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], "Damages not recorded": []}
    for hurricane, damage in dictionary.items():
        if damage == "Damages not recorded":
            damage_rating["Damages not recorded"].append(hurricane)
        elif damage_scale[0] == damage:
            damage_scale[0].append(damage)
        elif damage_scale[0] < damage <= damage_scale[1]:
            damage_rating[1].append(hurricane)
        elif damage_scale[1] < damage <= damage_scale[2]:
            damage_rating[2].append(hurricane)
        elif damage_scale[2] < damage <= damage_scale[3]:
            damage_rating[3].append(hurricane)
        elif damage_scale[3] < damage <= damage_scale[4]:
            damage_rating[4].append(hurricane)
        else:
            damage_rating[5].append(hurricane)
    return damage_rating


# Test data, smaller data size that is easier to work with and manipulated to test if functions work. Use this so as not to make changes to the actual data.
test_years = [2018, 2019, 2019, 2020, 2020, 2021]
test_names = ["Steve", "Mom", "Dad", "Dave", "Cole", "Graham"]
test_months = ["January", "February", "March", "April", "May", "June"]
test_max_winds = [150, 120, 155, 200, 100, 40]
test_areas_affected = [["Costco"], ["Work"], ["Panama", "Home", "Construction Site"], ["Downtown", "Downtown", "Panama"], ["Construction Site"],
                       ["Tool Trailer", "Tool Trailer"]]
test_damages = ["0.1M", "1B", "Damages not recorded", "10B", "50B", "100B"]
test_deaths = [0, 1, 100, 500, 1000, 1000000]

# function testing:

# hurricanes = construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# print(hurricanes)
# print(convert_damages(test_damages))
updated_damages = convert_damages(test_damages)
# print(updated_damages)
# convert_damages() works
steve = construct_dict(test_names, test_months, test_years, test_max_winds, test_areas_affected, test_damages, test_deaths)
# print(steve)
# construct_dict() function works
steve_years = convert_to_years(steve)
# print(steve_years)
# convert_to_years() works
steve_years_from_lists = construct_years_dict(test_names, test_months, test_years, test_max_winds, test_areas_affected, test_damages, test_deaths)
print(steve_years_from_lists)
# construct_years_dict() works
steve_affected_areas = count_affected_areas(steve)
# print(steve_affected_areas)
# count_affecetd_areas() works
steve_affected_areas_list = areas_list_to_dict(test_areas_affected)
# print(steve_affected_areas_list)
# areas_list_to_dict() function works
steve_area_most_affected = area_most_affected(steve_affected_areas)
# print(steve_area_most_affected)
print()
# area_most_affected() function works
steve_death_dict = death_dict(steve)
# print(steve_death_dict)
# death_dict() function works
steve_death_list_to_dict = death_list_to_dict(test_names, test_deaths)
# print(steve_death_list_to_dict)
# death_list_to_dict() function works
steve_most_deaths = most_deaths(steve_death_dict)
# print(steve_most_deaths)
print()
# most_deaths() function works
steve_mortality = hurricane_mortality(death_dict(steve))
# print(steve_mortality)
# hurricane_mortality() function works.
steve_damage = damage_dict(steve)
# print(steve_damage)
# damage_dict() function works
print()
steve_damage_list_to_dict = damage_list_to_dict(test_names, test_damages)
# print(steve_damage_list_to_dict)
# damage_list_to_dict() function works
steve_most_damage = most_damage(steve_damage)
# most_damage() function works
print()
steve_damage_scale = damage_scale(steve_damage)
# print(steve_damage_scale)
# damage_scale() function works
