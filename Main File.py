'''
Importeren van alle functies uit verschillende python bestanden
'''

sys.path.append(r'C:\Program Files\Plaxis\PLAXIS 2D\python\Lib\site-packages')

from plxscripting.easy import *

## Plaxis Ports
output  = 10000
input   = 10001


## Hier hetzelfde wachtwoord als in Plaxis invoeren
wachtwoord = 'D<V3e#Fv/Dv5cv$V'     # (standaaard wachtwoord Plaxis)

plaxis_connection(output_port, input_port, password)




Output_type = KeuzeMenu()


''''

    if output_type = ....
        coordinaten = 

'''

fases = Keuzelijst_fases(g_i)


