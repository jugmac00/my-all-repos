# my-all-repos
custom code / plugins / applications for the wonderful [all-repos](https://github.com/asottile/all-repos) command line tool

## tox.py

### background

Bernát Gábor asked for [support to alpha-test the upcoming `tox 4`](https://twitter.com/gjbernat/status/1365663098116468738),
which is a complete rewrite for the current and wide-spread `tox` (version 3).

I already used `tox 4 alpha` for my day-to-day work, noticed and reported a couple of issues, which were fixed in no time.

But as I am also a contributor/maintainer of the almost [300 active Zope repositories](https://github.com/zopefoundation/),
which basically all use `tox`,
I needed some tooling support to run `tox 4 alpha` on all of them.

For more information about the background story, see my [blog post](https://jugmac00.github.io/blog/testing-the-tox-4-pre-release-at-scale/).

### all-repos-configuration

```
{
    "output_dir": "output_zope",
    "source": "all_repos.source.github_org",
    "source_settings":  {
        "api_key": "xxx",
        "org": "zopefoundation"
    },
    "push": "all_repos.push.github_pull_request",
    "push_settings": {
        "api_key": "xxx",
        "username": "jugmac00"
    }
}

all-repos-zope.json (END)
```
### preparations

- create a virtualenv
- `pip install all-repos`  # this is necessary as it is used as a library
- make sure you have `tox 4 alpha` on your path (`pip install --pre tox`)

### relevant commands

#### clone all repos

```
all-repos-clone -C all-repos-zope.json
```

#### run tox 4 on all repos

```
python tox.py -C all-repos-zope.json
```
