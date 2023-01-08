import pygame
import math
import numpy as np

pygame.init()

# display parameters
WHITE = (255, 255, 255) # font colour
OFFBLACK = (20, 20, 20) # screen colour 

WIDTH = 1920 # // 2
HEIGHT = 1080 # // 2

dx = 10 # // 2
dy = 20 # // 2

rows = HEIGHT // dy
columns = WIDTH // dx
screen_size = rows * columns

x_start, y_start = 0, 0
x_offset, y_offset = columns / 2, rows / 2

# animation parameters
A, B = 0, 0

theta_spacing = 0.07
phi_spacing = 0.02

theta_range = np.arange(0, 2 * math.pi, theta_spacing)
phi_range = np.arange(0, 2 * math.pi, phi_spacing)

chars = ".,-~:;=!*#$@" # luminanace index

# init display 
display_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DONUT!!!")
font = pygame.font.SysFont('Arial', 18, bold=True)

# function to display texts
def display_text(letter, x_start, y_start):
    text = font.render(str(letter), True, WHITE)
    display_window.blit(text, (x_start, y_start))

# spin the donut!
run = True
while run:
    display_window.fill(OFFBLACK)

    z = [0] * screen_size
    b = [' '] * screen_size

    # donut math
    sinA = math.sin(A)
    sinB = math.sin(B)
    cosA = math.cos(A)
    cosB = math.cos(B)
    for ii in range(len(theta_range) - 1):
        theta = theta_range[ii]
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)
        h = cosTheta + 2
        for ii in range(len(phi_range) - 1):
            phi = phi_range[ii]
            cosPhi = math.cos(phi)
            sinPhi = math.sin(phi)

            D = 1 / (sinPhi * h * sinA + sinTheta * cosA + 5)
            t = sinPhi * h * cosA - sinTheta * sinA 
            x = int(x_offset + 40 * D * (cosPhi * h * cosB - t * sinB))
            y = int(y_offset + 20 * D * (cosPhi * h * sinB + t * cosB))
            o = int(x + columns * y)
            N = int(8 * ((sinTheta * sinA - sinPhi * cosTheta * cosA) * cosB - sinPhi * cosTheta * sinA - sinTheta * cosA - cosPhi * cosTheta * sinB))# luminance 
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * dy - dy:
        y_start = 0

    for ii in range(len(b)):
        A += 0.000002 * 10
        B += 0.000001 * 10
        if ii == 0 or ii % columns:
            display_text(b[ii], x_start, y_start)
            x_start += dx
        else:
            y_start += dy 
            x_start = 0
            display_text(b[ii], x_start, y_start)
            x_start += dx

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




 

