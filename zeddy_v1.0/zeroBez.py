#python
import lx
	


count = 0;
bezTotal = lx.eval('query sceneservice bezierNode.N ?');
list = range(0, bezTotal);

for i in list:
	
	bez = lx.eval('query sceneservice bezierNode.id ? %s' %count);
		
	#lx.out('Node is: %s and index is: %s' %(bez, count));

	#get the last bezierNode in the list
	def store():
		return bez;
	lastBez = store();

	#increase the count
	count = count + 1;

	#get the total bezierNodes in the scene
	def total():
		return count;
	bezAll = total();


#IMPORTANT index for bezierNodes
aMinus = bezAll - 2;
bMinus = aMinus -1;
cMinus = bMinus -1;
dMinus = cMinus -1;


#the last 5 bezierNode id's stored in variables
T = lastBez;
U = lx.eval('query sceneservice bezierNode.id ? %s' %aMinus);
V = lx.eval('query sceneservice bezierNode.id ? %s' %bMinus);
W = lx.eval('query sceneservice bezierNode.id ? %s' %cMinus);
X = lx.eval('query sceneservice bezierNode.id ? %s' %dMinus);

lx.out('check T: %s' %T);
lx.out('check U: %s' %U);
lx.out('check V: %s' %V);
lx.out('check W: %s' %W);
lx.out('check X: %s' %X);

#======================================================
# zero T
#drop all items
lx.eval('select.drop item');
lx.eval('select.subItem %s set' %T);
lx.eval('anim.setup on');
lx.eval('transform.zero translation');
lx.eval('anim.setup off');
lx.eval('transform.zero translation');
lx.eval('select.drop item');

# zero U
#drop all items
lx.eval('select.drop item');
lx.eval('select.subItem %s set' %U);
lx.eval('anim.setup on');
lx.eval('transform.zero translation');
lx.eval('anim.setup off');
lx.eval('transform.zero translation');
lx.eval('select.drop item');

# zero V
#drop all items
lx.eval('select.drop item');
lx.eval('select.subItem %s set' %V);
lx.eval('anim.setup on');
lx.eval('transform.zero translation');
lx.eval('anim.setup off');
lx.eval('transform.zero translation');
lx.eval('select.drop item');

# zero W
#drop all items
lx.eval('select.drop item');
lx.eval('select.subItem %s set' %W);
lx.eval('anim.setup on');
lx.eval('transform.zero translation');
lx.eval('anim.setup off');
lx.eval('transform.zero translation');
lx.eval('select.drop item');

# zero X
#drop all items
lx.eval('select.drop item');
lx.eval('select.subItem %s set' %X);
lx.eval('anim.setup on');
lx.eval('transform.zero translation');
lx.eval('anim.setup off');
lx.eval('transform.zero translation');
lx.eval('select.drop item');


#create locators and parent them to bezierNodes
#lx.eval('@createloc.py');
