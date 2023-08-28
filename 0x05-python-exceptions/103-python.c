#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) /* Use PyList_Check to check the type */
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = Py_TYPE(list->ob_item[i])->tp_name; /* Use Py_TYPE to get type */
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[i]);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) /* Use PyBytes_Check to check the type */
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    if (size >= 10)
        size = 10;

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
    char *buffer = NULL;

    PyFloatObject *float_obj = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) /* Use PyFloat_Check to check the type */
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
            Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);
}
