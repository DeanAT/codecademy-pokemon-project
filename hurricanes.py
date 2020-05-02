# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#damages function here 

def damages_1(damages_list):
  new_damages =[]
  conversion = {"M": 1000000, "B": 1000000000}
  for i in damages_list:
    if 'B' in i:
      i = i.strip("B")
      i = float(i)
      i = i * conversion.get("B")
      new_damages.append(i)
    elif 'M' in i:
      i = i.strip("M")
      i = float(i)
      i = i * conversion.get("M")
      new_damages.append(i)
    else:
      new_damages.append(i)
  print(new_damages)
  return new_damages


# write your construct hurricane dictionary function here:

def hurricane(name, month, year, max_w, areas, damage, death):
  dict_hurricane = {}
  count = 0
  for i in name:
    dict_hurricane[i] = {}
  for i in dict_hurricane:
    dict_hurricane[i] = {"Name": name[count], "Month": month[count], "Year":year[count], "Sustained Wind": max_w[count], "Areas Affected": areas[count], "Damages": damage[count], "Deaths": death[count]}
    count += 1
  print(dict_hurricane)
  return dict_hurricane

# write your construct hurricane by year dictionary function here:

def hurricane_by_year(dictionary):
  years_dict = {}
  for i in dictionary.values():
      print(i)
      year = i.get("Year")
      name = i.get("Name")
      month = i.get("Month")
      year = i.get("Year")
      max_w = i.get("Max Sustained Wind")
      area_a = i.get("Areas Affected")
      damage = i.get("Damage")
      deaths = i.get("Deaths")
      years_dict.update({year: [name, month, year, max_w, area_a, damage, deaths]})
  print(years_dict)
  return years_dict


# write your count affected areas function here:

def count_areas_affected(dictl):
  total_areas ={}
  number = []
  areas = []
  areas1 =[]
  num = 0
  for i in dictl.values():
    areas.append(i.get("Areas Affected"))
  for a in areas:
    for x in a:
      areas1.append(x)
  for c in areas1:
    num = areas1.count(c)
    total_areas[c] = num
  print(total_areas)
  return total_areas
  

# write your find most affected area function here:

def most_affected_area(areas):
  max_area ={}
  for i,x in areas.items():
    max_area[x] = i
  maxnum = max(max_area.keys())
  maxarea = max_area[maxnum]
  print("The area most affected is {mxa}, with {mxn} hurricanes.".format(mxa=maxarea, mxn=maxnum))
  return maxnum, maxarea


# write your greatest number of deaths function here:

def max_deaths(names, deaths):
  hurricane_deaths = {keys:values for keys,values in zip(deaths, names)}
  maxdeaths = max(hurricane_deaths.keys())
  maxdeathhurricane = hurricane_deaths[maxdeaths]
  print("The dealiest hurricane is {} with {} dead.".format(maxdeathhurricane, maxdeaths))
  return maxdeathhurricane, maxdeaths,hurricane_deaths

# write your catgeorize by mortality function here:

def mortality(dictionary):
  mortality_scale = {0: 0, 1: 100, 2:500, 3:1000, 4:10000}
  count = 0
  mortality_dictionary = {}
  for i in mortality_scale.keys():
    mortality_dictionary.update({i:0})
  for i in dictionary.values():
    death = i.get("Deaths")
    if death == mortality_scale.get(0):
      mortality_dictionary[0] +=1
      print(mortality_dictionary)
    elif death  <= mortality_scale.get(1):
      mortality_dictionary[1] +=1
    elif death <= mortality_scale.get(2):
      mortality_dictionary[2] +=1
    elif death <= mortality_scale.get(3):
      mortality_dictionary[3] += 1
    elif death <= mortality_scale.get(4):
      mortality_dictionary[4] += 1
    else:
      mortality_dictionary.update({5: 0})
      mortality_dictionary[5] += 1 
  print(mortality_dictionary) 
  return mortality_dictionary


# write your greatest damage function here

def most_damage(dictionary):
    newD = {}
    for i in dictionary.values():
      n = i.get("Name")
      d = i.get("Damages")
      if 'B' in d:
        d = d.strip('.')
        d = d.strip("B")
        d = float(d)
        d = d * 1000000000
        d = int(d)
        newD[d] = n
      elif 'M' in d:
        d = d.strip('.')
        d = d.strip("M")
        d = float(d)
        d = d * 1000000
        d = int(d)
        newD[d] = n
      else:
        d = 0
        newD[d] = n
    maxDamage = max(newD.keys())
    maxName = newD[maxDamage]
    print("The most $ damage caused by a hurricane is {m} from hurricane {h}.".format(m=maxDamage, h=maxName))
    return maxName, maxDamage

#function for how much damage caused   

def damage_scale(dictionary):
  damage_scale = {0 : 0, 1: 100000000, 2: 1000000000, 3:10000000000, 4: 50000000000}
  scale_total = {}
  for s in damage_scale.keys():
    scale_total[s] = 0
  newlist = []
  damage_raw = []
  for i in dictionary.values():
    damage_raw.append(i.get("Damages"))
  for x in damage_raw:
    x.strip('.')
    if x =="damages not recorded":
      continue
    elif 'M' in x:
      x = x.replace('M', ' ')
      x = float(x)
      x = x * 1000000
      x = float(x)
      newlist.append(x)
    elif 'B' in x:
      x = x.replace('B', ' ')
      x = float(x)
      x = x * 1000000000
      x = int(x)
      newlist.append(x)
  for i in newlist:
    if i == damage_scale[0]:
      scale_total[0] += 1
    elif i <= damage_scale[1]:
      scale_total[1] += 1
    elif i <= damage_scale[2]:
      scale_total[2] += 1
    elif i <= damage_scale[3]:
      scale_total[3] += 1   
    elif i <= damage_scale[4]:
      scale_total[4] += 1
    else:
      scale_total[5] = 0
      scale_total[5] += 1
  print(scale_total)
  return scale_total




damages1 = damages_1(damages)
print("\n")

hurricane_dictionary = hurricane(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
print("\n")

years = hurricane_by_year(hurricane_dictionary)
print("\n")

most_affected = count_areas_affected(hurricane_dictionary)
print("\n")

area_most_affected = most_affected_area(most_affected)
print("\n")

maximum_death = max_deaths(names, deaths)
print("\n")

mortality_rate = mortality(hurricane_dictionary)
print("\n")

most_damage_hurri = most_damage(hurricane_dictionary)
print("\n")

damage_scale1 = damage_scale(hurricane_dictionary)
