#Code made for calculating different optical measures in a basic source-lens setup

#Optical system variables. 0 if unknown.
dObj = 0                       #Object-Lens distance. (mm) Also known as p.
dImg = 0                       #Lens-Image distance. (mm) Also known as q.
f = 100                        #Lens focal. (mm)
m = -2.3                        #Resultant object magnification. (Scalar(adimensional)) 

def calc_this(dObj, dImg, f, m):
    if dObj != 0 and m != 0:
        dImg = -(m*dObj)
        f = ((-m)*dObj)/(1-m)

    elif dObj != 0 and dImg != 0:
        f = (dObj*dImg)/(dObj+dImg)
        m = (-dImg)/dObj

    elif dObj != 0 and f !=0:
        dImg = (f*dObj)/(dObj-f)
        m = (-dImg)/dObj

    elif dImg !=0 and m !=0:
        dObj = (-dImg)/m
        f = (-dImg)/(m-1)

    elif dImg != 0 and f != 0:
        dObj = (f*dImg)/(dImg - f)
        m = (-dImg)/dObj

    elif m != 0 and f != 0:
        dObj = f - f/m
        dImg = (-m)*dObj

    return(round(dObj, 3), round(dImg, 3), round(f, 3), round(m, 3))

my_sistem = calc_this(dObj, dImg, f, m)

######while dObj==0 or dImg==0 or f==0 or m==0:

print("Object distance:", my_sistem[0],"mm", ", Image distance:", my_sistem[1],"mm", ", Lens focal:", my_sistem[2],"mm", ", Magnification:", my_sistem[3],"mm",)
