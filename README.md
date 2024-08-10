# [PyProgressBar](https://pypi.org/project/ProgressBarPy)

This is a lightweight Python package that provides a simple, customizable progress bar displayed in a windowed interface using [**Tkinter**](https://docs.python.org/3/library/tkinter.html). It allows developers to easily integrate a visual progress indicator into their applications without needing to manage complex GUI elements. With straightforward methods for updating progress and setting labels, **PyProgressBar** is an ideal solution for adding a user-friendly progress bar to your Python projects.

## How to use it?

Before you start you've t import package:

    pip install PyProgressBar

Now it's ready to work. Let's check an example of using this package:

    from PyProgressBar import ProgressBar

    import time

    max_progress = 100
    progressbar = ProgressBar(max_progress=max_progress, title='Progress bar example', message='Processing...')
    progressbar.display()
    for _ in range(max_progress+1):
        time.sleep(0.05)
        progressbar.update()

    progressbar.destroy()

```ProgressBar``` has three arguments ```max_progress```(necessary argument), ```title```('Progress Bar' by default) and ```message```(not necessary argument).

Class object of ```ProgressBar``` has three methods ```display()```(displays progress bar), ```update(value)```(updates progress bar by value(value is 1 by default)) and ```destroy()```(destroys progress bar window).

That's everything you need to know about **PyProgressBar**.

#

Thanks for attention!
