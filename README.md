# Documentation for NumPy

This repo holds the generated documentation for historical versions of NumPy.

To add documentation for a version:

- Run [`make dist`](https://stackoverflow.com/questions/43197756/what-is-the-difference-between-make-and-make-dist) in
  the `doc` directory of a numpy source checkout

- Expand the resulting `build/dist.tar.gz in the appropriately-named top-level
  directory, and add it to git. So for NumPy release 1.18 something like:

  ```bash
  git rm -r 1.18
  mkdir 1.18
  tar -C 1.18 <path-to-numpy>/doc/build/dist.tar.gz
  git add 1.18
  git commit -m"Add documentation for v1.18"
  ```

- Edit the `index.html` to reflect the new files by copy-pasting an existing
  stanza beginning with `<!-- tag vX.YY.Z -->` after the
  `<!-- insert here -->` comment, and changing the `href` locations
  appropriately.

- Finally, run `pip install packaging; python3 update.py` and commit all changes.
