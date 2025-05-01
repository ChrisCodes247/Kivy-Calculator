#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Entry point for Calculator mobile app
"""

# Import your app code from calculator.py
from calculator import *

# If calculator.py has a main() function or entry point, call it here
if __name__ == '__main__':
    # If your calculator.py has a MyApp class that extends App:
    try:
        # Try to run the app
        app = MyApp()
        app.run()
    except NameError:
        # If MyApp is not defined, try to find other App classes
        import inspect
        import sys
        from kivy.app import App
        
        # Find all App subclasses in the calculator module
        app_classes = [obj for name, obj in inspect.getmembers(sys.modules['calculator']) 
                      if inspect.isclass(obj) and issubclass(obj, App) and obj != App]
        
        # Run the first App class found
        if app_classes:
            app = app_classes[0]()
            app.run()
        else:
            print("Error: No App class found in calculator.py")
