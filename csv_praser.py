#%%
import xml.etree.ElementTree as ET
import pandas as pd
import os
#%%
files_in_dir = os.listdir("dumps/yohananof") 
list(map(lambda x:parse_csv("dumps","yohananof",x),files_in_dir))
# %%

def parse_csv(root,folder,file_name):
	print(file_name)
	if file_name.startswith("Price") or file_name.startswith("PriceFull"):
		tree = ET.parse("%s/%s/%s" % (root,folder,file_name))
		root = tree.getroot()

		#%%
		iteams = root.find("Items")
		get_range = lambda col: range(len(col))
		l = [{r[i].tag:r[i].text for i in get_range(r)} for r in iteams]

		df = pd.DataFrame.from_dict(l)
		
		return df
# %%
