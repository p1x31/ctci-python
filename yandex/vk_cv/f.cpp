//what this is doing is that it is adding 2*i+1 to a and then printing a
int main()
{
    int a = 0;
    for (int i = 0; i < 10; ++i)
    {
        a = a + 2 * i +1;;
        printf("%d\n", a);
    }
}