class MyClock24:
    
    # class attributes:
        
    # initializer:    
    def __init__(self, hh, mm, ss): 
        # check for hh values > 23:
        if(hh>23):
            hh = hh - 24
        # check for mm values > 60:
        if(mm>60):
            mm = mm - 60    
        # check for ss values > 60:
        if(ss>60):
            ss = ss - 60        
            
        self.hours = hh
        self.minutes = mm
        self.seconds = ss
        
        
    def tick(self): 
        #self.seconds = int(self.seconds)
        self.seconds += 1
        if(self.seconds//60>0):
            self.seconds = self.seconds % 60
            #self.seconds = str(self.seconds)
            #self.minutes = int(self.minutes)
            self.minutes += 1
            if(self.minutes//60>0):
                self.minutes = self.minutes % 60
               # self.minutes = str(self.minutes)
                #self.hours = int(self.hours)
                self.hours += 1
                if(self.hours//24>0):
                    self.hours = self.hours % 24
                   # self.hours = str(self.hours)
                    # or:
                    #self.hours = 0
        return str(self)
    
    @property
    def hh(self):
        """The hours property."""
        #print("Get hours")
        return self._hh

    @hh.setter
    def hh(self, value):
        #print("Set hours")
        self._hh = value
    
    @property    
    def mm(self):
        """The minutes property."""
        #print("Get minutes")
        return self._mm

    @mm.setter
    def mm(self, value):
        #print("Set minutes")
        self._mm = value 
        
    @property    
    def ss(self):
        """The seconds property."""
        #print("Get seconds")
        return self._ss

    @ss.setter
    def ss(self, value):
        #print("Set seconds")
        self._ss = value     

    # @radius.deleter
    # def radius(self):
    #     print("Delete radius")
    #     del self._radius
        
    
    
    # display methods:
    def __str__(self):
        
        #return f"{self.hours}:{self.minutes}:{self.seconds}" 
        #st = ("%02d:%02d:%02d" % (int(self.hours), int(self.minutes), int(self.seconds)))
        if(len(str(self.hours))==1):
            sthh = '0' + str(self.hours)
        else: 
            sthh = str(self.hours)
        #print('str(self.hours): ', sthh)
        if(len(str(self.minutes))==1):
            stmm = '0' + str(self.minutes)
        else: 
            stmm = str(self.minutes)    
        if(len(str(self.seconds))==1):
            stss = '0' + str(self.seconds)
        else: 
            stss = str(self.seconds)    
        #st = ("%02s:%02s:%02s" % (str(self.hours), str(self.minutes), str(self.seconds)))
        st = ("%02s:%02s:%02s" % (sthh, stmm, stss))
        return st
    
    
    def __repr__(self):
       rep  = str({'hours': self.hours, 'minutes': self.minutes, 'seconds': self.seconds})
       return rep
        
     
   # comparison methods:
    def __eq__(self, other):
        if(self.hours==other.hours and self.minutes==other.minutes and self.seconds==other.seconds):
            return True
        else:
            return False
 
    
    def __ne__(self, other):
        if(self.hours!=other.hours or self.minutes!=other.minutes or self.seconds!=other.seconds):
            return True
        else:
            return False
         
    
        
    def __lt__(self, other):
       if(self.hours < other.hours):
           return True
       if(self.hours > other.hours):
           return False
       if(self.hours == other.hours):
           #print('inside mm: ')
           if(self.minutes > other.minutes):
               return False
           if(self.minutes < other.minutes):
               return True
           if(self.minutes == other.minutes):
               #print('inside ss: ')
               if(self.seconds > other.seconds):
                   return False
               if(self.seconds < other.seconds):
                       return True
               if(self.seconds == other.seconds):
                       return False
           
        
       

    def __gt__(self, other):
        if(self.hours > other.hours):
            return True
        if(self.hours < other.hours):
            return False
        if(self.hours == other.hours):
            #print('inside mm: ')
            if(self.minutes < other.minutes):
                return False
            if(self.minutes > other.minutes):
                return True
            if(self.minutes == other.minutes):
                #print('inside ss: ')
                if(self.seconds < other.seconds):
                    return False
                if(self.seconds > other.seconds):
                        return True
                if(self.seconds == other.seconds):
                        return False
   
    def __ge__(self, other):
        if (self.__eq__(other) or self._gt__(other)):
            return True
        else:
            return False
    
    def __le__(self, other):
        if (self.__eq__(other) or self._lt__(other)):
            return True
        else:
            return False
    
    
    def __add__(self, arg):
         
         if(type(arg)==type(self)):
             self.seconds += arg.seconds
             if (self.seconds//60>0):
                 self.minutes += 1
                 self.seconds = self.seconds % 60
                 
             self.minutes += arg.minutes
             
             if (self.minutes//60>0):
                 self.minutes = self.minutes % 60
                 self.hours += 1
             self.hours += arg.hours
             if (self.hours//24>0):
                 self.hours = self.hours % 24
             return self
         elif(isinstance(arg, int)):
             #print('\ninside int arg: \n')
             self.seconds += arg
             #print(self.seconds)
             if (self.seconds//60>0):
                # print('inside mm')
                 self.minutes += 1
                 self.seconds = self.seconds % 60
                 #print('secs: ', self.seconds)
                 #print('mins: ', self.minutes)
             if (self.minutes//60>0):
                 #print('inside hh')
                 self.hours += 1
                 self.minutes = self.minutes % 60
                 
             if (self.hours//24>0):
                 self.hours = self.hours % 24
             return self    
         else:
             raise ValueError('Argument not type int or type MyClock24')
         
    
    
    
   
    def __sub__(self, arg):
        if(type(arg)==type(self)):
            pass
            self.seconds -= arg.seconds
            if (self.seconds<0):
                 self.seconds += 60
                 self.minutes -= 1
            self.minutes -= arg.minutes                    
            if (self.minutes<0):
                 self.minutes += 60
                 self.hours -= 1
            self.hours -= arg.hours
            if (self.hours<0):
                   self.hours += 24
            return self    
            
        elif(isinstance(arg, int)):
            
            self.seconds -= arg
            if (self.seconds<0):
                 self.seconds += 60
                 self.minutes -= 1
            
            if (self.minutes<0):
                 self.minutes += 60
                 self.hours -= 1   
            if (self.hours<0):
                   self.hours += 24
            return self    
        else:
            raise ValueError('Argument not type int or type MyClock24')


if __name__ == "__main__":
    clock(argv)