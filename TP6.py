# IMPORTATION DES LIBRAIRIES DE FONCTION
from functionTp6 import entendreLeSon, note,assemblerLesNotes

#====================Sirene de la police===================================
# CREATION DES 2 NOTES DE LA SIRENE
note1 = note(435,1,0.5)     # Fréquence: 435Hz
                            # Amplitude: 1 
                            # Durée 0.5s
                            
note2 = note(580,1,0.5)


#===============ASSEMBLAGE DE LA SUITE DE NOTE=============================
#L'argument de la fonction assemblerLesNotes s'écrit comme ceci: (note1, note2,...)

sirene = assemblerLesNotes( (note1,note2,note1) ) 

#=================== ECOUTER LA SUITE DE NOTE===============================
entendreLeSon(sirene)



