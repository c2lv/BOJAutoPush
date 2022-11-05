#include <iostream>

#include<stack>

#include<string>

using namespace std;
int main() {
  stack < char > st;
  string str;
  cin >> str;
  int temp = 1;
  int sum = 0;

  for (int i = 0; i < str.length(); i++) {
      
    if (str[i] == '(') {
      st.push(str[i]);
      temp *= 2;
    }
        
    else if (str[i] == '[') {
      temp *= 3;
      st.push(str[i]);
    }
        
    else if (str[i] == ')') {
        
      if (st.empty() || st.top() != '(') {
        sum = 0;
        break;
      }
        
      if (str[i - 1] == '(') {
        sum += temp;
        temp /= 2;
        st.pop();
      } 
      else {
        temp /= 2;
        st.pop();
      }
        
    }
    else if (str[i] == ']') {
        
      if (st.empty() || st.top() != '[') {
        sum = 0;
        break;
      }
        
      if (str[i - 1] == '[') {
        sum += temp;
        temp /= 3;
        st.pop();
      } else {
        temp /= 3;
        st.pop();
      }
        
    }

  }
  if (!st.empty()) sum = 0;
  cout << sum << endl;
}