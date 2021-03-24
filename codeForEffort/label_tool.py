import sys
import pandas as pd

df = pd.read_excel('./excel/data_withoutshort.xlsx', index_col=0)
index = 0  
# Check where was left off
for i in range(len(df)):
    if df['label'].loc[i]==-1:
        index = i
        print('Starting at: '+str(index))
        break

stop = False
while(stop==False):
    reviewText = df['reviewText'].loc[index]
    summary = df['summary'].loc[index]
    asin = df['asin'].loc[index]
    reviewerName=df['reviewerName'].loc[index]
    reviewerID=df['reviewerID'].loc[index]
    score = df['overall'].loc[index]
    verified = df['verified'].loc[index]
    print(reviewText)
    print("Summary: "+str(summary))
    print("asin: "+str(asin))
    print("Name: "+str(reviewerName))
    print("reviewerID: "+str(reviewerID))
    print("rate score: "+str(score))
    print("index at "+str(index))
    if verified==0:
        print("Not verified purchase")
    else:
        print("verified purchase")
    print("******************************************************************************")
    label = input()
    if label=='exit':
        break
    elif df['label'].loc[index]!=-1:
        index+=1
        continue
    else:
        df['label'].loc[i] = int(label)
        count = 0
        for i in range(len(df)):
            if i == index:
                continue
            if df['reviewerID'].loc[i]==reviewerID:
                count+=1
                print(df['reviewText'].loc[i])
                print("###########################################################################")
                sub_label = input()
                df['label'].loc[i] = int(sub_label)
        print("Other reviews marked: "+str(count))
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        index+=1
df.to_excel('./excel/data_withoutshort.xlsx')