#Shannon Kelly 13051174
#Desert Crossing Task


def safe(self): #safe function, self is used to call it in other functions
    state = [0,3,[0,0,0,0]] #state of the beginning of the program
                    #first 0 is the camp
                #3 is the amount of fuel
                #the other list is the fuel at each camp


    if state == state[1] < 0: #if the state of the fuel is less than 0, this is not a safe state
        return not state[1] #do not return the fuel state if it is less than 0

class Crossing:

    def start(self):#start of the program, structures the format of the data

        return [0,3,[0,0,0,0]]
                #first 0 is the camp
                #3 is the amount of fuel
                #the other list is the fuel at each camp

    def goal(self, state):
        return state[0] == 4 #the goal method, if the truck reaches camp 4, the program should stop and return True


    def succ(self, state):
        active_camp = [state]#the active camp is the state of the data
        max_fuel = 3 #maximum fuel is 3

        succlist=[active_camp] #the successor list takes the active_camp data


        for total_movement in range(1,max_fuel+1): #sets the minimum fuel to 1 and maximum to 3
            for travel in range(0, 2): #the amount of moves the truck can do
             #   if total_movement <0:
              #      print "cannot go past base camp"
                #    continue
               # if state[0] > 4:
               #     print "cannot go past goal camp"
                #    continue

                #if travel==1:
                #    total_movement *= -1

                
                
                if state[0] < state[1]: #if state is between 0 and 2
                    state[0]=state[0]+1#add one to camp state to move up a camp
                    state[1] -= 1#each time it moves up take one away from fuel
                    if state[1] < state[0]:#if the fuel is less than the state of the camp
                        print "this should not happen"#this should not happen, this creates the validation
                        
                    if state[1] < total_movement:#if the fuel is less than the movement
                        state[0] = state[0] - 1#the camp state will take away 1 to move backwards
                        state[0] -=1
                    if state[0] == 0:#if the truck is at base camp
                        state[1] = state[1] +3#add 3 to fuel state
                    if state[0] == 1:#is the truck is at camp one
                        state[2][0] = state[1]#the first camp in the list array should equal the amount of fuel available
                    if state[0] == 2:#if the truck is as camp two
                        state[2][1] = state[1]#the second camp in the list away should equal the amount of fuel available
                        continue


                if state[0] > state[1]: #if state is between 3 and 4
                    if state[1] < state[0]:#if the fuel is less than the camp state
                        state[0] = state[0] - state[1]#move the camp backwards with the amount of fuel available
                        state[0] -=1
                    if state[0] == 0:#if the truck is at base camp
                        state[1] = state[1] +3#add 3 to fuel state


                    if state[0] == 3:#if the truck is at camp 3
                        state[2][2] = state[1]#the third camp in the list array should equal the amount of fuel available
                    if state[0] == 4:#if the truck is at camp 4
                        state[2][3] = state[1]#the fourth camp in the list array should equal the amount of fuel available
                        continue


                if state[2][0] < state[0]:#if the first list array is less than the camp state
                    state[0] -=total_movement#move the camp backwards
                    
                print state#print the states
                        
                                        
                
                    

##                


                new_state=[0,3,[0,0,0,0]]#the new state is used if the safe method is not safe


                if safe(new_state):#if safe occurs
                    succlist.append(new_state)#add the new state to the succlist
#

                

        return succlist#print the succlist

        

        

        



        
