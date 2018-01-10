#scipy.io.loadmat() cargar archivos
#scipy.io.savemat()	escribir archivos
import scipy.io
filename = "workspace.mat"

mat = scipy.io.loadmat(filename)

print (type(mat[x]))