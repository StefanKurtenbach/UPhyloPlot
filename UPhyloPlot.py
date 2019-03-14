# UPhyloPlot Version 1.1
# Stefan Kurtenbach
# Stefan.Kurtenbach@med.miami.edu

import csv
import math
import os

for file in os.listdir("./Inputs"):
    if file.endswith(".csv"):
        output = []    

        with open("Inputs/" + file) as p:
            reader = csv.reader(p, delimiter=",")
            Instructions = list(reader)

            
        #first circle
        coordxc1 = 400
        coordyc1 = 300
        rad1 = 60
         
        c1 = ('''<circle fill="#C4C3B1" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc1) + ''' " cy=''' + '''"''' + str(coordyc1) + '''"''' + ''' r="''' + str(rad1) + '''"/>''')


        #second circle and bar
        rad2 = rad1
        hightb1 = int(Instructions[0][2])*10 + rad1 + rad2
        coordxc2 = coordxc1
        coordyc2 = hightb1 + coordyc1
        widthb1 = 100

        b1 = ('''<rect x="''' + str(coordxc1-(widthb1/2)) + '''" y="''' + str(coordyc1) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" width="100" height=''' + '''"''' + str(hightb1) + '''"''' + "/>")
        c2 = ('''<circle fill="#4F5468" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc2) + ''' " cy=''' + '''"''' + str(coordyc2) + '''"''' + ''' r="''' + str(rad2) + '''"/>''')


        #third circle and bars
        if len (Instructions) > 1:
            rad3 = math.sqrt((113.0973355*int(Instructions[1][1]))/math.pi)
            hightb2 = int(Instructions[1][2])*10 + rad2 + rad3
            deltax = math.sin(math.radians(35)) * hightb2
            deltay = math.cos(math.radians(35)) * hightb2
            coordxc3 = coordxc1 - deltax
            coordyc3 = coordyc2 + deltay
            widthb2 = int(Instructions[1][1])

            c3 = ('''<circle fill="#877580" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc3) + ''' " cy=''' + '''"''' + str(coordyc3) + '''"''' + ''' r="''' + str(rad3) + '''"/>''')
            b2 = ('''<rect x="''' + str(coordxc2-(widthb2/2)) + '''" y="''' + str(coordyc2)  + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10"''' + ''' transform="rotate(35 ''' + str(coordxc2) + ''' ''' + str(coordyc2) + ''')" ''' + '''width="''' + str(widthb2) + '''" height=''' + '''"''' + str(hightb2) + '''"''' + "/>")


        # fourth circles and bars
        if len (Instructions) > 2:
            coordxc4 = coordxc3
            rad4 = math.sqrt((113.0973355*int(Instructions[2][1]))/math.pi)
            hightb31 = int(Instructions[2][2])*10 + rad3 + rad4
            hightb32 = int(Instructions[2][2])*10 + rad2 + rad4
            widthb3 = int(Instructions[2][1])
            coordxb3 = coordxc3 - (widthb3/2)
            coordyb3 = coordyc3
            coordyc4 = coordyb3 + hightb31
            coordyc5 = coordyc2 + hightb32
            coordxc5 = coordxc1
            
            c4 = ('''<circle fill="#596CAA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc4) + ''' " cy=''' + '''"''' + str(coordyc4) + '''"''' + ''' r="''' + str(rad4) + '''"/>''')
            c5 = ('''<circle fill="#596CAA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc5) + ''' " cy=''' + '''"''' + str(coordyc5) + '''"''' + ''' r="''' + str(rad4) + '''"/>''')
            b31 = ('''<rect x="''' + str(coordxc3 - (widthb3/2)) + '''" y="''' + str(coordyb3) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="3, 3" width="''' + str(widthb3) + '''" height=''' + '''"''' + str(hightb31) + '''"''' + "/>")
            b32 = ('''<rect x="''' + str(coordxc1 - (widthb3/2)) + '''" y="''' + str(coordyc2) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="3, 3" width="''' + str(widthb3) + '''" height=''' + '''"''' + str(hightb32) + '''"''' + "/>")
  

        # fifthth circles and bars
        if len (Instructions) > 3:
            rad5 = math.sqrt((113.0973355*int(Instructions[3][1]))/math.pi)
            hightb41 = int(Instructions[3][2])*10 + rad4 + rad5
            hightb42 = int(Instructions[3][2])*10 + rad3 + rad5
            hightb43 = int(Instructions[3][2])*10 + rad2 + rad5
            hightb44 = int(Instructions[3][2])*10 + rad4 + rad5
            widthb4 = int(Instructions[3][1])
            
            b41 = ('''<rect x="''' + str(coordxc3-(widthb4/2)) + '''" y="''' + str(coordyc4) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="5, 5" ''' + ''' transform="rotate(325 ''' + str(coordxc4) + ''' ''' + str(coordyc4) + ''')" ''' + ''' width="''' + str(widthb4) + '''" height=''' + '''"''' + str(hightb41) + '''"''' + "/>")
            b42 = ('''<rect x="''' + str(coordxc4-(widthb4/2)) + '''" y="''' + str(coordyc3) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="5, 5" ''' + ''' transform="rotate(325 ''' + str(coordxc3) + ''' ''' + str(coordyc3) + ''')" ''' + ''' width="''' + str(widthb4) + '''" height=''' + '''"''' + str(hightb42) + '''"''' + "/>")
            b43 = ('''<rect x="''' + str(coordxc2-(widthb4/2)) + '''" y="''' + str(coordyc2) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="5, 5" ''' + ''' transform="rotate(325 ''' + str(coordxc2) + ''' ''' + str(coordyc2) + ''')" ''' + ''' width="''' + str(widthb4) + '''" height=''' + '''"''' + str(hightb43) + '''"''' + "/>")
            b44 = ('''<rect x="''' + str(coordxc5-(widthb4/2)) + '''" y="''' + str(coordyc5) + '''" fill="#AEAEA0" stroke="#000000" stroke-miterlimit="10" stroke-dasharray="5, 5" ''' + ''' transform="rotate(325 ''' + str(coordxc5) + ''' ''' + str(coordyc5) + ''')" ''' + ''' width="''' + str(widthb4) + '''" height=''' + '''"''' + str(hightb44) + '''"''' + "/>")

            deltax41 = math.sin(math.radians(325)) * hightb41
            deltay41 = math.cos(math.radians(325)) * hightb41
            deltax42 = math.sin(math.radians(325)) * hightb42
            deltay42 = math.cos(math.radians(325)) * hightb42
            deltax43 = math.sin(math.radians(325)) * hightb43
            deltay43 = math.cos(math.radians(325)) * hightb43
            deltax44 = math.sin(math.radians(325)) * hightb44
            deltay44 = math.cos(math.radians(325)) * hightb44
            
            coordyc6 = coordyc4 + deltay41
            coordxc6 = coordxc3 - deltax41
            coordyc7 = coordyc3 + deltay42
            coordxc7 = coordxc3 - deltax42
            coordyc8 = coordyc2 + deltay43
            coordxc8 = coordxc2 - deltax43
            coordyc9 = coordyc5 + deltay44
            coordxc9 = coordxc5 - deltax44
            
            c6 = ('''<circle fill="#9DA8BA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc6) + ''' " cy=''' + '''"''' + str(coordyc6) + '''"''' + ''' r="''' + str(rad5) + '''"/>''')
            c7 = ('''<circle fill="#9DA8BA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc7) + ''' " cy=''' + '''"''' + str(coordyc7) + '''"''' + ''' r="''' + str(rad5) + '''"/>''')
            c8 = ('''<circle fill="#9DA8BA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc8) + ''' " cy=''' + '''"''' + str(coordyc8) + '''"''' + ''' r="''' + str(rad5) + '''"/>''')
            c9 = ('''<circle fill="#9DA8BA" stroke="#000000" stroke-width="1.0751" stroke-miterlimit="10" cx="''' + str(coordxc9) + ''' " cy=''' + '''"''' + str(coordyc9) + '''"''' + ''' r="''' + str(rad5) + '''"/>''')

        # Sample name
        Samplename = Instructions[0][3]
        L1 = ('''<text x="''' + str(coordxc1) + '''" y="''' + str(coordyc1 - rad1*1.5 - 20) + '''" text-anchor='middle' font-family="'ArialMT'" font-size="60">''' + Samplename + '''</text>''')

        #normal melanocytes
        x=coordxc1-rad1*4-50
        y=coordyc1 - 25

        L2 = ('''<text text-anchor='left' ><tspan x="''' + str(x) + '''" y="''' + str(y) + '''" font-family="'ArialMT'" font-size="40">Normal uveal</tspan><tspan x="''' + str(x) + '''" y="''' + str(y+40) + '''" font-family="'ArialMT'" font-size="40">melanocytes</tspan></text>''')

        #first description
        L3 = ('''<text text-anchor='left' >''')
        x = coordxc1 + rad1*1.5
        y = coordyc1

        linelist = []
        linelist.append(str(Instructions[0][1]) + "% Tumor Cells")
        linelist.append(str(Instructions[0][2]) + " Mutations")
        linelist = linelist + (Instructions[0][4]).split(", ")
        for line in linelist:
            temp = ('''<tspan x="''' + str(x) + '''" y="''' + str(y) + '''" font-family="'ArialMT'" font-size="40">''' + str(line) + '''</tspan>''')
            y = y + 40
            L3 = L3 + temp
        L3 = L3 + "</text>"

        #second description
        if len (Instructions) > 1:
            L4 = ('''<text text-anchor='left' >''')
            x = coordxc2 - rad2*6 - 50
            y = coordyc2 + rad2
            linelist = []
            linelist.append(str(Instructions[1][1]) + "% Tumor Cells")
            linelist.append(str(Instructions[1][2]) + " Mutations")
            linelist = linelist + (Instructions[1][4]).split(", ")            
            for line in linelist:
                temp = ('''<tspan x="''' + str(x) + '''" y="''' + str(y) + '''" font-family="'ArialMT'" font-size="40">''' + str(line) + '''</tspan>''')
                y = y + 40
                L4 = L4 + temp
            L4 = L4 + "</text>"

        #third description
        if len (Instructions) > 2:
            L5 = ('''<text text-anchor='left' >''')
            x = coordxc3 - rad3*6 - 50
            y = coordyc3 + 3*rad2
            linelist = [""]
            linelist.append(str(Instructions[2][1]) + "% Tumor Cells")
            linelist.append(str(Instructions[2][2]) + " Mutations")              
            
            if len(Instructions[2][1]) != 0:
                linelist = linelist + (Instructions[2][4]).split(", ")
            for line in linelist:
                temp = ('''<tspan x="''' + str(x) + '''" y="''' + str(y) + '''" font-family="'ArialMT'" font-size="40">''' + str(line) + '''</tspan>''')
                y = y + 40
                L5 = L5 + temp
            L5 = L5 + "</text>"

        #fourth description
        if len (Instructions) > 3:
            L6 = ('''<text text-anchor='left' >''')
            x = coordxc6 + rad4
            y = coordyc4
            linelist = []
            linelist.append(str(Instructions[3][1]) + "% Tumor Cells")
            linelist.append(str(Instructions[3][2]) + " Mutations")                    
            linelist = linelist + (Instructions[3][4]).split(", ")
            for line in linelist:
                temp = ('''<tspan x="''' + str(x) + '''" y="''' + str(y) + '''" font-family="'ArialMT'" font-size="40">''' + str(line) + '''</tspan>''')
                y = y + 40
                L6 = L6 + temp
            L6 = L6 + "</text>"

        #SVG header
        output.append('''<?xml version="1.0" encoding="utf-8"?>''')
        output.append('''<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">''')
        output.append('''<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"''')
        output.append("\t" + '''viewBox="0 0 1000 2000" enable-background="new 0 0 1000 2000" xml:space="preserve">''')

        if len (Instructions) > 3:
            output.append(b41)
            output.append(b42)
            output.append(b43)
            output.append(b44)
            output.append(c6)
            output.append(c7)
            output.append(c8)
            output.append(c9)
            output.append(L6)
                
        if len (Instructions) > 2:
            output.append(b31)
            output.append(b32)
            output.append(c4)
            output.append(c5)
            output.append(L5)

        if len (Instructions) > 1:
            output.append(b2)
            output.append(L4)
            output.append(c3)
            
        output.append(b1)    
        output.append(c2)
        output.append(c1)
        output.append(L1)
        output.append(L2)
        output.append(L3)

        newfilename = file.replace(".csv", ".svg")
        text_file = open(newfilename, "a")       
        text_file.write("\n".join(output))
        text_file.write("\n")
        text_file.write("</svg>")
        text_file.close()
