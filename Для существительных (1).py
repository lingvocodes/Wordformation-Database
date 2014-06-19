import codecs, re

b = raw_input(u'Инструкция к применению. При запросе программы введите слово с маленькой буквы(если это имя собственное, то с заглавной). Слово дожно быть существительным в начальной форме (Nom,Sg). После этого нажмите клавишу Enter.').decode('cp1251')
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

    if a.endswith(u'ь'):
        p = a[0:-1]
        print u'Окончание нулевое'
        for i in words:
            m = re.search(u'\\b' + p,i, flags = re.U)
            if m != None:
              print i

    if a.endswith(u'ик')  or a.endswith(u'ит') or a.endswith(u'ат') or a.endswith(u'ер') or a.endswith(u'ёр')\
       or a.endswith(u'ир') or a.endswith(u'ор') or a.endswith(u'аж') or a.endswith(u'аг') or a.endswith(u'сь')\
       or a.endswith(u'ед') or a.endswith(u'ам') or a.endswith(u'аз') or a.endswith(u'ур')\
       or a.endswith(u'нт') or a.endswith(u'нд') or a.endswith(u'им') or a.endswith(u'ес') or a.endswith(u'ут') or a.endswith(u'ук')\
       or a.endswith(u'ты') or a.endswith(u'од') or a.endswith(u'ел') or a.endswith(u'ай')\
       or a.endswith(u'из') or a.endswith(u'ек') or a.endswith(u'ез') or a.endswith(u'тр') or a.endswith(u'тор') or a.endswith(u'тит')\
       or a.endswith(u'ал') or a.endswith(u'рт') or a.endswith(u'ер') or a.endswith(u'он') or a.endswith(u'ев') \
       or a.endswith(u'ин'):
            e = a[0:-2]
            print u'Окончание нулевое'
            for i in words:
                m = re.search(u'\\b' + e,i, flags = re.U)
                if m != None:
                  print i


    if a.endswith(u'до') or a.endswith(u'мо') or a.endswith(u'ро') or a.endswith(u'ло') or a.endswith(u'ти'):
            print u'Несклоняемое существительное'
            for i in words:
                    m = re.search(u'\\b' + a,i, flags = re.U)
                    if m != None:
                      print i
           
    if a.endswith(u'рет') or a.endswith(u'лик') or a.endswith(u'лав') or a.endswith(u'кат') or a.endswith(u'фон') or a.endswith(u'ург') or a.endswith(u'таж')\
       or a.endswith(u'иль') or a.endswith(u'жер')  or a.endswith(u'дец') or a.endswith(u'анс') or a.endswith(u'ень') or a.endswith(u'ард') or a.endswith(u'ин')\
       or a.endswith(u'мер') or a.endswith(u'мен') or a.endswith(u'мат') or a.endswith(u'иум') or a.endswith(u'иец') or a.endswith(u'вод') or a.endswith(u'сон')\
       or a.endswith(u'рит') or a.endswith(u'ком') or a.endswith(u'ект'):
         d = a[0:-3]
         print u'Окончание нулевое'
         for i in words:
                m = re.search(u'\\b'+ d,i, flags = re.U)
                if m != None:
                  print i
           
    if a.endswith(u'овец') or a.endswith(u'мент') or a.endswith(u'олог') or a.endswith(u'анец') or a.endswith(u'ость'):
            c = a[0:-4]
            print u'Окончание нулевое'
            for i in words:
                m = re.search(u'\\b'+ c,i, flags = re.U)
                if m != None:
                  print i

    if a.endswith(u'а') or a.endswith(u'ы') or a.endswith(u'я') or a.endswith(u'е') :
        b = a[0:-1]

        if b.endswith(u'к') or b.endswith(u'ш') or b.endswith(u'н'):
            b = b[0:-1]
            for i in words:
                m = re.search(u'\\b' + b,i, flags = re.U)
                if m != None:
                  print i

        elif b.endswith(u'ни') or b.endswith(u'ик') or b.endswith(u'ух'):
            b = b[0:-2]
            for i in words:
                m = re.search(u'\\b' + b,i, flags = re.U)
                if m != None:
                  print i

        elif  b.endswith(u'аци') or b.endswith(u'очк') or b.endswith(u'овк') or b.endswith(u'анк') or b.endswith(u'ёжк') or b.endswith(u'ежк'): 
              b = b[0:-3]
              for i in words:
                  m = re.search(u'\\b' + b,i, flags = re.U)
                  if m != None:
                        print i           
            
        elif b.endswith(u'лени') or b.endswith(u'атор') or b.endswith(u'олог') or b.endswith(u'онок') or b.endswith(u'енок')\
             or b.endswith(u'ёнок'):
              b = b[0:-4]
              for i in words:
                    m = re.search(u'\\b' + b,i, flags = re.U)
                    if m != None:
                      print i
      
        elif b.endswith(u'имость'):
            b = b[0:-6]
            for i in words:
                m = re.search(u'\\b' + b,i, flags = re.U)
                if m != None:
                  print i

        elif b.endswith(u'аемость') or b.endswith(u'яемость'):
            b = b[0:-7]     
            for i in words:
                m = re.search(u'\\b' + b,i, flags = re.U)
                if m != None:
                  print i

        else:
            for i in words:
                m = re.search(u'\\b' + b,i, flags = re.U)
                if m != None:
                  print i

        
        print u'Окончание введённого слова: ',a[-1]

    print u'Предупреждение: омонимия не снята'

print u'Спасибо, что воспользовались продуктом компании Blazhiyevskaya software!'
