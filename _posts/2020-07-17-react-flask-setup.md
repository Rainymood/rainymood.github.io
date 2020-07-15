---
title: "How to set up a React and Flask project" 
date: 2020-07-15
categories:
  - blog
tags:
  - blog
  - git
  - tutorial
  - flask
  - react
header:
  teaser: "/assets/2020-07-17-react-flask-setup/flaskreact.png"
---

In this blog post I will go over how to set up your React and Flask project
while avoiding the dreaded Cross-Origin Resource Sharing (CORS) error.

This is what the final demo looks like. 

<img src="/assets/2020-07-17-react-flask-setup/demo.png">

You can find the code on Github [here](https://github.com/Rainymood/react-flask-demo).

## Flask server

Setting up the Flask server is easy. Make a new python file `server.py` and
add the following content.

```python
from flask import Flask
from flask import jsonify
import time
app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

if __name__ == '__main__':
   app.run(debug=True)
```

What we basically do here is that we set up a Flask webserver with a single
route called `/time` which returns a json object of the current time as a
UNIX timestamp. If you start the server you should be greeted with the
following output.

```bash
$ python3 server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 212-654-497
```

Sending a simple `GET` request with Postman should return a json object with
a single item called `time` which is a UNIX timestamp of the current time. We
will try to send this to our React frontend.

```json
{
  "time": 1594819306.902315
}
```

## React frontend

Getting started with the React frontend is also easy because we have
`create-react-app`. Assuming that we are already in the folder that you want
to work from and have created the `server.py` file, we will now create a new
react project in this folder.

```bash
npx create-react-app .
```

Now we just have to connect the React frontend with the Flask backend. 
We can do this by changing the contents of `src/App.js` into this. 

```js
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/time')
            .then((res) => res.json())
            .then((data) => {
                setCurrentTime(data.time);
            });
    }, []);

    return (
        <div className='App'>
            <header className='App-header'>
                <img src={logo} className='App-logo' alt='logo' />
                <p>The current time is {currentTime}.</p>
            </header>
        </div>
    );
}

export default App;
```

What does every line here do?

```js
import React, { useState, useEffect } from 'react';
```

This imports `useState` and `useEffect` which we need to manage states and
effects (which is a lifecycle method). `useEffect` allows us to "do
something" after everything has rendered. We will use this to plug in the
results from our api call to the Flask backend after everything has rendered.

```js
const [currentTime, setCurrentTime] = useState(0);
```

Here we use the `useState(0)` function to first set the initial state to
zero. We return the current state (`currentTime`) and a function to change
the state (`setCurrentTime`). This is how `useState()` works.

```js
useEffect(() => {
    fetch('/time')
        .then((res) => res.json())
        .then((data) => {
            setCurrentTime(data.time);
        });
}, []);
```

Here we call the method `useEffect()` which does something after all the
components are rendered. We use `fetch()` to make a `GET` request to our
endpoint `/time` which defaults to `localhost:3000` which is where our React
app is hosted. After receiving the endpoint we convert it into a json and
then set the new state using the function `setCurrentTime()` to the timestamp
we got from the api call.

```js
return (
    <div className='App'>
        <header className='App-header'>
            <img src={logo} className='App-logo' alt='logo' />
            <p>The current time is {currentTime}.</p>
        </header>
    </div>
);
```

Then our `render()` function which renders the JSX simply has another dynamic
field `{currentTime}` which displays the current time.

## Avoiding CORS issues

Finally, add this `proxy` setting to your `package.json`.

```json
{
  "proxy": "http://localhost:5000"
}
```

This is a crucial last step because if you to run your Flask server as a
normal server and try to make an api call to it you will be blocked because
of CORS.

>Access to fetch at 'http://127.0.0.1:5000/time' from origin
'http://localhost:3000' has been blocked by CORS policy: No
'Access-Control-Allow-Origin' header is present on the requested resource. If
an opaque response serves your needs, set the request's mode to 'no-cors' to
fetch the resource with CORS disabled.

This is basically what is happening:

* React runs on port 3000
* Flask runs on port 5000
* Usually for frontend and backend these are the same (so they "trust" each other)
* If they are not the same they do not "trust" each other and you have cross-origin issues (CORS)
* We configure React such that it forwards all requests it receives on 3000 to 5000
* This is how we avoid the CORS issues

You should be ready to run the React frontend now. 

```
npm start
```

# Conclusion

You're done! If you followed all the steps correctly your running React app
should look like this.

<img src="/assets/2020-07-17-react-flask-setup/demo.png">

That's it! In this blog post I provide you with a very small demo repository
that connects a React frontend with a Flask backend while avoiding CORS
issues.

# Subscribe

<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
  #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
  /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
     We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://gmail.us3.list-manage.com/subscribe/post?u=92fe86c389878585bc87837e8&amp;id=50543deff9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
  <label for="mce-EMAIL">Liked this article and want to hear more?</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->