#include<bits/stdc++.h>
using namespace std;

int day(int dd,int mm,int yy)
{
	int m[]={0,1,4,4,0,2,5,0,3,6,1,4,6};
	int y[4]={6,4,2,0};
	int d4=yy%100;
	int d5=d4/4;
	int sum=0,c;
	c=yy/100;
	c=c%4;
	sum=dd+m[mm]+y[c]+d4+d5;
	return sum%7;
}

int main()
{
	int dd,mm,yy;
	cout<<"Enter the date in the following format DD MM YYYY : ";
	cin>>dd>>mm>>yy;

	int i=day(dd,mm,yy);
	switch(i)
	{
		case 0:
			cout<<"Saturday\n";
			break;
		case 1:
			cout<<"Sunday\n";
			break;
		case 2:
			cout<<"Monday\n";
			break;
		case 3:
			cout<<"Tuesday\n";
			break;
		case 4:
			cout<<"Wednesday\n";
			break;
		case 5:
			cout<<"Thursday\n";
			break;
		case 6:
			cout<<"Friday\n";
			break;
		default:
			cout<<"Something went wrong\n";
	}
	return 0;
}