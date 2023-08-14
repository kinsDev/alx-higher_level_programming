#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: PyObject
 * 
 * Return: void 
 */
void print_python_list_info(PyObject *p)
{
    long int list_size, i;
    PyListObject *py_list;
    PyObject *list_item;

    list_size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", list_size);

    py_list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", py_list->allocated);

    for (i = 0; i < list_size; i++)
    {
        list_item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
    }
}
