#include <iostream>

using namespace std;
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int num_of_board;
    cin >> num_of_board;
    int zero_to_max = 0;
    int board[4][4];
    int start_num[16][2048];
    while (zero_to_max++ < num_of_board)
    {
        int count = 0;
        cin >> board[0][0] >> board[0][1] >> board[0][2] >> board[0][3];
        cin >> board[1][0] >> board[1][1] >> board[1][2] >> board[1][3];
        cin >> board[2][0] >> board[2][1] >> board[2][2] >> board[2][3];
        cin >> board[3][0] >> board[3][1] >> board[3][2] >> board[3][3];
        for (int i = 0; i < 16; i++)
        {
            start_num[i];
        }
        cout << "#" << zero_to_max << " " << count << "\n";
    }
}