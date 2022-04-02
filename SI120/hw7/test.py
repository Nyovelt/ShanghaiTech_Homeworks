# -*- coding: utf-8 -*-
from math import gcd
from typing import Tuple
from random import randint
import sys


def exgcd(a: int, b: int) -> Tuple[int, int]:
    # ax + by = \gcd(a, b)
    if b == 0:
        return 1, 0
    y, x = exgcd(b, a % b)
    return x, y - a // b * x


def inv(x: int, mod: int) -> int:
    return exgcd(x, mod)[0] % mod


def millerRabin(p: int) -> bool:
    def witness(v: int, p: int) -> bool:
        r, s, x = p - 1, 0, 0
        while ~r & 1:
            s += 1
            r >>= 1
        x = pow(v, r, p)
        if x == 1 or x == p - 1:
            return False
        while s:
            x = x * x % p
            if x == p - 1:
                return False
            s -= 1
        return True

    if p == 2:
        return True
    if p < 2 or not (p & 1):
        return False
    PRIME = [3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in PRIME:
        if p == i:
            return True
        if witness(i, p):
            return False
    for i in range(20):
        r = randint(2, p - 1)
        if witness(r, p):
            return False
    return True


class RSA:
    def __init__(self):
        self.e = self.d = self.phi = self.p = self.q = self.n = 0

    def generate(self, length: int) -> None:
        lower = 2 ** length
        upper = lower * 2 - 1
        while not millerRabin(self.p):
            self.p = randint(lower, upper)
        while self.q == self.p or not millerRabin(self.q):
            self.q = randint(lower, upper)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        while gcd(self.phi, self.e) != 1:
            self.e = randint(2, self.phi)
        self.d = inv(self.e, self.phi)

    def encrypt(self, m: int, key=None) -> int:
        if key is None:
            key = (self.e, self.n)
        return pow(m, key[0], key[1])

    def decrypt(self, c: int, key=None) -> int:
        if key is None:
            key = (self.d, self.n)
        return pow(c, key[0], key[1])

    def getPrivateKey(self) -> Tuple[int, int]:
        return self.d, self.n

    def getPublicKey(self) -> Tuple[int, int]:
        return self.e, self.n


if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    d = RSA()
#     d.generate(1024)
#     print(r'private: {d.getPrivateKey()}\npublic: {d.getPublicKey()}')
#     m = 998244353
#     c = d.encrypt(998244353)
#     print(d.encrypt(m))
#     print(d.decrypt(c))
#     assert d.decrypt(d.encrypt(m)) == m
#     while True:
#         m = int(input("please input a message"))
#         if m <= 0:
#             break
#         print(d.encrypt(m))
#         assert d.decrypt(d.encrypt(m)) == m
    e = 4099852173630681822722339660229701793484497077549023050739406744299194740794285841565894857183257305962091658478256403457898496259755474199072635097327398971990092224918103250375455707498928712201945370461644425637423044616348028546654820134532012544433519158531485300462390097592776352017667386632661678681500542766835469056490039928380877979712159080905348869475217939844173751698241442662611990406492300411900572847532884748092860563495914734527293634873292356463076178294881900968373918292064527855306925898818421646057616238873254251939953144948550922456255743607156013509822605943382352582252129366170771186337
    p = 92848022024833655041372304737256052921065477715975001419347548380734496823522565044177931242947122534563813415992433917108481569319894167972639736788613656007853719476736625612543893748136536594494005487213485785676333621181690463942417781763743640447405597892807333854156631166426238815716390011586838580891
    q = 149600854933825512159828331527177109689118555212385170831387365804008437367913613643959968668965614270559113472851544758183282789643129469226548555150464780229538086590498853718102052468519876788192865092229749643546710793464305243815836267024770081889047200172952438000587807986096107675012284269101785114471
    c = 1965004133006974659995314560167723896560162823992014763466676295156568780181324759118466356116827422439409513865820570400810380977333397895810023254515182242123244875173658899005048988942666876614798046351776061310094809679938914368938218289806790724992660151078718864505196754907261135221257146114289875149015431301569207527108638684989789729747097766650481983822742788958528594215002940645806662061041825912562593269329369550470854629711422167160350497882132054038403027493105855840606846063029571758386220434189610971724518330438082401592895354255430599515214166039595157639322144199213475742435020500518884278854
    i = inv(e, (p-1)*(q-1))
    print(d.decrypt(c, (i, p*q)))