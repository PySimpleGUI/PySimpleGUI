
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="人間のためのPythonGUI ">
  <h2 align="center">人間のためのPythonのGUI</h2>
</p>

tkinter、Qt、WxPython、およびRemi(ブラウザベース)のGUIフレームワークを、よりシンプルなインタフェースに変換します。ウィンドウ定義は初心者が理解するPythonコアデータ型 (リストと辞書) を使用して簡略化されます。コールバックベースのモデルからメッセージを渡すモデルにイベント処理を変更することでさらに単純化が行われます。 

コードはより多くのユーザーがパッケージを使用するのにオブジェクト指向アーキテクチャを持つ*必要はありません*。アーキテクチャは理解しやすいものですが、必ずしも*単純*な問題だけに制限されるわけではありません。

ただし、一部のプログラムはPySimpleGUIには適していません。 定義上、PySimpleGUI は基盤となるGUIフレームワークの機能のサブセットを実装します。どのプログラムがPySimpleGUIに適していてどのプログラムが適していないかを正確に定義することは難しいです。 プログラムの詳細によって異なります。エクセルを詳細に複製することはPySimpleGUIに適していないものの例です。

<hr>

# 統計 :chart_with_upwards_trend:

## PyPI インストール

<p align="center">
tkinter <img src="http://pepy.tech/badge/pysimplegui?color=blue&style=for-the-badge" width="100px"  align="center">
tkinter 2.7 <img src="https://pepy.tech/badge/pysimplegui27?color=blue&style=for-the-badge"  align="center"><br>
Qt <img src="https://pepy.tech/badge/pysimpleguiqt?color=blue&style=for-the-badge"  align="center">
WxPython<img src="https://pepy.tech/badge/pysimpleguiwx?color=blue&style=for-the-badge"  align="center">
Web (Remi) <img src="https://pepy.tech/badge/pysimpleguiweb?color=blue&style=for-the-badge"  align="center">
</p>


## GitHub

<p align="center">
<a href=""><img src="https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue&style=for-the-badge" alt="img" width="180px"></a>
<a href=""><img src="https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue&style=for-the-badge" alt="img"  width="200px"></a>
<a href=""><img src="https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?color=blue&style=for-the-badge" alt="img"  width="260px"></a>
<a href=""><img src="https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?color=blue&style=for-the-badge" alt="img"width="200px"></a>
<a href=""><img src="http://ForTheBadge.com/images/badges/makes-people-smile.svg" alt="img"width="190px"></a>
<a href=""><img src="https://img.shields.io/github/stars/PySimpleGUI/PySimpleGUI.svg?style=social&label=Star&maxAge=2592000" alt="img"width="140x"></a>
</p>


<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/?username=PySimpleGUI&bg_color=3e7bac&title_color=ffdd55&icon_color=ffdd55&text_color=ffdd55&show_icons=true&count_private=true">
</p>

## 最新の PyPI バージョン


<p align="center">
tkinter
<a href="pypi tkinter"><img src="https://img.shields.io/pypi/v/pysimplegui.svg?style=for-the-badge&color=red" alt="img" align="center" width="150px"></a>
Qt
<a href="https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>
Web
<a href="https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>
WxPython
<a href="https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>
</p>

<hr>

# PySimpleGUIとは何ですか:question:

PySimpleGUIはあらゆるレベルのPythonプログラマがGUIを作成できるようにするPythonパッケージです。ウィジェットを含む 「レイアウト」を使用して GUI ウィンドウを指定します (PySimpleGUI では「エレメント」と呼びます)。 レイアウトはサポートされている4つのフレームワークのいずれかを使用してウィンドウを作成して、ウィンドウの表示や操作するのに使用されます。 ササポートされるフレームワークは、tkinter、Qt、WxPython、WxPythonまたはRemiが含まれます。このようなパッケージには「ラッパー」という用語が使われることがあります。

PySimpleGUIは「ボイラープレートコード」の多くを実装しているため、基となるフレームワークで直接記述するよりも単純で短かいコードになります。
さらにインターフェイスは、望んだ結果を得るために必要なコードをできるだけ少なくするように単純化されています。使用するプログラムやフレームワークにもよりますが、PySimpleGUIでのプログラムはフレームワークのいずれかを直接使用して同じウィンドウを作成するよりも、コードの量は1/2から1/10程度になる場合があります。

目標は使用しているGUIフレームワーク上の特定のオブジェクトやコードをカプセル化/非表示にすることですが、必要に応じてフレームワークに依存しているウィジェットやウィンドウに直接アクセスできます。
設定や機能がまだ公開されておらず、PySimpleGUI APIを使用してアクセスできない場合でも、フレームワークから遮断されてません。PySimpleGUIのパッケージ自体を直接変更せずに機能を拡張できます。
## 「GUIのギャップ」を埋める

