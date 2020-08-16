#include <iostream>

using namespace std;
int main(void){
	int num;
	int input;
	int sorted[10001];

	cin>>num;
	for(int i=0;i<num;i++){
		cin>>input;
		sorted[input]++;
	}
	for(int i=1;i<=num;i++){
		for(int j=0;j<sorted[i];j++){
			cout<<i<<endl;
		}
	}
	return 0;
}
