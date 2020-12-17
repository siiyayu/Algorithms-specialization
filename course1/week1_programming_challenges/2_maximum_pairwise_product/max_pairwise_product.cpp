 #include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();
    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }
    return max_product;
}

long long MaxPairwiseProductFast(const std::vector<int>& numbers) {
	int n = numbers.size();
	int max_index1 = -1;
    int max_index2 = -1;
    for (int i = 0; i<n; ++i) {
        if ((max_index1 == -1) || numbers[i] > numbers[max_index1]) {
            max_index1 = i;
        }
    }
    for (int i = 0; i < n; ++i) {
        if ((max_index2 == -1 || numbers[i] > numbers[max_index2]) && i != max_index1) {
            max_index2 = i;
        }
    }
    long long res = numbers[max_index1]*numbers[max_index2];
	return ((long long) numbers[max_index1]) * numbers[max_index2];
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductFast(numbers) << "\n";
    return 0;
}
