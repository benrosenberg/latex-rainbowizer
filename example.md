---
title: Rainbow Text Example
author: Ben Rosenberg
date: \today
header-includes: \usepackage{xcolor}
geometry: margin=1.0in
---

This is an example document illustrating the functionality of the `rainbowizer` script. 

Rainbow text begins with a line that looks like this:

```markdown
 -=- rainbow -=-
```

...and ends with a line that looks like this:

```markdown
 -=- wobniar -=-
```

The script takes the following arguments:

 - `filename`: the name of the file to rainbowize
 - `random`: whether or not to make the colors random instead of in a smooth ROYGBIV-like order (values that make the script use random colors are `random`, `true`, `randomize`, or any uppercase variants of these)

This is what the text inside looks like:

-=- rainbow -=-

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec elementum lorem. Vestibulum ut risus justo. Maecenas lobortis ullamcorper velit, non posuere quam gravida vel. Cras maximus pharetra congue. Pellentesque tempus enim ac purus blandit pellentesque. Mauris efficitur posuere urna. Vivamus ipsum justo, imperdiet id bibendum rutrum, iaculis blandit sem. Donec cursus porttitor luctus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ullamcorper pellentesque enim eu feugiat. Nullam efficitur non diam a tempor. Curabitur dignissim lorem sed vestibulum sollicitudin.

-=- wobniar -=-

The script simply inserts `\textcolor{<color>}{<character>}` for each character, alternating colors in the following order (when `random` is not passed):

 - `purple`
 - `red`
 - `orange`
 - `yellow`
 - `lime`
 - `green`
 - `teal`
 - `cyan`
 - `blue`
 - `violet`

It generates a new file each time it is run, with the name `<filename without extension>_rainbowized.<extension>`. This is so that you can continue to edit the relevant text after running the script. 

To compile to PDF, just use whatever method you normally use, but remember to compile using the `rainbowized` version of your file.

The script requires the `xcolor` package to function. It should work on both Markdown files and LaTeX files.