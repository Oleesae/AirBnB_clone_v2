#!/usr/bin/python3

import os
from fabric.api import *

env.hosts = ['100.26.122.8', '54.209.216.103']
env.user = "ubuntu"

def do_create():
    put("~/AirBnB_clone_v2/okonta.txt", "~/kanayo.txt")
