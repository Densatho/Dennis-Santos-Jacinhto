class Agua:
    def __init__(self, nv):
        self.nome = 'Magia Azul Rank ' + nv
        self.a = [Azul1(1)]
        if nv == 'E' or nv == 'D' or nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Azul1(2)
        if nv == 'D' or nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a.append(Azul2(1, 'F'))
            self.a[0] = Azul1(3)
        if nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Azul1(4)
            self.a[1] = Azul2(2, 'E')
        if nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Azul1(5)
            self.a[1] = Azul2(3, 'D')
        if nv == 'A' or nv == 'S':
            self.a[0] = Azul1(6)
            self.a[1] = Azul2(4, 'C')
        if nv == 'S':
            self.a[0] = Azul1(7)
            self.a[1] = Azul2(5, 'B')
            self.a.append(Azul3('S', 'A'))


class Fogo:
    def __init__(self, nv):
        self.nome = 'Magia Vermelha Rank ' + nv
        self.a = [Vermelho1(1)]
        if nv == 'E' or nv == 'D' or nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Vermelho1(2)
        if nv == 'D' or nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a.append(Vermelho2(1, 'F'))
            self.a[0] = Vermelho1(3)
        if nv == 'C' or nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Vermelho1(4)
            self.a[1] = Vermelho2(2, 'E')
        if nv == 'B' or nv == 'A' or nv == 'S':
            self.a[0] = Vermelho1(5)
            self.a[1] = Vermelho2(3, 'D')
        if nv == 'A' or nv == 'S':
            self.a[0] = Vermelho1(6)
            self.a[1] = Vermelho2(4, 'C')
        if nv == 'S':
            self.a[0] = Vermelho1(7)
            self.a[1] = Vermelho2(5, 'B')
            self.a.append(Vermelho3('S'))


class Vermelho1:
    def __init__(self, nv):
        self.d = 10*nv
        self.nome = 'Fire bolt'
        self.mc = 5 + ((nv-1)*4)
        self.effect = 'none'


class Vermelho2:
    def __init__(self, nv, r):
        self.d = 50+((nv-1)*18)
        self.nome = 'Fireball'
        self.mc = 18+((nv-1)*6)
        self.effect = ['Queimadura '+r]


class Vermelho3:
    def __init__(self, r):
        self.d = 160
        self.nome = 'Fire Blast'
        self.mc = 180
        self.effect = ['Queimadura '+r]


class Azul1:
    def __init__(self, nv):
        self.d = 8*nv
        self.nome = 'Jato de\nAgua'
        self.mc = 3+((nv-1)*3)
        self.effect = 'none'


class Azul2:
    def __init__(self, nv, r):
        self.d = 40+((nv-1)*15)
        self.nome = 'Laminas de\nAgua'
        self.mc = 15+((nv-1)*5)
        self.effect = ['Sangramento '+r]


class Azul3:
    def __init__(self, r, r1):
        self.d = 120
        self.nome = 'Estacas de\nGelo'
        self.mc = 150
        self.effect = ['Lentidão '+r, 'Sangramento'+r1]


class Monster:
    def __init__(self, nv, r):
        self.nome = ''
        self.vida = 1
        self.vida_m = 1
        self.d = 1
        self.t = 1
        self.r = 1
        self.s = 1
        self.xp = 0
        self.nv = nv
        if r < 6:
            self.slime()
        elif r < 9:
            self.bigslime()
        elif r < 12:
            self.subdragon()
        elif r < 15:
            self.leao()
        elif r < 17:
            self.hidra()

    def slime(self):
        self.nome = 'Slime'
        self.vida = 12 + 4 * (self.nv - 1)
        self.vida_m = self.vida
        self.d = 3 + 3 * (self.nv - 1)
        self.t = 3 + self.nv - 1
        self.r = self.nv - 1
        self.s = 2 * (self.nv - 1)
        self.xp = 5 * self.nv

    def bigslime(self):
        self.nome = 'Big Silme'
        self.vida = 32 + 4 * (self.nv - 1)
        self.vida_m = self.vida
        self.d = 11 + 4 * (self.nv - 2)
        self.t = 14 + 2 * (self.nv - 1)
        self.r = 3 * self.nv
        self.s = 2 + 2 * self.nv
        self.xp = 10 * self.nv

    def subdragon(self):
        self.nome = 'Lacaio dos Dragões'
        self.vida = 5 * self.nv
        self.vida_m = self.vida
        self.d = 6 + 5 * self.nv
        self.t = 9 + 3 * (self.nv - 1)
        self.r = 2 * self.nv
        self.s = 6 + 3 * self.nv
        self.xp = 15 * self.nv
        
    def leao(self):
        self.nome = 'Leão Albino'
        self.vida = 15 + 5 * self.nv
        self.vida_m = self.vida
        self.d = 6 + 5 * self.nv
        self.t = 12 + 3 * (self.nv - 1)
        self.r = 2 * self.nv
        self.s = 16 + 2 * self.nv
        self.xp = 22 * self.nv
        
    def hidra(self):
        self.nome = 'Hidra'
        self.vida = 7 * self.nv
        self.vida_m = self.vida
        self.d = 17 + 5 * self.nv
        self.t = 18 + 3 * (self.nv - 1)
        self.r = 4 * self.nv
        self.s = 8 + 3 * self.nv
        self.xp = 28 * self.nv


class Player:
    def __init__(self):
        self.vida = 15           # vida
        self.vida_m = self.vida  # vida maxima
        self.d = 5               # dano
        self.t = 3               # tecnica
        self.i = 10              # inteligencia
        self.m = 15              # mana
        self.mm = self.m         # mana maxima
        self.r = 5               # resistencia
        self.s = 3               # velocidade


