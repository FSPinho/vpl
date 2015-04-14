#include <string>
#include <iostream>
using namespace std;

string sub_string(string palavra, int inicio, int tam){
    string res = "";
    for(int i = inicio; i < (inicio + tam); i++){
        if(i >= (int) palavra.size())
            break;
        res += palavra[i];
    }
    return res;
}

int main(){
    string texto;
    int ind;
    int qtd;
    getline(cin, texto);
    cin >> ind >> qtd;
    cout << sub_string(texto, ind, qtd) << endl;
    return 0;
}

