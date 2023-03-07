int foo(int a, int b)
{
    return b ? foo(b, a % b) : a;
}

int main()
{
    int a = 9000;
    int b = 1600;
    printf("%d\n", foo(a, b));
    return 0;
}
