#include <iostream>
using namespace std;

// Vigenere Function
string vigenere(string text, string key, bool EncDec)
{
    string newKey = key, newText;
    while (newKey.length() < text.length())
    {
        newKey += key;
    }

    if (EncDec == 0)
    {
        // Encrypt
        for (int i = 0; i < text.length(); i++)
        {
            newText += (text[i] + newKey[i]) % 26 + 65;
        }
    }
    else
    {
        //Decrypt
        for (int i = 0; i < text.length(); i++)
        {
            newText += (text[i] - newKey[i] + 26) % 26 + 65;
        }
    }
    return newText;
}

int main()
{
    string text;
    string cipher;
    string key;
    char y;

    do
    {
        cout << "Encrypter Decrypter Application" << endl;
        cout << "Please choose an option:" << endl;
        cout << "\t\t\t 1)Encryption\n\t\t\t 2)Decryption\n\t\t\t 3)Exit\n";

        int op;
        cin >> op;

        switch (op)
        {
        case 1:
            // Encryption

            cout << "Please enter plain text: ";
            cin >> text;
            cout << "Please enter the key: ";
            cin >> key;

            cipher = vigenere(text, key, 0);
            cout << "Cipher Text: " << cipher << endl;

            cout << "Enter Y/y to continue any other to exit" << endl;
            cin >> y;
            break;

        case 2:
            // Decryption

            cout << "Please enter cipher text: ";
            cin >> text;
            cout << "Please enter the key: ";
            cin >> key;

            cipher = vigenere(text, key, 1);
            cout << "Plain Text: " << cipher << endl;

            cout << "Enter Y/y to continue any other to exit" << endl;
            cin >> y;
            break;
        case 3:
            // Exit

            y = 'n';
            break;
        }

    } while (y == 'Y' || y == 'y');
}