Python はプログラミング コミュニティに多くの人々を招いています。プログラムの数と扱う領域の範囲は気が遠くなります しかし多くの場合、プログラムとテクノロジーは一握りの人々以外の手の届かないところにあります。Python プログラムの大半は"コマンドライン"ベースです。プログラマー系の人はテキストインターフェイスを介してコンピュータとやり取りすることに慣れていて、この問題はありません。 プログラマーはコマンドラインインターフェイスに問題はありませんがほとんどの「普通の人」は問題を抱えています。 これにより、デジタル・ディバイド、「GUIのギャップ 」が生み出されます。
プログラムにGUIを追加することで、そのプログラムはより多くの人に知ってもらえるようになります。プログラムはより親しみやすくなります。GUIはコマンドラインインターフェースに慣れているプログラマーであっても、いくつかのプログラムの操作を簡単にすることができます。 そして最後にGUIを必要とする問題もあります。   


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/GUI%20Gap%202020.png" width="600px">
</p>


<hr>

# 私について :wave:
こんにちは！ 私はマイクです。 GitHubのPySimpleGUIで問題を解決してPySimpleGUIを継続的に前進させ続けています。私は昼と夜と週末もプロジェクトとPySimpleGUIユーザーに捧げてきました。私たちの成功は最終的に共有されます。 あなたが成功したときに私は成功しています。

Pythonでは相対的な新人ですが、70年代からソフトウェアを書いてきました。 私のキャリアの大半はシリコンバレーでの製品開発に費やされました。PySimpleGUIには自分が開発した企業製品と同じようなプロフェッショナリズムと献身をもたらします。今、あなたは私の顧客です。


## プロジェクトの目標 :goal_net:

PySimpleGUIプロジェクトの重要な目標は以下の2つです。

* 楽しむこと
* あなたの成功

真面目なプロジェクトのゴールとして**楽しむ**というのは変に聞こえるかもしれませんが、これは真面目な目標です。私はこれらのGUIプログラムを書くことはとても楽しいと思います。その理由の1つは、完全なソリューションの作成にかかる時間がいかに短いかということです。もし私達がプロセスを楽しんでいない場合は、誰かがあきらめています。

膨大な量のドキュメント、クックブック、すぐに使える100種類以上のデモプログラム、詳細なコールリファレンス、YouTubeのビデオ、オンラインのTrinketのデモなど、すべてが楽しい体験を生み出すために作用しています。

