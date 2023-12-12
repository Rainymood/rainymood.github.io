# Styling

*Some notes that used to be in `main.scss`* 

How to edit minimal mistakes style if you use github pages

To make basic tweaks to theme’s style Sass variables can be overridden by adding
to <your_project>/assets/css/main.scss. For instance, to change the link color
used throughout the theme add:

From: https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/

Color settings MUST happen before the @import step

Interesting links: 
* https://github.com/k-bosko/k-bosko.github.io/blob/master/_sass/minimal-mistakes/_variables.scss
* highlighting: https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/
* https://glitchbone.github.io/vscode-base16-term/#/tomorrow-night
* https://nithiya.gitlab.io/development/pages-tweaks/

github syntax highlighting (base16):
* https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/#colors
* https://github.com/Defman21/base16-github-scheme/blob/master/github.yaml
* http://chriskempson.com/projects/base16/
* https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/#colors
* https://mmistakes.github.io/minimal-mistakes/markup-syntax-highlighting/#gfm-code-blocks

Moritz Lange writes: 
You'll have to first set variables (like those in _variables.scss), then import
minimal mistakes, and finally write the html code.
The html part will set the default font size (i.e. the text font size within
your posts). The type-size variables on the other hand will set font size for
other elements like table of content etc., relative to the default size
specified in the html block. 

From: https://github.com/mmistakes/minimal-mistakes/discussions/1352#discussioncomment-2074482


```scss
// 2023-01-07: Trying to hack this together. If this works I'm going to be so
// surprised!
$lightgreen: #dcfce7;
$darkgreen: #166534;
$lightyellow: #fef9c3;
$darkyellow: #854d0e;
$lightblue: #e0f2fe;
$darkblue: #0d5884;


// Overwrites default button style with things...
.btn-green {
  /* default */
  display: inline-block;
  margin-bottom: 0.25em;
  padding: 0.1em 0.7em; // top/sides 0.2 0.6 also works
  font-family: $sans-serif;
  font-size: $type-size-7;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 10px;
  background-color: $lightgreen;
  color: $darkgreen;
  cursor: pointer;
  &:visited {
    color: $darkgreen;
    };
}

// Overwrites default button style with things...
.btn-blue {
  /* default */
  display: inline-block;
  margin-bottom: 0.25em;
  padding: 0.1em 0.7em; // top/sides 0.2 0.6 also works
  font-family: $sans-serif;
  font-size: $type-size-7;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 10px;
  background-color: $lightblue;
  color: $darkblue;
  cursor: pointer;
  &:visited {
    color: $darkblue;
    };
}

.btn-yellow {
  /* default */
  display: inline-block;
  margin-bottom: 0.25em;
  padding: 0.1em 0.7em; // top/sides 0.2 0.6 also works
  font-family: $sans-serif;
  font-size: $type-size-7;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 10px;
  background-color: $lightyellow;
  color: $darkyellow;
  cursor: pointer;
  &:visited {
    color: $darkyellow;
    };
}
```