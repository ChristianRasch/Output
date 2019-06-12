def output_plates(g_o,x_coordinaten,plx_filename,phases):

    for x in x_coordinaten:

        df = pd.DataFrame()

        for phase in phases:

            try:
                plateX = g_o.getresults(phase, g_o.ResultTypes.Plate.X, 'node')
                plateY = g_o.getresults(phase, g_o.ResultTypes.Plate.Y, 'node')
                plateSPUx = g_o.getresults(phase, g_o.ResultTypes.Plate.SPUx, 'node')
                plateM = g_o.getresults(phase, g_o.ResultTypes.Plate.M2D, 'node')
                plateN = g_o.getresults(phase, g_o.ResultTypes.Plate.Nx2D, 'node')
                plateV = g_o.getresults(phase, g_o.ResultTypes.Plate.Q2D, 'node')

                fase = get_phase_screenname(phase)

                df_temp = pd.DataFrame()
                df_temp2 = pd.DataFrame()

                d = []

                for x, y, SPux, M, V, N in zip(plateX, plateY, plateSPUx, plateM, plateV, plateN):

                    if abs(x - x_coord) <= 1E-3:
                        d.append({'y [m]': y, 'M [kN/m]': M, 'V [kN/m]': V, 'ux [m]': SPux, 'Phase': fase})

                df_temp = pd.DataFrame(d)
                df_temp.sort_values('y [m]', ascending=False)

                df = df.append(df_temp)
                print('Resulten uitgelezen uit ' + fase)

            except:
                fase = get_phase_screenname(phase)
                print('geen plate gevonden in fase \"{}\" op x = {}'.format(fase, x_coord))

        try:
            df = df[['y [m]', 'M [kN/m]', 'V [kN/m]', 'ux [m]', 'Phase']]
        except:
            pass

        ts = time.time()
        output_sheet = pd.ExcelWriter(
            'D:/Output ' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H.%M.%S') + ' x = ' + str(
                x_coord) + ' ' + plxfilename + '.xlsx')
        df.to_excel(output_sheet, 'Blad1', index=False)
        output_sheet.save()