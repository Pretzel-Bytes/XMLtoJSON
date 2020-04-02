#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
## Loops through a supplied XML root and converts to a dict
##################################################
## Copyright (c) 2020 Pretzel Bytes LLC

## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
##################################################
## Author: Michael Pretzel (Pretzel Bytes LLC)
## License: MIT License
## Version: 0.1.1
## Maintainer: Michael Pretzel
## Email: michael(at)pretzelbytes.com
## Status: Early Development
##################################################

import traceback


def convert(root):
    return_dict = dict()  # Complete Dynamic Dictionary to be Returned
    for neighbor in root:  # Loop through the supplied root. This can be at any level in the XML
        try:
            if hasattr(neighbor, 'text'):  # Check if Element has Text
                if neighbor.text is not None:  # Ensure that Text is NOT None
                    # Ensure that text has greater than 0 length and is not a new line
                    if len(neighbor.text) > 0 and not neighbor.text.startswith('\n'):
                        return_dict[str(neighbor.tag)] = neighbor.text  # Create New Dictionary Item with Value
            if len(neighbor.attrib) > 0:  # Check if Element has Attributes
                for item in neighbor.attrib:  # Loop through the Attributes
                    return_dict[str(item)] = neighbor.attrib[item]  # Create dictionary item for attribute
            if len(list(neighbor)) > 0:  # Check if the element has sub elements
                # Run this function again against all sub elements and att to return_dict
                return_dict[str(neighbor.tag)] = convert(neighbor)
        except Exception as e:  # Error, Report It
            print("Offending Element: " + str(neighbor))  # What Element Failed Out
            traceback.print_exc()  # Give more detail into the Error
    return return_dict  # Return the return_dict
