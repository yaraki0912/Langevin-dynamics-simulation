# -*- coding: utf-8 -*-
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os



def input():
    #input parameters using argparse
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--temperature', metavar='temperature', type=float, nargs=1,
                    help=' ')
    parser.add_argument('--total_time', metavar='total_time', type=float, nargs=1,
                    help=' ')
    parser.add_argument('--time_step', metavar='time_step', type=float, nargs=1,
                    help=' ')
    parser.add_argument('--initial_position', metavar='initial_position', type=float, nargs=1,
                    help=' ')
    parser.add_argument('--initial_velocity', metavar='initial_velocity', type=float, nargs=1,
                    help=' ')
    parser.add_argument('--damping_coefficient', metavar='damping_coefficient', type=float, nargs=1,
                    help=' ')

    return parser

def random_f(temp, damping_coef,K_B=1,epsi=1):
    var = 2 * temp * damping_coef * K_B * epsi
    std = np.sqrt(var)  # standard deviation is sqrt of variance
    random_force=float(np.random.normal(0.0, std))
    #print("rf", random_force)
    return random_force

def drag_f(damping_coef,i_velocity):
    drag_force = -damping_coef * i_velocity
    #print("df",drag_force)
    return drag_force

def euler(time_step,velocity,position, damping_coef, temp):
    #velocity = list()
    #position = list()
    #time = list()
    #n = int(total_time // time_step)

    #velocity.append(i_velocity)
    #position.append(i_position)
    #time.append(0.0)

    #for i in range(n):
    a = drag_f(damping_coef, velocity) + random_f(temp, damping_coef,K_B=1,epsi=1)
    new_velocity = velocity + a* time_step
    new_position = position + velocity * time_step


        #t = time + time_step
        #velocity.append(velocity_t)
        #position.append(position_t)
        #time.append(t)
    #print("a,v,p=", a,new_velocity,new_position)
    return a,new_velocity, new_position

def write_output(output):
    #Write the output file containing index, time, position, and velocity of particles
    #assert((len(idx) == len(time)) == (len(position) == len(velocity)))
    header = "#Index    Time      Position      Velocity"
    Output = open('Output.txt', "w")
    Output.write(header)
    Output.write("\n")
    for line in output:
        for i in range(len(line)):
            if (i == 0):
                Output.write('{} '.format(line[i]))
            else:
                Output.write('{:.4f} '.format(line[i]))
        Output.write('\n')
    Output.close()

#def hit_wall(time_step, new_velocity, new_position, damping_coef, temp, time,wall):



        # await asyncio.sleep(0.05)
        #write_output(output)

 #           return True
  #      return False

def histogram():
    i_position = 0
    i_velocity = 0
    time_step = 0.1
    temp = 300
    wall = 5
    total_time = 1000
    damping_coef = 0.1
    n = int(total_time // time_step)
    new_position = i_position
    new_velocity = i_velocity
   # time = 0
    num_took = list()
    put=[]
    for i in range(n):
        if i !=0:
            new_position = new_pos
            new_velocity = new_vel
        for j in range(0,100):
            new_acc, new_vel, new_pos = euler(time_step, new_velocity, new_position, damping_coef, temp)
            #time += time_step
            # index += 1
            # output.append([index, time, new_pos, new_vel])

            if new_pos >= wall or new_pos <= -wall:
                num_took.append(j+1)
                break
        write_output(put)

    print(num_took, len(num_took))

               #result = hit_wall(time_step, new_velocity, new_position, damping_coef, temp,n, time,wall)
            #if result== True:

             #   break

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('# of time took to hit wall')
    #plt.hist(hit_wall())
    hist_path = os.path.join('histogram.png')
    plt.savefig(hist_path)



def main():  # pragma: no cover
    parser = input()
    args = parser.parse_args()
    temp = args.temperature[0]
    total_time = args.total_time[0]
    time_step = args.time_step[0]
    i_position = args.initial_position[0]
    i_velocity = args.initial_velocity[0]
    damping_coef = args.damping_coefficient[0]
    wall=5

    if (damping_coef <= 0 or temp <= 0 or time_step <= 0 or total_time <= 0):
        # damping coefficient, temperature and time must be positive
        raise ValueError("Damping coefficient, temperature, time_step and total_time must be non-zero positive values")

    n = int(total_time // time_step)
    new_position = i_position
    new_velocity=i_velocity
    time=0
    index=0
    output=[]

    for i in range(n):

        new_acc, new_vel, new_pos = euler(time_step,new_velocity,new_position, damping_coef, temp,)
        time += time_step
        index += 1
        output.append([index, time, new_pos, new_vel])
        new_position = new_pos
        new_velocity = new_vel
        #await asyncio.sleep(0.05)
        write_output(output)
        if new_position > wall or new_position < -wall:
            break
    return None

if __name__ == '__main__':
    input()
    main()
    histogram()

"""Main module."""

