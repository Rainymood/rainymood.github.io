# FAQ

## Q: How to view your bundler version?

```bash
cat Gemfile.lock | grep -A 1 "BUNDLED WITH"
BUNDLED WITH
   1.17.3
```

## Q: How to override settings

Change the settings in `assets/css/main.scss`.

## Q: How to change your home page?

Change settings in `index.html`.

## Q: How to uninstall all gems?

```bash
gem uninstall -aIx
```

## Q: How to resolve incompatible ruby gems

```bash
ruby_dep-1.5.0 requires ruby version >= 2.2.5, ~> 2.2, which is incompatible
with the current version, ruby 3.0.2p107
```

`bundle update`

## Q: How to solve cannot load such file (LoadError)

```bash
λ bundle exec jekyll serve
...
C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve/servlet.rb:3:in `require': cannot load such file -- webrick (LoadError)
```

`bundle add webrick`

## Q: How to resolve cannot load such file rubyeventmachine (LoadError)

```
Unable to load the EventMachine C extension; To use the pure-ruby reactor, require 'em/pure_ruby'
C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/eventmachine-1.2.7-x64-mingw32/lib/rubyeventmachine.rb:2:in `require': cannot load such file -- 3.0/rubyeventmachine (LoadError)
...
```

```bash
gem uninstall eventmachine 
gem 'eventmachine', '1.2.7', git: 'https://github.com/eventmachine/eventmachine.git', tag: 'v1.2.7'
bundle install
bundle exec jekyll
```

See: https://stackoverflow.com/a/65547010