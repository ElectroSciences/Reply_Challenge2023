#carrace

#T = int(input("number of test cases "))
R = 10
C = 2
car_id = 0
car_spd = 2
trb_spd = 3
trb_cooldown = 3
trb_cooldown1 = 0
trb_duration = 2
dist_trav = 0
result = int(0)
seconds_list = []
result_list = []


  

#while i != T:
#R, C = int(input("length of track ")), int(input("numbers of cars "))

  
for i in range(0, C):
  #car_id = id
  #car_spd = int(input("car speed"))
  #trb_spd = int(input("turbo speed"))
  #trb_cooldown = int(input("turbo cooldown"))
  #trb_duration = int(input("turbo duration"))
  

  dist_trav = 0
  trb_cooldown1 = 0
  
    
  while dist_trav <= R:
    if trb_duration > 1 :
       #print(dist_trav)#print(trb_cooldown1)
      if trb_cooldown1 == 0:
        for i in range(1, trb_duration):
        
          
          dist_trav = dist_trav + trb_spd
          result = result +1
          
            
          #print(dist_trav)
          #print(result)
      else:
        dist_trav = dist_trav + car_spd
        result = result + 1
      trb_cooldown1 = trb_cooldown
      trb_cooldown1 = trb_cooldown1 -1
      seconds_list.append(result)
      #print(seconds_list)
      #print(dist_trav)
    else:
      if trb_cooldown1 == 0:
          dist_trav = dist_trav + trb_spd
          result = result + 1
          #print(dist_trav)
      else:
        dist_trav = dist_trav + car_spd
        result = result + 1
        #print(dist_trav)
      trb_cooldown1 = trb_cooldown
      trb_cooldown1 = trb_cooldown1 -1
      seconds_list.append(result)
      #print(seconds_list)
  result_list.append(seconds_list[len(seconds_list) - 1])
  #print(result_list)
for i in range(len(result_list), 0, -1):
  result_list[len(result_list) - (i-1) ] = result_list[len(result_list) - (i-1)] - result_list[len(result_list) - (i-2)]

print(result_list)