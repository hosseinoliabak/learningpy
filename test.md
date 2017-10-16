Python Bullet Train (PBT)
=========================

Prompt decoration for ZSH and Bash. Inspired by the [Oh My
ZSH](https://github.com/robbyrussell/oh-my-zsh) [Bullet
Train](https://github.com/caiogondim/bullet-train.zsh) theme.


Installation
------------

In Arch Linux:

```shell
yaourt -S pbt-git
```

or via PyPi:

```shell
pip install pbt
# For ZSH
PROMPT='$(pbt $?)'
# For Bash
PS1='$(pbt $?)'
```

or directly from GitHub:

```shell
git clone https://github.com/jtyr/python-bullettrain.git ~/pbt
# For ZSH
PROMPT='$(~/pbt/pbt.py $?)'
# For Bash
PS1='$(~/pbt/pbt.py $?)'
```

In order to display all characters of the prompt correctly, the shell should
support UTF-8 and [Nerd](https://github.com/ryanoasis/nerd-fonts) (or at least
[Powerline](https://github.com/ryanoasis/powerline-extra-symbols) and
[Devicons](https://vorillaz.github.io/devicons/)) fonts should be installed and
set in the terminal application.


Usage
-----

```shell
### Test the Status car
false
true
### Test the Dir car
cd /
cd ~
cd /usr/share/doc/sudo
# Display only last 3 elements of the path
export PBT_CAR_DIR_DEPTH=3
# Display full path
export PBT_CAR_DIR_DEPTH=9999
# Show only last element of the path
unset PBT_CAR_DIR_DEPTH
### Test Time car
# Add the Time car into the train
export PBT_CARS="Status, Os, Time, Hostname, Dir, Sign"
# Set 12h format
export PBT_CAR_TIME_TIME_FORMAT="%I:%M:%S %p"
# Change background color of the all car
export PBT_CAR_TIME_BG=yellow
# Change color of Date part
export PBT_CAR_TIME_DATE_FG=black
# Reset the color of the Date part
unset PBT_CAR_TIME_DATE_FG
# Reset the background color of all Time car
unset export PBT_CAR_TIME_BG
# Remove the Date part from the car
export PBT_CAR_TIME_FORMAT=" {{ Time }} "
# Reset the format of the car
unset PBT_CAR_TIME_FORMAT
# Reset the original train
unset PBT_CARS
### Themes
# Load theme
source themes/square_brackets_multiline
```

In order to allow the `ExecTime` car to calculate the execution time of every
command executed by the shell, the following must be placed into the shell
profile file:

```shell
# For ZSH
source /path/to/the/pbt/sources/ExecTime.zsh
# For Bash
source /path/to/the/pbt/sources/ExecTime.bash
```


Compilation
-----------

It's also possible to compile the script into a binary executable file which
should make it run about 10-20% faster. For that we will need a tool called
[`freeze`](https://wiki.python.org/moin/Freeze) which we can find in the Python
source tree:

```shell
git clone https://github.com/python/cpython.git -b "v$(python --version 2>&1 | grep -Po '.* \K\d.*')" --depth 1 /tmp/cpython
```

Then we can compile it:

```shell
python /tmp/cpython/Tools/freeze/freeze.py pbt.py
make
```

That will create a binary file `pbt` which can be used in the `PROMPT`
environment variable instead of the Python script as shown above.

The conpilation process sometimes incorrectly recognizes where Python's libraries
are exactly installed. Then we can get errors like this:

```
Error: needed directory /usr/lib/python3.6/config-3.6m not found
```

and

```
gcc: error: /usr/lib/python3.6/config-3.6m/libpython3.6m.so: No such file or directory
```

That can be solved by symlinks:

```python3
ln -s /usr/lib/python3.6/config-3.6m{-x86_64-linux-gnu,}
```

and

```shell
ln -s /usr/lib/{libpython3.6m.so,python3.6/config-3.6m/}
```


Author
------

Jiri Tyr


License
-------

MIT
