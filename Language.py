# -*- coding: utf-8 -*-


class TranslationTable(object):
    def __init__(self, Chr=None, Uni=None, t1=None, pos=None):
        self.chr_name = Chr
        self.uni_value = Uni
        self.t1_value = t1
        self.t1_pos = pos

    def __str__(self):
        return self.uni_value.encode("UTF-8")

    def __repr__(self):
        return repr(self.uni_value)


class Tamil(object):  # Unicode Tamil
    om = TranslationTable('OM', u'\u0BD0')  # No Anu
    dot = TranslationTable('pulli', u'\u0BCD', u'\xf6')  # No Anu
    leg = TranslationTable('VOWEL SIGN AA', u'\u0BBE', u'V', 1)
    smhorn = TranslationTable('VOWEL SIGN I', u'\u0BBF', u'\xe5')  # No Anu
    bghorn = TranslationTable('VOWEL SIGN II', u'\u0BC0', u'\xe7')  # No Anu
    smu = TranslationTable('VOWEL SIGN U', u'\u0BC1', u'\xe9')  # No Anu
    bguu = TranslationTable('VOWEL SIGN UU', u'\u0BC2', u'\xe8')  # No Anu
    sme = TranslationTable('VOWEL SIGN E', u'\u0BC6', u'\xff', 0)
    bgee = TranslationTable('VOWEL SIGN EE', u'\u0BC7', u'\xba', 0)
    aii = TranslationTable('VOWEL SIGN AI', u'\u0BC8', u'\xc1', 0)
    smo = TranslationTable('VOWEL SIGN O', u'\u0BCA')
    bgoo = TranslationTable('VOWEL SIGN OO', u'\u0BCB')
    smau = TranslationTable('VOWEL SIGN AU', u'\u0BCC')
    llaau = TranslationTable('AU LENGTH MARK', u'\u0BD7')
    signs = [dot, smhorn, bghorn, smu, bguu, sme, bgee, aii, smo, bgoo,
             smau, llaau]
    a = TranslationTable('A', u'\u0B85', u'\u2202')
    aa = TranslationTable('AA', u'\u0B86', u'g')
    i = TranslationTable('I', u'\u0B87', u'\xf7')
    ii = TranslationTable('II', u'\u0B88', u'~')
    u = TranslationTable('U', u'\u0B89', u'c')
    uu = TranslationTable('UU', u'\u0B8A', u'\xaa')
    e = TranslationTable('E', u'\u0B8E', u'\xae')
    ee = TranslationTable('EE', u'\u0B8F', u'\u221e')
    ai = TranslationTable('AI', u'\u0B90', u'n')
    o = TranslationTable('O', u'\u0B92', u'\u0152')
    oo = TranslationTable('OO', u'\u0B93', u'{')
    au = TranslationTable('AU', u'\u0B94', u'\xa1')
    ak = TranslationTable('aytham', u'\u0B83', u'\u2021')
    indep_vowels = [a, aa, i, ii, u, uu, e, ee, ai, o, oo, au, ak]
    ka = TranslationTable('KA', u'\u0B95', u'\xd4')
    nga = TranslationTable('NGA', u'\u0B99', u'\xd9')
    ca = TranslationTable('CA', u'\u0B9A', u'\u0192')
    ja = TranslationTable('JA', u'\u0B9C', u'\xd6')
    nya = TranslationTable('NYA', u'\u0B9E', u'Q')
    tta = TranslationTable('TTA', u'\u0B9F', u'\xb6')
    nna = TranslationTable('NNA', u'\u0BA3', u'\xdc')
    ta = TranslationTable('TA', u'\u0BA4', u'>')
    na = TranslationTable('NA', u'\u0BA8', u'\xc2')
    nnna = TranslationTable('NNNA', u'\u0BA9', u'\u2122')
    pa = TranslationTable('PA', u'\u0BAA', u'\u221a')
    ma = TranslationTable('MA', u'\u0BAE', u'\\')
    ya = TranslationTable('YA', u'\u0BAF', u'B')
    ra = TranslationTable('RA', u'\u0BB0', u'\xb4')
    rra = TranslationTable('RRA', u'\u0BB1', u'\u2248')
    la = TranslationTable('LA', u'\u0BB2', u'\xc8')
    lla = TranslationTable('LLA', u'\u0BB3', u'e')
    llla = TranslationTable('LLLA', u'\u0BB4', u'w')
    va = TranslationTable('VA', u'\u0BB5', u'k')
    cons = [ka, nga, ca, ja, nya, tta, nna, ta, na, nnna, pa, ma, ya, ra, rra,
            la, lla, llla, va]
    sha = TranslationTable('SHA', u'\u0BB6')
    ssa = TranslationTable('SSA', u'\u0BB7', u'\u2260')
    sa = TranslationTable('SA', u'\u0BB8', u'v')
    ha = TranslationTable('HA', u'\u0BB9', u'\xab')
    fancy = [sha, ssa, sa, ha]

