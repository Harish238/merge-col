import pandas as pd
def merge_col(df,col_list,dest,sep):
	for i in range(len(col_list)):
		if(i+1)<len(col_list):
			df[dest] = df[col_list[i]].astype(str).str.cat(df[col_list[i+1]].astype(str),sep=sep)
			del df[col_list[i]]
	del df[col_list[-1]]
	return df