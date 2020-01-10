#include <stdio.h>

int main()
{
    int bingo[5][5];
    int bingo_conf[5][5];
    int i, j;
    for (i = 0; i < 5; i++)
    {
        scanf("%d %d %d %d %d", &bingo[i][0], &bingo[i][1], &bingo[i][2], &bingo[i][3], &bingo[i][4]);
        for (j = 0; j < 5; j++)
        {
            bingo_conf[i][j] = 0;
        }
    }
    int num_of_bingo = 0;
    int input[5][5];
    for (i = 0; i < 5; i++)
    {
        scanf("%d %d %d %d %d", &input[i][0], &input[i][1], &input[i][2], &input[i][3], &input[i][4]);
    }
    i = 0;
    j = 0;
    while (num_of_bingo < 3)
    {
        int a, b;
        for (a = 0; a < 5; a++)
        {
            for (b = 0; b < 5; b++)
            {
                if (bingo[a][b] == input[i][j])
                    break;
            }
            if (bingo[a][b] == input[i][j])
                break;
        }
        bingo_conf[a][b] = 1;
        int sum_of_line;
        for (a = 0; a < 5; a++)
        {
            sum_of_line = 0;
            for (b = 0; b < 5; b++)
            {
                sum_of_line = sum_of_line + bingo_conf[a][b];
            }
            if (sum_of_line == 5)
                num_of_bingo++;
            sum_of_line = 0;
            for (b = 0; b < 5; b++)
            {
                sum_of_line = sum_of_line + bingo_conf[b][a];
            }
            if (sum_of_line == 5)
                num_of_bingo++;
        }
        sum_of_line = bingo_conf[0][0] + bingo_conf[1][1] + bingo_conf[2][2] + bingo_conf[3][3] + bingo_conf[4][4];
        if (sum_of_line == 5)
            num_of_bingo++;
        sum_of_line = bingo_conf[0][4] + bingo_conf[1][3] + bingo_conf[2][2] + bingo_conf[3][1] + bingo_conf[4][0];
        if (sum_of_line == 5)
            num_of_bingo++;
        if (num_of_bingo < 3)
            num_of_bingo = 0;
        if (j < 5)
            j++;
        if (j == 5)
        {
            j = 0;
            i++;
        }
    }
    int num = i * 5 + j;
    printf("three-bingo까지 필요한 수 : %d\n", num);
    return 0;
}