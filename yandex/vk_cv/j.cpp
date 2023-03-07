//what this doing is that it is finding the two largest numbers in the array and printing them out.
int main()
{
    int pos1 = 1;
    int pos2 = 0;
    if (a[pos1] == a[pos2])
    {
        pos1 = 0;
        pos2 = 1;
    }
    for (int i = 2; i < size; ++i)
    {
        if (a[i] > a[pos1])
        //print 2 biggest numbers of array
        {
            pos2 = pos1;
            pos1 = i;
        }
        else if (a[i] > a[pos2])
        {
            pos2 = i;
        }
    }
}