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

    :param output: it contains index, time, position at the time, velocity at the time
    :return: output text file that
    '''
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

def hit_wall(time_step, new_velocity, new_position, damping_coef, temp, wall,n):

    time = 0
    position = []
    Time = []
    position.append(new_position)
    Time.append(time)
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
    time_took = []
    plt.rcParams.update({'figure.max_open_warning': 0})
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
        t,p,Time=hit_wall(time_step, new_velocity, new_position, damping_coef, temp, wall,n)
        time_took.append(t)

        if len(Time)>3:
           plt.figure()
           plt.xlabel('Time')
           plt.ylabel('distance')
           plt.plot(Time,p)
           trj_path = os.path.join('trajectory.png')
           plt.savefig(trj_path)

    print(time_took)
    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('# of time took to hit wall')
    plt.hist(time_took)
    hist_path = os.path.join('histogram.png')
    plt.savefig(hist_path)

    return trj_path,hist_path


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

