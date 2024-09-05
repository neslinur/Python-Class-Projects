import random
#we are writing the variables
for i in range(100):
    gen = ['F','M']
    sex = random.choice(gen)
    
    age = random.randrange(20,79)
    
    cho = random.randrange(159,281)
    
    yn = ['Y','N']
    smo = random.choice(yn)
    
    hdl = random.randrange(39,61)
    
    sbp = random.randrange(119,161)
    
    med = random.choice(yn)
    
    #starting on the if statements with the two biggest categories (sex)
    out = 0
    points = 0
    
    if sex == "F":
      #we go into age here - nesli
      if age >= 20 and age <= 39:
        #specific age points
        if age >= 20 and age <= 34:
          points -= 7
        elif age >= 35 and age <= 39:
          points -= 3
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 4
        elif cho >= 200 and cho <= 239:
          points += 8
        elif cho >= 240 and cho <= 279:
          points += 11
        elif cho >= 280:
          points += 13
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 9
    
      #we go into age here- JASMINE
      if age >= 40 and age <= 49:
        #specific age points
        if age >= 40 and age <= 44:
          points += 0
        elif age >= 45 and age <= 49:
          points += 3
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 3
        elif cho >= 200 and cho <= 239:
          points += 6
        elif cho >= 240 and cho <= 279:
          points += 8
        elif cho >= 280:
          points += 10
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 7
    
      #we go into age here- claudia
      if age >= 50 and age <= 59:
        #specific age points
        if age >= 50 and age <= 54:
          points = 6
        elif age >= 55 and age <= 59:
          points = 8
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 2
        elif cho >= 200 and cho <= 239:
          points += 4
        elif cho >= 240 and cho <= 279:
          points += 5
        elif cho >= 280:
          points += 7
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 4
    
      #we go into age here- soley
      if age >= 60 and age <= 69:
        #specific age points
        if age >= 60 and age <= 64:
          points += 10
        elif age >= 65 and age <= 6699:
          points += 12
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 4
        elif cho >= 200 and cho <= 239:
          points += 7
        elif cho >= 240 and cho <= 279:
          points += 9
        elif cho >= 280:
          points += 11
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 8
    
      #we go into age here- neslinur
      if age >= 70 and age <= 79:
        #specific age points
        if age >= 70 and age <= 74:
          points += 14
        elif age >= 75 and age <= 79:
          points += 16
        #cholesterol
        if cho < 160:
          points += 0
        elif (cho >= 160 and cho <= 199) or (cho >= 200 and cho <= 239):
          points += 1
        elif (cho >= 240 and cho <= 279) or (cho >= 280):
          points += 2
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 1
    
      #hdl
      if hdl >= 60:
        points -= 1
      elif hdl >= 50 and hdl <= 59:
        points += 0
      elif hdl >= 40 and hdl <= 49:
        points += 1
      elif hdl < 40:
        points += 2
      #bp
      if med == "N":
        if sbp < 120:
          points += 0
        elif sbp >= 120 and sbp <= 129:
          points += 1
        elif sbp >= 130 and sbp <= 139:
          points += 2
        elif sbp >= 140 and sbp <= 159:
          points += 3
        elif sbp >= 160:
          points += 4
      elif med == "Y":
        if sbp < 120:
          points += 0
        elif sbp >= 120 and sbp <= 129:
          points += 3
        elif sbp >= 130 and sbp <= 139:
          points += 4
        elif sbp >= 140 and sbp <= 159:
          points += 5
        elif sbp >= 160:
          points += 6
    
        #risk
      if points < 9:
        out = '<1'
      elif points == 9 or points == 10 or points == 11 or points == 12:
        out = 1
      elif points == 13 or points == 14:
        out = 2
      elif points == 15:
        out = 3
      elif points == 16:
        out = 4
      elif points == 17:
        out = 5
      elif points == 18:
        out = 6
      elif points == 19:
        out = 8
      elif points == 20:
        out = 11
      elif points == 21:
        out = 14
      elif points == 22:
        out = 17
      elif points == 23:
        out = 22
      elif points == 24:
        out = 27
      elif points >= 25:
        out = '>30'
    
    elif sex == "M":
      #we go into age here - nesli
      if age >= 20 and age <= 39:
        #specific age points
        if age >= 20 and age <= 34:
          points -= 9
        elif age >= 35 and age <= 39:
          points -= 4
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 4
        elif cho >= 200 and cho <= 239:
          points += 7
        elif cho >= 240 and cho <= 279:
          points += 9
        elif cho >= 280:
          points += 11
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 8
    
      #we go into age here- JASMINE
      if age >= 40 and age <= 49:
        #specific age points
        if age >= 40 and age <= 44:
          points -= 0
        elif age >= 45 and age <= 49:
          points += 3
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 3
        elif cho >= 200 and cho <= 239:
          points += 5
        elif cho >= 240 and cho <= 279:
          points += 6
        elif cho >= 280:
          points += 8
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 5
    
      #we go into age here- claudia
      if age >= 50 and age <= 59:
        #specific age points
        if age >= 50 and age <= 54:
          points = 6
        elif age >= 55 and age <= 59:
          points = 8
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 2
        elif cho >= 200 and cho <= 239:
          points += 3
        elif cho >= 240 and cho <= 279:
          points += 4
        elif cho >= 280:
          points += 5
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 3
    
      #we go into age here- soley
      if age >= 60 and age <= 69:
        #specific age points
        if age >= 60 and age <= 64:
          points += 10
        elif age >= 65 and age <= 69:
          points += 11
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 1
        elif cho >= 200 and cho <= 239:
          points += 1
        elif cho >= 240 and cho <= 279:
          points += 2
        elif cho >= 280:
          points += 3
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 1
    
      #we go into age here- neslinur
      if age >= 70 and age <= 79:
        #specific age points
        if age >= 70 and age <= 74:
          points += 12
        elif age >= 75 and age <= 79:
          points += 13
        #cholesterol
        if cho < 160:
          points += 0
        elif cho >= 160 and cho <= 199:
          points += 0
        elif cho >= 200 and cho <= 239:
          points += 0
        elif cho >= 240 and cho <= 279:
          points += 1
        elif cho >= 280:
          points += 1
        #non/smoker
        if smo == "N":
          points += 0
        elif smo == "Y":
          points += 1
    
      #hdl
      if hdl >= 60:
        points -= 1
      elif hdl >= 50 and hdl <= 59:
        points += 0
      elif hdl >= 40 and hdl <= 49:
        points += 1
      elif hdl < 40:
        points += 2
      #bp
      if med == "N":
        if sbp < 120:
          points += 0
        elif sbp >= 120 and sbp <= 129:
          points += 0
        elif sbp >= 130 and sbp <= 139:
          points += 1
        elif sbp >= 140 and sbp <= 159:
          points += 1
        elif sbp >= 160:
          points += 2
      elif med == "Y":
        if sbp < 120:
          points += 0
        elif sbp >= 120 and sbp <= 129:
          points += 1
        elif sbp >= 130 and sbp <= 139:
          points += 2
        elif sbp >= 140 and sbp <= 159:
          points += 2
        elif sbp >= 160:
          points += 3
    
      #risk
      if points < 0:
        out = '<1'
      elif points == 0 or points == 1 or points == 2 or points == 3 or points == 4:
        out = 1
      elif points == 5 or points == 6:
        out = 2
      elif points == 7:
        out = 3
      elif points == 8:
        out = 4
      elif points == 9:
        out = 5
      elif points == 10:
        out = 6
      elif points == 11:
        out = 8
      elif points == 12:
        out = 10
      elif points == 13:
        out = 12
      elif points == 14:
        out = 16
      elif points == 15:
        out = 20
      elif points == 16:
        out = 25
      elif points >= 17:
        out = '>30'
    
    print(f'sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out}')

