import codecs, re

b = raw_input(u'Инструкция к применению. При запросе программы введите слово с маленькой буквы(если это имя собственное, то с заглавной). Слово дожно стоять в начальной форме (Nom,Sg). После этого нажмите клавишу Enter.').decode('cp1251')
words = [] 
fname = u'dict.txt'
def load_dict(fname):
    f = codecs.open (fname,'r','utf-8')
    for line in f:
        line = line.split()
        for word in line:
            word = word.strip(u'.,!?()"/')
            words.append(word)
    f.close()
    return words


words = load_dict(fname)
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

   

    print u'Предупреждение: омонимия не снята'
