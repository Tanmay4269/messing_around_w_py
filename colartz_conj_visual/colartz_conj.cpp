#include <fstream>
#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<int, int> memo;

int collatz(int n) {
    if (n == 1) return 0;
    if (memo.count(n)) return memo[n];

    int count;
    if (n & 1) count = 1 + collatz(3*n + 1);
    else count = 1 + collatz(n / 2);

    memo[n] = count;
    return count;
}

void foo() {
    // Open the file in write mode
    ofstream file("coords.csv");
    
    file << "x,y\n";

    for (int i = 2; i < 200'000; i++) {
        int count = collatz(i);

        file << i << "," << count << "\n";
    }

    file.close();
}


int main() {
    foo();

    return 0;
}
