// https://www.codechef.com/JULY20B/problems/CRDGAME


#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int fun1(int x1)
{
    int s=0;
    while(x1>0)
    {
        int a=x1%10;
        s+=a;
        x1=x1/10;
    }
    return s;
}
int main()
{
    int t1;
    cin>>t1;
    while(t1--)
    {
        int n1;
        cin>>n1;
        int c=0;
        int c1=0;
        for(int i=0;i<n1;i++)
        {
            int s=0;
            int s1=0;
            int x,y;
            cin>>x>>y;
            //cout<<s<<' '<<s1<<endl;
            if(fun1(x)==fun1(y))
            {
                c+=1;
                c1+=1;
            }
            else if(fun1(x)>fun1(y))
            {
                c+=1;
            }
            else if(fun1(x)<fun1(y))
            {
                c1+=1;
            }
        }
            //cout<<c<<' '<<c1<<endl;
            if(c>c1)
            {
                cout<<0<<" "<<c<<endl;
            }
            else if(c<c1){
                cout<<1<<" "<<c1<<endl;
            }
            else if(c==c1){
                cout<<2<<" "<<c<<endl;
            }
    }
}