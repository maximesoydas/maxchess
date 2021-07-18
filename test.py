a = [[["Max","Soy"],["stevenson","steve"]],[["Maxime","Soydas"],["Louis","Jacob"]],[["Ellie","Mckenzie"],["Ellizabeth","Johnson"]]]
b = [[["Max","Soy"],["stevenson","steve"]],[["Maxime","Soydas"],["Louis","Jacob"]],[["Ellie","Mckenzie"],["Ellizabeth","Johnson"]]]


def ordre_equipe(e):
   return [e[0], e[1]] if e[0] < e[1] else [e[1], e[0]]

def ordre_match(m):
    e1 = ordre_equipe(m[0])
    e2 = ordre_equipe(m[1])
    return [e1, e2] if e1[0] < e2[0] else [e2, e1]

def matchs_unique(lm1, lm2):
    lm1 = ordre_match(lm1)
    lm2 = ordre_match(lm2)
    for m1 in lm1:
        if m1 in lm2:
            return False
    return True

#----------------------------

def test_string_compare():
    assert 'a' < 'b'
    assert 'aaaaa' < 'b'
    assert 'f' > 'c'
    assert 'f' > 'cccccccccc'

def test_ordre_equipe():
    assert ordre_equipe(['a', 'b']) == ['a', 'b']
    assert ordre_equipe(['b', 'a']) == ['a', 'b']
    assert ordre_equipe(['b', 'b']) == ['b', 'b']

def test_ordre_match():
    assert ordre_match([['a', 'b'], ['f', 'b']]) == [['a', 'b'], ['b', 'f']]
    assert ordre_match([['f', 'b'], ['b', 'a']]) == [['a', 'b'], ['b', 'f']]


def test_matchs_unique():
    assert matchs_unique(
            [['a', 'b'], ['f', 'b']],
            [['f', 'b'], ['b', 'a']]
    ) == False

    assert matchs_unique(
            [['a', 'b'], ['f', 'b']],
            [['b', 'f'], ['x', 'y']]
    ) == False    

    assert matchs_unique(
            [['a', 'b'], ['f', 'b']],
            [['x', 'y'], ['u', 'x']]
    ) == True