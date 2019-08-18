[PyLadies Tokyo Meetup #44 夏休み! PEP自由研究発表会](https://pyladies-tokyo.connpass.com/event/136599/) でワークした成果の資料

# PEP 257を調べる
[PEP 257](https://www.python.org/dev/peps/pep-0257/)

## お題
EP257 Docstring Conventionsの内容説明、および有名なDocstring記法について調査してください

----

## (1) PEP257 Docstring Conventionsの内容説明

### What is a Docstring? (kame-chan)
Docstringとは何だろな？

Docstringとは、モジュール、関数、クラス、メソッドなどの定義の最初に書く文字列です。 `__doc__` 属性で参照できるようになります。

あらゆるものにDocstringは必要です。モジュールがディレクトリの場合は、`__init__.py` に書かれたものが利用されます。

Docstringは三連引用符 `"""` を利用して書きましょう。Docstringの内部でバックスラッシュを利用したい場合は `r"""` を利用し、UnicodeのDocstringの場合は、 `u"""` を利用しましょう。

Docstringには、1行のものと複数行のものがあります。

### One-line Docstrings (sugita)
- docstringはワンライナーでも書くことができる
- 1行に収まる場合でも '''(三重引用符）を使用する
- 始まりと終わりの引用符が同じ行にある
- ピリオドで終わるフレーズにする。 
  - ex) `Return the pathname of the KOS root directory.` 
- 以下のような関数と同様の処理をdocstringに書くのは好ましくない
```
def function(a, b):
    """function(a, b) -> list"""
```
こう書くべき
```
def function(a, b):
    """Do X and return a list."""
```


### Multi-line Docstrings(riko)

- 複数行のdocstrings
- one-line docstringsの内容＋空白行＋詳細の説明行
    - クラスの説明のdocstringsは前後に空白行を挿入
    - 関数やメソッドの説明には基本的にルールはない
        - ただし関数やメソッドの本体が複数のセクションに分かれていて空白行で区切られている場合は空白行を挿入
- スクリプトのdocstringsは使用法のメッセージとして使える
    - スクリプトの引数指定が間違っていたり、-hオプションで起動したときに表示される
    - 使用法のメッセージは初めて使う人にもわかりやすく、かつ熟練者がすべてのオプションと引数を完全に把握できるほど詳細であるべき
- モジュールのdocstrings
    - 通常モジュールが提供するクラス、例外、関数について列挙し、それぞれ１行ずつにまとめる
- 関数やメソッドのdocstrings
    - 動作についての簡潔なまとめ
    - 引数や戻り値、副作用、発行される例外、関数やメソッドを呼び出せる状況の制限を説明
- クラスのdocstrings
    - 動作についてまとめ
    - 公開のメソッドやインスタンス変数を挙げる
- あるクラスが別のクラスをサブクラス化している場合
    - サブクラスの動作のほとんどが上位クラスから継承したものの場合、そのことをサブクラスのdocstringsで触れて、差分について説明
    - サブクラスのメソッドが上位クラスのメソッドを置き換えていて、上位クラスメソッドを呼ばない場合、上書き（override）という言葉を使う
    - サブクラスのメソッドが上位クラスのメソッドを呼んでいる場合、拡張（extends）という言葉を使う
- 関数やメソッドの引数を１行内に大文字で記述するEmacs様式は使わない
    - Pythonは大文字小文字を区別するので、大文字で記述した引数の名前をキーワード引数として扱ってしまうことがある
- docstringsでは引数は正しい名前で記述する
    - 個々の引数を別々の行に列挙するのが良い

### Handling Docstring Indentation (komo_fr)
+ **Docstringのパース処理**について説明している
+ 補足すると、Docstringは、
    - 記述時： インデントや空行がある
    - 参照時： 1つの文字列
    - なので、記述時 -> 参照時の形式への変換方法について書いてある（のだと思う）
+ 具体的には、以下のような流れで処理している
    - タブをスペースに変換して、行のリストに分割する
    - 一番小さいインデントの個数を特定する
      * 多分、書き方によって2個スペースだったり4個スペースだったりするため
    - インデントを取り除く
    - 前後の空白行を取り除く
    - （行を全部joinして）ひとつの文字列にする
- よくわかってない 🤔
    + この処理はいつ走るの？

----

## (2) 有名なDocstring記法
- reStructuredTextを使う方法
    - PEP 287 -- reStructuredText Docstring Format
        - https://www.python.org/dev/peps/pep-0287/
- http://www.sphinx-doc.org/ja/master/usage/extensions/napoleon.html
  + Googleスタイル
  + NumPyスタイル
