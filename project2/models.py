from django.db import models

# Create your models here.
class coin:
        def __init__(self,i,dn):
            self.i=i
            i=self.i
            self.buy_at=dn.iloc[i,4]
            self.buy_time=dn.iloc[i,0]
            self.length=((dn.iloc[i,2]-dn.iloc[i,3])/(dn.iloc[i,3]))*100
            if (dn.iloc[i,1]>dn.iloc[i,4]) & (dn.iloc[i,4]-dn.iloc[i,3]>dn.iloc[i,2]-dn.iloc[i,1]):
                self.q=((dn.iloc[i,2]-dn.iloc[i,4])/(dn.iloc[i,2]-dn.iloc[i,3]+.0000011))
                self.tail=dn.iloc[i,3]
                self.strategy="long"
                
            elif (dn.iloc[i,1]>dn.iloc[i,4]) & (dn.iloc[i,4]-dn.iloc[i,3]<dn.iloc[i,2]-dn.iloc[i,1]):
                self.q=((dn.iloc[i,1]-dn.iloc[i,3])/(dn.iloc[i,2]-dn.iloc[i,3]+.0000011))
                self.tail=dn.iloc[i,2]
                self.strategy="short"
                
                
            elif (dn.iloc[i,4]>dn.iloc[i,1]) & (dn.iloc[i,1]-dn.iloc[i,3]>dn.iloc[i,2]-dn.iloc[i,4]):
                self.q=((dn.iloc[i,2]-dn.iloc[i,1])/(dn.iloc[i,2]-dn.iloc[i,3]+.0000011))
                self.tail=dn.iloc[i,3]
                self.strategy="long"
                
                
            elif (dn.iloc[i,4]>dn.iloc[i,1]) & (dn.iloc[i,2]-dn.iloc[i,4]>dn.iloc[i,1]-dn.iloc[i,3]):
                self.q=((dn.iloc[i,4]-dn.iloc[i,3])/(dn.iloc[i,2]-dn.iloc[i,3]+.0000011))
                self.tail=dn.iloc[i,2]
                self.strategy="short"           
            else :  
                self.q=1
                self.strategy="none"
