def output_keuze(g_i):


    'Opties geven voor outputkeuze'

    'Standaardkeuzelijst maken met TKinter'

    return(type)




def invullen_coordinaten_plate(g_i):



    return(coords)




def keuzelijst_fases(g_o):

    title = "Plaxis Output"
    question = "Kies de fases voor de output \n(Meerdere fases zijn mogelijk)"
    keuzelijst = [get_phase_screenname(fase) for fase in g_o.Phases[:]]
    fases = eg.multchoicebox(question,title,keuzelijst)

    output_fases = []

    for phase in g_o.Phases[:]:
        if get_phase_screenname(phase) in fases:
        output_fases.append(phase)

    return(ouput_fases)