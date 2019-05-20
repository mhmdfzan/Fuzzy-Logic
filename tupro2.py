import csv;
import numpy as np;
import matplotlit as plt;

def turun(a,b,x):
    return (b-x)/(b-a);

def naik(a,b,x):
    return (x-a)/(b-a);
        
def rules(pr,ps,pt,hr,hs,ht):
    TL = 0
    L=0
    if pr>0 and hr>0:
        TL=cek(pr,hr,TL)
    if pr>0 and hs>0:
        L=cek(pr,hs,L)
    if pr>0 and ht>0:
        L=cek(pr,ht,L)
    if ps>0 and hr>0:
        TL=cek(ps,hr,TL)
    if ps>0 and hs>0:
        L=cek(ps,hs,L)
    if ps>0 and ht>0:
        L=cek(ps,ht,L)
    if pt>0 and hr>0:
        TL=cek(pt,hr,TL)
    if pt>0 and hs>0:
        TL=cek(pt,hs,TL)
    if pt>0 and ht>0:
        L=cek(pt,ht,L)
    return L,TL

def cek(a,b,c):
    if (a<b):
        if (a>c):
            return a
        else:
            return c
    elif (b<a):
        if (b>c):
            return b
        else:
            return c
    elif (a==b):
        if (a>c):
            return a
        else:
            return c

def hutang(x):
    hr=0; hs=0; ht=0;
    if (x>=0 and x<=18):
        hr=1
    elif (x>18 and x<50):
        hr=turun(18,50,x)
        hs=naik(18,50,x)
    elif (x==50):
        hs=1
    elif (x>50 and x<=82):
        hs=turun(50,82,x)
        ht=naik(50,82,x)
    elif (x>=82 and x<=100):
        ht=1
    return hr,hs,ht

def score(l,tl):
    return ((tl*30)+(l*80))/(tl+l)

def grafikPendapatan():
    plt.title('Pendapatan')
    plt.plot([0,0.50,1],[1,1,0],label='rendah')
    plt.plot([0.50,1,1.70],[0,1,0],label='sedang')
    plt.plot([1,1.70,2],[0,1,1],label='tinggi')
    plt.legend(loc="best")
    plt.show()

def grafikHutang():
    plt.title('Hutang')
    plt.plot([0,18,50],[1,1,0],label='rendah')
    plt.plot([18,50,82],[0,1,0],label='sedang')
    plt.plot([50,82,100],[0,1,1],label='tinggi')
    plt.legend(loc="center right")
    plt.show()
    
def main():
    list = []
    data = np.genfromtxt("DataTugas2.csv",delimiter=",",skip_header=True)
    o = open('TebakanTugas2.csv','w')
    w = csv.writer(o)
    
    for i in range(len(data)):
        pr=0; ps=0; pt=0;
        hr=0; hs=0; ht=0;
        L=0; TL=0; hasil=0;
        if (data[i][1]>=0 and data[i][1]<=0.50):
            pr=1
            hr,hs,ht = hutang(data[i][2])
            L,TL=rules(pr,ps,pt,hr,hs,ht)
            hasil=score(L,TL)
        elif (data[i][1]>0.50 and data[i][1]<1):
            pr=turun(0.50,1,data[i][1])
            ps=naik(0.50,1,data[i][1])
            hr,hs,ht = hutang(data[i][2])
            L,TL=rules(pr,ps,pt,hr,hs,ht)
            hasil=score(L,TL)
        elif (data[i][1]==1):
            ps=1
            hr,hs,ht = hutang(data[i][2])
            L,TL=rules(pr,ps,pt,hr,hs,ht)
            hasil=score(L,TL)
        elif (data[i][1]>1 and data[i][1]<1.70):
            pt=naik(1,1.70,data[i][1])
            ps=turun(1,1.70,data[i][1])
            hr,hs,ht = hutang(data[i][2])
            L,TL=rules(pr,ps,pt,hr,hs,ht)
            hasil=score(L,TL)
        elif(data[i][1]>=1.70 and data[i][1]<=2):
            pt=1
            hr,hs,ht = hutang(data[i][2])
            L,TL=rules(pr,ps,pt,hr,hs,ht)
            hasil=score(L,TL)
            
        if(hasil>=30):
            hasil = {
                "no" : int(data[i][0]),
                "score" : hasil
            }
            list.append(hasil);
            
    list.sort(key=lambda x: x['score'], reverse = True)
    tebakan = []
    print("20 Kepala Keluarga yang layak menerima BLT")
    for x in range(20):
        tebakan.append(list[x]['no'])
        print(tebakan[x],":",list[x]['score']);
    w.writerow(tebakan);
    grafikPendapatan();
    #NOTED: close terlebih dahulu grafik pendapatan untuk melihat grafik hutang
    grafikHutang();
    
main();
