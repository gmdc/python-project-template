# -*- coding: utf-8 -*-

import sys
import os
import pytest
os.chdir(os.path.abspath('..'))
errcode = pytest.main()
sys.exit(errcode)
