#include <iostream>
#include <fstream>

using namespace std;

int main() {
    // 데이터 파일 생성
    ofstream dataFile("data.dat");
    if (!dataFile) {
        cerr << "Error opening data file!" << endl;
        return 1;
    }

    // 데이터 파일에 데이터 쓰기
    for (int i = 0; i < 10; ++i) {
        dataFile << i << " " << i * i << endl;
    }
    dataFile.close();

    // GNU Plot을 호출하여 그래프 생성
    system("gnuplot -persist -e \"plot 'data.dat' with lines\"");

    return 0;
}