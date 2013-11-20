Quickstart:
-----------

```
% python main.py <input-filename>
```


Virtual Machine:
----------------

Comes packaged with a virtual machine for environment reproduction.

```
% vagrant up
% vagrant ssh
$ cd /vagrant
$ python main.py <input-filename>
```


Dependencies:
-------------

This software is built over Python 2.7. The `iteritems` method and tuple unpacking are both deprecated in Python 3+ and will _not_ be backcompatible with this build.


Authors:
--------

 - Andy Chiang
 - ...


License:
--------

Copyright &copy; 2013 Andy Chiang.

Distributed under the MIT License.