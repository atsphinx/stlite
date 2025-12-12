===============
atsphinx-stlite
===============

Embed Stlite frame into Sphinx documentation.

Overview
========

This is Sphinx extension to provide directive
to render Streamlit application on document using Stlite.

When you use this, your document will display interactive contents.

Example
=======

This is example to display table from pandas DataFrame.

.. code:: rst

   .. stlite::

      import streamlit as st
      import pandas as pd

      df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
      })

      st.write(df)

If you want to know how does it display,
go to `demo page of document <https://atsphinx.github.io/stlite/en/examples/pandas-dataframe/>`_.

You can also set external python file.

.. code:: rst

   .. stlite:: example.py

Usage
=====

1. Install from PyPI (e.g. ``pip install atsphinx-stlite`` )
2. Add ``atsphinx.stlite`` to ``extensions`` in ``conf.py`` of your document.
3. Write contents refer to `documents <https://atsphinx.github.io/stlite/en/>`_.
4. Build your document using HTML-based builders (e.g. ``make html`` )
5. Show it!

For contributing
================

*Do you have a feedback to this?*

When you want to contribute to this project,
please follow the `atsphinx's common contributing guide <https://atsphinx.github.io/en/contributing/>`_.

License
=======

This project is licensed under the Apache License 2.0.
See `it <https://github.com/atsphinx/stlite/blob/main/LICENSE>`_.
