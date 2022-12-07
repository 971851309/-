#        origin_A = np.array([20, 20])
#        # create oval
#        oval_center =origin + np.array([UNIT * 1, UNIT * 20]) #origin_A#只调整右边的UNIT 
#        self.oval = self.canvas.create_oval(
#            oval_center[0] - 15, oval_center[1] - 15,
#            oval_center[0] + 15, oval_center[1] + 15,
#            fill='yellow')


K = 100
##最密集的成功方案
K = 100


for i in range(K):#生成K次


    print(
        '''


        origin_A = np.array([20, 20])
        # create oval
        oval_center =origin + np.array([UNIT * 1, UNIT * 1*{}]) #origin_A#只调整右边的UNIT 
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')


            '''.format(i)

        )






###较为分散的方案
#for i in range(K):#生成K次
#
#
#    print(
#        '''
#
#
#        origin_A = np.array([20, 20])
#        # create oval
#        oval_center =origin - np.array([UNIT * 1, UNIT * 20*{}]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
#        self.oval = self.canvas.create_oval(
#            oval_center[0] - 15, oval_center[1] - 15,
#            oval_center[0] + 15, oval_center[1] + 15,
#            fill='yellow')
#
#
#            '''.format(i)
#
#        )
#






#更加分散的方案
for i in range(K):#生成K次


    print(
        '''


        origin_A = np.array([20, 20])
        # create oval
        oval_center =origin - np.array([UNIT * 1, UNIT * 50*{}]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')


            '''.format(i)

        )
