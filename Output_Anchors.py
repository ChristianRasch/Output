def output_notetonode(fases, coords_nodetonode):

    book = xlwt.Workbook(encoding="utf-8")

    for coord in coordinaten:

        x_coord = coord[0]
        y_coord = coord[1]

        sheet1 = book.add_sheet(str("x" + str(x_coord) + " y" + str(y_coord)))

        sheet1.write(0, 1, 'x')
        sheet1.write(0, 2, 'y')
        sheet1.write(0, 3, 'N [kN]')
        sheet1.write(0, 4, 'Fase')

        i = 0

        for fase in fases:

            i = i + 1

            fase_ID = fase.Identification

            sheet1.write(i, 4, str(fase.Identification))

            try:

                anchorF = g_o.getresults(fase, g_o.ResultTypes.NodeToNodeAnchor.AnchorForce2D, 'node')
                anchorX = g_o.getresults(fase, g_o.ResultTypes.NodeToNodeAnchor.X, 'node')
                anchorY = g_o.getresults(fase, g_o.ResultTypes.NodeToNodeAnchor.Y, 'node')

                for x, y, f in zip(anchorX, anchorY, anchorF):

                    if abs(x - x_coord) < 1e-3 and abs(y - y_coord) < 1e-3:
                        sheet1.write(i, 1, x)
                        sheet1.write(i, 2, y)
                        sheet1.write(i, 3, f)

            except:
                sheet1.write(i, 1, x_coord)
                sheet1.write(i, 2, y_coord)
                sheet1.write(i, 3, 0)

    book.save(path + '/' + datetime.datetime.fromtimestamp(time.time()).strftime(
        '%Y-%m-%d %H.%M') + " " + plxfilename + " NodeToNodeAnchors.xlsx")

