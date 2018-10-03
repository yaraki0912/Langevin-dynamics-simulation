#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Project_1` package."""

import pytest

from click.testing import CliRunner

from Project_1 import Project_1
import io
import os
import numpy as np
import argparse
import unittest
import Project_1.Project_1 as project_1

class Test_Project_1(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def test_inputs(self):
       #parse = project_1.input(['--temperature', '300','--total_time', '1000','--time_step', '0.1','--initial_position', '0','--initial_velocity', '0','--damping_coefficient', '0.1' ])

       #self.assertIsInstance(parse, dict)
       #self.assertEqual(parse['temperature'], 300)
       #self.assertEqual(parse['total_time'], 1000)
       #self.assertEqual(parse['time_step'], 0.1)
       #self.assertEqual(parse['initial_position'], 0)
       #self.assertEqual(parse['initial_velocity'], 0)
       #self.assertEqual(parse['damping_coefficient'], 0.1)
       self.parser = project_1.input()
       parsed = self.parser.parse_args(['--temperature', '300','--total_time', '1000','--time_step', '0.1','--initial_position', '0','--initial_velocity', '0','--damping_coefficient', '0.1'])
       self.assertEqual([parsed.temperature,parsed.total_time, parsed.time_step, parsed.initial_position, parsed.initial_velocity,   parsed.damping_coefficient], [300, 1000, 0.1, 0, 0, 0.1] )
 
        
        
    def test_random_f(self):
        '''Tests if random generator works fine'''
        self.assertEqual(project_1.random_f(1, 0,K_B=1,epsi=1), 0)

    def test_drag_f(self):
       self.assertEqual(project_1.drag_f(0, 2), 0)

    def test_euler(self):
        '''Tests if the force, position and velocity calculated are correct'''
        self.assertEqual(project_1.euler(0,0,0,0,0), (0,0))

    def test_write_output(self):
        '''Tests if the output file is written correctly'''
        test_string = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        test_string2 = '1 2.0000 3.0000 4.0000 \n'
        test_string3 = '5 6.0000 7.0000 8.0000 \n' 
        out_file = './tests/test_output.txt'
        project_1.write_output(out_file, test_string)
        output = open(out_file, 'r')
        test_data = list(output.readlines())
        output.close()
        self.assertEqual(test_data[1], test_string2)
        self.assertEqual(test_data[2], test_string3)
