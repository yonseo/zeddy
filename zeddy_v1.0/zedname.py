#python
import lx



#query the number of bezier nodes
itemNum = lx.eval('query sceneservice bezierNode.N ?');



    
    
#BUG FOUND! when getting the bezierNode.id to scale you need to select the correct index that corresponds to that node, otherwise it will scale all nodes in the scene.
#--------------------------------------------------------------------------------------
#begin resize function
int = 1;

indexA = 0;
indexB = 4;
indexC = 2;




#resize the first and last bezierNodes in a group of 5.
while int < itemNum:
    
    #query all first bezierNodes in groups of 5
    result = lx.eval('query sceneservice bezierNode.id ? %s' %indexA);
    #lx.out(result);
  

 #=======Use this to resize/scale the first node============================================#
    #select the bezier node
    lx.eval('select.item %s set' %(result));
    #scale the bezier node smaller in size
    lx.eval('tool.set TransformScaleItem on');

    lx.eval('transform.channel scl.X 0.100');
    lx.eval('transform.channel scl.Y 0.100');
    lx.eval('transform.channel scl.Z 0.100');
    lx.eval('tool.clearTask snap');
    
    indexA = indexA + 5;

    #query all last bezierNodes in groups of 5
    result = lx.eval('query sceneservice bezierNode.id ? %s' %indexB);
    #lx.out(result);


 #=======Use this to resize/scale the last node============================================#
    #select the bezier node
    lx.eval('select.item %s set' %(result));
    #scale the bezier node smaller in size
    lx.eval('tool.set TransformScaleItem on');

    lx.eval('transform.channel scl.X 0.100');
    lx.eval('transform.channel scl.Y 0.100');
    lx.eval('transform.channel scl.Z 0.100');
    lx.eval('tool.clearTask snap');
    
    indexB = indexB + 5;
    
    
     #query all 3rd bezierNodes in groups of 5
    result = lx.eval('query sceneservice bezierNode.id ? %s' %indexC);
    #lx.out(result);
  

    #=======Use this to resize/scale the middle node============================================#
    #select the bezier node
    lx.eval('select.item %s set' %(result));
    #scale the bezier node smaller in size
    lx.eval('tool.set TransformScaleItem on');

    lx.eval('transform.channel scl.X 1.500');
    lx.eval('transform.channel scl.Y 1.500');
    lx.eval('transform.channel scl.Z 1.500');
    lx.eval('tool.clearTask snap');
    
    indexC = indexC + 5;
    
    
    
    #increase int by 5 for the loop
    int = int + 5; #!IMPORTANT
    

    
    
    
#-------------------------------------------------------------   

    
    
    
    
    
    #Group the items
    #-------------------------------------------------------------
bezTotal = lx.eval('query sceneservice deform.bezier.N ?');
bezIndex = bezTotal - 1;
bezVar = lx.eval('query sceneservice deform.bezier.id ? %s' %bezIndex);

locTotal = lx.eval('query sceneservice groupLocator.N ?');
locIndex = locTotal - 1;
num = locIndex + 1;
newname = "zedfolder_%s" %num;


#select the bezier deformer
lx.eval('select.item %s set' %bezVar);
#select all items within thr bezier deformer group
lx.eval('group.scan sel item');
#group the selection
lx.eval('layer.groupSelected');
#rename the group folder
lx.eval('item.name %s groupLocator' %newname);
    
    

#----------------------------------------------------------------------------------
#add mesh item to a group named zedhair_unselectable
#make the item group unselectable
meshTotal = lx.eval('query sceneservice mesh.N ?');
meshIndex = meshTotal - 1;
meshVar = lx.eval('query sceneservice mesh.id ? %s' %meshIndex);
int = 0;

            
#query the number of groups and bring me back their index and id
groupNum = lx.eval('query sceneservice group.N ?');


#create a list and number the list of items starting from zero
groupNumList = range(0,groupNum);


for num, item in enumerate(groupNumList):
    
    groupID = lx.eval('query sceneservice group.name ? %s' %item);
    #itemList.append(itemID);
    xName = "Group Name_{}: {}".format(num, groupID);
    gName = groupID;

    
    #use the names in the item List to group the bezierNodes, connect them to their respective influencer and resize
    #lx.out(xName);
    #lx.out(gName);
    
    
    #if group id is NOT equal to zedhair_unselectable execute code
    if 'zedhair_unselectable' != gName:
        lx.out('skip me!');
        int = int +1;
        
        #if all groups have gone through the loop then create a new group
        if int >= groupNum:
            lx.eval('group.create zedhair_unselectable');
            #make group unselectable
            lx.eval('item.channel group$select off');
            lx.eval('select.drop item');
            lx.eval('select.item zedhair_unselectable set');
            lx.eval('select.item %s set' %meshVar);
            #add it to zedhair_unselectable group
            lx.eval('group.edit add item');
            lx.eval('select.drop item');
            lx.out("create a NEW group");
    
    #if gName equals group name zedhair_unselectable add the mesh item to that group
    if gName == 'zedhair_unselectable' :
        
        lx.eval('select.drop item');
        lx.eval('select.item zedhair_unselectable set');
        lx.eval('select.item %s set' %meshVar);
        #add it to zedhair_unselectable group
        lx.eval('group.edit add item');
        lx.eval('select.drop item');
        lx.out('Add to group');

       

#zero Transofrmations for each bezierNode
lx.eval('@zeroBez.py');
    
        

            