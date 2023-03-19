# -*- coding: utf-8 -*-
import os

def run(msg):
    return "Received message: " + msg

def setup(config):
    os.environ['test_file'] = config["test_file"]
    return "Setup complete with config: " + config["test_file"]
