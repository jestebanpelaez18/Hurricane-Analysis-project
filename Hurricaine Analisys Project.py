#!/usr/bin/env python
# coding: utf-8

# # Information providing by Codeacademy

# ## Names of hurricanes

# In[2]:


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']


# ## Months of hurricanes

# In[3]:


months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']


# ## Years of hurricanes

# In[4]:


years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]


# ## Maximum sustained winds (mph) of hurricanes

# In[5]:


max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]


# ## Areas affected by each hurricane

# In[6]:


areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# ## Damages (USD($)) of hurricanes

# In[7]:


damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# ## Deaths for each hurricane

# In[8]:


deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# # Program

# ## Update recorded Damages

# In[9]:


conversion = {"M": 1000000,
              "B": 1000000000}


# In[10]:


damages_update = []
def update_data_damages(listado):
    for cost in listado:
        if 'Damages not recorded' in cost:
            damages_update.append(cost)
        elif "M" in cost:
            damages_update.append(float(cost.replace("M",""))*conversion["M"])
        elif "B" in cost:
            damages_update.append(float(cost.replace("B",""))*conversion["B"])
    return damages_update
            


# In[11]:


update_data_damages(damages)


# ## View the hurricanes dictionary per name

# In[31]:


def info_per_name(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
    hurricane_names = {}
    update_hurricane_names = {}
    for i in range(0,len(names)):
        update_hurricane_names[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
        hurricane_names.update(update_hurricane_names)
    return hurricane_names
hurricane_names = info_per_name(names,months,years,max_sustained_winds,areas_affected,damages_update,deaths)
hurricane_names


# ## Write your construct hurricane by year dictionary function here:

# In[57]:


def info_per_year(dic_per_name):
    hurricane_years = {}
    for years in dic_per_name.values():
        if years["Year"] not in hurricane_years:
            hurricane_years[years["Year"]] = [years]
        else:
            hurricane_years[years["Year"]].append(years)
    return hurricane_years
hurricane_years=info_per_year(hurricane_names)
hurricane_years


# ## Counting damaged areas

# In[40]:


def counting_damaged_ares(data):
    num_affect= {}
    for arealist in data.values():
        for area in arealist['Areas Affected']:
            if area not in num_affect:
                num_affect[area] = 1
            else:
                num_affect[area] += 1
    return num_affect
num_affect = counting_damaged_ares(hurricane_names)
num_affect


# ## Write your find most affected area function here:

# In[33]:


def most_affected_area(affected_dic):
    for place, times in affected_dic.items():
        if max(affected_dic.values()) == times:
            return place
most_affected_area(num_affect)


# ## Write your greatest number of deaths function here:

# In[34]:


def number_deaths(deaths_dic):
    list_of_deaths = []
    for hurricane in deaths_dic.values():
        list_of_deaths.append(hurricane["Deaths"])
        max_deaths = max(list_of_deaths)
        if max_deaths == hurricane["Deaths"]:
            name_hurricane = hurricane["Name"]
    return name_hurricane,max_deaths
number_deaths(hurricane_names)   


# ## Write your catgeorize by mortality function here:

# In[16]:


mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


# In[36]:


def mortality_ratings(mortality_dic):
    ratings_mortality = {}
    rating_0 = []
    rating_1 = []
    rating_2 = []
    rating_3 = []
    rating_4 = []
    rating_5 = []
    for mortality in mortality_dic.values():
        if mortality["Deaths"] == mortality_scale[0]: 
            rating_0.append((mortality))
        elif mortality["Deaths"] > mortality_scale[0] and mortality["Deaths"] <= mortality_scale[1]:
            rating_1.append((mortality))
        elif mortality["Deaths"] > mortality_scale[1] and mortality["Deaths"] <= mortality_scale[2]:
            rating_2.append((mortality))
        elif  mortality["Deaths"] > mortality_scale[2] and mortality["Deaths"] <= mortality_scale[3]:
            rating_3.append((mortality))
        elif  mortality["Deaths"] > mortality_scale[3] and mortality["Deaths"] <= mortality_scale[4]:
            rating_4.append((mortality))
        else:
            rating_5.append((mortality))
    ratings_mortality[0] = rating_0
    ratings_mortality[1] = rating_1
    ratings_mortality[2] = rating_2
    ratings_mortality[3] = rating_3
    ratings_mortality[4] = rating_4
    ratings_mortality[5] = rating_5
    return ratings_mortality
mortality_ratings(hurricane_names)


# ## Write your greatest damage function here:

# In[37]:


def number_damages(damages_dic):
    list_of_damages = []
    for damages in damages_dic.values():
        if damages["Damage"] != 'Damages not recorded' :
            list_of_damages.append(damages["Damage"])
            max_damages = max(list_of_damages)
            if max_damages == damages["Damage"]:
                name_hurricane_damages = damages["Name"]
    return name_hurricane_damages,max_damages
number_damages(hurricane_names)  


# ## Write your catgeorize by damage function here:

# In[19]:


damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


# In[38]:


def damages_ratings(new_damages_dic):
    ratings_damages = {}
    damages_rating_0 = []
    damages_rating_1 = []
    damages_rating_2 = []
    damages_rating_3 = []
    damages_rating_4 = []
    damages_rating_5 = []
    for new_damages in new_damages_dic.values():
        if new_damages["Damage"] == 'Damages not recorded' :
            damages_rating_0.append((new_damages))
        if new_damages["Damage"] != 'Damages not recorded' :   
            if new_damages["Damage"] >= damage_scale[0] and new_damages["Damage"] < damage_scale[1]:
                damages_rating_1.append((new_damages))
            elif new_damages["Damage"] >= damage_scale[1] and new_damages["Damage"] < damage_scale[2]:
                damages_rating_2.append((new_damages))
            elif  new_damages["Damage"] >= damage_scale[2] and new_damages["Damage"] < damage_scale[3]:
                damages_rating_3.append((new_damages))
            elif  new_damages["Damage"] >= damage_scale[3] and new_damages["Damage"] < damage_scale[4]:
                damages_rating_4.append((new_damages))
            else:
                damages_rating_5.append((new_damages))
    ratings_damages[0] = damages_rating_0
    ratings_damages[1] = damages_rating_1
    ratings_damages[2] = damages_rating_2
    ratings_damages[3] = damages_rating_3
    ratings_damages[4] = damages_rating_4
    ratings_damages[5] = damages_rating_5
    return ratings_damages
damages_ratings(hurricane_names)

