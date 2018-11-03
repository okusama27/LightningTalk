Sphinxで発表資料
=====================


Sphinxインストール
--------------------------

.. code-block::

  $ pip install sphinx


テーマ
---------
テーマは `sphinxjp.themes.gopher <https://pypi.org/project/sphinxjp.themes.gopher/>`_ を利用

テーマのインストール
+++++++++++++++++++++++++

.. code-block::

  $ pip install sphinxjp.themes.gopher


テーマの設定
+++++++++++++++++++++++++
``conf.py`` に以下を記述

.. code-block::

  extensions = ['sphinxjp.themes.gopher']
  html_theme = 'gopher'
  html_use_index = False

プロジェクトの作成
---------------------------

.. code-block::

   $sphinx-quickstart プロジェクト名

make
----------

.. code-block::

  $ make html