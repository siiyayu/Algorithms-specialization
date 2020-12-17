#include <iostream>
#include <vector>

using std::vector;

vector<int> optimal_summands(int n) {
    vector<int> summands;
    //write your code here
    if (n == 2 or n == 1) {
        summands.push_back(n);
        return summands;
    }
    int candies_res = n;
    int candies = 1;



    while (candies_res > 0 and candies_res - candies > candies) {
        summands.push_back(candies);
        candies_res = candies_res - candies;
        candies += 1;
    }
    summands.push_back(candies_res);
    return summands;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> summands = optimal_summands(n);
    std::cout << summands.size() << '\n';
    for (size_t i = 0; i < summands.size(); ++i) {
        std::cout << summands[i] << ' ';
    }
}