def letra(lt):
    if lt == 'F':
        lt = 'E'
    elif lt == 'E':
        lt = 'D'
    elif lt == 'D':
        lt = 'C'
    elif lt == 'C':
        lt = 'B'
    elif lt == 'B':
        lt = 'A'
    elif lt == 'A':
        lt = 'S'
    return lt


def custo(t1):
    a = 0
    if t1 == 'F':
        a = 10
    elif t1 == 'E':
        a = 20
    elif t1 == 'D':
        a = 40
    elif t1 == 'C':
        a = 80
    elif t1 == 'B':
        a = 160
    elif t1 == 'A':
        a = 320
    elif t1 == 'S':
        a = 640        
    return a


def rankefeito(t1):
    a = 0
    if t1 == 'F':
        a = 1
    elif t1 == 'E':
        a = 2
    elif t1 == 'D':
        a = 3
    elif t1 == 'C':
        a = 4
    elif t1 == 'B':
        a = 5
    elif t1 == 'A':
        a = 6
    elif t1 == 'S':
        a = 7       
    return a


"""
Veneno - 1% por rank de dano por 3 turnos                                                                    1
Sangramento = 0.5% por rank de dano por 5 turnos                                                             2
Queimadura = -7% por rank Resistencia por 3 turnos                                                           3
Lentidão = -10% por rank velocidade por 3 turnos                                                             4
Selo Magico = Sem Habilidades Magicas por 4 turnos                                                           5
Distração = -3% por rank de resistencia e o inimigo perde um turno                                           6
Prisão = inimigo perde 2 turnos                                                                              7
Speed = +20% por rank de velocidade por 3 turnos                                                             8
Chuva Magica = Recuperação de +5% por rank de vida por 4 turnos                                              9
Armadura = +10% por rank de Resistencia por 3 turnos                                                         10
Maldição de mana = -5% por rank de mana por 5 turnos                                                         11
Roubo de vida = tira a vida do inimigo e aumenta uma porcentagem(5% por rank) do dano dado a sua vida        12
"""


def verific(x):  # if(self.p[5][self.VE[0]].a[0].effect != 'none'):
    e = [[0.1, 0], [0.1, 0], [0.1, 0], [0.1, 0], [False, 0], 0, [False, 0], [0.1, 0], [0.1, 0], [0.1, 0], [0.1, 0], 0]
    if x == 'none':
        return e
    tam = len(x)
    for i in range(0, tam):
        if x[i][0:-2] == 'Veneno':
            aux = rankefeito(x[i][-1])
            e[0][0] = float('{:4.4}'.format(1 - ((1*aux)/100)))
            e[0][1] = 3
        elif x[i][0:-2] == 'Sangramento':
            aux = rankefeito(x[i][-1])
            e[1][0] = float('{:4.4}'.format(1 - ((0.5*aux)/100)))
            e[1][1] = 5
        elif x[i][0:-2] == 'Queimadura':
            aux = rankefeito(x[i][-1])
            e[2][0] = float('{:4.4}'.format(1 - ((aux*7)/100)))
            e[2][1] = 3
        elif x[i][0:-2] == 'Lentidão':
            aux = rankefeito(x[i][-1])
            e[3][0] = float('{:4.4}'.format(1 - ((aux*10)/100)))
            e[3][1] = 3
        elif x[i] == 'Selo Magico':
            e[4][0] = True
            e[4][1] = 4
        elif x[i][0:-2] == 'Distração':
            aux = rankefeito(x[i][-1])
            e[5][0] = float('{:4.4}'.format(1 - ((3*aux)/100)))
            e[5][1] = 1
        elif x[i][0:-2] == 'Prisão':
            e[6][0] = True
            e[6][1] = 2
        elif x[i][0:-2] == 'Speed':
            aux = rankefeito(x[i][-1])
            e[7][0] = float('{:4.4}'.format(1 + ((20*aux)/100)))
            e[7][1] = 3            
        elif x[i][0:-2] == 'Chuva Magica':
            aux = rankefeito(x[i][-1])
            e[8][0] = float('{:4.4}'.format(1 + ((5*aux)/100)))
            e[8][1] = 4
        elif x[i][0:-2] == 'Armadura':
            aux = rankefeito(x[i][-1])
            e[9][0] = float('{:4.4}'.format(1 + ((10*aux)/100)))
            e[9][1] = 1
        elif x[i][0:-2] == 'Maldição de mana':
            aux = rankefeito(x[i][-1])
            e[10][0] = float('{:4.4}'.format(1 - ((aux*5)/100)))
            e[10][1] = 5
        elif x[i][0:-2] == 'Roubo de vida':
            aux = rankefeito(x[i][-1])
            e[11] = float('{:4.4}'.format(1 + ((5*aux)/100)))
    return e

#   aux = dano(rB, x, 0, self.p[1].r, self.m.d, False) - monstro
#   aux = dano(rB, x, 0, self.p[1].r, self.m.d, False) - monstro
#   aux = dano(rA, x, self.dm, self.m.r, self.p[1].d, self.hih) - Player


def dano(a, b, c, d, e, f):
    if a >= b:
        if f and int(c) > d:
            x = int(int(c) - (d/2))
        elif e > d and not f:
            x = e - d
        else:
            x = 0
    else:
        x = 0
    return x


def atkb(x, w, y, z):   # atkb(1, self.AZ[0], self.p[1].m, self.p)
    r1 = int(z[5][w].a[x].d * (z[1].i/50))
    r2 = y - z[5][w].a[x].mc
    return r1, r2
