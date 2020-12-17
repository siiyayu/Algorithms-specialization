#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int BinarySearch(vector<int> &data, int key, int low, int high) {
    if (high < low) {
        return -1;
    }
    int mid = low + (high - low)/2;
    if (key == data[mid]) {
        return mid;
    } else if (key < data[mid]) {
        return BinarySearch(data, key, low, mid - 1);
    } else {
        return BinarySearch(data, key, mid + 1, high);
    }
}

int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); i++) {
        std::cin >> a[i];
    }
    int m;
    std::cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; ++i) {
        std::cin >> b[i];
    }
    for (int i = 0; i < m; ++i) {
        //replace with the call to binary_search when implemented
        std::cout << BinarySearch(a, b[i], 0, a.size() - 1) << ' ';
    }
}