# /usr/bin/env python
# -*- coding: utf-8 -*-

from 框架.report.school_rep import Test_rep
from 框架.data.读取_数据 import all_data
run = Test_rep()
All_data = all_data()
duqv = All_data.run_name()
if __name__ == '__main__':
    if 'all' in duqv:
        run.run_everyone()
    else:
        run.run_some(duqv)


