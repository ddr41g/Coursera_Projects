#include <iostream>
using namespace std;

int main()
{
    char text='J';
    char cipher;
    char key='B';
    
    cipher= (text+key)%26 +65;
    cout<<cipher<<endl;

    text=(cipher-key+26)%26 +65;
    cout<<text;
    
}