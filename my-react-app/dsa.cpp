#include <iostream>
using namespace std;

void print()
{

  for (int i = 1; i <= 5; i++)
  {
    for (int j = 0; j <= i; j++)
    {
      cout << "*";

      for (int k = 5; k < i - j; k++)

        cout << " ";
    }
  }
}
int main()
{

  print();
}
