---
title: "Hello World"
date: 2021-04-12T15:33:44+02:00
draft: false
tags: ['cloud','hetzner']
---

This is a fresh new blog built with Hugo and Ink theme in less than an hour!

This is more random text

This is a code sample

```python
squares1 = [x**2 for x in range(1, 11)]

squares2 = list(x**2 for x in range(1, 11))
```

And this is another snippet

```python
from __future__ import print_function  # Only needed for Python 2
print("hi there", file=f)

f = open('myfile', 'w')
f.write('hi there\n')  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it
```

This is a bash snippet
```bash
ls -al
wget https://lsyncd.com/lsync.tar.gz
tar -xzf lsync.tar.gz
```