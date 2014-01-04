# -*- coding: utf-8 -*-


class TranslationTable(object):
    def __init__(self, Chr=None, Uni=None, t1=None):
        self.chr_name = Chr
        self.uni_value = Uni
        self.t1_value = t1

    def __str__(self):
        return self.uni_value.encode("UTF-8")

    def __repr__(self):
        return repr(self.uni_value)


class Tamil(object):  # Unicode Tamil
    om = TranslationTable('OM', u'\u0BD0')
    dot = TranslationTable('pulli', u'\u0BCD', u'\xf6')
    leg = TranslationTable('VOWEL SIGN AA', u'\u0BBE', u'V')
    smhorn = TranslationTable('VOWEL SIGN I', u'\u0BBF', u'\xe5')
    bghorn = TranslationTable('VOWEL SIGN II', u'\u0BC0', u'\xe7')
    smu = TranslationTable('VOWEL SIGN U', u'\u0BC1', u'\xe9')
    bguu = TranslationTable('VOWEL SIGN UU', u'\u0BC2', u'\xe8')
    sme = TranslationTable('VOWEL SIGN E', u'\u0BC6', u'\xff')
    bgee = TranslationTable('VOWEL SIGN EE', u'\u0BC7', u'\xba')
    aii = TranslationTable('VOWEL SIGN AI', u'\u0BC8', u'\xc1')
    smo = TranslationTable('VOWEL SIGN O', u'\u0BCA')
    bgoo = TranslationTable('VOWEL SIGN OO', u'\u0BCB')
    smau = TranslationTable('VOWEL SIGN AU', u'\u0BCC')
    llaau = TranslationTable('AU LENGTH MARK', u'\u0BD7')
    signs = [dot, leg, smhorn, bghorn, smu, bguu, sme, bgee, aii, smo, bgoo,
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

tm = Tamil()
#for i in tm.indep_vowels: print i
for i in tm.cons: print i
#for i in tm.signs: print i