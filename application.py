#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app
from config import profiles

from app.utils import pid
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument('--active_profile')
parser.add_argument('--mongo_user')
parser.add_argument('--mongo_password')
parser.add_argument('--log_path')
command_args, unknown = parser.parse_known_args()

active_profile = command_args.active_profile or 'default'

config = profiles[active_profile]
config.merge_args(command_args)
logger = logging.getLogger(__name__)

app = create_app(config)

if __name__ == '__main__':
    pid.write()
    print('Active profile is ' + active_profile)

    app.run(host='0.0.0.0')
