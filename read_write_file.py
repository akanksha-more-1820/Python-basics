with open("D:\\funny.txt","r") as f:
    with open("D:\\funny_wc.txt","w") as f_out:
        for line in f:
            words=line.split(' ')
            f_out.write(" wordCount :-"+ str(len(words))+line)
            print(line, len(words))
    f_out.close()
f.close()
print(f.closed)