def answer(x, y, z):

    NUM_MONTHS = 12
    NUM_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    gotit = 0

    #x,y,z = x/y/z -> x,y,z are the same
    #check for lowest constraint match (NUM_MONTHS)
    if (x <= NUM_MONTHS and y == z and x == z):
        strdate = "%02d/%02d/%02d" % (x,y,z)    
        return strdate

    #x,y,z = x/y/z
    if (x <= NUM_MONTHS and y <= NUM_DAYS[x-1]):
        gotit = 1
        strdate = "%02d/%02d/%02d" % (x,y,z)

    #x,y,z = y/x/z
    if (y <= NUM_MONTHS and x <= NUM_DAYS[y-1]):
        if (not gotit):
            gotit = 1
            strdate = "%02d/%02d/%02d" % (y,x,z)  
        #check if earlier match has yielded a date that is same as this one (e.g., "1"/1/15 and 1/"1"/15) 
        elif strdate != "%02d/%02d/%02d" % (y,x,z):
            return "Ambiguous"
        
    #x,y,z = z/x/y
    if (z <= NUM_MONTHS and x <= NUM_DAYS[z-1]):
        if (not gotit):
            gotit = 1
            strdate = "%02d/%02d/%02d" % (z,x,y)      
        #check if earlier match has yielded a date that is same as this one (e.g., "1"/1/15 and 1/"1"/15) 
        elif strdate != "%02d/%02d/%02d" % (z,y,x):
            return "Ambiguous"
        
    #x,y,z = x/z/y
    if (x <= NUM_MONTHS and z <= NUM_DAYS[x-1]):
        if (not gotit):
            gotit = 1
            strdate = "%02d/%02d/%02d" % (x,z,y)      
        #check if earlier match has yielded a date that is same as this one (e.g., "1"/1/15 and 1/"1"/15) 
        elif strdate != "%02d/%02d/%02d" % (x,z,y):
            return "Ambiguous"
    
    #x,y,z = z/y/x
    if (z <= NUM_MONTHS and y <= NUM_DAYS[z-1]):
        if (not gotit):
            gotit = 1
            strdate = "%02d/%02d/%02d" % (z,y,x)      
        #check if earlier match has yielded a date that is same as this one (e.g., "1"/1/15 and 1/"1"/15) 
        elif strdate != "%02d/%02d/%02d" % (z,y,x):
            return "Ambiguous"

    #x,y,z = y/z/x
    if (y <= NUM_MONTHS and z <= NUM_DAYS[y-1]):
        if (not gotit):
            gotit = 1
            strdate = "%02d/%02d/%02d" % (y,z,x)
        #check if earlier match has yielded a date that is same as this one (e.g., "1"/1/15 and 1/"1"/15) 
        elif strdate != "%02d/%02d/%02d" % (y,z,x):
            return "Ambiguous"
        
    return strdate

if __name__ == "__main__":
   print answer(19, 11, 33)

