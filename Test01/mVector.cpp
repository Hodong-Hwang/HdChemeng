#include <iostream>
#include <vector>

int main() {
    // 원래 벡터
    std::vector<int> original = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // 조건을 만족하는 요소를 옮길 벡터
    std::vector<int> filtered;

    // 조건: 짝수인 경우만 filtered로 옮기기
    auto condition = [](int x) { return x % 2 == 0; };

    // 인덱스로 접근하여 삭제
    for (size_t i = 0; i < original.size();) {
        if (condition(original[i])) {
            filtered.push_back(original[i]);      // 조건 만족 시 filtered에 추가
            original.erase(original.begin() + i); // 조건 만족 요소 삭제
        } else {
            ++i; // 조건 미만족 시 다음 요소로 이동
        }
    }

    // 결과 출력
    std::cout << "Filtered vector : ";
    for (int num : filtered) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    std::cout << "Original vector : ";
    for (int num : original) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    return 0;
}
