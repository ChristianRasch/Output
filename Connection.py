def plaxis_connection():

    global s_i, g_i, s_o, g_o
    global plxfilename
    s_i, g_i = new_server('localhost', self.input_port, password = self.password)
    s_o, g_o = new_server('localhost', self.output_port, password = self.password)

    plxfilename = os.path.basename(g_i.Project.Filename.value)
    plxfilename = plxfilename.replace(".p2dx", "")

