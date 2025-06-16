import luxgfx
import time
import random

app = luxgfx.LuxGFX(800, 600, "LuxGFX Game Example")

player = {'x': 400, 'y': 300, 'w': 50, 'h': 50, 'color': (0, 1, 0)}
enemy = {'x': random.randint(0, 750), 'y': random.randint(0, 550), 'w': 50, 'h': 50, 'color': (1, 0, 0)}

while app.is_running():
    app.clear(0.1, 0.1, 0.1)

    app.handle_player_movement(player, speed=5)
    app.draw_rect(player['x'], player['y'], player['w'], player['h'], player['color'])
    app.draw_rect(enemy['x'], enemy['y'], enemy['w'], enemy['h'], enemy['color'])

    if app.check_collision(player, enemy):
        print("Sudar!")
        enemy['x'] = random.randint(0, 750)
        enemy['y'] = random.randint(0, 550)

    app.present()
    time.sleep(0.01)

app.quit()