# qrange
A small, easy-to-use library for working with ranges.

## Installation
This package can be installed with the command:
```
pip install qrange
```
## How to use
Use qrange in your project by adding the following line at the top of your file:
```
import qrange
```
This library provides a set of functions for making it easier to work with ranges:
- `set_min_max(x, min_max, min_max_new)`: Takes an `x` that's between `min_max[0]` and `min_max[1]`, and changes the limits to `min_max_new[0]` and `min_max_new[1]`. Example usage:
```py
color = [128, 0, 0]
color[0] = set_min_max(color[0], [0, 255], [0, 1]) #converts 0-255 color to 0-1 color range.
```
![set_min_max](https://raw.githubusercontent.com/Forfunckle/images/master/set_min_max.gif)
----
- `reverse_range(x, min_max)`: Reverses an `x` value in a `min_max` range. Suppose you have a `softness` variable, but you made the program so that the higher the softness is, the harder it gets. `reverse_range` can fix that for you:
```py
softness = reverse_range(softness, [0, 10])
# If the variable was 0, this function made it 10.
# similarly, if it had a value of 10, it is now 0.
```
![reverse_range](https://raw.githubusercontent.com/Forfunckle/images/master/reverse_range.gif)
----
- `is_in_range(x, min_max, limits = ['c', 'c'])`: Checks if an `x` value is between `min_max[0]` and `min_max[1]`. The limits of the range are closed by default, so if `x` is equal to one of them, the function returns `True`. However, you can choose between `c` and `o` (closed/open) for each one of the two limits.
An example:
```py
isBetween = is_in_range(var, [25, 75])
```
![is_in_range](https://raw.githubusercontent.com/Forfunckle/images/master/is_in_range.gif)
----
- `range_lerp(min_max, t)`: Returns the linear interpolation between `min_max[0]` and `min_max[1]`. The following line prints the value halfway between 1 and 5:
```py
print(range_lerp([1, 5], 0.5))
# outputs 3
```
![range_lerp](https://raw.githubusercontent.com/Forfunckle/images/master/range_lerp.gif)
----
-  `find_lerp(x, min_max)`: returns the corresponding `t` value (between 0 and 1) of an `x` value between `min_max[0]` and `min_max[1]`. Consider the following examples:
```py
print(find_lerp(5, [5, 10])) #outputs 0
print(find_lerp(10, [5, 10])) #outputs 1
print(find_lerp(8, [5, 10])) #outputs 0.6
```
![find_lerp](https://raw.githubusercontent.com/Forfunckle/images/master/find_lerp.gif)
----
- `clamp(x, min_max)`: Restricts the value to stay within the limits `min_max[0]` and `min_max[1]`.
```py
var = clamp(var, [25, 75])
```
![clamp](https://raw.githubusercontent.com/Forfunckle/images/master/clamp.gif)

## Changelog
### Version 1.0.0
- qrange has been created

## About the author
Hi! I am a solo software developer. I created **qrange** as an open source library to simplify the process of using ranges in Python. Check out my [other repositories](https://github.com/Forfunckle?tab=repositories) as well.
If you want to support me, please [buy me a coffee here](https://www.paypal.me/forfunckle). Any amount is appreciated! :)
