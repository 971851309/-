
from maze_env import Maze
from RL_brain import SarsaTable
#引入计时器运算运行时间
import time
 

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        # RL choose action based on observation
        action = RL.choose_action(str(observation))

        while True:
            # fresh env
            env.render()
            time_start = time.time() #开始计时

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL choose action based on next observation
            action_ = RL.choose_action(str(observation_))

            # RL learn from this transition (s, a, r, s, a) ==> Sarsa
            RL.learn(str(observation), action, reward, str(observation_), action_)

            # swap observation and action
            observation = observation_
            action = action_
            time_end = time.time()    #结束计时
            time_c= time_end - time_start   #运行所花时间
            print('time cost/运行时间', time_c, 's')
#            # break while loop when end of this episode
#            if done:
#                break
#
#    # end of game
#    print('game over')
#    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()