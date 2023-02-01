#include<iostream>
#include<string.h>
using namespace std;
int recv(char *ip,char *op,char *poly, int mode)
{
    strcpy(op,ip);
    
    return 1;
}
int main()
{
    char poly[50],ip[50],op[50],rec[50];
    cout<<"Enter the divisor in binary: "<<endl;
    cin>>poly;
    cout<<"Enter the input message(dividend) in binary: "<<endl;
    cin>>ip;
    crc(ip,op,poly,1);
    cout<<"The transmitted message is: "<<ip<<op+strlen(ip)<<endl;
    cout<<"Enter the received mesage in binary: "<<endl;

    if(crc(recv,op,poly,0))
        cout<<"No error in data"<<endl;
    else
        cout<<"Error in data transmission has occured"<<endl;
}