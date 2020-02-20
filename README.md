# About

Creates an export dart files which export all
the files under the `src` folder.

# Installation

To install this, git clone this repo under the `lib`
folder on your Flutter packages. All packages must be
under under the `src` to have this exporter list all
the widgets and exported.

For example:

```
lib/
   |-> src/ Your files to be package and exported.
   |-> git clone here!
```

# How to run

If you don't have `make` installed, you can
install using `brew` if you are on MacOS.
Type `brew install make` to install `make`.

To run and create export file type `make FILE='your_export_name'`.