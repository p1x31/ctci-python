//what this is doing is finding the first element in the array a that is greater than or equal to key.
int find(int *a, int begin, int end, int key)
{
    if (begin == end)
        return end;
    int middle = (begin + end) / 2;
    if(a[middle] <= key)
        end = middle;
    else
        begin = middle;
}