#include <iostream>
#include <vector>
using namespace std;

int get_change(int money, const vector<int>& coins) {
    vector<int> min_num_coins(money + 1);
    min_num_coins[0] = 0;
    for (int m = 1; m <= money; m++) {
        min_num_coins[m] = 1e6;
        for (int coin : coins) {
            if (m >= coin) {
                int num_coins = min_num_coins[m - coin] + 1;
                if (num_coins < min_num_coins[m]) {
                    min_num_coins[m] = num_coins;
                }
            }
        }
    }
    return min_num_coins[money];
}

int main() {
    int m;
    std::cin >> m;
    vector<int> coins = {1, 3, 4};
    std::cout << get_change(m, coins) << '\n';
}
