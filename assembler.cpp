#include <bits/stdc++.h>
using namespace std;

bool checkCode(ifstream* file){
    return true;
}

int main(int argc, char *argv[]){
    if (argc != 2){
        cout << "Usage: ./assembler <Input File name>" << endl;
        return 0;
    } 
    ifstream file(argv[1]);
    if (file.is_open() == false){
        cout << "Error reading input file. Check whether the name is correct" << endl;
        return 0;
    }
    vector<char[32]> output;
    map<string, int> labelTable;
    return 0;
}