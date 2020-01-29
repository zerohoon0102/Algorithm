#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num_of_input, num_of_search;
    scanf("%d %d", &num_of_input, &num_of_search);
    int *input_num = (int *)malloc(sizeof(int) * num_of_input);
    int *search_num = (int *)malloc(sizeof(int) * num_of_search);
    int *num_check = (int *)malloc(sizeof(int) * num_of_search);
    for (int i = 0; i < num_of_input; i++)
        scanf("%d", &input_num[i]);
    for (int i = 0; i < num_of_search; i++)
    {
        scanf("%d", &search_num[i]);
        num_check[i] = 0;
    }
    for (int i = 0; i < num_of_input; i++)
    {
        for (int j = 0; j < num_of_search; j++)
        {
            if (input_num[i] == search_num[j])
            {
                num_check[j]++;
                break;
            }
        }
    }
    for (int i = 0; i < num_of_search; i++)
        printf("%d\n", num_check[i]);
    free(input_num);
    free(search_num);
    free(num_check);
}