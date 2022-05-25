#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'maximum_path' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY node_values as parameter.
 */

int maximum_path(vector<int> node_values) {
    vector<vector<int>>triangle;
    for(int i=1, j=0; j<node_values.size(); i++){
        vector<int>v;
        for(int k=0; k<i; j++, k++){
            v.push_back(node_values[j]);
        }
        triangle.push_back(v);
    }
for(int i = triangle.size()-2; i>=0;i--){
    for(int j=0; j<triangle[i].size();j++){
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1]);
        
    }
}
return triangle[0][0];
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string node_values_count_temp;
    getline(cin, node_values_count_temp);

    int node_values_count = stoi(ltrim(rtrim(node_values_count_temp)));

    vector<int> node_values(node_values_count);

    for (int i = 0; i < node_values_count; i++) {
        string node_values_item_temp;
        getline(cin, node_values_item_temp);

        int node_values_item = stoi(ltrim(rtrim(node_values_item_temp)));

        node_values[i] = node_values_item;
    }

    int result = maximum_path(node_values);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
