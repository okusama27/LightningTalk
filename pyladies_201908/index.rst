=====================================
PEPの紹介
=====================================

2019-08-18

本資料は、 
`PyLadies Tokyo Meetup #44 夏休み! PEP自由研究発表会 <https://pyladies-tokyo.connpass.com/event/136599/>`_ の資料です。

.. contents:: Outline

お前誰よ
=====================================
大村 亀子（ `@okusama27 <https://twitter.com/okusama27>`_ ）

- PyLadies Tokyo スタッフ
- 普段はPython教育サービスの開発、Pythonを利用した受託開発に従事
- 最近は投資分析の勉強中

.. image:: images/cow.png

Pythonの歴史
=====================================

詳しくは、 `Python の歴史 <https://docs.python.org/ja/3/license.html>`_ を参照ください。

1989年
---------------

オランダ人の `Guido van Rossum <https://en.wikipedia.org/wiki/Guido_van_Rossum>`_ がクリスマス休暇中に暇だったので開発を開始したのがはじまり。

イギリスで大人気だったテレビ番組「空飛ぶモンティ・パイソン」（Monty Python's Flying Circus）から取って、Pythonと名付けた。

.. image:: images/python-logo-master-v3-TM.png
   :width: 300px

.. パイソンとは「ニシキヘビ」のことなので、Python関連のライブラリやアプリケーション、コミュニティーのシンボルるに蛇にちなんだアイコンが使われます。


2001年
-------------

Pythonソフトウェア財団、PSF（ `PythonSoftwareFoundation <https://www.python.org/psf/>`_ ）が組織される。

Python関連の知的所有権を所有するために作られた非営利団体。
Pythonのリリースはすべて `オープンソース <https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%82%BD%E3%83%BC%E3%82%B9%E3%81%AE%E5%AE%9A%E7%BE%A9>`_ です。

参照: `Python公式ドキュメント: 歴史とライセンス <https://docs.python.org/ja/3/license.html>`_

