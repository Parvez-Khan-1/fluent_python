Decorators in Python:


- Decorators are use to modify the behaviour of function or class
- Strictly speaking, decorators are just syntactic sugar. As we can always simply call a decorator like any regular callable, passing another function.
- A Key feature of decorator is they run right after the decorated function is defined. That is usually at import time (Refer dec_exec_seq.py)
- The main point here is - the function decorators are executed as soon as the module is imported, but the decorated functions only run when they are explicitly invovked.
- Python has 3 built in decorators:
    * @classmethod
    * @staticmethod
    * @property
    