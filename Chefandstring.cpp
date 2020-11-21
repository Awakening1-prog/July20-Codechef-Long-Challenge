// https://www.codechef.com/JULY20B/problems/CHEFSTR1/
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int t1;
    cin>>t1;
    while(t1--)
    {
        long long int n;
        cin>>n;
        vector<int>l;
        for(int i=0;i<n;i++)
        {
            long long int a1;
            cin>>a1;
            l.push_back(a1);
        }
        long long int s1=0;
        for(int i=1;i<n;i++)
        {
            s1+=(abs(l[i]-l[i-1])-1);
        }
        cout<<s1<<endl;
        
    }
}
