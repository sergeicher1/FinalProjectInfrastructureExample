# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Title       : Full stack test Python Automation
# Teacher     : Yoni Flenner
# description : Fix For Ms EDGE and IE
# ----------------------------------------------------------------------------------------
from abc import ABC

from webdriver_manager import utils
from webdriver_manager.driver import EdgeChromiumDriver
from webdriver_manager.driver import IEDriver
from webdriver_manager.manager import DriverManager
import os
import logging


class EdgeChromiumDriverManager(DriverManager, ABC):

    def __init__(
            self,
            version="latest",
            os_type=utils.os_type(),
            # path=None,
            path=r".\\Drivers",
            name="edgedriver",
            url="https://msedgedriver.azureedge.net",
            latest_release_url="https://msedgedriver.azureedge.net/LATEST_RELEASE",
            log_level=logging.INFO,
            print_first_line=None,
            cache_valid_range=1,
    ):
        super().__init__(path, log_level, print_first_line, cache_valid_range)
        self.driver = EdgeChromiumDriver(
            version=version,
            os_type=os_type,
            name=name,
            url=url,
            latest_release_url=latest_release_url,
        )
