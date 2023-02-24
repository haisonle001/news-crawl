i=0
def create_file(i):
    name="source"+str(int(i/100))+".txt"
    fi = open(name, 'w')
    return fi

for line in open("source/articles_baomoi.txt"):
    if (i%100==0):
        fi=create_file(i)
    fi.writelines(line)
    i+=1
