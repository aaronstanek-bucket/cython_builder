# cython_builder

This will create and run your cython setup.py for you, hiding all the options so that you can get back to writing code.
This assumes that you have cython installed. If you do not you can get it through "pip install cython".

## how to use

So make your setup.py, open cython_builder.py from terminal, passing the name of the cython source file.
So, if the head file of your cython code is called "hello_world.pyx", you would run from terminal: "python cython_builder.py hello_world.pyx".

Once you have your setup.py file, you are ready to compile, just call "cython_builder.py" from terminal without any arguments and it will compile inplace,
please note that this is python version sensitive, so if you are using cython on version 2, the call would be "pyhton cython_builder.py",
if you are using cython on version 3, the call would be "python3 cython_builder.py".
