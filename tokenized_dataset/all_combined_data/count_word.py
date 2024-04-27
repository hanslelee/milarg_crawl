f = open("test_corpus.tsv" , 'r') #파일을 오픈한다
data = f.read() #f.read()로 yesterday.txt의 내용전체를 읽어온다.
print(data.count("일반\t")) #data 변수에 count를 활용하여 yesterday가 얼마나 들어있는지 세어준다.
f.close()