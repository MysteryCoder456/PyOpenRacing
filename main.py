import pygame
from pygame.locals import *
pygame.init()

from OpenGL.GL import *
from OpenGL.GLU import *


def start():
	# Put any initializing code for the GAME not PROGRAM below this line
	glTranslatef(0, -0.5, -5)
	glRotatef(20, 1, 0, 0)

	global fill, outline, pos, size, vertices, edges, faces

	fill = (1, 0, 0)
	outline = (1, 1, 1)

	size = (0.7, 0.7, 1.5)
	pos = (0, size[1], 0)

	vertices = (
		(pos[0] + size[0], pos[1] - size[1], pos[2] - size[2]), # 0
		(pos[0] + size[0], pos[1] + size[1], pos[2] - size[2]), # 1
		(pos[0] - size[0], pos[1] + size[1], pos[2] - size[2]), # 2
		(pos[0] - size[0], pos[1] - size[1], pos[2] - size[2]), # 3
		(pos[0] + size[0], pos[1] - size[1], pos[2] + size[2]), # 4
		(pos[0] + size[0], pos[1] + size[1], pos[2] + size[2]), # 5
		(pos[0] - size[0], pos[1] + size[1], pos[2] + size[2]), # 6
		(pos[0] - size[0], pos[1] - size[1], pos[2] + size[2])  # 7
	)

	edges = (
		(0, 1),
		(0, 3),
		(0, 4),
		(1, 2),
		(1, 5),
		(2, 3),
		(2, 6),
		(3, 7),
		(4, 5),
		(4, 7),
		(5, 6),
		(6, 7)
	)

	faces = (
		(0, 1, 2, 3),
		(3, 7, 4, 0),
		(2, 3, 7, 6),
		(1, 2, 5, 6),
		(4, 5, 6, 7),
		(0, 1, 4, 5)
	)


def logic():
	# Put all code for game logic here
	global fill, outline, pos, size, vertices, edges, faces


def render():
	global fill, outline, pos, size, vertices, edges, faces

	# Put all rendering code between glClear() and pygame.display.flip()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	# Render Ground
	glBegin(GL_LINES)

	for x in range(-100, 100, 2):
		glVertex3fv((x, 0, -100))
		glVertex3fv((x, 0, 100))

	for z in range(-100, 100, 2):
		glVertex3fv((-100, 0, z))
		glVertex3fv((100, 0, z))

	glEnd()

	# Fill cube
	glBegin(GL_QUADS)
	glColor3fv(fill)

	for face in faces:
		for vertex in face:
			glVertex3fv(vertices[vertex])

	glEnd()

	# Outline cube
	glBegin(GL_LINES)
	glColor3fv(outline)

	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])

	glEnd()

	pygame.display.flip()

















# Change the code below only if absolutely needed!!
def main():
	width = 800
	height = 600
	win = pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
	pygame.display.set_caption("Boilerplate Title")

	clock = pygame.time.Clock()
	running = True
	FPS = 60 # Frames Per Second
	FOV = 75 # Field Of Vision (in degrees)
	render_dist = 50.0

	gluPerspective(FOV, (width / height), 0.1, render_dist)
	start()

	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		logic()
		render()


if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
