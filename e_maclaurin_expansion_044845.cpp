#include <iostream>

using namespace std;

int main()
{
	// Get N as input
	int n;
	cout << "( Calculate Sum of First N Sequence for E ) ";
	cout << "\nEnter N: ";
	cin >> n;

	// Calculate Factoriels
	int fac[n-1];
	fac[0] = 1;
	for (int i = 1; i < n; i++)
		fac[i] = i * fac[i-1]; 

	double sum = 0;
	for (int i = 1; i <= n; i++)
		sum += (1) / (double) (fac[i-1]);
	cout << "E: " << sum << endl;
	
	return 0;
}
