import sys

print("사용방법 : [파일이름] [찾고싶은 단어]") 

# 첫 번째 인자로는 파일 이름, 두 번째 인자로는 찾을 단어를 입력받는다.
file_name =  sys.argv[1]
word = sys.argv[2]

# 파일을 열고 읽는다.
with open(file_name, 'rt', encoding='UTF8') as file:
    x = file.read()

# 단어가 몇 번  나오는지 세고 출력한다.
print(x.count(word)+"번")
