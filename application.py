#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app
import config
from config import profiles
from flasgger import Swagger, swag_from
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

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--active_profile')
    parser.add_argument('--mongo_user')
    parser.add_argument('--mongo_password')
    parser.add_argument('--log_path')
    command_args, unknown = parser.parse_known_args()
    active_profile = command_args.active_profile or 'default'

    config.default_config = profiles[active_profile]
    config.default_config.merge_args(command_args)

    pid.write()
    logger.info('Active profile is ' + active_profile)
    app = create_app(config.default_config)
    swag = Swagger(app)
    app.run(host='0.0.0.0')

