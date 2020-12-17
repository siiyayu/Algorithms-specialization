#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

bool IsGreaterOrEqual(int digit, int max_digit) {
    string digit_s = std::to_string(digit);
    string max_digit_s = std::to_string(max_digit);
    return stoi(max_digit_s + digit_s) <= stoi(digit_s + max_digit_s);
}

string largest_number(vector<string> a) {
    //write your code here
    std::stringstream ret;
    while (a.size() > 0) {
        int max_digit = -1e5;
        int index_to_del = -1;
        for (int i = 0; i < a.size(); ++i) {
            int digit = stoi(a[i]);
            if (IsGreaterOrEqual(digit, max_digit)) {
                max_digit = digit;
                index_to_del = i;
            }
        }
        ret << max_digit;
        a.erase(a.begin() + index_to_del);
    }
    string result;
    ret >> result;
    return result;
}

int main() {
    int n;
    std::cin >> n;
    vector<string> a(n);
    for (size_t i = 0; i < a.size(); i++) {
        std::cin >> a[i];
    }
    std::cout << largest_number(a);


}
