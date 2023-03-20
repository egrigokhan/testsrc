# -*- coding: utf-8 -*-
import os

def run(msg):
    return "Received message: " + open(os.environ['test_file'], "r").read()

def setup(config):
    os.environ['test_file'] = config["test_file"]
    return "Setup complete with config: " + config["test_file"]