tm = Tamil()
trans = {}
anu_consDot = unicode("¬∫áÎâ‚ı›Õ[©DFÏu_^µÀ", "UTF-8")
anu_smhorn = unicode("˛EÉË]WM∏tlˆ§oÑas", "UTF-8")
anu_bghorn = unicode("ˇÊœßy¿Ã¨*XZS‹C—T", "UTF-8")
anu_smu = unicode("zà|ÓmO–Ax•ÚÆK”ø°", "UTF-8")
anu_bguu = unicode("ÌÛ˘I#±˚ØJR‘GŸjÒ∆", "UTF-8")
tm_smhorn = []
tm_bghorn = []
tm_smu = []
tm_bguu = []
tm_sme = []
tm_bgee = []
tm_ai = []
tm_smo = []
tm_bgoo = []
tm_smau = []


for x in tm.indep_vowels+tm.cons+tm.fancy:
    trans[x.uni_value] = x.t1_value

trans[tm.leg.uni_value] = tm.leg.t1_value

for i, x in enumerate(tm.cons):
    tm_smhorn.append(x.uni_value+tm.smhorn.uni_value)
    tm_bghorn.append(x.uni_value+tm.bghorn.uni_value)
    tm_smu.append(x.uni_value+tm.smu.uni_value)
    tm_bguu.append(x.uni_value+tm.bguu.uni_value)
    tm_sme.append(x.uni_value+tm.sme.uni_value)
    tm_bgee.append(x.uni_value+tm.bgee.uni_value)
    tm_ai.append(x.uni_value+tm.aii.uni_value)
    tm_smo.append(x.uni_value+tm.smo.uni_value)
    tm_bgoo.append(x.uni_value+tm.bgoo.uni_value)
    tm_smau.append(x.uni_value+tm.smau.uni_value)
    cons_dot = x.uni_value+tm.dot.uni_value
    trans[cons_dot] = anu_consDot[i]

#TODO check and update if AnuFonts support the characters
tm_smhorn.pop(1)  # ஙி not in Anu
tm_smhorn.pop(2)  # ஜி not in Anu
tm_smhorn.pop(2)  # ஞி not in Anu

tm_bghorn.pop(1)  # ஙீ not in Anu
tm_bghorn.pop(2)  # ஜீ not in Anu
tm_bghorn.pop(2)  # ஞீ not in Anu

tm_smu.pop(1)  # ஙு not in Anu
tm_smu.pop(2)  # ஜு not in Anu
tm_smu.pop(2)  # ஞு not in Anu

tm_bguu.pop(1)  # ஙூ not in Anu
tm_bguu.pop(2)  # ஜூ not in Anu
tm_bguu.pop(2)  # ஞூ not in Anu

for i, x in enumerate(tm_smhorn):
    trans[x] = anu_smhorn[i]

for i, x in enumerate(tm_bghorn):
    trans[x] = anu_bghorn[i]

for i, x in enumerate(tm_smu):
    trans[x] = anu_smu[i]

for i, x in enumerate(tm_bguu):
    trans[x] = anu_bguu[i]

for i, x in enumerate(tm_sme):
    trans[x] = tm.sme.t1_value+tm.cons[i].t1_value

for i, x in enumerate(tm_bgee):
    trans[x] = tm.bgee.t1_value+tm.cons[i].t1_value

for i, x in enumerate(tm_ai):
    trans[x] = tm.aii.t1_value+tm.cons[i].t1_value

for i, x in enumerate(tm_smo):
    trans[x] = tm.sme.t1_value+tm.cons[i].t1_value+tm.leg.t1_value

for i, x in enumerate(tm_bgoo):
    trans[x] = tm.bgee.t1_value+tm.cons[i].t1_value+tm.leg.t1_value

for i, x in enumerate(tm_smau):
    trans[x] = tm.sme.t1_value+tm.cons[i].t1_value+tm.lla.t1_value
