import glfw
from OpenGL.GL import *
import numpy as np

class LuxGFX:
    def __init__(self, width=800, height=600, title="LuxGFX Game Engine"):
        if not glfw.init():
            raise Exception("GLFW initialization failed")
        self.width = width
        self.height = height
        self.window = glfw.create_window(width, height, title, None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window creation failed")

        glfw.make_context_current(self.window)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)  # 2D koordinatni sistem
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glfw.set_key_callback(self.window, self._on_key)

        self.keys = {}

    def _on_key(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self.keys[key] = True
        elif action == glfw.RELEASE:
            self.keys[key] = False

    def is_key_pressed(self, key):
        return self.keys.get(key, False)

    def clear(self, r=0, g=0, b=0):
        glClearColor(r, g, b, 1)
        glClear(GL_COLOR_BUFFER_BIT)

    def draw_rect(self, x, y, w, h, color=(1, 1, 1)):
        glColor3f(*color)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + w, y)
        glVertex2f(x + w, y + h)
        glVertex2f(x, y + h)
        glEnd()

    def draw_line(self, x1, y1, x2, y2, color=(1, 1, 1), width=1):
        glLineWidth(width)
        glColor3f(*color)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    def present(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def is_running(self):
        return not glfw.window_should_close(self.window)

    def quit(self):
        glfw.terminate()

    # 🟢 Funkcija za kretanje igrača
    def handle_player_movement(self, player, speed=5):
        if self.is_key_pressed(glfw.KEY_W): player['y'] -= speed
        if self.is_key_pressed(glfw.KEY_S): player['y'] += speed
        if self.is_key_pressed(glfw.KEY_A): player['x'] -= speed
        if self.is_key_pressed(glfw.KEY_D): player['x'] += speed

    # 🔴 Provera sudara (AABB)
    def check_collision(self, rect1, rect2):
        return (
            rect1['x'] < rect2['x'] + rect2['w'] and
            rect1['x'] + rect1['w'] > rect2['x'] and
            rect1['y'] < rect2['y'] + rect2['h'] and
            rect1['y'] + rect1['h'] > rect2['y']
        )