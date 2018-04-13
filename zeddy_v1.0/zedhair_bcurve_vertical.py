#python
import lx


#create the hair mesh cube
lx.eval('@zedhair_cube_vertical.py');


    #add a genInfluencer

lx.eval('item.addDeformer genInfluence true');

    # dialog options preset
lx.eval('deform.bezier.create false true 5 y 8.0');



    
#-------------------------------------------------------------------
idxA = 0;
idxB = 5;


#---------------------------------------------
bezTotal = lx.eval('query sceneservice deform.bezier.N ?');
bezIndex = bezTotal - 1;
bezVar = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);



genTotal = lx.eval('query sceneservice genInfluence.N ?');
genIndex = genTotal - 1;
genVar = lx.eval('query sceneservice genInfluence.id ? %s' %genIndex);

    

meshTotal = lx.eval('query sceneservice mesh.N ?');
meshIndex = meshTotal - 1;
meshVar = lx.eval('query sceneservice mesh.id ? %s' %meshIndex);

#-----------------------------------------------

#query item id
meshID = lx.eval('query sceneservice mesh.id ? %s' %meshIndex);
bezierID = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);

#add the item to the bezier effector group
lx.eval('group.itemPos %s %s 0' %(meshID, bezierID));


#query bezier ID
bezierID = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);
#select the bezier effector and add to schematic
lx.eval('select.item %s set' %(bezierID));
lx.eval('schematic.addItem %s group093 true' %(bezierID));


#select the mesh and add to schemtaic
meshID = lx.eval('query sceneservice mesh.id ? %s' %meshIndex);
lx.eval('select.item %s set' %(meshID));
lx.eval('schematic.addItem %s group093 true' %(meshID));

#select the general influencer and add to schemtaic
genINF = lx.eval('query sceneservice genInfluence.id ? %s' %genIndex);
lx.eval('select.item %s set' %(genINF));
lx.eval('schematic.addItem %s group093 true' %(genINF));


#query bezier ID
bezierID = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);
genINF = lx.eval('query sceneservice genInfluence.id ? %s' %genIndex);

#link bezier effector to general influence
lx.eval('item.link $infeff %s %s posT:0 replace:false' %(bezierID, genINF));



#enable scale resize and useTwist
bezierID = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);
lx.eval('select.item %s set' %(bezierID));
lx.eval('item.channel useScale true');
lx.eval('item.channel useTwist true');
lx.eval('tool.noChange');
lx.eval('tool.doApply');




lx.eval('@zedname.py');



