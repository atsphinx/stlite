===============
atsphinx-stlite
===============

.. toctree::
   :maxdepth: 1
   :hidden:

   guide
   changes

.. raw:: html

   <style>
     h2, h3, p, ul {
       text-align: center;
     }
     h1 {
       display: none;
     }
     .content ul {
       list-style-type: none;
     }
   </style>

**atsphinx-stlite** is Sphinx extension to embed Stlite contents into your documentation.

Show the demo
=============

Whn you write left-side content into your document,

.. grid:: 2

   .. grid-item-card::

      .. tab-set::

         .. tab-item:: RST

            .. code:: rst

               .. stlite::

                  # This source is copy from "Hello" app from https://streamlit.io/playground
                  import streamlit as st

                  st.title("Hello Streamlit-er 👋")
                  st.markdown(
                      """
                      This is a playground for you to try Streamlit and have fun.

                      **There's :rainbow[so much] you can build!**

                      We prepared a few examples for you to get started. Just
                      click on the buttons above and discover what you can do
                      with Streamlit.
                      """
                  )

         .. tab-item:: MD

            .. code:: md

               ```{stlite}
               # This source is copy from "Hello" app from https://streamlit.io/playground
               import streamlit as st

               st.title("Hello Streamlit-er 👋")
               st.markdown(
                   """
                   This is a playground for you to try Streamlit and have fun.

                   **There's :rainbow[so much] you can build!**

                   We prepared a few examples for you to get started. Just
                   click on the buttons above and discover what you can do
                   with Streamlit.
                   """
               )
               ```

   .. grid-item-card::

      .. stlite::

         # This source is copy from "Hello" app from https://streamlit.io/playground
         import streamlit as st

         st.title("Hello Streamlit-er 👋")
         st.markdown(
             """
             This is a playground for you to try Streamlit and have fun.

             **There's :rainbow[so much] you can build!**

             We prepared a few examples for you to get started. Just
             click on the buttons above and discover what you can do
             with Streamlit.
             """
         )

         if st.button("Send balloons!"):
             st.balloons()

When do you use this?
=====================

* Write description about Streamlit app on Sphinx.
* Write demonstration of presentation using sphinx-revealjs.

Are you interested in this?
===========================

Let's got to :doc:`./guide`.
