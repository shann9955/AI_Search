#Shannon Kelly 13051174
#Desert Crossing Task

import random

def dist(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))     # L_inf

########################################################################

class Klingon:
    klingon_range = 10
    def __init__(self):
        self.x = random.randrange(self.klingon_range)
        self.y = random.randrange(self.klingon_range)

    def move(self):
        pass                            # basic klingon does not move in core task

    def estimated_by(self, ship):
        ship.measure(dist(self.x, self.y,
                          ship.x, ship.y))

    def found_by(self, ship):
        return dist(self.x, self.y, ship.x, ship.y) == 0

    def __repr__(self):
        return "Klingon is at %d,%d" % (self.x, self.y)

########################################################################

class Ship:
    def __init__(self, xklingon, yklingon):
        self.x_range = xklingon
        self.y_range = yklingon
        
        # this is the a priori probability
        p_w = {}
        for x in range(xklingon): 
            for y in range(yklingon):
                p_w[x,y] = float(1)/(self.x_range * self.y_range)  #probability of the where the Klingon could be, one within the size of the  

        self.p_w = p_w

        self.x = random.randrange(self.x_range)
        self.y = random.randrange(self.y_range)

    # characteristics of distance measure: p(d|x,y) where x,y is a
    # possible position of the klingon (remember the mine problem)

    def p_d_cond_w(self, d, x, y):
        if dist(x,y,self.x,self.y) == d: #if the location of the klingon (x,y) and the location of the ship is on the correct track
            return 1.0 #it will return the probability of 1.0, if not then 0.0
        else:
            return 0.0
        # fill in probability p(d|x,y) of finding a distance d if x,y
        # is the position of the klingon. Note that ship has access to
        # its own position via self.x and self.y

    def measure(self, d):
        # for each possible position w=x,y of the klingon
        # calculate p(w|d)

        p_w_cond_d = {}
        # new probabilities for klingon position, if distance 'd' has
        # been measured: p(w|d) = p(d|w) p(w)

        for x in range(0, self.x_range):
            for y in range(0, self.y_range):
                p_w_cond_d[x,y] = self.p_d_cond_w(d,x,y) * self.p_w[x,y]


        z= sum(self.p_d_cond_w(d,x,y)*self.p_w[x,y] for [x,y] in self.p_w)

        for [x,y] in p_w_cond_d:
            p_w_cond_d[x,y] /= z

        self.p_w = p_w_cond_d
        # fill in the Bayesian formula for calculating p_w_cond_d, i.e. p(w|d)


    def show_model(self):

        for x in range(0, self.x_range):
            string = ""
            for y in range(0, self.y_range):
                string += "| " + str(self.p_w[x,y])
            print string + "|"
      #  print self.p_w
        # fill in a print routine printing the current Bayesian model
        # p(w|d) where w is the klingon position (x,y)

    def move(self):
       for x in range(0, self.x_range):#for all X range
            for y in range(0, self.y_range):# for all in Y range

                self.x = random.randrange(self.x_range)#randomise the coordinates of the Ship to move within the range of X and Y of the grid
                self.y = random.randrange(self.y_range)        
    #highest probability
        # fill in a ship's move. Begin with random jumps, for simplicity

    def __repr__(self):
        return "Ship at %d,%d" % (self.x, self.y) # pretty print

########################################################################

def run(klingon, ship):
    while not klingon.found_by(ship):
        raw_input()
        klingon.move()
        klingon.estimated_by(ship)            # ship gets distance

        ship.show_model()                   # show current Bayesian model
        ship.move()                         
        print ship
    print "Klingon found"

klingon = Klingon()
ship = Ship(klingon.klingon_range, klingon.klingon_range)
run(klingon, ship)


    
