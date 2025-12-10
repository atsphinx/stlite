Show table from pandas DataFrame
================================

Code
----

.. code-block:: rst

   .. stlite::

      import streamlit as st
      import pandas as pd

      df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
      })

      st.write(df)

Application
-----------

.. stlite::

   import streamlit as st
   import pandas as pd

   df = pd.DataFrame({
       'first column': [1, 2, 3, 4],
       'second column': [10, 20, 30, 40]
   })

   st.write(df)
