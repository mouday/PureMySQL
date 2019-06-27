# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu

import logging

pure_mysql_logger = logging.getLogger(__name__)
pure_mysql_logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
pure_mysql_logger.addHandler(stream_handler)