.. Pythonは1990年代初頭に、オランダのStichtingMathematischCentrum(CWI。http://www.cwi.nl/参照)にいたGuidovanRossumにより、
   ABCという言語の後継として創造された。
   現在Pythonには他者からのコントリビューションが数多く含まれるが、第一著者は依然としてGuidoである。
   Guidoは1995年からヴァージニア州レストンにあるCorporationforNationalResearchInitiatives(CNRI。http://www.cnri.reston.va.us/参照)でPythonの作業を続け、ここでいくつかのバージョンをリリースした。
   2000年、GuidoとPythonコア開発チームはBeOpen.comに移り、BeOpenPythonLabsチームを結成した。
   同年10月、PythonLabsチームはDigitalCreation(現在はZopeCorporation。http://www.zope.com/参照)に移った。
   2001年、PythonSoftwareFoundation(PSF。https://www.python.org/psf/参照)が組織される。
   これはPython関連の知的所有権を所有するために作られたNPO団体である。ZopeCorporationはPSFの後援会員である。
   PythonのリリースはすべてOpenSourceである(大文字に注意。オープンソースの定義についてはhttp://opensource.org/参照)。
   歴史的には、ほとんどのPythonリリースはGPLコンパチブルだが、すべてがそうではない。
   「GPLコンパチブル」とは、我々がPythonをGPLで配布するという意味ではない。Pythonは全ライセンスにおいて、
   改変部分をオープンソースとしない改変版の配布を認めているが、これはGPLとは異なる。
   GPLコンパチブルなライセンスとは、PythonをGPLでリリースされたソフトウェアと組み合わせることを可能にするものである。
   コンパチブルでないライセンスでは不可能ということだ。
   Guidoの指揮のもと作業を行い、これらのリリースを可能にしてくれた数多くの外部ボランティアに感謝する。


PEPとは
=====================================

`PEP <https://github.com/python/peps>`_ はPython 拡張提案(Python Enhancement Proposal)の略語です。

Pythonについて大きな変更が行われるときは、PEPという文書が書かれて議論されます。

最初のコミットは2000年7月13日: `Initial set of Python Enhancement Proposals <https://github.com/python/peps/commit/41021a4bf9c3d410c7082cb514d8805e1eea2c8d>`_

PEPの利用方法、書き方などの運用のプロセスも PEPとしてまとまっています。

PEPについて詳しくは、 に記載があります。

.. 和訳 `Python Enhancement Proposal: 1 <http://sphinx-users.jp/articles/pep1.html>`_

また、 `PEP 0 -- Index of Python Enhancement Proposals (PEPs) <https://www.python.org/dev/peps/>`_ を参照すると、PEPの歴史を一覧で参照できます。


PEP 1 -- PEPの目的とガイドライン
====================================================
`PEP 1 -- PEP Purpose and Guidelines <https://www.python.org/dev/peps/pep-0001/>`_ の紹介をします。

PEPの対象者
--------------------------
PEPの主な対象者は、Python言語の実装者です。


PEPの種類
-------------
PEPには以下の3つの種類のドキュメントがあります。

Standards Track(標準化過程)
++++++++++++++++++++++++++++++++++++++++++++++++++
Pythonの新しい機能や実装について説明するドキュメント

Informational(情報)
++++++++++++++++++++++++++++++++++++++++++++++++++
Pythonの設計上の課題や、Pythonコミュニティに知らせる一般的なガイドラインや情報などを説明するドキュメント


Process(プロセス)
++++++++++++++++++++++++++++++++++++++++++++++++++
Pythonを取り巻くプロセスについて説明をしたり、プロセスや、プロセス中のイベントについて提案したりするドキュメント


PEPワークフロー
--------------------------
PEPの作成からの流れを紹介します。

Pythonの運営委員会
+++++++++++++++++++++++++++
PEPを受け入れるか拒否するかを最終的に決めるPythonの運営委員会があります。詳しくは、 `PEP13 <https://www.python.org/dev/peps/pep-0013/#current-steering-council>`_ で説明されています。

現在は以下の５人の人が投票で選ばれました。選出についての `PEP8100 <https://www.python.org/dev/peps/pep-8100/>`_ もあります。

* Barry Warsaw
* Brett Cannon
* Carol Willing
* Guido van Rossum
* Nick Coghlan

Pythonの生みの親であるGuidoさんも選挙に参加しています。投票はアクティブなPythonコアの開発者が行います。

以前は、GuidoさんがBDFL(慈悲深き終身独裁者）として決めていましたが、2018年7月にBDFLから引退しました。


アイデア
++++++++++++++++++++++++++++++++++++++++++++++++++

Pythonの言語に関するアイデアは特定のメーリングリスト( python-ideas@python.org 、python-list@python.org)や `SIG's <https://www.python.org/community/sigs/>`_ などで議論されている。

アイデアを思いついたら、メーリングリストやSIG'sに投げて議論します。

PEPの提出
++++++++++++++++++
議論後、PEPを提出します。PEP作成者がコア開発者でない場合は、コア開発スポンサーを見つける必要があります。コア開発スポンサーは、PEP作成者をメンターとして支援します。

PEPの提出準備ができたら、PEPのDraftとして、GitHubのプルリクエストを作成します。PEPの書き方（ `PEP12 <https://www.python.org/dev/peps/pep-0012/>`_ ）を守って記述します。
書き方を守らないと却下されます（ちょっとした不具合はPEP編集者が直してくれる場合もあります）。

Draft(草案)
++++++++++++++++++++++++++++++++++++++++++++++++++
PEP編集者が承認するとPEP番号が割り当てられます。ステータスは"Draft"(草案)になります。

Accepted（受理）、Rejected（却下）
++++++++++++++++++++++++++++++++++++++++++++++++++
PEPができたら、コア開発者にレビューを要求できます。
最終的に運営委員会が受理か、却下を行います。
そのPEPの最終決定を行うのにふさわしい経験があるコア開発者が申し出れば、BDFLの権利を移譲したりします。

Final（確定）
++++++++++++++++++++++++++++++++++++++++++++++++++
承認されて、 `リファレンス実装（Reference implementation） <https://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E5%AE%9F%E8%A3%85>`_ が完成し、main source code repositoryに取り込まれたら、"Final"（確定）になります。


PEPのステータスの移行可能な経路
++++++++++++++++++++++++++++++++++++++++++++++++++

流れはこんな感じだそうですが、違う場合もあるそうです。

.. image:: images/pep_image.png

図は、 `PEP1 <https://www.python.org/dev/peps/pep-0001/>`_ より参照。

Deferred（延期）、Withdrawn（取り下げ）、Active（完成させることを意図していない。PEP1など）などに設定されることもあります。

PEPを読もう
========================
新しいPythonに採用されたPEPがわかります。

例. `Python3.8 <https://docs.python.org/3.8/>`_ の「What’s New In Python 3.8」をクリックすると追加させた機能などが見れます。

参考資料
=====================================

日本人のPEPへの貢献
---------------------------------
日本人にもPEPを作り確定した方がいらっしゃいます。

* `Atsuo Ishimoto <https://twitter.com/atsuoishimoto>`_ さんの `PEP 3138 -- String representation in Python 3000 <https://www.python.org/dev/peps/pep-3138/>`_

* `INADA Naoki <https://twitter.com/methane>`_ さんの `PEP 545 -- Python Documentation Translations <https://www.python.org/dev/peps/pep-0545/>`_

`PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ しか読んだことがなかったので、これからはもうちょっと読んでいこうと思います。


リンク一覧
---------------------------------
* PSF: https://www.python.org/psf/
* PEP: https://github.com/python/peps
* 最近のPython: http://dsas.blog.klab.org/archives/2018-04/python-dev.html
