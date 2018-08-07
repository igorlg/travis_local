#!/usr/bin/env python

import yaml

path = '/home/travis/src/.travis.yml'

with open(path, 'r') as f:
  travis_yaml = yaml.load(f)

phases    = [ 'before_install', 'install', 'post_install',
              'before_script', 'script', 'post_script',
            ]
commands  = [ 'source ~/virtualenv/python3.6/bin/activate',
              'cd /home/travis/src',
            ]

for i in phases:
  try:
    [commands.append(c) for c in travis_yaml[i]]
  except KeyError as e:
    pass

for cmd in commands:
  print(cmd)
