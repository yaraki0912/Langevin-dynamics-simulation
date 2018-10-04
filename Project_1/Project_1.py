# -*- coding: utf-8 -*-
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def input():
    '''
    This function reads parameter from user's input
    :return:
    parser that includes temperature, total time, time step, initial position, initial velocity, and damping coefficient
    based on user's input from a command line
    '''
    parser = argparse.ArgumentParser(description='Please input emperature, total time, time step, initial position, initial velocity, and damping coefficient')
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
    '''
    This function takes temperature and damping coefficient and kb(default to 1), epsilon(default to 1)
    and calculates random force

    :param temp: temperature
    :param damping_coef: dumping coefficient
    :param K_B:boltzmann constant (reduced unit), defaulted as 1
    :param epsi: delta(t-t') defaulted as 1
    :return:random force
    '''
    var = 2 * temp * damping_coef * K_B * epsi
    std = np.sqrt(var)  # standard deviation is sqrt of variance
    random_force=float(np.random.normal(0.0, std))
    return random_force

def drag_f(damping_coef,i_velocity):
    '''
    This function takes damping coefficient from user input and velocity and calculates drag force
    :param damping_coef: damping coefficient from user input
    :param i_velocity: velocity at time t
    :return: drag force
    '''
    
    drag_force = -damping_coef * i_velocity
    return drag_force

def euler(time_step,velocity,position,damping_coef,temp):
    '''
    This function calculates new position and new velocity based on previous velocity, position, time step, damping coefficient
    temperature.
    :param time_step: time step from user imput (delta t)
    :param velocity: previous velocity you calculated (can be initial velocity if it's a first step)
    :param position: previous position you calculated (can be initial velocity if it's a first step)
    :param damping_coef: damping coefficient from user input
    :param temp: temperature from user input
    :return: new position and new velocity
    '''

    # call the functions drag_f and random_f to calculate new accerelation
    a = drag_f(damping_coef, velocity) + random_f(temp, damping_coef,K_B=1,epsi=1)
    new_velocity = velocity + a*time_step
    new_position = position + velocity * time_step

    return new_velocity, new_position

def write_output(output):
    '''
    This function creates a text file that contains the result which answers the second requirement
    :param output: List that contains index, time, position at the time, velocity at the time
    :return: output text file that contains index, time, position at the time, velocity at the time till hit the wall
    '''
    header = "#Index    Time      Position      Velocity"
    #make a text file called "Output"
    Output = open('Output.txt', "w")
    Output.write(header)
    Output.write("\n")
    #except for the header, it writes index,time,position line by line
    for line in output:
        for i in range(len(line)):
            if (i == 0):
                Output.write('{} '.format(line[i]))
            else:
                Output.write('{:.4f} '.format(line[i]))
        Output.write('\n')
    Output.close()

def hit_wall(time_step, new_velocity, new_position, damping_coef, temp, wall,n):
    '''
    This function calculate time, position and time list the contains each time steps till the particle hits the wall
    :param time_step: time step inout from user
    :param new_velocity: initial velocity when you generate this function
    :param new_position: initial position when youo generate this function
    :param damping_coef: damping coefficient from user input
    :param temp: temperature input from user
    :param wall: wall size that is defaulted as 5 in this project
    :param n: total time divided by time step
    :return: time, position and time list the contains each time steps till the particle hits the wall
    '''

    time = 0
    #position and Time saves all the position and time untill the particle hits the wall.They are used to make trajectory
    position = []
    Time = []
    position.append(new_position)
    Time.append(time)
    #keep caluculating new velocity and position untill the particle hits the wall or till time is up
    for i in range(n):
        new_vel, new_pos = euler(time_step, new_velocity, new_position, damping_coef, temp, )
        time += time_step
        new_position = new_pos
        new_velocity = new_vel
        position.append(new_position)
        Time.append(time)
        if new_position > wall or new_position < 0:

            return time, position,Time


def plot():
    '''
    This function generates histogram and trajectory based on the hit_wall function
    The histogram shows how long the particle took to hit the wall in every 100 runs
    The trajectory takes one of the 100 runs and shows the path it took till hitting the wall
    :return: histogram and trajectory
    '''

    time_took = []
    plt.rcParams.update({'figure.max_open_warning': 0})
    # the for loop runs hit_wall for 100 times to collect data for the histogram with given condition i the prompt
    for j in range(100):
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
        #t is the time the particle hits the wall, p/Time  contains all the path/time the particle took till it hits the wall
        t,p,Time=hit_wall(time_step, new_velocity, new_position, damping_coef, temp, wall,n)
        #collect the time the partcle hits the wall to make a histogram
        time_took.append(t)
        #this if statement privents making a tajectory that only contains two points where the partcle goes to the negative
        #direction and hits the wall immediently. It is not a wrong data but graph looks too funky.
        if len(Time)>3:
           plt.figure()
           plt.xlabel('Time')
           plt.ylabel('Distance')
           #time vs position graph from one of the
           plt.plot(Time,p)
           trj_path = os.path.join('trajectory.png')
           plt.savefig(trj_path)

    #make a histohram of time it took to hit the walls
    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('# of runs that hits at the time')
    plt.hist(time_took)
    hist_path = os.path.join('histogram.png')
    plt.savefig(hist_path)

    return trj_path,hist_path


def main():  # pragma: no cover
    #generates initial values based on the user input using parser
    parser = input()
    args = parser.parse_args()
    temp = args.temperature[0]
    total_time = args.total_time[0]
    time_step = args.time_step[0]
    i_position = args.initial_position[0]
    i_velocity = args.initial_velocity[0]
    damping_coef = args.damping_coefficient[0]
    #wall size is default
    wall=5

    n = int(total_time // time_step)
    new_position = i_position
    new_velocity=i_velocity
    time=0
    index=0
    output=[]

    #run euler till time is up or hit the wall
    for i in range(n):

        new_vel, new_pos = euler(time_step,new_velocity,new_position, damping_coef, temp,)
        time += time_step
        index += 1
        output.append([index, time, new_pos, new_vel])
        new_position = new_pos
        new_velocity = new_vel
        write_output(output)
        if new_position > wall or new_position < 0:
            break
    return None

if __name__ == '__main__':
    input()
    main()
    plot()

"""Main module."""

