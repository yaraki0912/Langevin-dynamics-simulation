=========
CHE 477 Langevin Dynamics Project
=========


.. image:: https://img.shields.io/pypi/v/Project_1.svg
        :target: https://pypi.python.org/pypi/Project_1

.. image:: https://img.shields.io/travis/yaraki0912/Project_1.svg
        :target: https://travis-ci.org/yaraki0912/Project_1

.. image:: https://readthedocs.org/projects/Project-1/badge/?version=latest
        :target: https://Project-1.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/yaraki0912/Project_1/shield.svg
     :target: https://pyup.io/repos/github/yaraki0912/Project_1/
     :alt: Updates

.. image:: https://coveralls.io/repos/github/yaraki0912/Project_1/badge.svg?branch=master
:target: https://coveralls.io/github/yaraki0912/Project_1?branch=master





* Free software: MIT license
* Documentation: https://Project-1.readthedocs.io.


Overview
--------
This is one dimensional python implementaion Langevin Dynamics Simulation. It utilizes Euler integration and calculates position and velocity of a particle based on the  initial position, velocity, temperature, damping coefficient, time step and total time users input. 

Installation 
------------
To install this project, use following command in your terminal

git clone git@github.com:yaraki0912/Project_1.git
pip install Project_1

How to Use
--------
This simulator has a command line interface where the user can input parameters using the command libe bellow (values are arbitrary).

py Project_1/Project_1.py --temperature 300 --total_time 1000  --time_step 0.1 --initial_position 0 --initial_velocity 0 --damping_coefficient 0.1

Outputs are textfile, histogram, and trajectory.
Result is in the form of a text file which contains position and velocity for each time step.
histogram.png plots how many times the particle hits the wall at the time out of 100 runs with a given condition. 
trajectory.png plots a path of the particle untill it hits the wall. The graph represents one of the 100 runs performed above.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
