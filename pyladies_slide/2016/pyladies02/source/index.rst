.. index.rst


ブログをWordpressからSphinxに乗り換えた話
==================================================

私とブログ
------------------

- 1995年にパソコン購入。同時にパソコン通信（niftyサーブ）開始。
- 1999年当時のプロバイダだったInfoWeb（現@nifty）からホームページスペースを与えられたので、htmlを自分で書いてブログスタート。
- 2004年html書くのめんどくさくなって、どっかのブログサービスでブログ開始。
- 2006年フリーランスになったので、勉強のために自分でCMSを運営しようとhetemlと契約。Nucleus CMSにブログを乗り換え。
- 2010年Wordpressの仕事が増えて、プラグインを作ったりしていた。Nucleus CMSの更新がほぼなくなり、hetemlがサポートするPHPのバージョンと合わなくなってくる。hetemlにWordpress簡単インストールというサービスができた機にWordpressに乗り換え。
- 2016年Sphinx製の静的Webページに乗り換え

どうして乗り換えたか
------------------------------------

- PHPを書かなくなっているうちにhetemlのPHPがバージョン7になった。
- Wordpressがしょっちゅう更新しろ！と言ってきて、鬱陶しくなった。
- Wordpressにセキュリティーホールが見つかるたびにhetemlからお知らせが来て、対応しないといけないのがめんどくさくなってきた。
- ブログしかやってないので、はてなにでも乗り換えようか。。。
- セキュリティーとか気にしなくていい、静的HTMLに乗り換えよう！
- せっかく、Pythonかけるようになったし、Sphinxだ！

乗り換え方
------------------

元のサイトをcurlする
+++++++++++++++++++++++++++++

**curl** はHTTPアクセスをしてコンテンツを取得できるコマンドです。

私のブログは記事に番号がついていてそれがURLでした。

::

    http://kamekokamekame.net/archives/1207/


↑こんなの

::

    curl http://kamekokamekame.net/archives/[1-9999]/ -o "#1.html"


これで、 **[記事の番号].html** というファイル名で取得できます。

htmlをMarkdownに変換
+++++++++++++++++++++++++++++

htmlを編集し続けるのが嫌だったので、どこにでも持っていきやすいMarkdownにPythonスクリプト書いて置き換えました。

(ここが素敵だとかっこいいんですが、一回だけなんで、愚直に適当に書いてしまいました。見たかったらどうぞ [gist](https://gist.github.com/okusama27/66d184a5e7091b1e24948af66c205106))

Sphinxでhtmlを作ろう
----------------------
インストール
+++++++++++++++++++++++++++++

::

    $ python3 -m venv env
    $ pip install Sphinx commonmark recommonmark


プロジェクト作成
++++++++++++++++++++

::

    $ sphinx-quickstart


conf.pyの修正
^^^^^^^^^^^^^^^^^^^^^^

::

    source_suffix = ['.rst', '.md']
    source_parsers = {
        '.md': 'recommonmark.parser.CommonMarkParser',
    }


index.rstを作成
^^^^^^^^^^^^^^^^^^^^^^

ビルド

::

    make html


**build/html** フォルダの中身をサーバーにドーン！


まとめ
-----------

- 実はあまりPythonをわかっていなくても, Markdownが書ければ、いいだけな気がする。
- 嫌になったら、Githubでブログを営むこともできるのでMarkdownにしておくのはいいと思う。

おまけ(rss)
-------------
feedのプラグインがなかったんで、feedを出力してくれるスクリプトも作りました。

自分のMarkdownから、タイトルとか記事とか取るだけのスクリプト。（汚いですが、見たかったらどうぞ。 [gist](https://gist.github.com/okusama27/fc87c5f9ebd0b38590bcaa05a070736a)）

結局、 **feedgenerator** というのを使うと各情報を渡すだけでfeedできます。どーん。

::

    # フィードを生成
    return feedgenerator.Rss201rev2Feed(title=title,link=link,feed_url=feed_url,description=description,language="ja")


これはもうちょっと綺麗にしたいです。

