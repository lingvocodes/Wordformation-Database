import codecs, re

b = raw_input(u'Инструкция к применению. При запросе программы введите слово с маленькой буквы(если это имя собственное, то с заглавной). Слово дожно стоять в начальной форме (Nom,Sg). После этого нажмите клавишу Enter.').decode('cp1251')
words = [] 
transcr = {}
prefix = {}
suffix = {}
fname = u'dict.txt'
pristname= u'prist.csv'
sufname = u'suf.csv'
def load_dict(fname):
    f = codecs.open (fname,'r','utf-8')
    for line in f:
        line = line.split()
        for word in line:
            word = word.strip(u'.,!?()"/')
            words.append(word)
    f.close()
    return words

def load_prist(pristname):
    prist = codecs.open (pristname, 'r', 'utf-8')
    for line2 in prist:
        line2 = line2.strip()
        prist, meaning1 = line2.split(';')
        prefix[prist] = meaning1
    prist.close()
    return prefix

def load_suf(sufname):
    suf = codecs.open (sufname, 'r', 'utf-8')
    for line3 in suf:
        line3 = line3.strip()
        suf, meaning2 = line3.split(';')
        suffix[suf] = meaning2
    suf.close()
    return suffix

words = load_dict(fname)
prefix = load_prist(pristname)
suffix = load_suf(sufname)
a = u'' 
while True:
    a = raw_input(u'Введите слово: ').decode('cp1251')
    if len(a) == 0:
        break
    
    if re.search(u'^[А-ЯЁ]', a, flags=re.U) != None:  
        print u'Имя собственное'

    
    elif re.search(u'до|мо|ро|ло|ти', a, flags = re.U) != None:
          print u'Несклоняемое существительное'
          for i in words:
                    m = re.search(u'\\b' + a,i, flags = re.U)
                    if m != None:
                      print i


    elif re.search(u'а|ы|я|е', a, flags = re.U) != None:
        print u'Часть речи: существительное. Окончание введённого слова: ',a[-1]
        b = a[0:-2]
        for i in words:
            m = re.search(u'\\b' + b,i, flags = re.U)
            if m != None:
                  print i


    elif re.search(u'ый|ий|ая|ое|яя|ее', a, flags = re.U) != None:
        print u'Часть речи: прилагательное или причастие'
        b = a[0:-2]
        for i in words:
            m = re.search(u'\\b' + b,i, flags = re.U)
            if m != None:
                  print i

    elif re.search(u'о|е|ё', a, flags = re.U) != None:
        print u'Часть речи: наречие'
        b = a[0:-1]
        for i in words:
            m = re.search(u'\\b' + b,i, flags = re.U)
            if m != None:
                  print i

    elif re.search(u'ть|ти', a, flags = re.U) != None:
        print u'Часть речи: глагол'
        b = a[0:-2]
        for i in words:
            m = re.search(u'\\b' + b,i, flags = re.U)
            if m != None:
                  print i

    elif re.search(u'ться|тись', a, flags = re.U) != None:
        print u'Часть речи: глагол (возвратный)'
        b = a[0:-3]
        for i in words:
            m = re.search(u'\\b' + b,i, flags = re.U)
            if m != None:
                  print i

    else:
        print u'Окончание нулевое'
        for i in words:
            m = re.search(u'\\b' + a,i, flags = re.U)
            if m != None:
                  print i

 
    for i in prefix:
        if re.search(prist, a , flags = re.U) != None:
            print prist, prefix[prist]

    for k in suffix:
        if re.search(suf, a, flags = re.U) != None:
            print suf, suffix[suf]
            
    print u'Предупреждение: омонимия не снята'
