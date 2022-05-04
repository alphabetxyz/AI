#include<bits/stdc++.h>
using namespace std;
int c = 0;
bool isQueenSafe(int row,int col,vector<vector<int>> chess)
{
        for(int i=row-1,j=col;i>=0;i--)
        {
            if(chess[i][j]==1)
            {
                return false;
            }
        }
        
        for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--)
        {
            if(chess[i][j]==1)
            {
                return false;
            }
        }
        
        
        for(int i=row-1,j=col+1;i>=0 && j< chess.size();i--,j++)
        {
            if(chess[i][j]==1)
            {
                return false;
            }
        }
        return true;
}

void printNQueens(vector<vector<int>> chess,string qsf,int row)
{
    if(row==chess.size())
    {
            //cout << qsf << ". "<<
            //cout<<c<<endl;
            c++;
            return;
    }
    for(int col=0;col<chess.size();col++)
    {
        if(isQueenSafe(row,col,chess))
        {
            chess[row][col]=1;
            printNQueens(chess,qsf+to_string(row)+"-"+to_string(col)+",",row+1);
            chess[row][col]=0;
        }
    }
}
int main(){
cout<<"Enter the no. of Queens \n";
int n;
cin >> n;
vector<vector<int>> chess(n , vector<int> (n));
printNQueens(chess,"",0);
cout<<"No. of solutions for the given condition is --->";
cout<<c;
return 0;
}
