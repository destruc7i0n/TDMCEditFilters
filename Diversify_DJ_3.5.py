# You may modify and reuse this filter, but if you do, please give credit to WumpaCraft
# Edited for 247FlashGames by destruc7i0n & jgierer12
# http://youtube.com/WumpaCraft
# http://youtube.com/TheDestruc7i0n

import pymclevel
import random

displayName = "Diversify_DJ 3.0"

inputs = (
        ("Created by WumpaCraft, Edited A Bit By destruc7i0n & jgierer12", "label"),
        ("Works on wool, glass, clay, wood, bricks, planks, and leaves", "label"),
	("Diversify: ", ("Wool","Stained Glass","Stained Glass Panes", "Stained Clay", "Carpet", "Wood Blocks", "Stone Bricks", "Wood Planks", "Leaves")), 
        ("Diversify Amount: ", ("(1-5 Randomness) A Little Random", "(1-10 Randomness) Normal Randomness", "(1-15 Randomness) VERY Random"),
        ("The Numbers Of Randomness Is The Options Of Random Data Values. Will Only Work On Rainbow Blocks (Carpets, Wool etc.)", "label"),
)

def perform(level, box, options):
        diversify = options["Diversify: "]
        diversifyAmount = options["Diversify Amount: "]

        clay=159
	carpet=171
	wool=35
	stainedGlass=95
	stainedGlassPanes=160
        stoneBricks=98
        wood=17
        planks=5
        leaves=18
        
        for x in xrange(box.minx, box.maxx):
                for z in xrange(box.minz, box.maxz):
                        for y in xrange(box.miny, box.maxy):
                                if diversify == "Wool" and level.blockAt(x, y, z) == wool:
                                        level.setBlockDataAt(x, y, z, random.randint(0,15))
				elif diversify == "Stained Glass" and level.blockAt(x, y, z) == stainedGlass:
                                        level.setBlockDataAt(x, y, z, random.randint(0,15))
				elif diversify == "Stained Clay" and level.blockAt(x, y, z) == clay:
                                        level.setBlockDataAt(x, y, z, random.randint(0,15))
				elif diversify == "Stained Glass Panes" and level.blockAt(x, y, z) == stainedGlassPanes:
                                        level.setBlockDataAt(x, y, z, random.randint(0,15))
				elif diversify == "Carpet" and level.blockAt(x, y, z) == carpet:
                                        level.setBlockDataAt(x, y, z, random.randint(0,15))
                                elif diversify == "Stone Bricks" and level.blockAt(x,y,z) == stoneBricks:
                                        level.setBlockDataAt(x, y, z, random.randint(0,3))
                                elif diversify == "Wood Blocks" and level.blockAt(x,y,z) == wood:
                                        level.setBlockDataAt(x, y, z, random.randint(0,3))
                                elif diversify == "Wood Planks" and level.blockAt(x,y,z) == planks:
                                        level.setBlockDataAt(x, y, z, random.randint(0,5))
                                elif diversify == "Leaves" and level.blockAt(x,y,z) == leaves:
                                        level.setBlockDataAt(x, y, z, random.randint(4,7))
