from mcpi.minecraft import Minecraft;
craft = Minecraft.create("localhost", 4711);

while True:
	cor=craft.player.getTilePos();
	craft.postToChat("x = " + str(cor.x) + " y = " + str(cor.y) + "z = " + str(cor.z));