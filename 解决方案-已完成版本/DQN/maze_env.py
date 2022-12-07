
import numpy as np
import time
import sys
if sys.version_info.major == 2:
	import Tkinter as tk
else:
	import tkinter as tk

UNIT = 40   # pixels

#区域大小
MAZE_H = 40  # grid height
MAZE_W = 5  # grid width


class Maze(tk.Tk, object):
	def __init__(self):
		super(Maze, self).__init__()
		self.action_space = ['u','d']#只能上和下
		self.n_actions = len(self.action_space)
		self.n_features = 2
		self.title('maze')
		self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
		self._build_maze()

	def _build_maze(self):
		self.canvas = tk.Canvas(self, bg='white',
						   height=MAZE_H * UNIT,
						   width=MAZE_W * UNIT)

		# create grids
		for c in range(0, MAZE_W * UNIT, UNIT):
			x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
			self.canvas.create_line(x0, y0, x1, y1)
		for r in range(0, MAZE_H * UNIT, UNIT):
			x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
			self.canvas.create_line(x0, y0, x1, y1)

		# create origin
		origin = np.array([20, 20])



#
		# create oval#目标
		oval_center = origin + np.array([UNIT, UNIT * 2])#UNIT * 2
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')

#        #建立第二个目标
		oval_center_2 = origin + np.array([UNIT*2, UNIT])#UNIT * 2
		self.oval = self.canvas.create_oval(
		   oval_center_2[0] - 15, oval_center_2[1] - 15,
		   oval_center_2[0] + 15, oval_center_2[1] + 15,
		   fill='yellow')







		
		self.rect = self.canvas.create_rectangle(
		  origin[0] - 15, origin[1] - 15,
		  origin[0] + 15, origin[1] + 15,
		  
			fill='red')



		self.rect_2 = self.canvas.create_rectangle(
			oval_center_2[0] - 1, oval_center_2[1] - 1,
			oval_center_2[0] + 1, oval_center_2[1] + 1,
			fill='red')






		# pack all
		self.canvas.pack()








		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*0]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*1]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*2]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*3]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*4]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*5]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*6]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*7]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*8]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*9]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*10]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*11]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*12]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*13]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*14]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*15]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*16]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*17]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*18]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*19]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*20]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*21]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*22]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*23]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*24]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*25]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*26]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*27]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*28]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*29]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*30]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*31]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*32]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*33]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*34]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*35]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*36]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*37]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*38]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*39]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*40]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*41]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*42]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*43]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*44]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*45]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*46]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*47]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*48]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*49]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*50]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*51]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*52]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*53]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*54]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*55]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*56]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*57]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*58]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*59]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*60]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*61]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*62]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*63]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*64]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*65]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*66]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*67]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*68]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*69]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*70]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*71]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*72]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*73]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*74]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*75]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*76]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*77]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*78]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*79]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*80]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*81]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*82]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*83]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*84]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*85]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*86]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*87]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*88]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*89]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*90]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*91]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*92]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*93]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*94]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*95]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*96]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*97]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*98]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin + np.array([UNIT * 1, UNIT * 1*99]) #origin_A#只调整右边的UNIT 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*0]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*1]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*2]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*3]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*4]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*5]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*6]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*7]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*8]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*9]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*10]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*11]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*12]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*13]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*14]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*15]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*16]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*17]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*18]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*19]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*20]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*21]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*22]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*23]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*24]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*25]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*26]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*27]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*28]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*29]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*30]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*31]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*32]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*33]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*34]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*35]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*36]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*37]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*38]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*39]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*40]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*41]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*42]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*43]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*44]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*45]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*46]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*47]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*48]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*49]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*50]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*51]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*52]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*53]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*54]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*55]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*56]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*57]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*58]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*59]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*60]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*61]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*62]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*63]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*64]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*65]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*66]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*67]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*68]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*69]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*70]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*71]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*72]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*73]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*74]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*75]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*76]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*77]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*78]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*79]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*80]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*81]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*82]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*83]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*84]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*85]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*86]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*87]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*88]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*89]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*90]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*91]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*92]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*93]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*94]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*95]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*96]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*97]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*98]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			



		origin_A = np.array([20, 20])
		# create oval
		oval_center =origin - np.array([UNIT * 1, UNIT * 50*99]) #origin_A#只调整右边的UNIT#更散的可以调整成100 
		self.oval = self.canvas.create_oval(
			oval_center[0] - 15, oval_center[1] - 15,
			oval_center[0] + 15, oval_center[1] + 15,
			fill='yellow')


			











#这个函数才是真正支配智能体个数的函数
#第一个智能体的配套动作
	def reset(self):
		self.update()
		#time.sleep(0.1)
		self.canvas.delete(self.rect)
		origin = np.array([20, 20])
		origin =origin + np.array([UNIT, UNIT * 2])
		#originA = np.array([40, 40])
		self.rect = self.canvas.create_rectangle(
			origin[0] - 15, origin[1] - 15,
			origin[0] + 15, origin[1] + 15,
			fill='red')

		return (np.array(self.canvas.coords(self.rect)[:2]) - np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)


#第二个智能体的配套动作
	def reset_2(self):
		self.update()
		#time.sleep(0.1)
		self.canvas.delete(self.rect_2)#删除，真正的变量与位置在这里
		originA = np.array([20, 400])#前为第几行后为第几列
		self.rect_2 = self.canvas.create_rectangle(
			originA[1] - 15, originA[0] - 15,
			originA[1] + 15, originA[0] + 15,
			fill='red')
		# return observation
		return (np.array(self.canvas.coords(self.rect_2)[:2]) - np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)





	def step(self, action):
		s = self.canvas.coords(self.rect)
		base_action = np.array([0, 0])
		if action == 0:   # up
			if s[1] > UNIT:
				base_action[1] -= UNIT
		elif action == 1:   # down
			if s[1] < (MAZE_H - 1) * UNIT:
				base_action[1] += UNIT
#只有上下


		self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

		next_coords = self.canvas.coords(self.rect)  # next state

		# reward function
		if next_coords == self.canvas.coords(self.oval):
			reward = 1
			done = True

		else:
			reward = 0
			done = False
		s_ = (np.array(next_coords[:2]) - np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)
		return s_, reward, done








	def step_2(self, action):
		s = self.canvas.coords(self.rect_2)
		base_action = np.array([0, 50])
		if action == 0:   # up
			if s[1] > UNIT:
				base_action[1] -= UNIT
		elif action == 1:   # down
			if s[1] < (MAZE_H - 1) * UNIT:
				base_action[1] += UNIT
#只有上下
		self.canvas.move(self.rect_2, base_action[0], base_action[1])  # move agent

		next_coords = self.canvas.coords(self.rect_2)  # next state

		# reward function
		if next_coords == self.canvas.coords(self.oval):
			reward = 1#这里直接设置遇见几个电梯，搭载到，就得一分
			done = True


#关闭阻碍/HELL
		else:
			reward = 0
			done = False
		s_ = (np.array(next_coords[:2]) - np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)
		return s_, reward, done












	def render(self):
		# time.sleep(0.01)
		self.update()


