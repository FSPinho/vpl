#include <iostream>
#include <string.h>
using namespace std;

int contar(string str, char letra){
    int cont = 0;
    for(char c : str){
        if(c == letra)
            cont++;
    }
    return cont;
}

bool eh_anagrama(string A, string B) {
    //@@return false;
    if(A.length() != B.length())
        return false;
    for(char c : A)
        if(contar(A, c) != contar(B, c))
            return false;
    return true;
}

int main()
{
    string A, B;
    cin >> A >> B;
    if(eh_anagrama(A, B))
        cout << "sim" << endl;
    else {
        cout << "nao" << endl;
    }
}
