t=int(input())
tt=1
for _ in range(t):
    s=str(input())
    ss=""
    for i in range(len(s)):
        if(s[i]=='0'):
            dep=0
            ss+=s[i]
        else:
            if(i==0):
                dep=int(s[i])
                ss+='('*dep+s[i]+')'*dep
            else:
                # dep=int(s[i])
                if(dep-int(s[i])>=0):
                    # print('hi')
                    dep=int(s[i])
                    ss=ss[:-1*dep]+s[i]+ss[-1*dep:]
                    
                else:
                    p=int(s[i])-dep
                    sn='('*p+s[i]+')'*p
                    if(dep==0):
                        ss+=sn
                        dep=p
                    else:
                        ss=ss[:-1*dep]+sn+ss[-1*dep:]
                        dep+=p
                        
        # print(ss)
    print("Case #"+str(tt)+": "+ss)
    tt+=1
        
