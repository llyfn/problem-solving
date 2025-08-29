#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
bool comp(string s){
    if(s.length()>19)return true;
    if(s.length()<19)return false;
    return s.compare("9223372036854775807")>0;
}
int main() {
    long long a,b,r;
    string x,y;
    cin>>x>>y>>r;
    if(x=="0"||y=="0")cout<<"0";
    else if(comp(x)||comp(y))cout<<"overflow";
    else{
        a=stoll(x);
        b=stoll(y);
        if(a>r/b)cout<<"overflow";
        else cout<<a*b;
    }
}