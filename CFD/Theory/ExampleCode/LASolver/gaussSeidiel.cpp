#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Gauss-Seidel 함수
bool gaussSeidel(const vector<vector<double>>& A, const vector<double>& b, vector<double>& x, int maxIterations, double tolerance) {
    int n = A.size();
    
    for (int iter = 0; iter < maxIterations; ++iter) {
        vector<double> x_old = x; // 이전 x 값 저장
        
        // 각 방정식에 대해 반복
        for (int i = 0; i < n; ++i) {
            double sum = b[i];
            
            // a_ij * x_j 계산
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    sum -= A[i][j] * x[j];
                }
            }
            
            // 새로운 x_i 계산
            x[i] = sum / A[i][i];
        }
        
        // 오차 계산
        double error = 0.0;
        for (int i = 0; i < n; ++i) {
            error += abs(x[i] - x_old[i]);
        }
        
        // 지정된 오차 범위 내에 수렴 시, 반복 종료
        if (error < tolerance) {
            return true;
        }
    }
    
    return false; // 수렴하지 않으면 false 반환
}

int main() {
    // 예제 행렬 A와 벡터 b
    vector<vector<double>> A = {
        {4, -1, 0, 0},
        {-1, 4, -1, 0},
        {0, -1, 4, -1},
        {0, 0, -1, 3}
    };
    vector<double> b = {15, 10, 10, 10};
    
    // 초기 추정값 x
    vector<double> x = {0, 0, 0, 0};
    
    // 반복 설정
    int maxIterations = 100;
    double tolerance = 1e-6;
    
    // Gauss-Seidel 수행
    bool converged = gaussSeidel(A, b, x, maxIterations, tolerance);
    
    if (converged) {
        cout << "Solution converged:\n";
        for (double xi : x) {
            cout << xi << " ";
        }
        cout << endl;
    } else {
        cout << "Solution did not converge within the given iterations.\n";
    }
    
    return 0;
}