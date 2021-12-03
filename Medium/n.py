def pang(a):
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ruLetters = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'

    temp = sum(list(map(lambda x: x in letters or x in ruLetters,a)))

    return temp == len(letters)/2 or temp == len(ruLetters)/2 or temp== (len(letters)+len(ruLetters))/2