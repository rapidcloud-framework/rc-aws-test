#!/usr/bin/env python3

__author__ = "Igor Royzis"
__copyright__ = "Copyright 2023, Kinect Consulting"
__license__ = "Commercial"
__email__ = "iroyzis@kinect-consulting.com"

import logging

logger = logging.getLogger("server")
logger.setLevel(logging.INFO)


def example_data():
    return [
        {"name": "example"}
    ]

def custom_endpoint(action, params, boto3_session, user_session):
    if action == "example":
        return example_data()
    else:
        logger.warning(f"no such endpoint: {action}")
        return []
