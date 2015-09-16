#!/bin/sh

python -m cProfile -o profiling.dat profiling.py

runsnake profiling.dat  
