---
title: python学习
---

int对象，加法溢出判断。

```c
static PyObject *
int_add(PyIntObject *v, PyIntObject *w)
{
	register long a, b, x;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	x = a + b;
	if ((x^a) >= 0 || (x^b) >= 0)
		return PyInt_FromLong(x);
	return PyLong_Type.tp_as_number->nb_add((PyObject *)v, (PyObject *)w);
}
```

