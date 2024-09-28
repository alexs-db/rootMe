Looking at the source code of the page, we can see a very interesting comment:
# Nginx Alias Misconfiguration

## Issue Description
We encountered a misconfiguration issue with the `/assets/` alias. When navigating to this page, nothing interesting appears. However, if we remove the trailing slash (`/assets`), we are redirected correctly to `/assets/`. Notably, the port changes, indicating a configuration error.

## Research and Solution
During our research, we found a useful tool on [GitHub](https://github.com/shiblisec/Kyubi) that lists paths with configuration errors.

To use the tool, run:
```sh
kyubi -v http://challenge01.root-me.org:59092/assets/
```

Several paths are suggested. Testing the first one revealed something interesting:
```
http://challenge01.root-me.org:59092/assets../
```

## Conclusion
The next step is to access the `flag.txt` file.