import re
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList 클래스 (자료구조) 정의
class LinkedList:
    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

            self.before.next = self.current.next
            self.current = self.before # 중요 : current가 next가 아닌 before로 변경된다.

            self.num_of_data -= 1

            return pop_data

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0: # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data


    def traverse(self):
        if self.first()==None:
            print("No node in the list! \n")
            return
        current = self.current
        while current != None :
            print(current.data, end=" ")
            current = current.next
        print()

    def insert_after_data(self, new_data, key):
        if self.first()==None:
            self.append(new_data)
        else:
            current = self.current
            while current != self.tail and current.data != key :
                current = current.next
            new = Node(new_data)
            new.next = current.next
            current.next = new
            if current==self.tail :
                self.tail = new
     # 노드의 갯수 세는 메소드
    def traverse_count(self,bucket):
        count = 0
        bucket.first()
        while True:
            count += 1
            if bucket.next() == None:
                break
            bucket.next()
        return count
# list 안의 값을 내림차순으로 정렬하는 메소드
def sort_list(top = [[]]):
    for i in range(1, len(top)): # 리스트의 크기만큼 반복
        for j in range(0, len(top)-1): # 각 회전당 정렬이 끝나지 않은 친구들을 위해 반복
            if top[j][1] < top[j+1][1]: # 현재 인덱스의 값이 다음 인덱스의 값보다 크면 실행
                top[j+1], top[j] = top[j], top[j+1] # swap해서 위치 바꾸기
    return top

class HashTable:
    def read_word(self):
        # list of common words you want to remove
        stop_words = ['queen', 'hamlet', 'horatio', 'barnardo', 'francisco', 'king', 'polonius', 'laertes', 'cornelius',
                      'voltemand', 'marcellus',
                      'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                      "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                      'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
                      'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
                      'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                      'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
                      'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
                      'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
                      'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
                      'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
                      'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
                      "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
                      "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
                      "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
                      'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
                      "weren't", 'won', "won't", 'wouldn', "wouldn't"]

        with open("hamlet.txt") as text_file:
            wordlist=[] # 단어들을 넣을 리스트 wordlist 생성
            for line in text_file:
                newline = re.sub(r'[^\w\s]', '', line)
                for word in newline.split():
                    word = word.lower()
                    if word not in stop_words:
                        wordlist.append(word)
        return wordlist

    def count(self,wordlist):
        temp = []
        word_count=[]
        #중복제거
        word_count.append([wordlist[0],None])
        for i in wordlist:
            temp.append([i, None])
            if temp[0] not in word_count:
                word_count.append(temp[0])
            del temp[0]
        #단어 빈도 수 세기
        for i in range(len(word_count)):
            word_count[i][1]=wordlist.count(word_count[i][0])
        return word_count

    def hash_function(self,word_count):
        bucket=[[None]]*997
        index = ""
        alp=['#','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #리스트의 인덱스 1~26까지의 슬롯에 a부터 z를 담음
        for i in range(len(word_count)):
            for j in range(1,27):
                if alp[j] == word_count[i][0][0]:
                    index = str(j) + "00" + str(len(word_count[i][0])) # 단어를 "단어 첫 알파벳의 인덱스값 + 00 + 단어의 길이"으로 나타냄
                    index=int(index)
                    index%=997 # 크기가 997인 bucket에 담기 위해 index를 997로 나눈 나머지로 나타냄
                    if bucket[index] == [None]: # bucket[index]에 값이 없으면
                        bucket[index] = LinkedList()
                    bucket[index].append(word_count[i]) #bucket[index]안의 연결리스트에 값을 추가함
                    if bucket[index].first() == None:
                        bucket[index].first() # 연결리스트의 current값을 지정
        return bucket

    def rate(self,bucket):
        top=[]
        for i in range(997): # bucket의 크기만큼
            if bucket[i]!=[None]: # bucket[i]에 값이 있을때
                if bucket[i].next() != None: # 연결리스트를 선형탐색해야할때
                    bucket[i].first()
                    for j in range(bucket[i].traverse_count(bucket[i])): # 연결리스트의 노드 갯수만큼
                        if j == 0:
                            bucket[i].first()
                        if len(top)<50: # top길이가 50미만일 때
                            top.append(bucket[i].current.data)
                            bucket[i].next()
                            sort_list(top)
                        else: # top길이가 50이상일 때
                            if top[49][1] < bucket[i].current.data[1]:
                                top.pop()
                                top.append(bucket[i].current.data)
                                bucket[i].next()
                                sort_list(top)
                else: # bucket에 하나의 값만 있을 때
                    if len(top)<50: # top 길이 50미만
                        bucket[i].first()
                        top.append(bucket[i].current.data)
                        sort_list(top)

                    else: # top 길이 50이상
                        if top[49][1] < bucket[i].current.data[1]:
                            top.pop()
                            top.append(bucket[i].current.data)
                            sort_list(top)
        return top
abc=HashTable()
w_list=[]
w_list=abc.read_word()
w_list=abc.count(w_list)
w_list=abc.hash_function(w_list)
w_list=abc.rate(w_list)
print("Top 50 word:")
for i in range(len(w_list)):
    print(w_list[i][0]) # 빈도수가 top 50인 단어들을 출력

#빈도수가 top 50인 단어들과 그 빈도수를 함께 출력
#for j in range(len(w_list)):
    #print(w_list[j][0],w_list[j][1])