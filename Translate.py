from Database import find
from Language import tm, trans
from string import punctuation

def unicodeToindica(verse):
    verse_lenght = len(verse) - 1
    results = u''
    for i, char in enumerate(verse):
        if ' ' in char or any(i in char for i in punctuation):
            results += char
            continue  # Skip to end, avoid further processing
        if i < verse_lenght:
            next_char = verse[i+1]
            if any(i.uni_value in next_char for i in tm.signs):
                signed_char = char+next_char
                #print ">>>", signed_char
                if signed_char in trans:
                    #print i, trans[signed_char]
                    results += trans[signed_char]
            else:
                if char in trans:
                    #print i, trans[char]
                    results += trans[char]

    if results != u'': return results

def Translate(search_results, multi_verse=False):
    if search_results:
        #print search_results
        if multi_verse:
            for i in search_results:
                yield str(i[0])+': '+unicodeToindica(i[1])
        else:
            yield str(search_results[0])+': '+unicodeToindica(search_results[1])

#results = find('jhn3:10-16', 'tamil')
#print results
#for i in Translate(results, True): print i
