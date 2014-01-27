# MCEdit filter created by TheDestruc7i0n
# http://youtube.com/TheDestruc7i0n

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String

displayName = "1.7 CTI"

def fixedString(s):
	chars = list(s)
	pref = []
	newStr = ""
	format = unichr(167)
	
	i = 0
	for c in chars:
		if c == "&":
			if chars[i+1] != "r":
				pref.append(chars[i+1])
			else:
				pref = ["r"]
			del(chars[i+1])
		elif c != " ":
			for code in pref:
				newStr += format + code
			x = 0
			for cd in pref:
				if cd == "r":
					del(pref[x])
				x += 1
					
				
			newStr += c
		else:
			newStr += c
		
		i += 1
		
	return newStr
			
		
	
			
def perform(level, box, options):
	for (chunk, slices, point) in level.getChunkSlices(box):
		for e in chunk.Entities:
			x = e["Pos"][0].value
			y = e["Pos"][1].value
			z = e["Pos"][2].value
			
			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				if e["id"].value == "MinecartCommandBlock":
						cmd = e["Command"].value
						newcmd = fixedString(cmd)
						if newcmd != cmd:
							e["Command"] = TAG_String(newcmd)
							chunk.dirty = True
							
		for t in chunk.TileEntities:
			x = t["x"].value
			y = t["y"].value
			z = t["z"].value
				
			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				if t["id"].value == "Sign":
					for l in range(1, 5):
						line = t["Text" + str(l)].value
						newline = fixedString(line)
						if line != newline:
							t["Text" + str(l)] = TAG_String(newline)
							chunk.dirty = True
				if t["id"].value == "Control":
					cmd = t["Command"].value
					newcmd = fixedString(cmd)
					if newcmd != cmd:
						t["Command"] = TAG_String(newcmd)
						chunk.dirty = True
