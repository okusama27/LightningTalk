memo
=========
Python チュートリアル第3版より


C.1 このソフトウェアの歴史
-----------------------
Python は 1990 年代初頭に、オランダの Stichting Mathematisch Centrum(CWI。http://www.cwi.nl/ 参照)にいた Guido van Rossum により、ABC という言語の後 継として創造された。現在 Python には他者からのコントリビューションが数多く含 まれるが、第一著者は依然として Guido である。

Guido は 1995 年からヴァージニア州レストンにある Corporation for National Research Initiatives(CNRI。http://www.cnri.reston.va.us/ 参照)でPython の作 業を続け、ここでいくつかのバージョンをリリースした。

2000 年、Guido と Pythonコア開発チームはBeOpen.comに移り、BeOpen PythonLabs チームを結成した。

同年 10 月、PythonLabs チームは Digital Creation(現在は Zope Corporation。http://www.zope.com/ 参照)に移った。

2001 年、Python Software Foundation(PSF。https://www.python.org/psf/ 参照)が組織される。これは Python 関連の知的所有権を所有するために作られた NPO 団体である。Zope Corporation は PSF の後援会員である。
  
Python のリリースはすべて Open Source である(大文字に注意。オープンソース の定義については http://opensource.org/ 参照)。歴史的には、ほとんどのPython リリースは GPL コンパチブルだが、すべてがそうではない。
「GPL コンパチブル」とは、我々が Python を GPL で配布するという意味ではな い。Python は全ライセンスにおいて、改変部分をオープンソースとしない改変版の 配布を認めているが、これは GPL とは異なる。GPL コンパチブルなライセンスとは、 Python を GPL でリリースされたソフトウェアと組み合わせることを可能にするも のである。コンパチブルでないライセンスでは不可能ということだ。Guido の指揮のもと作業を行い、これらのリリースを可能にしてくれた数多くの外 部ボランティアに感謝する。


1.3 PEP文書から最新の変更情報を得る
Python コミュニティは変化を取り入れるための、成熟したメカニズムを備えています。ちょっとし た Python の言語に関するアイデアは特定のメーリングリスト(python-ideas@python.org)で議論 されますが、大きな変更が行われるときは、必ず PEP と呼ばれる文書が書かれることになっていま す。PEP は Python 拡張提案(Python Enhancement Proposal)の略語です。PEP は Python に変更 を加えるための提案書で、コミュニティが議論を行うための出発点となります。PEP の目的、フォー マット、ワークフローといったもの自身も、Python 拡張提案の形式で標準化されています。詳しくは PEP 1(https://www.python.org/dev/peps/pep-0001)を参照してください∗5。
PEP の各文書は Python にとって非常に重要なものです。それぞれの文書はトピックに応じていく つかの目的を持ちます。
● 通知(Informing):Python のリリーススケジュールについて、コア Python の開発者が必要な情 報をまとめて伝えます。
● 標準化(Standardizing):コードスタイル、ドキュメント、またはその他のガイドラインを提供 します。
● 設計(Designing):提案された機能について説明します。
提案されたすべての PEP のリストは、PEP 0(https://www.python.org/dev/peps/)にあります。 PEP 文書は 1 カ所に集約されていて、実際の URL を推測するのも簡単なので、本書の中では番号を 使って参照します。
Python 言語がどこに向かっているか興味があるけれど、Python メーリングリストで行われる議論 の流れをすべて追いかける時間を持てない人にとって、PEP 0 は情報の宝庫です。この文書を読むと、 すでに承認されているがまだ実装されていない PEP 文書や、現在検討中の PEP 文書もわかります。
PEP はこれ以外にも役立ちます。たとえば、次のような質問が頻繁に行われます。
● なぜ機能 A はこのようになっているんですか? ● なぜ Python には機能 B がないんですか?
ほとんどのケースで、質問の答えが書かれた PEP 文書を見つけられます。提案されたけれど、受理 されなかった Python 言語機能を紹介した PEP 文書もたくさんあります。これらの文書は歴史的な文 献として残されています。