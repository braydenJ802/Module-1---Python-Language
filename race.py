import racing_animals
import time

#animals
animals_list = [cls.__name__ for cls in racing_animals.Animal.__subclasses__()] #get subclass names from parent class and append to a list

print(f"""All of the animals are getting ready for their big race! 
\nHere is the list: {animals_list}.""")
    
#['Cheetah', 'Antelope', 'Fox', 'Bunny', 'Cat', 'Dog', 'Turtle'] #animals sorted fastest to slowest, with regular speeds
#animals 
if __name__== "__main__":

    anim_objects = [racing_animals.Dog(), racing_animals.Cat(), racing_animals.Fox(), racing_animals.Turtle(), racing_animals.Bunny(), racing_animals.Antelope(), racing_animals.Cheetah()]
    
    animal_dict = {}
    for anim in anim_objects:
        animal_dict[anim.animal_type] = [anim.speed, anim.three_limbed] #create dict -> {"Aniaml name": "[Speed, three_limbed: True or False]"}
   
    #animals enter the race 
    sorted_animal_dict = sorted(animal_dict.items(), key=lambda x: x[1], reverse=True) #sort dict by speed, descending order
    position = 1
    threads = []
    for key, val in sorted_animal_dict:
        animal_dict[key] = val + [position] #add position values to dict
        
        #instantiate threads! 
        threads.append(racing_animals.AnimalRaceManager(position, key))

        position +=1


print("\n\nStarting ...")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!\n")
for n in threads:
    n.start()
for j in threads:
    j.join()


print(f"\nAnimal details - (Animal: \"speed\", \"three_limbed: true or false\", \"starting position in race\"):\n {animal_dict}")

