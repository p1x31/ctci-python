//what this is doing is creating a new array_t object, and then passing it to the add function. 
//The add function then modifies the array_t object, but the changes are not reflected in the original array_t object. 
//This is because the array_t object is passed by value, so the add function is working on a copy of the original array_t object.
struct array_t {
    int *data;
    int capacity;
    int size;
};
void add(array_t array, int value)
{
    if (array.size == array.capacity)
    {
        array.capacity *= 2;
        array.data = (int*)realloc(array.data, array.capacity * sizeof(int));
    }
    array.data[array.size] = value;
    array.size++;
}