**あなたの成功**は共通の目標です。 PySimpleGUI は開発者向けに構築されました。あなたは私の仲間です。ユーザーとPySimpleGUIの共同作業の結果を見るのは予想外の報酬でした。ドキュメントやその他の資料を使用してアプリケーションの構築に役立ててください。トラブルに遭遇した場合は、[PySimpleGUI GitHub の問題](http://Issues.PySimpleGUI.org)でIssue を開いてヘルプを利用できます。 以下のサポートのセクションを見てください。

<hr>

# 教育リソース :books:

www.PySimpleGUI.org は覚えやすく、ドキュメントが配置されている場所です。上部にはいくつかの異なるドキュメントを表すタブがあります。ドキュメントは「Read The Docs」に記載されており、各ドキュメントの目次があり検索が簡単です。

数百ページの文書化されたドキュメントと数百のサンプルプログラムがあり、あなたが非常に速く効果を発揮するのに役立ちます。
単一の GUI パッケージを学ぶのに数日または数週間投資するよりも、PySimpleGUIを使用すると午後一回でプロジェクトを完成させられるかもしれません。


## 例 1 - ワンショットウィンドウ

このタイプのプログラムは、ウィンドウが1回表示されて収集された値が閉じられるため、「ワンショット」ウィンドウと呼ばれます。 ワードプロセッサのように長い間開いたままになっていません。
### 単純なPySimpleGUIプログラムの解剖学

PySimpleGUIプログラムには5つのセクションがあります



```python
import PySimpleGUI as sg                                 # パート 1 - インポート

# ウィンドウの内容を定義する
layout = [  [sg.Text("お名前は何ですか？")],     # パート 2 - レイアウト
            [sg.Input()],
            [sg.Button('はい')] ]
# ウィンドウを作成する
window = sg.Window('ウィンドウタイトル', layout)      # パート 3- ウィンドウ定義
                                                
# ウィンドウを表示し、対話する
event, values = window.read()                   # パート 4- イベントループまたは Window.read 呼び出し

# 収集された情報で何かをする
print('ハロー ', values[0], "! PySimpleGUIを試してくれてありがとう")

# 画面から削除して終了
window.close()                                  #パート 5 - ウィンドウを閉じる
```

コードは、以下のウィンドウを生成します

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourNameBlank1.jpg">
</p>


<hr>

## 例 2 - インタラクティブウィンドウ

この例では、ユーザーがウィンドウを閉じるか、または [終了] ボタンをクリックするまで、ウィンドウは画面上に残ります。 先ほど見たワンショットウィンドウとインタラクティブウィンドウの主な違いは、「イベントループ」の追加です。イベントループはウィンドウからイベントと入力を読み込みます。 アプリケーションの中心はイベントループになります。

```python
import PySimpleGUI as sg

# ウィンドウの内容を定義する
layout = [[sg.Text("お名前は何ですか？")],
          [sg.Input(key='-入力-')],
          [sg.Text(size=(55,1), key='-出力-')],
          [sg.Button('はい'), sg.Button('終了')]]

# ウィンドウを作成する
window = sg.Window('ウィンドウタイトル',layout)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了':
        break

    # Output a message to the window
    window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()
```

以下はは、例2が作成するウィンドウです。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourNameBlank.jpg">
</p>



入力フィールドに値を入力して [OK] ボタンをクリックした後の表示は次のようになります。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/HelloWorld1.jpg">
</p>


この例とワンショット ウィンドウの違いについて簡単に見てみましょう。
まず、レイアウトの違いに気づくでしょう。 特に2つの変更が重要です。 1つは`Input`エレメントと`Text`エレメントの1つに`key`パラメータを追加することです。 「key」はエレメントの名前のようなものです。 または、Pythonの言葉では、辞書キーのようなものです。 `Input`エレメントのキーは、コードの後半で辞書キーとして使用されます。


もう1つの違いは、この `Text`エレメントの追加です:
```python
          [sg.Text(size=(40,1), key='-OUTPUT-')],
```

すでにカバーしている「キー」という2つのパラメータがあります。 `Size`パラメーターはエレメントの文字数のサイズを定義します。 この場合、`Text`エレメントは幅40文字、高さ1文字であることを示しています。テキストの文字列が指定されていないので空白になることに注意してください。 作成されたウィンドウでは空白行が簡単に見れます。

また 、[終了]ボタンを追加しました。

イベントループには、おなじみの`window.read()`呼び出ししがあります。

読み込んだ後に続くのは、このif文です。
```python
    if event == sg.WINDOW_CLOSED or event == '終了':
        break
```

このコードは、ユーザーが 「X（閉じる）」 をクリックしてウィンドウを閉じたか、または「終了」ボタンをクリックしたかどうかを確認します。 これらのいずれかが発生した場合、コードはイベント ループから抜け出します。

ウィンドウが閉じられず、「終了」ボタンがクリックされていない場合は、動作が継続されます。 起こりうる唯一の事は、ユーザーが「OK」ボタンをクリックしたことです。 イベントループの最後のステートメントは次のとおりです。




```python
    window['-OUTPUT-'].update('ハロー  ' + values['-INPUT-'] + "! PySimpleGUI をお試しいただきありがとうございます")
```

このステートメントは、`-OUTPUT-`キー を持つ`Text`エレメントを文字列で更新します。`window['-OUTPUT-']`は`-OUTPUT-`キーを持つエレメントを検索します。 キーは、空白の`Text`エレメントに属します。 エレメントが検索から返されると、そのエレメントの`update`メソッドが呼び出されます。 ほとんどすべてのエレメントは`update`メソッドを持っています。 このメソッドはエレメントの値や構成を変更したりするのに使用します。

テキストを黄色にしたい場合は、`update`メソッドに`text_color`パラメータを追加して以下のように処理します。
```python
    window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます", text_color='yellow')
```

`text_color`パラメータを追加した後、これが新しい結果ウィンドウとなります。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/HelloWorldYellow.jpg">
</p>


各エレメントで使用できるパラメータは[call referenceドキュメント](http://calls.PySimpleGUI.org)とdocstrings と両方に記載されています。PySimpleGUIには、利用可能なすべてのオプションを理解するのに役立つ豊富なドキュメントが用意されています。 `Text`エレメントの`update'`メソッドを検索すると、以下のような定義が見つかります:

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/TextUpdate.jpg">
</p>


ご覧のように、いくつかのものは、`Text`エレメントに変更できます。 call referenceドキュメントはPySimpleGUIでのプログラミングを簡単にする貴重なリソースです。

<hr>

##レイアウトは面白いです LOL! :laughing:

ウィンドウのレイアウトは「リストのリスト」(LOL)です。 ウィンドウは「行」に分割されます。 ウィンドウの各行はレイアウトのリストになります。 すべてのリストを連結すると、レイアウトができあがります。...リストのリストです。

行の定義方法を簡単に確認できるように、各行に追加の 'Text' エレメントを追加したレイアウトは、以前と同じです:

```python
layout = [  [sg.Text('ライン 1'), sg.Text("お名前は何ですか")],
            [sg.Text('ライン 2'), sg.Input()],
            [sg.Text('ライン 3'), sg.Button('はい')] ]
```

このレイアウトの各行は、ウィンドウ内の行に表示されるエレメントのリストです。


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/rows.jpg">
</p>



リストを使用してGUIを定義する場合、他のフレームワークを使用してGUIプログラミングを行う方法にくらべていくつか大きな利点があります。 たとえば、Python のリスト内包表記を利用して、1 行のコードでボタンのグリッドを作成できます。



次の3行のコードです。

```python
import PySimpleGUI as sg

layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]

event, values = sg.Window('List Comprehensions', layout).read(close=True)
```

ボタンの4 x 4グリッドを持つウィンドウを生成します。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/4x4grid.jpg">
</p>

「楽しむ」がプロジェクトの目的の１つであることを思い出してください。 Pythonの強力な基本機能をGUIの問題に直接適用するのは楽しいです。GUIを作成するコードのページの代わりに、数行 (または多くの場合1行) のコードを作成します。

## コードの折りたたみ

ウィンドウのコードを1行のコードに凝縮できます。 レイアウトの定義、ウィンドウ作成、表示、およびデータ収集はすべて、次の1行のコードで書けます。
```python
event, values = sg.Window('Window Title', [[sg.Text("お名前は何ですか？")],[sg.Input()],[sg.Button('はい')]]).read(close=True)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourName.jpg">
</p>


同じウィンドウが表示され、PySimpleGUIプログラムのセクションを示す例と同じ値が返されます。 非常に少ない量で多くのことを行うことができるため、Pythonコードにすばやく簡単にGUIを追加できます。 データを表示してユーザーからの選択を得たい場合は、1ページのコードではなく1行のコードで行うことができます。

短縮エイリアスを使用してより少ない文字数でコードのスペースをさらに短くできます。  すべてのエレメントには、使用できる短い名前が１つ以上含まれています。 たとえば、`Text`エレメントは単に`T`として書けます。`Input`エレメントは `I`、`Button`は`B`と書けます。 したがって、ウィンドウの1行のコードは以下にになります:

```python
event, values = sg.Window('Window Title', [[sg.T("あなたの名前は何ですか?")],[sg.I()],[sg.B('はい')]]).read(close=True)
```


### コードの移植性

PySimpleGUIは現在、4つのPythonのGUIフレームワークで実行できます。 使用するフレームワークは、importステートメントを使用して指定します。 インポートを変更すると、基本のGUIフレームワークが変更されます。プログラムによっては、別のGUIフレームワークで実行するためにはimport ステートメント以外の変更は必要ありません。 上記の例では、インポートを`PySimpleGUI`から`PySimpleGUIQt`、`PySimpleGUIWx`、`PySimpleGUIWeb`、`PySimpleGUIWeb`に変更すると、フレームワークが変更されます。

| ステートメントをインポート | 結果ウィンドウ |
|--|--|
| PySimpleGUI |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg) |
| PySimpleGUIQt |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Qt.jpg) |
| PySimpleGUIWx |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-WxPython.jpg) |
| PySimpleGUIWeb |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Remi.jpg) |



GUIのコードをあるフレームワークから別のフレームワークに移植する (例えば、コードをtkinterからQtに移動する) には、通常はコードの書き換えが必要です。  PySimpleGUI は、フレームワーク間の簡単な移動を可能にするように設計されています。 場合によってはいくつかの変更が必要ですが、目的は最小限の変更で移植性の高いコードを作ることです。 

システム トレイ アイコンなどの一部の機能は、すべてのポートで使用できないです。 システムトレイアイコン機能はQtおよびWxPythonポートで使用できます。 シミュレートされたバージョンはtkinterで使用できます。 システムトレイアイコンは、PySimpleGUIWebポートではサポートされません。

##  ランタイム環境

|環境 |サポートされる |
|--|--|
|パイソン| Python  3.4+ |
|オペレーティング システム |ウィンドウズ, Linux, マック |
|ハードウェア |デスクトップ PC, ノートパソコン, ラズベリーパイ, PyDroid3 を実行しているアンドロイドデバイス |
|オンライン |repli.it、Trinket.com (どちらもブラウザ上でtkinterを実行する) |
|GUI フレームワーク |tkinter, pyside2, WxPython, Remi |


## 統合
200 以上の「デモプログラム」の中には、多くの人気のPythonパッケージをGUIに統合する方法の例が見つかります。

あなたのウィンドウにMatplotlibの描画を埋め込みたいですか?  問題ありません、 デモコードをコピーすると即座にあなたの夢のMatplotlibの描画をあなたのGUIに組み込めます。  

これらのパッケージやその他のパッケージは、デモプログラムやデモレポが用意されているので、GUIに入れる準備ができています。

|パッケージ |説明 |
|--|--|
 Matplotlib |グラフやプロットの多くの種類 |
 OpenCV |コンピュータビジョン (AIでよく使用) |
 VLC |ビデオ再生 |
 pymunk |物理エンジン|
 psutil |システム環境の統計 |
 prawn |Reddit  API |
json |PySimpleGUI は、「ユーザー設定」を格納する特別なAPIをラップします。 |
 weather |お天気アプリを作るためにいくつかの天気APIと統合 |
 mido |MIDI 再生 |
 beautiful soup |ウェブスクレイピング (GitHub issueウォッチャーでの例) |

<hr>

# インストール :floppy_disk:


PySimpleGUIをインストールする一般的に2つの方法があります。

1. PyPIからpipでインストールする
2. PySimpleGUI.pyファイルをダウンロードしてアプリケーションのフォルダに配置します


### Pipインストールとアップグレード

現在提案されている`pip`コマンドを呼び出す方法は、Pythonを使ってモジュールとして実行することです。 以前は、`pip`または`pip3`コマンドはコマンドライン/シェル上で
直接実行されました。 提案された方法は以下となります。

Windows の初期インストール

`python -m pip install PySimpleGUI`

Linux および MacOS の初期インストール

`python3 -m pip install PySimpleGUI`

`pip`を使用してアップグレードするには、単に2つのパラメータ`--upgrade --no-cache-dir`を指定するだけです。

Windows のアップグレード

`python -m pip install --upgrade --no-cache-dir PySimpleGUI`

Linux および MacOS のアップグレード

`python3 -m pip install --upgrade --no-cache-dir PySimpleGUI`


### 単一ファイルのインストール

PySimpleGUIはRaspberry Pi のようなインターネットに接続されていないシステムにも簡単にインストールできるように、単一の .py ファイルとして作成されました。 PySimpleGUI.pyファイルをインポートするアプリケーションと同じフォルダに置くだけです。Python はインポート時にローカルのコピーを使用します。

.pyファイルを使用してインストールする場合は、PyPIから入手するか、最新の未リリースバージョンを実行したい場合はGitHubからダウンロードします。

PyPIからインストールするには、wheelまたは .gz ファイルをダウンロードして解凍します。 .whlファイルを.zipにリネームすると、通常のzipファイルと同じように開くことができます。 フォルダの中にPySimpleGUI.pyファイルがあります。 このファイルをアプリケーションのフォルダーにコピーすると完了です。

tkinter バージョンの PySimpleGUI の PyPI リンクです
https://pypi.org/project/PySimpleGUI/#files

GitHubリポジトリの最新バージョンは、こちらで確認できます
https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/PySimpleGUI.py


「そうだけど、巨大なソースファイルを一つだけ持つのはなんてひどい考えです」と今、考えている人もいるでしょう。 これは*時には*ひどい考えかもしれません。 今回は、メリットはデメリットを大幅に上回りました。 コンピュータサイエンスの概念の多くはトレードオフまたは主観的なものです。 一部の人が望むのと同じくらい、すべてが白黒ではありません。 多くの場合、質問に対する答えは「次第」です。



## ギャラリー :art:

ユーザーが投稿したGUIとGitHubにあるGUIのより正式なギャラリーの作成は進行中ですが、readmeを作成時点ではまだ完成していません。現在まとまってスクリーンショットを見れる場所は2か所あります。願わくば人々が作っている素晴らしい作品を正当化するためのWikiやその他の仕組みがすぐにリリースされることを願っています。

### ユーザーが提出したギャラリー

1つ目は、GitHubにある[ユーザーがスクリーンショットを提出したissue](https://github.com/PySimpleGUI/PySimpleGUI/issues/10)です。 これは、人々が作ったものを披露するための非公式な方法です。 理想的ではありませんがスタートでした。

### 大量にスクラップされたGitHubの画像

2つ目は、PySimpleGUIを使用していると伝えられているGitHubの1,000のプロジェクトか集めた[3,000以上の画像の大規模なギャラリー ](https://www.dropbox.com/sh/g67ms0darox0i2p/AAAMrkIM6C64nwHLDkboCWnaa?dl=0)です。 手作業でフィルタリングされており初期のドキュメントで使用されていた古いスクリーンショットがたくさんあります。 しかし、そこにあなたの想像力を引き起こす何かが見つかもしれません。

<hr>

# PySimpleGUI の用途です :hammer:

次のセクションでは、PySimpleGUIの用途の一部を紹介します。 GitHub だけでも1,000 以上のプロジェクトでPySimpleGUI を使用しています。本当にこれだけの多くの人々の可能性が広がったことはは本当に驚くべきことです。 多くのユーザーは以前にPythonでGUIを作成しようとして失敗ししたと話していましたが、彼らがPySimpleGUIを試してみたときに最終的に自分の夢を達成したと話をしました。

## 最初のGUI

もちろん、PySimpleGUIの最も優れた使い方の一つはPythonプロジェクト用のGUIを作ることです。 ファイル名をリクエストするだけの小さなプロジェクトから開始できます。 このためには、`popup`と呼ばれる「ハイレベル関数」の1つを1回呼び出すだけで済みます。 ポップアップにはあらゆる種類があり、一部は情報を収集します

`popup`自体で情報を表示するためのウィンドウを作成します。printと同じように複数のパラメータを渡せます。情報を取得したい場合は、`popup_get_filename`のように`popup_get_で`始まる関数を呼び出すします。

コマンドラインでファイル名を指定する代わりに、ファイル名を取得するための1行を追加することで、プログラムは「普通の人」が快適に使用できるプログラムに変身します。


```python
import PySimpleGUI as sg

filename = sg.popup_get_file('処理したいファイルを入力してください')
sg.popup('入力した', filename)
```


このコードは、2つのポップアップウィンドウを表示します。 1つはファイル名を取得するためで、入力ボックスの閲覧やペーストができます。  

<p align="center">
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/popupgetfilename.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/popupgetfilename.jpg"  alt="img" width="400px"></a>
</p>

もう一方のウィンドウは収集された内容を出力します。

<p align="center">
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/popupyouentered.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/popupyouentered.jpg"  alt="img" width="175px"></a>

</p>


<br>

## Rainmeter風スタイルウィンドウ

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/RainmeterStyleWidgets.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/RainmeterStyleWidgets.jpg"  alt="img" align="right" width="500px"></a>
GUIフレームワークのデフォルト設定では見栄えの良いウィンドウは作成できません。しかし細部に注意することでウィンドウを魅力的に見せるためにいくつかのことをおこなえます。 PySimpleGUIは、色やタイトルバーの削除などの機能をより簡単に操作できます。 その結果、典型的なtkinterのようには見えないウィンドウができます。

ここでは、典型的なtkinterのように見えないウィンドウをWindowsで作成する方法の例を紹介します。 この例ではウィンドウのタイトル バーが削除されています。その結果としてデスクトップウィジェットプログラムのRainmeterように見えるウィンドウができあがります。

<br><br>
ウィンドウの透明度も簡単に設定できます。 同じRainmeterスタイルのデスクトップウィジェットの他の例を紹介します。 半透明なので、薄暗く表示される場合もあります。
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/semi-transparent.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/semi-transparent.jpg"  alt="img" align="right" width="500px"></a>



タイトルバーの削除とウィンドウの半透明化の両方の効果はウィンドウを作成する際に2つのパラメータを設定することで実現しています。 これはPySimpleGUIがいかに機能に簡単にアクセスできるかを示す例です。 また、PySimpleGUI のコードはGUIフレームワーク間で移植可能なので、Qtのような他のポートでも同じパラメータで動作します。


例１のウィンドウ作成の呼び出しを以下のコードに変更すると同様の半透明のウィンドウが作成されます。
```python
window = sg.Window('My window', layout, no_titlebar=True, alpha_channel=0.5)
```

## ゲーム

ゲーム開発用の SDK としては特に記述されていませんが、PySimpleGUIはゲームの開発を非常に簡単にします。

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Chess.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Chess.png"  alt="img" align="right" width="500px"></a>
このチェスプログラムはチェスをするだけでなく、チェスAI「Stockfish」を統合します。
<br><br><br><br><br><br><br><br><br>
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Minesweeper.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Minesweeper.gif"  alt="img" align="right" width="500px"></a>
マインスイーパのいくつかのバリエーションがユーザーによってリリースされました。

<br><br><br><br>
<br><br><br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/minesweeper_israel_dryer.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/minesweeper_israel_dryer.png"  alt="img" align="right" width="500px"></a>
<br><br><br><br><br><br><br><br><br><br>


<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Solitaire.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Solitaire.gif"  alt="img" align="right" width="500px"></a>
<br><br>

PySimpleGUIの`Graph`エレメントを使用すると画像の操作が簡単なので、カードゲームはPySimpleGUIを使用すると簡単です。

ゲーム開発用のSDKとして書かれたわけではありませんが、PySimpleGUIはゲームの開発を非常に簡単にします。<br><br>
<br><br>
<br><br><br>


## メディアのキャプチャと再生

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/OpenCV.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/OpenCV.jpg"  alt="img" align="right" width="400px"></a>


WEBカメラからビデオをキャプチャしてGUIで表示するのには、PySimpleGUIのコードでは4行でできます。 さらに印象的なのはこらの4行のコードが tkinter、Qt、および Web ポートで動作します。  tkinterを使用して画像を表示するのと同じコードを使用して、ブラウザでWebカメラをリアルタイムが表示できます。

また、VLCプレーヤーを使って、オーディオやビデオなどのメディア再生も可能です。デモアプリケーションが提供されているので実際の作業例が用意されています。このreadmeに記載されている内容は全て、あなた自身の創作の出発点として利用できます。
<br><br><br><br><br>
<br><br><br><br><br>
<br><br>
## 人工知能

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"  alt="img" align="right" width="500px"></a>



AIとPythonは長い間、この2つが組み合わされたときのスーパーパワーとして認識されてきました。しかし、多くの場合、ユーザーがGUIを使用してこれらのAIアルゴリズムを身近に操作する方法が欠けています。

これらのYOLOのデモは、GUIがAIアルゴリズムとの対話においていかに大きな違いをもたらすかの素晴らしい例です。 これらのウィンドウの下部にある2つのスライダーに注目してください。 この2つのスライダーは、YOLOアルゴリズムが使用するパラメータを変更します。 

コマンドラインのみを使用してYOLOデモをチューニングする場合は、アプリケーションを起動するときに、パラメーターを設定し、その実行方法を確認し、アプリケーションを停止し、パラメーターを変更し、最後に新しいパラメーターでアプリケーションを再起動する必要があります。
<br><br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"  alt="img" align="right" width="500px"></a>

これらのステップと、GUIを使用して実行できる操作と比較してみます。 GUIを使用すると、これらのパラメータをリアルタイムで変更できます。 アルゴリズムにどのような影響を与えているかについて、すぐにフィードバックを得られます。



<br><br><br><br><br>
<br><br>
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"  alt="img" align="right" width="500px"></a>


公開されているAIプログラムには、コマンドラインで動かすプログラムが非常に多く存在します。 これ自体は大きなハードルではありませんが、コマンドラインでカラーリングしたいファイル名を入力/貼り付け、プログラムを実行して、出力ファイルの結果をファイルビューアで開くには十分「面倒くさい」です。


GUI には、**ユーザーエクスペリエンスを変更する**を「GUIギャップ」に変化させる力があります。 このカラーライズの例では、ユーザーは画像が格納されてたフォルダを指定して、画像をクリックするだけでカラーリングと結果表示の両方を行えます。  
カラーライズを行うプログラム/アルゴリズムは自由に利用可能で、使用可能でした。 不足していたのはGUIがもたらす使いやすさです。


<hr>

## グラフ化

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/CPU%20Cores%20Dashboard%202.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/CPU%20Cores%20Dashboard%202.gif"  alt="img" align="right" width="500px"></a>

GUIでのデータの表示と操作はPySimpleGUIを使用すると簡単です。いくつかのオプションがあります。
組み込みの描画/グラフ作成機能を使用してカスタムグラフを作成できます。 このCPU使用率モニタは`Graph`エレメントを使用します。
<br><br>
<br><br>
<br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib.jpg"  alt="img" align="right" width="500px"></a>


MatplotlibはPythonユーザーに人気があります。 PySimpleGUIは、MatplotlibのグラフをGUIウィンドウに直接埋め込めます。 Matplotlibのインタラクティブ機能を保持したい場合はインタラクティブコントロールをウィンドウに埋め込むこともできます。

<br><br>
<br><br>
<br><br>
<br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib2.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib2.jpg"  alt="img" align="right" width="500px"></a>
PySimpleGUIのカラーテーマを使用すると、ほとんどの人がMatplotlibで作成するデフォルトのグラフよりも一段上のグラフを作成できます。

<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>

<hr>

## フロントエンド


<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/JumpCutter.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/JumpCutter.png"  alt="img" align="right" width="500px"></a>

前述の「GUI ギャップ」は、PySimpleGUIを使用して簡単に解決できます。 GUIを追加するプログラムにソースコードを用意する必要もありません。 「フロントエンド」GUI は、コマンドラインアプリケーションに渡す情報を収集するGUIです。
フロントエンドGUI は、プログラマにとってユーザーがコマンドライン・インターフェースを使い心地よく感じなかったために、以前は使いたがらなかったアプリケーションを配布するための素晴らしい方法です。これらのGUIは、ソースコードにアクセスできないコマンドラインプログラムのための唯一の選択肢です。
この例は、「Jump Cutter」というプログラムのフロントエンドです。 パラメーターはGUIをとおして収集されて、それらのパラメータを使用してコマンドラインが構築されて、コマンドラインプログラムの出力がGUIインターフェイスにルーティングされてコマンドが実行されます。この例では、実行されたコマンドが黄色で表示されています。
<br><br>
<hr>

## Raspberry Pi

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"  alt="img" align="right" width="500px"></a>


PySimpleGUIはPython 3.4に対応しているため、Raspberry Piのプロジェクト用のGUIを作成できます。 タッチスクリーンと組み合わせると特にうまく機能します。 モニターが接続されていない場合は、PySimpleGUIWebを使用してPiを制御することもできます。

<br><br>
<br><br>
<br><br>
<br><br><br>
<hr>


## 高度な機能への簡単なアクセス
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"  alt="img" align="right" width="500px"></a>


基礎となる GUIフレームワークの機能の多くに非常に簡単にアクセスできるため、GUIフレームワークを直接使っているようには見えないアプリケーションを作るための機能を組み合わせられます。

たとえば、tkinterやその他のGUIパッケージを使用してタイトルバーの色や外見を変更することはできませんが、PySimpleGUI を使用すると、カスタムタイトルバーを持っているかのように表示されるウィンドウを簡単に作成できます。
<br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Desktop%20Bouncing%20Balls.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Desktop%20Bouncing%20Balls.gif"  alt="img" align="right" width="500px"></a>

信じられないことに、このウィンドウはスクリーンセーバーのように見えるものを実現するためにtkinterを使用しています。

ウィンドウではtkinter はアプリケーションから背景を完全に取り除けます。 繰り返しますがPySimpleGUIはこれらの機能へのアクセスを簡単にします。 透明なウィンドウを作成するには、`Window`を作成する呼び出しにパラメータを1つ追加する必要があります。 1つのパラメータ変更だけで、次の効果を持つ単純なアプリケーションを作成できます。

デスクトップ上のすべてのものをフルスクリーンウィンドウをクリックして操作できます。
<hr>

# テーマ

デフォルトのグレーのGUIにうんざりしましたか?  PySimpleGUI は`theme`関数の呼び出しを行うこだけで、ウィンドウの見た目を素敵にします。 150種類以上のカラーテーマを選択できます:
<p align="center">
<a href=""><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ThemePreview.jpg"  alt="img" width="900px"></a>
</p>


ほとんどのGUIフレームワークでは、作成するすべてのウィジェットの色を指定する必要があります。  PySimpleGUIは、この雑用を代わりに行い自動的に選択したテーマに合わせてエレメントを色付けします。

テーマを使用するには、ウィンドウを作成する前にテーマ名を指定して`theme`関数を呼び出します。読みやすくするためにスペースを追加できます。 テーマを「dark grey 9」に設定するには
```python
import PySimpleGUI as sg

sg.theme('dark grey 9')
```

この1行のコードでウィンドウの外観を完全に変更します:
<p align="center">
<a href=""><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/DarkGreyJapanese.jpg"  alt="img" width="400px"></a>
</p>


テーマは、背景、テキスト、入力背景、入力テキスト、およびボタンの色を変更しました。 このような配色を変更する他のGUIパッケージでは、各ウィジェットの色を個別に指定する必要があり、コードを何度も変更する必要があります。

<hr>

# サポート:muscle:

最初のステップは[ドキュメンテーション](http://www.PySimpleGUI.org)と[デモプログラム](http://Demos.PySimpleGUI.org)でなければなりません。 です。もしまだ質問があったり、ヘルプが必要な場合は...問題ありません...ヘルプは無料で提供されています。PySimpleGUIのGitHubリポジトリで[Issueを提出](http://Issues.PySimpleGUI.org)するだけで、助けが得られます。

ほとんどのソフトウェア会社は、バグレポートに付随するフォームを持っています。 それは悪い取引ではありません.フォームに必要事項記入すれば、無料でソフトウェアのサポートを受けられます。この情報は効率的に回答を得るのに役立ちます。

PySimpleGUIのバージョン番号や基になるGUIフレームワークなどの情報を要求するだけでなく、問題の解決に役立つかもしれない項目のチェックリストも提供されます。

***フォームに記入してください 。*** 　あなたには無意味に感じるかもしれません。ほんの一瞬ですが苦痛に感じるかもしれません。記入はあなたがより早く解決策を得るのに役立ちます。もしあなたがスピーディーな回答と解決を得るために役立つ必要な情報でなければ、記入は必要ではありません。「私はあなたを助けるために私を助ける」。


# サポート	<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"  alt="img"  width="90px"></a>

プロジェクトの財政的支援は非常に高く評価されています。 正直に言うと、経済的な援助が必要です。 ライトをつけ続けるだけで高価です。 ドメイン名登録、トリンケット、コンサルティングヘルプなどのサブスクリプションの長いリストは、すぐにかなりの繰り返しコストに加算されます。

PySimpleGUI は作成するのに安価ではありませんでした。愛の労働は、非常に面倒でした。ソフトウェアとドキュメントを現在のレベルに到達するには、週7日の作業に2年以上必要です。

PySimpleGUIにはオープンソースライセンスがあり、そのまま残ることができれば素晴らしいことです。 お客様またはお客様の会社 (特に企業でPySimpleGUIを使用している場合) が、PySimpleGUIを使用して経済的に利益を得ている場合は、プロジェクトの寿命を延長する機能を持ちます。

###　Buy Me a Coffee

「Buy Me a Coffee」は、開発者を公的にサポートするための素晴らしい方法です。 素早く、簡単に、貢献は記録されるので、あなたがPySimpleGUI のサポーターであることを他の人に見せられます。寄付を非公開にもできます。

<a href="https://www.buymeacoffee.com/PySimpleGUI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>



### GitHubスポンサー

<a href="https://github.com/sponsors/PySimpleGUI" target="_blank"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&link=%3Curl%3E&color=f88379"></a>

[GitHub定期的なスポンサーシップ](https://github.com/sponsorsー/PySimpleGUI)は、継続的にさまざまなレベルのサポートでプロジェクトをスポンサーする方法です。これにより、多くのオープンソース開発者が企業レベルのスポンサーシップを受けられます。

プロジェクトに金銭的に貢献していただけると、非常にありがたいです。オープンソースの開発者であることは、経済的に困難です。YouTube動画のクリエイターは、動画作成で生計を立てています。オープンソース開発者にとってはまだそれほど簡単ではありません。
# 貢献:construction_worker:

PySimpleGUI は現在、オープンソースライセンスでライセンスされていますが、プロジェクト自体は製品のように構成されています。プルリクエストは受け付けられません。

貢献する最も良い方法の1つは、アプリケーションの作成と公開です。 ユーザーは、他のユーザーが構築するものを見てインスピレーションを得ています。 GitHubリポジトリを作成し、コードを投稿して、リポジトリのReadmeファイルにスクリーンショットを含めてください。  

不足している機能があったり、機能強化を提案したい場合は、[issueを開いてください](https://github.com/PySimpleGUI/PySimpleGUI/issues/new?assignees=&labels=&template=issue-form---must-fill-in-this-form-with-every-new-issue-submitted.md&title=%5B+Enhancement%2FBug%2FQuestion%5D+My+problem+is.)) 。


# 特別な感謝 :pray:


PySimpleGUIのこのバージョンのreadmeは[@M4cs](https://github.com/M4cs)の助けなしでは実現しませんでした。彼は素晴らしい開発者で、プロジェクトの立ち上げからずっとPySimpleGUIのサポーターです。 [@Israel Dryer](https://github.com/israel-dryer)もまた長期的なサポーターであり、パッケージの機能の限界を押し広げたいくつかのPySimpleGUIプログラムを書いています。 ボードの画像を使用したユニークなマインスイーパーはIsraelにが作成しました。 [@jason990420](https://github.com/jason990420)は上の写真のような、PySimpleGUI を使った最初のカードゲームと、PySimpleGUI で作られた最初のマインスイーパゲームを公開して、多くの人を驚かせました。
日本語版の readme は[@okajun35](https://github.com/okajun35) さんの協力で大幅に改善されました。

PySimpleGUI を使用している 1,200 以上の GitHub リポジトリにも「ありがとう」の言葉があります。このプロジェクトのエンジンを動かしているのは、あなたのインスピレーションのおかげです。

一晩中Twitter に投稿してくれる海外のユーザーは、PySimpleGUIの一日の作業を始めるきっかけとなります。彼らはポジティブなエネルギーの源であり、開発エンジンを始動させ、毎日稼働させる準備をしてくれています。感謝の意を込めて、このreadmeファイルを(日本語)[https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md]に翻訳しました。

皆さんはオープンソース開発者が望む最高のユーザーコミュニティです。



&copy; Copyright 2020 PySimpleGUI.org 
