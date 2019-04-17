#先讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines

#把每一行分開 姓名 引號 拿出來 所以要用for x in x 然後split
def convert(lines):
    new = []
    person = None
    allen_word_count = 0
    allen_stick_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_stick_count = 0
    viki_image_count = 0
    for line in lines: #把每一行拿出來 #print(line) 會印出每一行 
        s = line.split(' ') #遇到空白鍵 切分開每個詞 切完以後變成['s[0]',s[1]''s[2],]
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_stick_count += 1 #只要s2是貼圖  我就每次看到一個就給他累加1上去
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]: #m =message 把每個s2以後的每個訊息拿出來
                    allen_word_count += len(m) #把每個訊息數目加進去
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_stick_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen says',allen_word_count,'字', )
    print('allen傳了',allen_stick_count, '個貼圖')
    print('allen傳了',allen_image_count, '個圖片')
    print('viki says', viki_word_count,'字',)    
    print('viki傳了',allen_stick_count, '個貼圖')        
    print('viki傳了',allen_image_count, '個圖片')
    return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

#寫成main
def main():
    lines = read_file('line.txt')
    lines = convert(lines)   #很重要
    # write_file('output.txt', lines)


main()