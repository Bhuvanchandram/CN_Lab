#include<iostream>
#include<string.h>
using namespace std;
string crc(string data,string poly,bool errchk){
    string rem=data;
    int i,j;
    if(!errchk){
        for(i=0;i<poly.length()-1;i++){
            rem.append("0");
        }
    }
    for(i=0;i<rem.length()-poly.length()+1;i++){
        if(rem[i]=='1'){
            for(j=0;j<poly.length();j++){
                if(rem[i+j]==poly[j]){
                    rem[i+j]='0';
                }else{
                    rem[i+j]=1;
                }
            }
        }
    }
    return rem.substr(rem.length()-poly.length()+1);
}
int main()
{
    string data,poly;
    cout<<"Enter the data to be transmitted: ";
    cin>>data;
    cout<<"Enter the generating polynomial: ";
    cin>>poly;
    string rem=crc(data,poly,0);
    string codeword=data+rem;
    cout<<"The reminder is "<<rem<<endl;
    cout<<"The codeword is "<<codeword<<endl;
    
    //Error checking
    string newcodeword;
    cout<<"Enter the data has been received: ";
    cin>>newcodeword;
    string newrem=crc(newcodeword,poly,1);
    if(stoi(newrem)==0)
        cout<<"There has been no error in data transmission";
    else
        cout<<"There has been error in data transmission";
}