def collision(sprite, otherSprite):
    sprite.destroy(effects.fire, 1000)
    otherSprite.destroy(effects.fire, 1000)
    scene.camera_shake(20, 1000)
    music.big_crash.play()
    pause(1000)
    info.player1.change_life_by(-1)

def hit(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    scene.camera_shake(20, 500)
    music.big_crash.play()
    info.player1.change_score_by(1)

def fire():
    laser = sprites.create_projectile_from_sprite(img("""
        . . . . . . 9 9 9 . . . . . . .
        . . . . . 9 9 1 9 9 . . . . . .
        . . . . . 9 1 1 1 9 . . . . . .
        . . . . . 9 1 1 1 9 . . . . . .
        . . . . . 9 1 1 1 9 . . . . . .
        . . . . . 9 9 1 9 9 . . . . . .
        . . . . . . 9 1 9 . . . . . . .
        . . . . . . 9 1 9 . . . . . . .
        . . . . . . 9 9 9 . . . . . . .
        . . . . . . 9 9 9 . . . . . . .
        . . . . . . . 9 . . . . . . . .
        . . . . . . . 9 . . . . . . . .
        . . . . . . . 9 . . . . . . . .
        . . . . . . . 9 . . . . . . . .
        . . . . . . . 9 . . . . . . . .
        . . . . . . . 9 . . . . . . . .
    """), spaceship, 0, -50)
    laser.set_kind(SpriteKind.projectile)
    music.pew_pew.play()
    laser.set_flag(SpriteFlag.AUTO_DESTROY, True)

def spawner():
    yVel = randint(20, 50)
    asteroid = sprites.create_projectile_from_sprite(img("""
        . . . . . . . c c c a c . . . .
        . . c c b b b a c a a a c . . .
        . c c a b a c b a a a b c c . .
        . c a b c f f f b a b b b a . .
        . c a c f f f 8 a b b b b b a .
        . c a 8 f f 8 c a b b b b b a .
        c c c a c c c c a b c f a b c c
        c c a a a c c c a c f f c b b a
        c c a b 6 a c c a f f c c b b a
        c a b c 8 6 c c a a a b b c b c
        c a c f f a c c a f a c c c b .
        c a 8 f c c b a f f c b c c c .
        . c b c c c c b f c a b b a c .
        . . a b b b b b b b b b b b c .
        . . . c c c c b b b b b c c . .
        . . . . . . . . c b b c . . . .
    """), None, 0, yVel)

    xPos = randint(0, scene.screen_width())
    asteroid.set_position(xPos, 0)
    asteroid.set_kind(SpriteKind.enemy)
    asteroid.set_flag(SpriteFlag.AUTO_DESTROY, True)

# Background
effects.star_field.start_screen_effect()

# Set Score and Life
info.player1.set_life(1)
info.player1.set_score(0)

# Spaceship
spaceship = sprites.create(img("""
    . . . . . . . c d . . . . . . .
    . . . . . . . c d . . . . . . .
    . . . . . . 8 c d 8 . . . . . .
    . . . . . 8 8 c b 8 8 . . . . .
    . . . . . . . f f . . . . . . .
    . . . . . . . c 6 . . . . . . .
    . . . . . . . f f . . . . . . .
    . . . . . . . 8 6 . . . . . . .
    . . . . . . 8 8 9 8 . . . . . .
    . . . . . . 8 6 9 8 . . . . . .
    . . . . . c c c 8 8 8 . . . . .
    . . . . 8 8 6 6 6 9 8 8 . . . .
    . . 8 f f f c c e e f f 8 8 . .
    . 8 8 8 8 8 8 6 6 6 6 9 6 8 8 .
    8 8 8 8 8 8 8 8 6 6 6 9 6 6 8 8
    8 8 8 8 8 8 8 8 6 6 6 6 9 6 8 8
"""))
spaceship.set_position(75, 111)
spaceship.set_kind(SpriteKind.player)
controller.move_sprite(spaceship, 100, 0)
spaceship.set_stay_in_screen(True)

# Spawn Asteroids
game.on_update_interval(1000, spawner)

# Set up the fire button
controller.A.on_event(ControllerButtonEvent.PRESSED, fire)

# Check for collisions
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, collision)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, hit)