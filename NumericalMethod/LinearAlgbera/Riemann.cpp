#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

// 물리 상수
const double gamma = 1.4;

// 유체 상태 구조체
struct State {
    double rho;  // 밀도
    double u;    // 속도
    double p;    // 압력

    double energy() const {
        return p / (gamma - 1) + 0.5 * rho * u * u;
    }
};

// 플럭스 구조체
struct Flux {
    double mass;
    double momentum;
    double energy;
};

// 초기 조건 설정 함수
std::vector<State> initialize() {
    std::vector<State> U(100);
    for (int i = 0; i < 50; ++i) {
        U[i] = {1.0, 0.0, 1.0};
    }
    for (int i = 50; i < 100; ++i) {
        U[i] = {0.125, 0.0, 0.1};
    }
    return U;
}

// 플럭스 계산 함수
Flux compute_flux(const State& s) {
    double e = s.energy();
    return {s.rho * s.u, s.rho * s.u * s.u + s.p, s.u * (e + s.p)};
}

// Roe 평균 계산 함수
void roe_averages(const State& left, const State& right, double& rho, double& u, double& H) {
    double sqrt_rho_L = std::sqrt(left.rho);
    double sqrt_rho_R = std::sqrt(right.rho);
    double inv_sqrt_rho_sum = 1.0 / (sqrt_rho_L + sqrt_rho_R);

    rho = sqrt_rho_L * sqrt_rho_R;
    u = (sqrt_rho_L * left.u + sqrt_rho_R * right.u) * inv_sqrt_rho_sum;
    double h_L = (left.energy() + left.p) / left.rho;
    double h_R = (right.energy() + right.p) / right.rho;
    H = (sqrt_rho_L * h_L + sqrt_rho_R * h_R) * inv_sqrt_rho_sum;
}

// Roe Solver 함수
std::vector<State> roe_solver(const std::vector<State>& U, double dx, double dt) {
    std::vector<State> U_new(U.size());

    for (size_t i = 1; i < U.size() - 1; ++i) {
        State left = U[i];
        State right = U[i + 1];

        double rho, u, H;
        roe_averages(left, right, rho, u, H);

        double a = std::sqrt((gamma - 1) * (H - 0.5 * u * u));
        double lambda[3] = {u - a, u, u + a};

        for (int j = 0; j < 3; ++j) {
            if (lambda[j] < 0) {
                lambda[j] = 0;
            }
        }

        Flux flux_left = compute_flux(left);
        Flux flux_right = compute_flux(right);

        double delta_rho = right.rho - left.rho;
        double delta_u = right.u - left.u;
        double delta_p = right.p - left.p;

        double delta[3] = {
            0.5 * (delta_rho - delta_p / (a * a)),
            delta_u - delta_p / (a * a),
            0.5 * (delta_rho + delta_p / (a * a))
        };

        double alpha[3] = {
            delta[0] + delta[2],
            delta[1] - delta[2] * (u - a),
            delta[1] + delta[2] * (u + a)
        };

        double roe_flux[3] = {0.0, 0.0, 0.0};

        for (int j = 0; j < 3; ++j) {
            roe_flux[0] += alpha[j] * lambda[j];
            roe_flux[1] += alpha[j] * lambda[j] * (u + (j - 1) * a);
            roe_flux[2] += alpha[j] * lambda[j] * (H + u * (j - 1) * a);
        }

        U_new[i].rho = left.rho - dt / dx * (roe_flux[0] - flux_left.mass);
        U_new[i].u = left.u - dt / dx * (roe_flux[1] - flux_left.momentum) / left.rho;
        U_new[i].p = left.p - dt / dx * (roe_flux[2] - flux_left.energy) * (gamma - 1);
    }

    return U_new;
}

// 결과를 파일에 저장하는 함수
void save_to_file(const std::vector<State>& U, int timestep) {
    std::ofstream file("output_" + std::to_string(timestep) + ".dat");
    for (const auto& state : U) {
        file << state.rho << " " << state.u << " " << state.p << "\n";
    }
}

int main() {
    // 초기 조건 설정
    std::vector<State> U = initialize();
    double dx = 0.01;
    double dt = 0.005;
    int num_steps = 100;

    // 시간 스텝 반복
    for (int t = 0; t < num_steps; ++t) {
        U = roe_solver(U, dx, dt);
        save_to_file(U, t);
    }

    return 0;
}