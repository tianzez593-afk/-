def read_text(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        if word in counts:
             # TODO: 如果 word 已经在 counts 里，次数 +1
            counts[word] += 1
        # TODO: 否则，把 word 的次数设为 1
        else:
            counts[word] = 1
    return counts
def top_n(counts, n):
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
def main():
    try:
        path="day02/sample.txt"   
        text = read_text(path)
    except FileNotFoundError:
        print(f"找不到文件：{path}")
        return
    counts = count_words(text)

    
    
    
    for word, count in top_n(counts, 10):
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()

