from NXController import Controller

# Full party lead with flame body, on your bike, egg is ready to pick
# Text speed fast. No animation.

#cycle = 20			# Egg cycles
#hatchingtime = 9	# Unfreeze the game before fly, egg hatching time in seconds. 18 is safest
#slot = 1			# The first party slot to be replaced (1~5)
#N = 210				# Number of eggs to receive

#利用5号道路长直线的原理进行孵蛋。
#使用方法：队首带一个特性为【火焰之躯】的宝可梦（例如巨碳山）。剩下五个位置全部是空的。
#然后保证当前所在的电脑箱子开始往后，全部是蛋（虽然没有应该也不会触发问题）
#原理： 【根据需要孵蛋的数量N，逐次往后一箱子一箱子孵【根据箱子特征，竖排往后逐次孵完一箱【根据孵蛋周期，确定单轮5个蛋的孵化小周期】】】

#单次Hatch_time完成后，必须进行全力往右的行进，从而可以被黑色西装男挡住，进行步长偏移的消除。回归单个小周期的初始态。

Hatch_time = 20 #此处请参考宝可梦百科中的 孵化周期，必定为 15 20 25 30 35 40其中的值。。
ctr = Controller()

for i in range(Hatch_time//5):
    # Backwards
    # Hold two stick in the oppsite direction
    for ii in range(2):
        ctr.rs_l(-1)
        ctr.ls_r(-1)
        ctr.pause(4.5)
        ctr.release()
        ctr.pause(0.3)
        # Backwards
        ctr.rs_r(-1)
        ctr.ls_l(-1)
        ctr.pause(4.7)
        ctr.release()
        ctr.pause(0.3)
for j in range(5):
    ctr.pause(0.5)
    ctr.A()
    ctr.pause(17)
    ctr.B()
    ctr.pause(3.5)
    ctr.rs_l(-1)
    ctr.ls_r(-1)
    ctr.pause(0.6)
    ctr.release()
ctr.rs_r(-1)
ctr.ls_l(-1)
ctr.pause(6)
ctr.release()
ctr.pause(0.3)
