#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bus processor.  This runs as a subprocess from the coprocess.py example

import sys
from coprocess import recvfrom
from buses import (buses_to_dicts, filter_on_field, bus_locations)


recvfrom(sys.stdin,
         filter_on_field('route', '22',
            filter_on_field('direction', 'North Bound',
                bus_locations())))
