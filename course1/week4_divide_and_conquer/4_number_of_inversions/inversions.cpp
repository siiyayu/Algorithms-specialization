#include <iostream>
#include <vector>

using std::vector;


long long merge(vector<int> &a, vector<int> &b, size_t left, size_t ave, size_t right) {
    size_t i, j, k;
    long long number_of_inversions = 0;
    i = left;
    j = ave + 1;
    k = left;
    while ((i <= ave) and (j <= right)) {
        if (a[i] <= a[j]) {
            b[k++] = a[i++];
        } else {
            b[k++] = a[j++];
            number_of_inversions += ave - i + 1;
        }
    }
    while (i <= ave) {
        b[k++] = a[i++];
    }
    while (j <= right) {
        b[k++] = a[j++];
    }
    for (auto i = left; i <= right; i++) {
        a[i] = b[i];
    }
    return number_of_inversions;

}


long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right) {
    long long number_of_inversions = 0;
    if (right <= left) return number_of_inversions;
    size_t ave = left + (right - left) / 2;
    number_of_inversions += get_number_of_inversions(a, b, left, ave);
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right);
    number_of_inversions += merge(a, b, left, ave, right);
    return number_of_inversions;
}


int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); i++) {
        std::cin >> a[i];
    }
    vector<int> b(a.size());
    std::cout << get_number_of_inversions(a, b, 0, a.size() - 1) << '\n';
//    std::cout << 5/2;
}
//5
//2 3 9 2 9