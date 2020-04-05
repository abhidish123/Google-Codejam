#include<bits/stdc++.h>

#define ll long long int
#define pb push_back
#define ppb pop_back
#define ff first
#define ss second
#define vvi vector<vector<ll>>
#define vi vector<ll>
#define all(a) (a).begin(),(a).end()
#define pii pair<ll,ll>
#define rep(x,n) for(ll i=x;i<n;++i)
#define repd(x,n) for(ll i=x-1;i>=n;--i)
#define repn(x,n) for(ll j=x;j<n;++j)
#define repnd(x,n) for(ll j=x-1;j>=n;--j)
#define endl '\n'
#define M 1000000007
const ll INF = 1ll<<60;

using namespace std;

ll fact(ll n){ ll p=1; rep(1,n+1){ p*=i; } return p; }

bool isprime(ll a){
    if(a==2) {
        return 1;
    }
    if(!(a&1) ) {return 0;}
    for(ll i=3;i*i<=a;i+=2){
        if(a%i==0) {return 0;}
    }
    return 1;
}

ll fast_power(long long base, long long power)  //for(2^100)
{   long long result=1;
    while(power>0) {
        if(power&1) {
            result=(result*base)%M;
        }
        base=(base*base)%M;
        power>>=1;
    }
    return result;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

    int t,n;
    cin>>t;
    int tt=1;
    while(t--){
        cin>>n;
        int a[n][n];
        int trace=0;
        int r=0,c=0;
        rep(0,n){
            repn(0,n){
                cin>>a[i][j];
                if(i==j) trace+=a[i][j];
            }
        }
        rep(0,n){
            map<int,int> mp;
            repn(0,n){
                if(!mp[a[i][j]]) mp[a[i][j]]=1;
                else{
                    r++;
                    break;
                }
            }
        }
        repn(0,n){
            map<int,int> mp;
            rep(0,n){
                if(!mp[a[i][j]]) mp[a[i][j]]=1;
                else{
                    c++;
                    break;
                }
            }
        }
        cout<<"Case #"<<tt<<": "<<trace<<" "<<r<<" "<<c<<endl;
        tt++;
    }


	return 0;
}

