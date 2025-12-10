==========
User guide
==========

Installation
============

This is published on PyPI.
You can install this by your using package managers.

.. tab-set::

   .. tab-item:: pip

      .. code-block:: console

         pip install atsphinx-stlite

   .. tab-item:: uv

      .. code-block:: console

         uv add atsphinx-stlite

Usage
=====

1. Register as extension
------------------------

Append this into ``extensions`` of your ``conf.py``:

.. code-block:: python

   extensions = [
       # Using other extensions
       ...,
       # Append it.
       "atsphinx.stlite",
   ]

2. Write Stlite contents
------------------------

Write your Stlite app code into document using ``stlite`` directive.

.. code-block:: rst

   .. stlite::

      import streamlit as st
      import pandas as pd

      df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
      })

      st.write(df)


3. Build as HTML
----------------

When you build by HTML-based builder, there are applications of Stlite on your documents.

Please see ":doc:`./examples/pandas-dataframe`" to know build result.

Configuration
=============

There are some configuration values for this extension.

.. confval:: stlite_default_version
   :type: str
   :default: "latest"

   Using version of Stlite from CDN.

   If you want to lock version of Stlite, set this value.
