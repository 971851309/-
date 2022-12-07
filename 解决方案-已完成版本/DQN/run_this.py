from maze_env import Maze
from RL_brain import DeepQNetwork






#引入计时器运算运行时间
import time
 
 

 

 

 
 






#step
def run_maze():
	time_start = time.time() #开始计时
	step = 0#属于智能体1
	step_2 = 0#属于智能体2
	for episode in range(30000000):
		
		observation = env.reset()
		observation_2 = env.reset_2()

		while True:
			# fresh env
			env.render()

			# RL choose action based on observation

			action = RL_1.choose_action(observation)

			action_2 = RL_2.choose_action(observation_2)




			# RL take action and get next observation and reward
			observation_, reward, done = env.step(action)

			 
			observation_2A, reward_2, done_2 = env.step(action_2)


			#RL.store_transition(observation, action, reward, observation_)
			RL_1.store_transition(observation, action, reward, observation_)
			time_end = time.time()    #结束计时
			time_c= time_end - time_start   #运行所花时间
			print('time cost/运行时间', time_c, 's')

			break#跳出循环直接计数



#			RL_2.store_transition(observation_2, action_2, reward_2, observation_2A)

			if (step > 20) and (step % 5 == 0):#200步学习一次
				RL_1.learn()
#				RL_2.learn()
				



			# swap observation
			observation = observation_
#			observation_2 = observation_2A




if __name__ == "__main__":
	# maze game
	env = Maze()


	RL_1 = DeepQNetwork(env.n_actions, env.n_features,
					  learning_rate=0.00001,#0.01
					  reward_decay=0.00001,#,
					  e_greedy=0,#0.9
					  replace_target_iter=1,#200
					  memory_size=1,#2000,
					  # output_graph=True
					  )


	RL_2 = RL_1






	env.after(100, run_maze)
	env.mainloop()
	RL_1.plot_cost()
	RL_2.plot_cost()
