import mcpi.minecraft as minecraft;
import mcpi.block as block;


craft = minecraft.Minecraft.create("localhost", 4711);
cor=craft.player.getTilePos();

craft.setBlock(cor.x+2, cor.y, cor.z, block.DIAMOND_BLOCK.id);
craft.postToChat("x = " + str(cor.x) + " y = " + str(cor.y) + "z = " + str(cor.z));