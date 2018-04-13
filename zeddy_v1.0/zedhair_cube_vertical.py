#python
import lx

#Create or import a flat sphere 
#lx.eval('script.implicit "Unit Sphere Item"');



import modo
scene = modo.Scene()
lx.eval('layer.new')

lx.eval('query sceneservice mesh.id ? first');
#-----------------------------------------

#-----------------------------------------

lx.eval('tool.set prim.cube on');
lx.eval('tool.reset prim.cube');


#zero its position
lx.eval('tool.setAttr prim.cube cenX 0.0');
lx.eval('tool.setAttr prim.cube cenY 0.0');
lx.eval('tool.setAttr prim.cube cenZ 0.0');

#Size
lx.eval('tool.setAttr prim.cube sizeX 0.5');
lx.eval('tool.setAttr prim.cube sizeY 8.0');
lx.eval('tool.setAttr prim.cube sizeZ 0.2');

#give it segments

#lx.eval('tool.setAttr prim.cube sides 24');
lx.eval('tool.attr prim.cube segmentsZ 4');
lx.eval('tool.attr prim.cube segmentsX 4');
lx.eval('tool.attr prim.cube segmentsY 48');
lx.eval('tool.setAttr prim.cube axis y');
lx.eval('tool.setAttr prim.cube uvs true');
lx.eval('tool.apply');
lx.eval('tool.set prim.cube off 0');

lx.eval('poly.convert face subpatch true');

#lx.eval('select.edgeLoop base false m3d middle');
#lx.eval('tool.set TransformRotate on');
#lx.eval('tool.setAttr xfrm.transform RX 16.0'); 
#lx.eval('#lx.eval('tool.setAttr xfrm.transform SZ 0.455');
#drop tool 
lx.eval('tool.clearTask snap');
lx.eval('select.drop item');




