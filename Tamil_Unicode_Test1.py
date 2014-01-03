# -*- coding: utf-8 -*-


class TranslationTable(object):
    def __init__(self, Chr=None, Uni=None, t1=None):
        self.chr_name = Chr
        self.uni_value = Uni
        self.t1_value = t1


class Tamil(object):  # Unicode Tamil
    om = TranslationTable('OM', u'\u0BD0')
    dot = TranslationTable('pulli', u'\u0BCD')
    leg = TranslationTable('VOWEL SIGN AA', u'\u0BBE')
    smhorn = TranslationTable('VOWEL SIGN I', u'\u0BBF')
    bghorn = TranslationTable('VOWEL SIGN II', u'\u0BC0')
    smu = TranslationTable('VOWEL SIGN U', u'\u0BC1')
    bguu = TranslationTable('VOWEL SIGN UU', u'\u0BC2')
    sme = TranslationTable('VOWEL SIGN E', u'\u0BC6')
    bgee = TranslationTable('VOWEL SIGN EE', u'\u0BC7')
    aii = TranslationTable('VOWEL SIGN AI', u'\u0BC8')
    smo = TranslationTable('VOWEL SIGN O', u'\u0BCA')
    bgoo = TranslationTable('VOWEL SIGN OO', u'\u0BCB')
    smau = TranslationTable('VOWEL SIGN AU', u'\u0BCC')
    llaau = TranslationTable('AU LENGTH MARK', u'\u0BD7')
    signs = [dot, leg, smhorn, bghorn, smu, bguu, sme, bgee, aii, smo, bgoo,
             smau, llaau]
    a = TranslationTable('A', u'\u0B85')
    aa = TranslationTable('AA', u'\u0B86')
    i = TranslationTable('I', u'\u0B87')
    ii = TranslationTable('II', u'\u0B88')
    u = TranslationTable('U', u'\u0B89')
    uu = TranslationTable('UU', u'\u0B8A')
    e = TranslationTable('E', u'\u0B8E')
    ee = TranslationTable('EE', u'\u0B8F')
    ai = TranslationTable('AI', u'\u0B90')
    o = TranslationTable('O', u'\u0B92')
    oo = TranslationTable('OO', u'\u0B93')
    au = TranslationTable('AU', u'\u0B94')
    ak = TranslationTable('aytham', u'\u0B83')
    indep_vowels = [a, aa, i, ii, u, uu, e, ee, ai, o, oo, au, ak]
    ka = TranslationTable('KA', u'\u0B95')
    nga = TranslationTable('NGA', u'\u0B99')
    ca = TranslationTable('CA', u'\u0B9A')
    ja = TranslationTable('JA', u'\u0B9C')
    nya = TranslationTable('NYA', u'\u0B9E')
    tta = TranslationTable('TTA', u'\u0B9F')
    nna = TranslationTable('NNA', u'\u0BA3')
    ta = TranslationTable('TA', u'\u0BA4')
    na = TranslationTable('NA', u'\u0BA8')
    nnna = TranslationTable('NNNA', u'\u0BA9')
    pa = TranslationTable('PA', u'\u0BAA')
    ma = TranslationTable('MA', u'\u0BAE')
    ya = TranslationTable('YA', u'\u0BAF')
    ra = TranslationTable('RA', u'\u0BB0')
    rra = TranslationTable('RRA', u'\u0BB1')
    la = TranslationTable('LA', u'\u0BB2')
    lla = TranslationTable('LLA', u'\u0BB3')
    llla = TranslationTable('LLLA', u'\u0BB4')
    va = TranslationTable('VA', u'\u0BB5')
    cons = [ka, nga, ca, ja, nya, tta, nna, ta, na, nnna, pa, ma, ya, ra, rra,
            la, lla, llla, va]

tm = Tamil()
#for i in tm.indep_vowels: print i.uni_value
#for i in tm.cons: print i.uni_value
for i in tm.signs: print i.uni_value