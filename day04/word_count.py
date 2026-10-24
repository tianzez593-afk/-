def duqu(path):
    with open(path,"r",encoding="utf-8") as f:
        return f.read()

def count_words(text):
  
    words=text.lower().split()
    counts={}
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts


def tongji(count,n):
    return sorted(count.items(),key=lambda x:x[1],reverse=True)[:n]
def main():
    path="day02/sample.txt"
    try:
      text =duqu(path)   
      
    except FileNotFoundError:
        print(f'找不到文件:{path}')
        return
    counts=count_words(text)
    for word,n in tongji(counts,10):
        print(f'{word}:{n}')
if __name__ =="__main__":
    main()

