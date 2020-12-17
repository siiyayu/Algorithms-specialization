#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
    int start, end;
};

int choose_min_right_segment(const vector<Segment> &segments) {
    int min_right = 1e10;
    for (int i = 0; i < segments.size(); ++i) {
        if (segments[i].end < min_right) {
            min_right = segments[i].end;
        }
    }
    return min_right;
}

void exclude_segments(vector<Segment> &segments, int min_right) {
    segments.erase(
            std::remove_if(
                    segments.begin(),
                    segments.end(),
                    [min_right](Segment const& s) { return s.start <= min_right and s.end >= min_right; }
            ),
            segments.end()
    );

}
vector<int> optimal_points(vector<Segment> &segments) {
    vector<int> points;
    //write your code here
    while (segments.size() > 0) {
        int min_right = choose_min_right_segment(segments);
        points.push_back(min_right);
        exclude_segments(segments, min_right);
    }
        return points;
}

int main() {
    int n;
    std::cin >> n;
    vector<Segment> segments(n);
    for (size_t i = 0; i < segments.size(); ++i) {
        std::cin >> segments[i].start >> segments[i].end;
    }
    vector<int> points = optimal_points(segments);
    std::cout << points.size() << "\n";
    for (size_t i = 0; i < points.size(); ++i) {
        std::cout << points[i] << " ";
    }
}
