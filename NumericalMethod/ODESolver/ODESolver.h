#pragma once
#include <iostream>
template<typename T>
class ODESolver {
public:
    virtual T solve(T (*function)(T, T), T initial_value, T step_size, T final_time) = 0;
    // 순수 가상 함수로, 파생 클래스에서 구현할 solve 메서드 정의
};