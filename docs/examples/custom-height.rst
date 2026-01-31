==================
Custom Height Demo
==================

This example demonstrates how to use the ``:height:`` option to control the size of stlite components.

Basic Usage
===========

Simple example with 400px height:

.. stlite::
   :height: 400px

   import streamlit as st
   
   st.title("Custom Height Example")
   name = st.text_input("Your name")
   st.write(f"Hello, {name or 'World'}!")

Larger Component
================

For charts and visualizations, use a larger height:

.. stlite::
   :requirements: matplotlib
   :height: 600px

   import streamlit as st
   import matplotlib.pyplot as plt
   import numpy as np

   size = st.slider("Sample size", 100, 1000, 500)
   
   data = np.random.normal(0, 1, size)
   fig, ax = plt.subplots()
   ax.hist(data, bins=20)
   st.pyplot(fig)
