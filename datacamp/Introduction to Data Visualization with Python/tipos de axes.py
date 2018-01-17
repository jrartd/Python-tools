#normal
axes(x,y,width,height)

plt.xlim((1900,2017)) #definir ancho de x
plt.ylim((0,1000)) 	#definir largo de y

plt.axis((1990,2010,0,50)) #definir en una sola linea
axis("equal") #proporcion igual de x y y  	
axis("tight") #ajusta toda la data

plt.tight_layout() ajusta toda la ventana