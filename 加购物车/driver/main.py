# /usr/bin/env python
# -*- coding: utf-8 -*-

from 加购物车.data.car_data import all_data
from 加购物车.report.add_report import Test_rep

All_data = all_data()
Run = Test_rep()
Run_data = All_data.car_run()

for i in Run_data:
    if i =='All':
        Run.run_everyone()
    else:
        Run.run_some(Run_data)

