#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["cats", "chickens", "cows", "llamas", "pigs", "sheep"]

def animals_in_farm(animal_list):
    global animals
    return [a for a in animal_list if a in animals]

NE_animals = animals_in_farm(farms[0]["agriculture"])
print(f'Animal in NE farm {NE_animals}')

farm_name = input("Choose a farm (NE Farm, W Farm, or SE Farm)>> ")

for farm in farms:
    if farm["name"] == farm_name:
        print(f'Plant and animals raised in {farm_name} are {farm["agriculture"]}')
        print(f'Animals raised in {farm_name} are {animals_in_farm(farm["agriculture"])}')
    

