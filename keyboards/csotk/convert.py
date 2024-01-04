import json 
from math import floor

data = r"""[[{"y":0.25,"x":1.25},"Esc","F1","F2","F3","F4","F5",{"x":0.25},"Insert",{"x":0.25},"F6","F7","F8","F9","F10","F11","F12",{"x":0.25},"PrtSc"],
[{"y":0.25,"x":1.25},"`","1","2","3","4","5",{"x":0.25},"Delete",{"x":0.25},"6","7","8","9","0","-","=","BKSP"],
[{"x":1.25},"Tab","Q","W","E","R","T",{"x":0.25},"Home",{"x":0.25},"y","I","U","O","P","[","]","\\"],
[{"x":1.25},"Caps Lock","A","S","D","F","G",{"x":0.25},"End",{"x":0.25},"H","J","K","L",";","'",{"w":2},"Enter"],
[{"y":-0.75},"VolUp"],
[{"y":-0.25,"x":1.25},"Shift","Z","x","C","V","B",{"x":1.5},"N","M",",",".","/",{"w":2},"Shift"],
[{"y":-0.75},"VolDn",{"x":6.5},"↑",{"x":7.5},"PgUp"],
[{"y":-0.25,"x":1.25},"Ctrl","Win","Alt",{"a":7,"w":2},"",{"x":3.5,"a":4,"w":2},"Backspace","Alt","Win",{"w":2},"Ctrl"],
[{"y":-0.75},"Mute",{"x":5.5},"←","↓","→",{"x":6.5},"PgDn"]]"""

data = json.loads(data)

x_set = set()
y = 0
w = 1
for c, row in enumerate(data):
    x = 0
    for cell in row:
        if type(cell) is dict:
            if "x" in cell:
                x += cell["x"]
            if "y" in cell:
                y += cell["y"]
            w = cell.get("w", w)
        else:
            print(f"""{{"label": "{cell}", "matrix": [{floor(y)}, {min(floor(x), 15)}], "x": {x}, "y": {y}, "w": {w}}},""")
            x_set.add(floor(x))

            x += w
            w = 1

    y += 1
