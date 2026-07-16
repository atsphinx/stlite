Plot histogram chart
====================

Code
----

.. code-block:: rst

   .. stlite::
      :width: 800
      :config:
        [client]
        toolbarMode = "viewer"
      :requirements:
        matplotlib

      import streamlit as st
      import matplotlib.pyplot as plt
      import numpy as np

      size = st.slider("Sample size", 100, 1000)
      arr = np.random.normal(1, 1, size=size)
      fig, ax = plt.subplots()
      ax.hist(arr, bins=20)
      st.pyplot(fig)

Application
-----------


.. stlite::
   :width: 800
   :config:
     [client]
     toolbarMode = "viewer"
   :requirements:
     matplotlib

   import streamlit as st
   import matplotlib.pyplot as plt
   import numpy as np

   size = st.slider("Sample size", 100, 1000)
   arr = np.random.normal(1, 1, size=size)
   fig, ax = plt.subplots()
   ax.hist(arr, bins=20)
   st.pyplot(fig)
