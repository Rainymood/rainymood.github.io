
# Vim solarized-dark terminal #

18-05-2016: first draft 

tl;dr (1) Download iterm2 configuration (2) Add stuff to your .vimrc

I finally got my solarized-dark colorscheme working on my terminal again. As of
18-05-2016 on iTerm 2.1.4 Mac OSX Yosemite 10.10.3 and Vim 7.3. 

Does your Vim in the terminal look like this? 

image-of-vim.jpg

A lot of people on the internet suggested to add 

    let g:solarized_termtrans=1
    let g:solarized_termcolors=256

But I found out later that that was actually the _cause_ of my problems. To fix
this ugly monstrosity, first follow this link 

*link*

And import them into your iterm2 like this

*image*

and make sure to actually set the colorscheme as follows

*image*

Then add this to your ~/.vimrc

    if !has("gui_running")
        " These options fixed my solarized-dark problems
        let g:solarized_termcolors = 16
        let g:solarized_termtrans  = 16
        let g:solarized_contrast   = "high"
        let g:solarized_visibility = "high"
    endif
    set background=dark
    colorscheme solarized

I am not exactly sure what is happening, but my terminal vim now looks like this

*image*

which I am very pleased with. 






