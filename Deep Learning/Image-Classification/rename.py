import os
os.chdir('S:/PycharmProjects/AI-Intern/dataset/train/joker')
i=1
for file in os.listdir():
    src=file
    dst="joker"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1
