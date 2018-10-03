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
from io import StringIO
class Test_Project_1(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def test_inputs(self):
       
       self.parser = project_1.input()
       parsed = self.parser.parse_args(['--temperature', '300.0','--total_time', '1000.0','--time_step', '0.1','--initial_position', '0.0','--initial_velocity', '0.0','--damping_coefficient', '0.1'])
       self.assertEqual([parsed.temperature,parsed.total_time, parsed.time_step, parsed.initial_position, parsed.initial_velocity,   parsed.damping_coefficient], [[300.0], [1000.0], [0.1], [0.0], [0.0], [0.1]] )
 
        
        
    def test_random_f(self):
        '''Tests if random generator works fine'''
        self.assertEqual(project_1.random_f(1, 0,K_B=1,epsi=1), 0)

    def test_drag_f(self):
       self.assertEqual(project_1.drag_f(0, 2), 0)

    def test_euler(self):
        '''Tests if the force, position and velocity calculated are correct'''
        self.assertEqual(project_1.euler(0,0,0,0,0), (0,0))
        
      
    def test_hit_wall(self):
        self.assertEqual(project_1.hit_wall(0,0,0,0,0,0,0),(0,0,[]))
    
   # def test_main(self):
    #    self.assertEqual(project_1.main(), None)

   # def test_write_output(self):
    #    outfile = StringIO()
     #   project_1.write_output([0.0,0.0,0.0,0.0])
      #  outfile.seek(0)
       # content = outfile.read()
        #output_list = content.split('\n')
        #self.assertEqual(project_1.write_output([0.0,0.0,0.0,0.0]),output_list)
            
