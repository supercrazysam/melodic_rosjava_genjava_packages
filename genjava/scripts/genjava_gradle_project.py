#!/usr/bin/env python

"""
ROS message source code generation for Java, integration with ros' message_generation.

Converts ROS .msg files in a package into Java source code implementations.
"""
import os
import sys

import genjava

if __name__ == "__main__":
    genjava.main(sys.argv)

