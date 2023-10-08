#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int i, len = PyList_Size(p);
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", object->allocated);
	for (i = 0; i < len; i++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}
