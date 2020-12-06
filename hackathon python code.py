#Assume the user is a underweight teenager
#high metabolism
#underweight
#numbers are just for representation
#more factors would be taken into account for the real product
#benchmark and specific numbers would be adjusted after consultation with medical experts

def main():

    protein=["steak","chicken","pork","duck"] #menu is sorted out into diff types of food 
    normalcarbo=["noodles"]
    supercarbo=["rice", "potato"]
    
    metabolism=110#this data will be directly transferred to the reciever through the chip
    weight=35#more factors besides weight and metabolism will be considered

    if (weight<40):#just a number for representation
               if metabolism > 100:
                   print("you should eat",supercarbo)
               else:
                   print("you should eat", normalcarbo)

    else:
              if metabolism>100:
                  print("you should eat", normalcarbo)
              else:
                  print("you should eat",protein)
        
                   
                   
    
    

    
   
main()
