
import numpy as np

def load_data(fpath_in):
	# preparations...
	
	fo = open(fpath_in, "r")
	lines = fo.readlines()
	fo.close()
	N = len(lines)-2    
	n = 0               
	headers = (lines[1].strip()).split(',')
	y_col = len(headers)
	M = y_col - 1      
	X = np.zeros((N,M))
	y = np.zeros(N)
	
	for ix in range(2,len(lines)):
		rec = (lines[ix].strip()).split(',')
		for j in range(0,M):
			X[n,j] = float(rec[j])
			y[n] = float(rec[-1])
		n += 1
	return M,N,X,y,headers
	
