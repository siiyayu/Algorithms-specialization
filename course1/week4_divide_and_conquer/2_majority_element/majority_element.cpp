#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;


#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

int partition2(vector<int> &a, int l, int r) {
    int x = a[l];
    int j = l;
    for (int i = l + 1; i <= r; i++) {
        if (a[i] <= x) {
            j++;
            swap(a[i], a[j]);
        }
    }
    swap(a[l], a[j]);
    return j;
}

std::pair<int, int> partition3(vector<int> &a, int l, int r) {
    int m = partition2(a, l, r);
    int x = a[m];
    int j = m;
    for (int i = m - 1; i >= l; i--) {
        if (a[i] == x) {
            j--;
            swap(a[i], a[j]);
        }
    }
    return std::make_pair(j, m);
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
    if (l >= r) {
        return;
    }

    int k = l + rand() % (r - l + 1);
    swap(a[l], a[k]);
    auto res = partition3(a, l, r);
    auto m1 = res.first;
    auto m2 = res.second;
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);
}

int get_majority_element(vector<int> &a, int left, int right) {

    randomized_quick_sort(a, left, right);
    int result = 0;
    int count = 0;
    int comp = a[0];
    for (int i = 0; i <= right; i++) {
        if (a[i] == comp) {
            count += 1;
            if (result < count) {
                result = count;
            }
        } else {
            comp = a[i];
            count = 1;
        }
    }

    return result > a.size()/2;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << get_majority_element(a, 0, a.size() - 1) << '\n';
}
