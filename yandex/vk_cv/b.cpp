//what this code do is to convert a binary tree to a linked list
struct node_t
{
    node_t *left;
    node_t *right;
    int data;
};

node_t* func(node_t *curr, node_t * part)
{
    if (!curr)
        return part;
    node_t *tmp = curr;
    while(curr->right)
        curr = curr->right;
    curr->right = part;
    return tmp;
}
node_t* foo(node_t *curr)
{
    if (curr == NULL)
        return NULL;
    node_t *tmp = foo(curr->left);
    curr->left = NULL;
    curr->right = foo(curr->right);
    return func(tmp, curr);
}
int main()
{   
    node_t *root;
    foo(root);
    return 0;
}