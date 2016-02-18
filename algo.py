#!/usr/bin/python3
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

def bod_quiz_algo(value):
    """
    Performs the requested operations on the provided value, which should be
    passed as a tuple. Returns a list of floats with the result of the
    performed operation.
    Raises a TypeError exception if a value not specified int the quiz is
    passed to the function.
    """

    case_a = set([1, 2, 3])
    case_b = set([4, 9])
    case_c = (6, 7, 8)

    if value == case_c:
        result = [float(x / 9) for x in value] # Solve case_c in one strike.
    else:
        result = []
        for values in value:
            if values in case_a:
                result.append(float(values * values)) # Square of the value.
            elif values in case_b:
                result.append(float(values ** (1/2))) # Sqrt of the value.
            else:
                err_string = "Invalid value passed to bod_quiz_algo. The "\
                             "value '" + str(values) + "' is invalid."
                raise TypeError(err_string)

    return result


#print(bod_quiz_algo((1,2,3,4,5)))
