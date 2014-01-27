# MCEdit Filter By destruc7i0n  
# http://youtube.com/TheDestruc7i0n
 
displayName = "DPlace Blocks"
 
inputs = (
        ("Place Block?", True),
	("With What?", "blocktype"),
)
 
def perform(level, box, options):
        pb = options["Place Block?"]
		ww = options["With What?"].ID
 
        for x in xrange(box.minx, box.maxx):
                for y in xrange(box.miny, box.maxy):
                        for z in xrange(box.minz, box.maxz):

				if pb == True:
					level.setBlockAt(x, y, z, ww)    
 
        level.markDirtyBox(box)
