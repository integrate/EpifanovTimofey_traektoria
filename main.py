import wrap

wrap.world.create_world(800, 700)
wrap.world.set_back_color(100, 200, 10)
mod = "default"
tochka = []
pacman = None
t2 = 0

@wrap.on_key_down(wrap.K_d)
def mods(pos_x,pos_y):
    global mod,pacman,t2
    if mod == "default":
        mod = "tochka"
        for t in tochka:
            wrap.sprite.remove(t)
        tochka.clear()
        t2 = 0
        t1 = wrap.sprite.add("pacman",pos_x,pos_y)
        tochka.append(t1)
    else:
        mod = "default"
        pacman = wrap.sprite.add("pacman",wrap.sprite.get_x(tochka[0]),wrap.sprite.get_y(tochka[0]),"player2")

@wrap.on_mouse_move()
def tochki(pos_x, pos_y):
    if mod == "tochka":
        t1 = wrap.sprite.add("pacman", pos_x, pos_y)
        tochka.append(t1)

@wrap.always(25)
def pacman1():
    global t2
    if pacman != None and mod == "default":
        x = wrap.sprite.get_x(tochka[t2])
        y = wrap.sprite.get_y(tochka[t2])
        wrap.sprite.set_angle_to_point(pacman,x,y)
        wrap.sprite.move_at_angle_point(pacman,x,y,3)
        if len(tochka)-1 > t2 and wrap.sprite.is_collide_sprite(pacman,tochka[t2]):
            t2 += 1
