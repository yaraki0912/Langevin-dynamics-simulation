#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Project_1` package."""

import pytest
import matplotlib
matplotlib.use('Agg')
import unittest
import matplotlib.pyplot as plt
import Project_1
from Project_1 import Project_1
import io
import os
import numpy as np
import argparse
import Project_1.Project_1 as project_1
from io import StringIO

class Test_Project_1(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def test_inputs(self):
        '''
        Tests if parser is working properly. if its taking user input correctly
        '''
        self.parser = project_1.input()
        parsed = self.parser.parse_args(['--temperature', '300.0','--total_time', '1000.0','--time_step', '0.1','--initial_position', '0.0','--initial_velocity', '0.0','--damping_coefficient', '0.1'])
        self.assertEqual([parsed.temperature,parsed.total_time, parsed.time_step, parsed.initial_position, parsed.initial_velocity,   parsed.damping_coefficient], [[300.0], [1000.0], [0.1], [0.0], [0.0], [0.1]] )
 
        
        
    def test_random_f(self):
        '''Tests if random force generator works '''
        self.assertEqual(project_1.random_f(1, 0,K_B=1,epsi=1), 0)

    def test_drag_f(self):
        '''Tests if drag force generator works '''
        self.assertEqual(project_1.drag_f(0, 2), 0)

    def test_euler(self):
        '''Tests if the force, position and velocity are calculated are correctly'''
        self.assertEqual(project_1.euler(0,0,0,0,0), (0,0))
        
      
    def test_hit_wall(self):
        '''Tests if  the position and time calculated by hit wall is correct'''
        self.assertEqual(project_1.hit_wall(200,1,1,1,1,1,1),(200, [1, 201], [0, 200]))


    def test_write_output(self):
        '''Tests is writing out put function writes a file that contains correct values'''
        test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        test_value1 = '1 2.0000 3.0000 4.0000 \n'
        test_value2 = '5 6.0000 7.0000 8.0000 \n'
        project_1.write_output(test_string)
        out='Output.txt'
        f = open(out, 'r')
        test_data = list(f.readlines())
        f.close()
        self.assertEqual(test_data[1], test_value1)
        self.assertEqual(test_data[2], test_value2)

    def test_plot(self):
        '''Tests to make sure if the plot function is making plots'''
        trj_path, hist_path = project_1.plot()
        self.assertEqual(hist_path, 'histogram.png')

