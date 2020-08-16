#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int getSum(const string a){
	int sum=0;
	for(int i=0;i<a.length();i++){
		if(1<=a[i]-'0'&&a[i]-'0'<=9){
			sum+=a[i]-'0';
		}
	}
	return sum;
}

bool compare(const string a,const string b){
	if(a.length()!=b.length()){
		return a.length()<b.length();
	}else{
		int aSum=getSum(a);
		int bSum=getSum(b);
		if(aSum!=bSum){
			return aSum<bSum;
		}
		else{
		return a<b;
	}
}
	}

int main(void){
	int num;
	string a[1000];
	cin>>num;
	
	for(int i=0;i<num;i++){
		cin>>a[i];
	}
	sort(a,a+num,compare);
	for(int i=0;i<num;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}
