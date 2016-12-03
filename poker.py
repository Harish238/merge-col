import pandas as pd
def merge_col(df,col_list,dest,sep):
	for i in range(len(col_list)):
		if(i+1)<len(col_list):
			df[dest] = df[col_list[i]].astype(str).str.cat(df[col_list[i+1]].astype(str),sep=sep)
			del df[col_list[i]]
	del df[col_list[-1]]
	return df
poker = pd.read_csv("/home/harishvenkataraman/poker.csv",names=["S1","C1","S2","C2","S3","C3","S4","C4","S5","C5","Class"])
print(poker.head())
poker = merge_col(poker,["S1","C1"],"S1-C1","-")
poker = merge_col(poker,["S2","C2"],"S2-C2","-")
poker = merge_col(poker,["S3","C3"],"S3-C3","-")
poker = merge_col(poker,["S4","C4"],"S4-C4","-")
poker = merge_col(poker,["S5","C5"],"S5-C5","-")
print(poker.head())