import os
import numpy as np
import pandas as pd
from pandas import DataFrame

os.chdir("G:\\python\\Date secience\\csv")
DAU = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-dau.csv'))
DPU = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-dpu.csv'))
INSTALL = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-install.csv'))

DAU_INSTALL = pd.merge(INSTALL, DAU, how='outer',on=['user_id', 'app_name'])
DAU_DPU_INSTALL = pd.merge(DAU_INSTALL, DPU, how="outer", on=['user_id', 'app_name', 'log_date'])
DAU_DPU_INSTALL = DAU_DPU_INSTALL.fillna(value=0)
DAU_DPU_INSTALL = DataFrame(DAU_DPU_INSTALL, columns=['app_name','user_id', 'log_date', 'install_date', 'payment', 'statu'])
print(DAU_DPU_INSTALL[DAU_DPU_INSTALL['install_date'] > '2013-4'])
