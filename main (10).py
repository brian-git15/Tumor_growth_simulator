import random 
import math
#Variables
Month = 0
tumor_size = 50 #in percentage 
chemo_rate = 1
chemo_rate = (random.randint(2,3))/1000
print(chemo_rate)
surgery_chance = 50
therepy_increase = 0
fact = 0
nextMonth = "yes"
#Intro
print("Welcome to ___Name___, an immersive journey into the world of ")
print("Tumors In this simulation, you'll have the unique opportunity to  learn and more about how tumors work and how to deal with one.") 
print("\nLets Begin!!!\n")
print("===============================================================================")
print("Quick disclaimer before we start, this simulation is heavily generalized and ")
print("may be inaccurate. The tumor in this simulaton starts at 50%, which is why")
print("chemotherepy is used instead of earlier streatment methods")
print("===============================================================================")
#Facts
def facts(fact):
  if fact == 1:
    print("FUN FACT: ")
    print("Almost at least one third of all deaths related to cancer could be prevented through routine screening, and early detection and treatment of tumors.")
  elif fact == 2:
    print("FUN FACT: ")
    print("Make sure to look for signs of tumor growth because treating it early is the best way to prevent cancer")
  elif fact == 3:
    print("FUN FACT: ")
    print("Chemo is effective way to fight against a growing tumor but is not 100% effective cure and other methods may be needed")
  elif fact == 4:
    print("FUN FACT: ")
    print("Smaller tumors are called Benign tumors")
  elif fact == 5:
    print("FUN FACT: ")
    print("very large tumors are called malignant tumors")
  elif fact == 6:
    print("FUN FACT: ")
    print("There are more skin cancer cases due to indoor tanning than lung cancer cases due to smoking")
  elif fact == 7:
    print("FUN FACT: ")
    print("More than 40% of cancer-related death could be preventable as they are linked to modifiable risk factors such as smoking, alcohol use, poor diet and physical inactivity")
  elif fact == 8:
    print("FUN FACT: Radiation therepy is used to eliminate tumors in the early stages, or late stages. radiation therepy can be used before surgery or with chemotherepy")
  elif fact == 9:
    print("FUN FACT: ")
    print("It is estimated that 55,000 Canadians are surviving with a brain tumour")
  elif fact == 10:
    print("FUN FACT: ")
    print("There are over 120 different types of brain tumours, making effective treatment very complicated.")
  return None
  
#Tumor Size
def tumor_size_calc(tumor_size,rate):
#tumor_size = inital tumor at the time(the percent) in reference in cubic centeimeter
#time_months = time in mounths
#rate = rate of increase (5%) --> 0.05
  tumor_size = tumor_size * (rate)
  return tumor_size

#option 1 loop 
while((tumor_size > 20 or tumor_size < 100) and nextMonth == "yes"):
 #note: insert more facts
  if tumor_size < 20: 
    print("Since the tumor has now become small enough, we can use other treatment methods.")
  
  if tumor_size < 10:
    facts(4)
  
  if tumor_size > 80:
    facts(5)
  
  if tumor_size > 100:
    print("GAME OVER!!!!💀💀💀💀")
    print("\nunfortunatly, you let the tumor is grow too large")
    break
  
  #generating which fact
  fact = (random.randint(1,20))
  tumor_string1 = ("The tumor is currently at: " , (tumor_size/5) , "cm^3, ")
  tumor_string2 = (format(tumor_size,".2f")) , "% of it's lethal size"
  print(tumor_string1 , tumor_string2)
  print("You have three options: \n\t a) take commercial drugs")
  print("\t b) start chemotherepy \n\t c) do nothing")
  choice = input().lower()
  if choice == "a" or choice == "c":
    tumor_size = tumor_size_calc(tumor_size, 1.05)
  if choice == "b":
    chemo_rate += 0.02
    tumor_size = tumor_size_calc(tumor_size,(1.05-chemo_rate))
  else:
    print("Not a valid answer.")
  print("would you like to move on to the next Month?(yes or no: ")
  print(facts(random.randint(1,10)))
  nextMonth = input()



while (tumor_size < 20 and tumor_size > 1):
  print("You are now able to use different treatment methods.")
  choice = input("your options are:\n\t a) surgery \n\t b) radiation therepy").lower()
  if (choice == "a"):
    surgery_chance = random.randint(0,100) + therepy_increase
    if surgery_chance > 50:
      print("\ncongradulations, you have sucsessfully removed the tumor!")
      break
    elif surgery_chance < 50:
      print("Most often, radiation therepy can help boost surgery sucsess rates by further decreasing the tumor")
  if (choice == "b"):
    facts(8)
    therepy_increase = 30
  else: 
    print("not a valid option")