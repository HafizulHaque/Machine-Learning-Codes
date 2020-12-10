import random

def sq(x):
    return x*x

def eudis(x,y):
    val = 0
    for i in range(1,14):
        #print("{} {}".format(x[i],y[i]))
        val+=sq(x[i]-y[i])
    return val

def ignorezerodiv(n,d):
    return n/d if d else 0

def calvariance(cnt):
    x=0
    for i in cnt:
        x+=i
    avg=x/len(cnt)
    x=0
    for i in cnt:
       x+=sq(avg-i)
    return x/len(cnt)

def update(x,y):
    for i in range(1,14):
        x[i]=(x[i]+y[i])/2
    return x

#random.seed(995)
"""
fname = os.path.join(sys.path[0],"wine.xlsx")

df1 = pd.read_excel(fname,sheet_name = 'wine')

df = df1.values.tolist()
"""

def userKmeans2(df,nok,run):
    type = []
    var = 0
    for loop in range(0,run):
        tmp = Kmeans(df,nok)
        cnt = []
        for i in range(0,nok):
            cnt.append(0)
        for i in range(0,178):
            cnt[tmp[i]]+=1

        x = calvariance(cnt)

        if not type:
            type = tmp
            var = x
        else:
            if x < var:
                var = x
                type = tmp
        print(cnt)
        print(var)
    return type

def Kmeans(df,nok):
    centroids = []
    cnt = []
    inival = []
    for i in range(0,nok):
        inival.append(random.randint(0,177))
        centroids.append(df[inival[i]])
        cnt.append(0)
    #print(inival)
    dis = []
    type = []
    for i in range(0, 178):
        dis.append(1e9)
        type.append(-1)
    for loop in range(0,200):
        for i in range(0, 178):
            dis[i] = 1e9
        for i in range(0, nok):
            cnt[i] = 0
        for i in range(0,178):
            for j in range(0,nok):
                x = eudis(df[i],centroids[j])
                #print("{} {} {}".format(i,j,x))
                if x < dis[i]:
                    dis[i]=x
                    type[i]=j
            centroids[type[i]]=update(centroids[type[i]],df[i])

        for i in range(0,178):
            cnt[type[i]]+=1
        #print(cnt)

        #print(centroids)
    return type

#for x in centroids:
#    print(x)
