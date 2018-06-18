**Welcome fellow developers, this guide is intended for python-scaleway maintainers.
If you are not a maintainer, you probably want to check out the [documentation](README.rst)
instead.**

![Are you ready ?](https://media.giphy.com/media/lvuKkjGQvT4hq/giphy.gif)

## Package release HOWTO

Releasing a new python-scaleway version implies following the 3 following steps.

* Update the CHANGES file to add the date of release and if it's missing the
changes since the last one.
* Push the tags of the new version.
* Pushing a post release commit to let the place as it was when you found it.

For the sake of the example, we assume you want to release the version `42.8.0`
and the previous version was `42.7.0`.

### Update files before committing

The top part of the [CHANGES](CHANGES.rst) should contain a version with an
`unreleased` date.

```
`42.8.0 (unreleased) <https://github.com/scaleway/python-scaleway/compare/v42.7.0...develop>`_
--------------------------------------------------------------------------------------------

* Let the SDK make coffee.
```

You have to replace the `unreleased` statement with the date of the day.

Then you have to make sure the version you want to push is well defined in
`setup.cfg` and `scaleway.__init__.py`files. If it's not done please update
them to your version before committing.

### The Commit and The Tag

Now that you're confident in your changes and you are sure to push the right
code, you can commit them on the `develop` branch, tag your version and merge
it on `master`.

```bash
$> git commit -m "Release v42.8.0"
$> git tag "v42.8.0"
$> git push
$> git push --tags
$> git checkout master
$> git pull
$> git merge "v42.8.0"
$> git push
```

![Well done](https://media.giphy.com/media/d31w24psGYeekCZy/giphy.gif)

### This is the end, my friend

Now that you've push your version and you're happy, make the next one happy by
creating a `Post version bump` commit to let the repository like it was when
you've started using it.

You just have to update the same file you've changed when you did the release
commit.

1. CHANGES.rst: Add a new entry at the top of the file

```
`42.8.1 (unreleased) <https://github.com/scaleway/python-scaleway/compare/v42.8.0...develop>`_
--------------------------------------------------------------------------------------------

* Post release version bump.
```

2. setup.cfg: Update the `current_version` key with `42.8.1`
3. scaleway.__init__.py: Update the `__version__` key with `42.8.1`

Then just checkout `develop` add you changes and create a new commit.

```bash
$> git checkout develop
$> git add ./scaleway/__init__.py
$> git add ./CHANGES.rst
$> git add ./setup.cfg
$> git commit -m "Post release version bump."
$> git push
```

![Job done](https://media.giphy.com/media/l0MYw3oeYCUJhj5FC/giphy.gif)
