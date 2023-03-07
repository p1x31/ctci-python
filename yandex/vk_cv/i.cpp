//what this do is print the data of the node and then print the data of the node again
struct node_t
{
    node_t *next;
    int data;
};
void foo(node_t *curr)
{
    if (curr == NULL)
        return;
    printf("%d ", curr->data);
    if(curr->next != NULL)
        foo(curr->next->next);
    printf("%d ", curr->data);
}