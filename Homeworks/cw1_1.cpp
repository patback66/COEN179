#include <stdio.h>
#include <iostream>
#include <math.h>
#include <time.h>

using namespace std;

int main(){

  int steps[] = {10, 20, 40, 100, 200, 400, 1000, 2000, 4000, 10000};
  for(int i = 0; i < 10; i++){
    int N = steps[i];
    //get current time
    //clock_t now = clock();
    //the hw code
    long long x = 0;
    long long count = 0;
    for(long long i=1; i <= N; i++)
            for(long long j=1; j <= i; j++)
                  for(long long k=1; k <= i*sqrt(j); k++){
                    x = i+j+k;
                    //cout << x << endl;
                    count++;
                  }

    //get end time
    //get difference
    //clock_t curTime = clock();
    cout << "N: " << N;
    cout << " Steps: " << count << endl;
    //cout << " Time: " << float(curTime - now)/CLOCKS_PER_SEC << endl;
  }
}
