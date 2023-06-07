#include <iostream>
using namespace std;

int main()
{
    string text;
    string cipher;
    string key;

    cout<<"Enter plain text: ";
    cin>>text;

    cout<<"Enter a key: ";
    cin>>key;

    string newKey=key;
    while (newKey.length()<text.length())
    {
        newKey+=key;
    }

    //Encryption
    
    for (int i = 0; i < text.length(); i++)
    {
        cipher+=(text[i]+newKey[i])%26 +65;
    }
    cout<<cipher<<endl;

    //Decryption

    // for (int i = 0; i < text.length(); i++)
    // {
    //     cipher+=(text[i]-newKey[i]+26)%26+65;
    // }
    // cout<<cipher<<endl;
}