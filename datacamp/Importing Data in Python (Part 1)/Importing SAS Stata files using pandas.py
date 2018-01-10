#sas statistical analysis system
#stata = statistics + data

#SAS
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT("sales.sas7bdat")as file:
	df_sas = file.to_data_frame()

#STATA
data = pd.read_stata("file.dta")

