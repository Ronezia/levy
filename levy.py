import random

import pygame

from p5 import core


def setup():
	print("Setup START---------")
	core.fps = 30
	core.WINDOW_SIZE= [400, 400]
	core.WINDOW_SIZE = [400, 400]
	core.memory("Pos",[200, 200])
	core.memory("Prev", [200, 200])
	core.memory("username", "Bob")
	core.memory("Prespos", [200, 200])




	print("Setup END----------")

def norme(v):
	return math.sqrt(v.x**2+v.y**2)

def normaliser(v):
	if norme(v) !=0:
		vectNorm= [v.x, v.y]
		f = [v.x, v.y]
		vectNorm.x = vectNorm.x / norme(f)
		vectNorm.y = vectNorm.y / norme(f)
		return vectNorm
	else:
		return[0,0]




def scale(v,a):
	return[v.x * a,v.y *a]

def run():

	core.memory("newX", 0)
	core.memory("newY", 0)

	core.memory("pas", random.randint(0, 99))
	if core.memory("pas")<10:
		core.memory("saut", 5)
	else :
		core.memory("saut", 5)


	def turnvector(v,a):
		if norme() != 0:
			a1= angle([0.1],v)
			a1= a1+a
			v1= [cos(a1),sin(a1)]
			scale(v1,norme(v))
			return v1

	def angle(v,v1):
		v2=v
		v3=v1
		if norme(v)!= 0:
			if norme(v1) !=0:
				v2 = normaliser(v2)
				v3 = normaliser(v3)
				cos = v2[0]*V3[0]+v2[1]*v3[1]
				sin = v2[0]*V3[0]-v2[1]*v3[1]
				angle = atan2 (sin,cos)
				return angle




	core.memory("nombreAleatoire",random.randint(0,3))


	if core.memory("nombreAleatoire") == 0:
		core.memory("newX", core.memory("Pos")[0]+ core.memory("saut"))
		core.memory("newY",core.memory("Pos")[1])
	if core.memory("nombreAleatoire") == 1:
		core.memory("newX", core.memory("Pos")[0])
		core.memory("newY",core.memory("Pos")[1]+core.memory("saut"))
	if core.memory("nombreAleatoire") == 2:
		core.memory("newX",core.memory("Pos")[0]-core.memory("saut"))
		core.memory("newY",core.memory("Pos")[1])
	if core.memory("nombreAleatoire") == 3:
		core.memory("newX",core.memory("Pos")[0])
		core.memory("newY",core.memory("Pos")[1]-core.memory("saut"))





	core.memory("Prespos",core.memory("Pos"))
	core.memory("Prev", [core.memory("newX"), core.memory("newY")])
	core.memory("Pos", [core.memory("newX"), core.memory("newY")])

	#pygame.draw.circle(core.screen,(255,255,255),core.memory("Pos"),10)
	pygame.draw.line(core.screen, (147, 152, 255), core.memory("Prespos"), core.memory("Pos"),2)




core.main(setup, run)