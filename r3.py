lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        # print(line)
        lines.append(line.strip()) #把每一行line放到lines清單裏頭
    for line in lines:
        s = line.split()  #split切割後變成清單  S[0]:時間人名連一起 S[1]內容
        time = s[0][:5]  #s0的前五個 第五個不包含
        name = s[0][5:]  #s0從第五個開始計算
        
        print(name)
