
#Lista de las vocales, las acentuadas y la u con diéresis.
v= ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'y']
#Lista de las consonantes que no son vocales.
c= ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q',
    'r', 's', 't', 'v', 'x', 'y', 'z']
#Lista de las consonantes que admiten detrás una R o una L.
crl= ['b', 'c', 'f', 'g', 'k', 'p', 't']
#Lista de las consonantes que admiten detrás una R
cr= ['d', 't']
#Lista de consonantes especiales.
ce= ['h', 'j', 'l', 'm', 'n', 'ñ', 'q', 'r', 's', 'v', 'x', 'y', 'z']





#Minima espresión pronunciable
def voc (pal):
    #Determina si pal tiene alguna vocal, si no tiene es impronunciable
    #Devuelve True en caso de que tenga alguna y False si no hay vocal.
    spp= False
    for i in v:
        if i in pal:
            spp= True
            break
    return spp

    
        
        

        

    
    
        
        

    


    
