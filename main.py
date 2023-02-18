import wrap,random

wrap.world.create_world(800, 700)
wrap.world.set_back_color(100, 200, 10)
mod = "default"
tochka = []
pacman = None
t2 = 0
spisok_pacman = []
spisok_celey_pacman = []



def delete_tochka():
    for t in tochka:
        wrap.sprite.remove(t)
    tochka.clear()


def create_tochka(pos_x, pos_y):
    t1 = wrap.sprite.add("pacman", pos_x, pos_y)
    tochka.append(t1)


def create_pacman():
    pacman = wrap.sprite.add("pacman", wrap.sprite.get_x(tochka[0]), wrap.sprite.get_y(tochka[0]), "player2")
    spisok_pacman.append(pacman)
    spisok_celey_pacman.append(0)


@wrap.on_key_down(wrap.K_d)
def mods(pos_x, pos_y):
    global mod, pacman, t2
    if mod == "default":
        mod = "tochka"
        delete_tochka()
        t2 = 0
        create_tochka(pos_x, pos_y)
    else:
        mod = "default"



@wrap.on_mouse_move()
def tochki(pos_x, pos_y):
    if mod == "tochka":
        create_tochka(pos_x, pos_y)


@wrap.always(25)
def pacman1():
    global t2
    if mod == "default":
        for pacman3 in spisok_pacman:
            nomer_pacman = spisok_pacman.index(pacman3)
            nomer_tochki = spisok_celey_pacman[nomer_pacman]
            idtochki = tochka[nomer_tochki]
            x = wrap.sprite.get_x(idtochki)
            y = wrap.sprite.get_y(idtochki)
            wrap.sprite.set_angle_to_point(pacman3, x, y)
            wrap.sprite.move_at_angle_point(pacman3, x, y, random.randint(1,6))
            if wrap.sprite.is_collide_sprite(pacman3, idtochki) and len(tochka) > nomer_tochki+1:
                spisok_celey_pacman[nomer_pacman] += 1


@wrap.always(1000)
def pacman2():
    if len(tochka) >= 1 and mod == "default":
        create_pacman()

