
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="人間のためのPythonGUI ">
  <h2 align="center">人間のためのPythonGUI</h2>
</p>

tkinter、Qt、WxPython、およびRemi（ブラウザベース）のGUIフレームワークを、よりシンプルなインタフェースに変換します。ウィンドウ定義は初心者が理解するPythonコアデータ型（リストと辞書）を使用して簡略化されます。コールバックベースのモデルからメッセージを渡すモデルにイベント処理を変更することでさらに単純化が行われます。 

コードはより多くのユーザーがパッケージを使用するのにオブジェクト指向アーキテクチャを持つ*必要はありません*。アーキテクチャは理解しやすいものですが、必ずしも*単純*な問題だけに制限されるわけではありません。

ただし一部のプログラムはPySimpleGUIには適していません。 定義上、PySimpleGUIは基盤となるGUIフレームワークの機能のサブセットを実装します。どのプログラムがPySimpleGUIに適していてどのプログラムが適していないかを正確に定義することは難しいです。 プログラムの詳細によって異なります。エクセルを詳細に複製することはPySimpleGUIに適していないものの例です。

[Japanese version of this readme](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md).

<a href="https://www.buymeacoffee.com/PySimpleGUI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

<!-- I could use a coffee!  It fuels consultants, editors, domain registration and so many other things required for PySimpleGUI to be a thriving project. -->
コーヒーが飲みたいです!  コンサルタント、エディター、ドメイン登録など、PySimpleGUIプロジェクトが繁栄するために必要な多くのものをまかなえます。

<hr>

# 統計 :chart_with_upwards_trend:


## PyPIの統計とバージョン

| TK | TK 2.7 | Qt| WxPython | Web (Remi) |
| -- | -- | -- | -- | -- |
| ![tkinter](https://img.shields.io/pypi/dm/pysimplegui?label=tkinter) | ![tkinter 2.7 downloads](https://img.shields.io/pypi/dm/pysimplegui27?label=tkinter%202.7) | ![qt](https://img.shields.io/pypi/dm/pysimpleguiqt?label=qt) | ![wx](https://img.shields.io/pypi/dm/pysimpleguiwx?label=wx) | ![web](https://img.shields.io/pypi/dm/pysimpleguiweb?label=web) |
| [![tkinter](http://pepy.tech/badge/pysimplegui)](http://pepy.tech/project/pysimplegui) | [![tkinter27](https://pepy.tech/badge/pysimplegui27)](https://pepy.tech/project/pysimplegui27) | [![Downloads](https://pepy.tech/badge/pysimpleguiqt)](https://pepy.tech/project/pysimpleguiqt) | [![Downloads](https://pepy.tech/badge/pysimpleguiwx)](https://pepy.tech/project/pysimpleguiWx) | [![Downloads](https://pepy.tech/badge/pysimpleguiweb)](https://pepy.tech/project/pysimpleguiWeb) |
| ![tkinter](https://img.shields.io/pypi/v/pysimplegui.svg?label=tkinter%20PyPI%20Ver&color=red) | ![tkinter 2.7](https://img.shields.io/pypi/v/pysimplegui27.svg?label=tkinter%202.7%20PyPI%20Ver&color=red) | ![qt](https://img.shields.io/pypi/v/pysimpleguiqt.svg?label=qt%20PyPI%20Ver&color=red) | ![wx](https://img.shields.io/pypi/v/pysimpleguiwx.svg?label=wx%20PyPI%20Ver&color=red) | ![web](https://img.shields.io/pypi/v/pysimpleguiweb.svg?label=web%20PyPI%20Ver&color=red) | 
|  [![PyPI pyversions](https://img.shields.io/pypi/pyversions/PySimpleGUI)](https://pypi.python.org/pypi/PySimpleGUI/)  |  [![PyPI pyversions](https://img.shields.io/pypi/pyversions/PySimpleGUI27)](https://pypi.python.org/pypi/PySimpleGUI27/)  | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/PySimpleGUIQt)](https://pypi.python.org/pypi/PySimpleGUIQt/) | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/PySimpleGUIWx)](https://pypi.python.org/pypi/PySimpleGUIWx/) | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/PySimpleGUIWeb)](https://pypi.python.org/pypi/PySimpleGUIWeb/) |


--------------------------

## GitHubの統計




|  Issues | Commit Activity | Stars | Docs | 
| -- | -- | -- | -- |
| ![GitHub issues](https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue)  | ![commit activity](https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?color=blue) | ![stars](https://img.shields.io/github/stars/PySimpleGUI/PySimpleGUI.svg?label=stars&maxAge=2592000) | ![Documentation Status](https://readthedocs.org/projects/pysimplegui/badge/?version=latest) |
|  ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue) | ![last commit](https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?color=blue)  |  |





<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/?username=PySimpleGUI&bg_color=3e7bac&title_color=ffdd55&icon_color=ffdd55&text_color=ffdd55&show_icons=true&count_private=true">
</p>



<hr>

# PySimpleGUIとは何ですか:question:

PySimpleGUIはあらゆるレベルのPythonプログラマがGUIを作成できるようにするPythonパッケージです。ウィジェットを含む「レイアウト」を使用して、GUIウィンドウを指定します（PySimpleGUIでは「エレメント」と呼びます）。 レイアウトはサポートされている4つのフレームワークのいずれかを使用してウィンドウを作成して、ウィンドウ表示や操作するのに使用されます。 サポートされるフレームワークは、tkinter、Qt、WxPython、WxPythonまたはRemiが含まれます。このようなパッケージを「ラッパー」と呼ぶ場合があります。

PySimpleGUIは「ボイラープレートコード」の多くを実装しているため、基となるフレームワークで直接記述するよりも単純で短かいコードになります。
さらにインターフェイスは、望んだ結果を得るために、必要なコードをできるだけ少なくするように単純化されています。使用するプログラムやフレームワークにもよりますがPySimpleGUIでのプログラムはフレームワークのいずれかを直接使用して同じウィンドウを作成するよりも、コードの量は1/2から1/10程度になる場合があります。

目標は使用しているGUIフレームワーク上の特定のオブジェクトやコードをカプセル化/非表示にすることですが、必要に応じてフレームワークに依存しているウィジェットやウィンドウに直接アクセスできます。
設定や機能がまだ公開されておらずPySimpleGUI APIを使用してアクセスできない場合でも、フレームワークから遮断されてません。PySimpleGUIのパッケージ自体を直接変更せずに機能を拡張できます。


## 「GUIのギャップ」を埋める

Pythonはプログラミング コミュニティに多くの人々を招いています。プログラムの数と扱う領域の範囲は気が遠くなります しかし多くの場合、プログラムとテクノロジーは一握りの人々以外の手の届かないところにあります。Pythonプログラムの大半は"コマンドライン"ベースです。プログラマー系の人はテキストインターフェイスを介してコンピューターとやり取りすることに慣れているため、この問題はありません。 プログラマーはコマンドラインインターフェイスに問題はありませんがほとんどの「普通の人」は問題を抱えています。 これにより、デジタル・ディバイド、「GUIのギャップ」が生み出されます。
プログラムにGUIを追加することで、そのプログラムはより多くの人に知ってもらえるようになります。プログラムはより親しみやすくなります。GUIはコマンドラインインターフェイースに慣れているプログラマーであっても、いくつかのプログラムの操作を簡単にできます。 そして最後にGUIを必要とする問題もあります。   


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/GUI%20Gap%202020.png" width="600px">
</p>


<hr>

# 私について :wave:
こんにちは！ 私はマイクです。 GitHubのPySimpleGUIで問題を解決してPySimpleGUIを継続的に前進させ続けています。私は昼と夜、そして週末もプロジェクトとPySimpleGUIユーザーに捧げてきました。私たちの成功は最終的に共有されます。 あなたが成功したときに私は成功しています。

Pythonでは相対的な新人ですが、70年代からソフトウェアを書いてきました。 私のキャリアの大半はシリコンバレーでの製品開発に費やされました。自分が開発してきた企業製品と同じような、プロフェッショナリズムと献身をPySimpleGUIにもたらします。今、あなたは私の顧客です。


## プロジェクトの目標 :goal_net:

PySimpleGUIプロジェクトの重要な目標は以下の2つです。

* 楽しむこと
* あなたの成功

真面目なプロジェクトのゴールとして**楽しむ**というのは変に聞こえるかもしれませんが、これは真面目な目標です。私はこれらのGUIプログラムを書くことはとても楽しいと思います。その理由の1つは、完全なソリューションの作成にかかる時間がいかに短いかということです。もし私達がプロセスを楽しんでいない場合は、誰かがあきらめています。

膨大な量のドキュメント、クックブック、すぐに使える100種類以上のデモプログラム、詳細なコールリファレンス、YouTubeのビデオ、オンラインのTrinketのデモなど、すべてが楽しい体験を生み出すために作用しています。

**あなたの成功**は共通の目標です。 PySimpleGUIは開発者向けに構築されました。あなたは私の仲間です。ユーザーとPySimpleGUIの共同作業の結果を見るのは予想外の報酬でした。ドキュメントやその他の資料を使用してアプリケーションの構築に役立ててください。トラブルに遭遇した場合は、[PySimpleGUI GitHub の問題](http://Issues.PySimpleGUI.org)でIssueを開いてヘルプを利用できます。 以下のサポートのセクションを見てください。

<hr>

# 教育リソース :books:

www.PySimpleGUI.orgは覚えやすく、ドキュメントが配置されている場所です。上部にはいくつかの異なるドキュメントを表すタブがあります。ドキュメントは「Read The Docs」に記載されており、各ドキュメントの目次があり、検索も簡単です。

数百ページの文書化されたドキュメントと数百のサンプルプログラムがあり、あなたが非常に速く効果を発揮するのに役立ちます。
単一のGUIパッケージを学ぶのに数日または数週間投資するよりも、PySimpleGUIを使用すると午後の時間だけでプロジェクトを完成させられるかもしれません。


## 例1 - ワンショットウィンドウ

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
print('ハロー ', values[0], "PySimpleGUIを試してくれてありがとう!")

# 画面から削除して終了
window.close()                                  #パート 5 - ウィンドウを閉じる
```

コードは、以下のウィンドウを生成します

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourNameBlank1.jpg">
</p>


<hr>

## 例2 - インタラクティブウィンドウ

この例では、ユーザーがウィンドウを閉じるか、または [終了] ボタンをクリックするまで、ウィンドウは画面上に残ります。先ほど見たワンショットウィンドウとインタラクティブウィンドウの主な違いは、「イベントループ」の追加です。イベントループはウィンドウからイベントと入力を読み込みます。アプリケーションの中心はイベントループになります。

```python
import PySimpleGUI as sg

# ウィンドウの内容を定義する
layout = [[sg.Text("お名前は何ですか？")],
          [sg.Input(key='-入力-')],
          [sg.Text(size=(55,1), key='-出力-')],
          [sg.Button('はい'), sg.Button('終了')]]

# ウィンドウを作成する
window = sg.Window('ウィンドウタイトル',レイアウト)

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

以下は、例2が作成するウィンドウです。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourNameBlank.jpg">
</p>



入力フィールドに値を入力して [OK] ボタンをクリックした後の表示は次のようになります。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/HelloWorld1.jpg">
</p>


この例とワンショット ウィンドウの違いについて簡単に見てみましょう。
まず、レイアウトの違いに気づくでしょう。とくに2つの変更が重要です。1つは`Input`エレメントと`Text`エレメントの1つに`key`パラメーターを追加することです。「key」はエレメントの名前のようなものです。 またはPythonの辞書キーのようなものです。 `Input`エレメントのキーは、コードの後半で辞書キーとして使用されます。


もう1つの違いは、この `Text`エレメントの追加です:
```python
          [sg.Text(size=(40,1), key='-OUTPUT-')],
```

すでにカバーしている「キー」という2つのパラメーターがあります。 `Size`パラメーターはエレメントの文字数のサイズを定義します。 この場合、`Text`エレメントは幅40文字、高さ1文字であることを示しています。テキストの文字列が指定されていないので空白で表示されていことに注意してください。 作成されたウィンドウでは空白行になっているのがわかります。

また 、[終了]ボタンを追加しました。

イベントループには、おなじみの`window.read()`呼び出しがあります。

読み込んだ後に続くのは、このif文です。
```python
    if event == sg.WINDOW_CLOSED or event == '終了':
        break
```

このコードは、ユーザーが「X（閉じる）」をクリックしてウィンドウを閉じたか、または「終了」ボタンをクリックしたかどうかを確認します。 これらのいずれかが発生した場合、コードはイベント ループから抜け出します。

ウィンドウが閉じられず、「終了」ボタンがクリックされていない場合は動作が継続されます。 起こりうる唯一の事は、ユーザーが「OK」ボタンをクリックしたことです。 イベントループの最後のステートメントは次のとおりです。




```python
    window['-OUTPUT-'].update('ハロー  ' + values['-INPUT-'] + "! PySimpleGUI をお試しいただきありがとうございます")
```

このステートメントは、`-OUTPUT-`キー を持つ`Text`エレメントを文字列で更新します。`window['-OUTPUT-']`は`-OUTPUT-`キーを持つエレメントを検索します。 キーは、空白の`Text`エレメントに属します。 エレメントが検索から返されると、そのエレメントの`update`メソッドが呼び出されます。 ほとんどすべてのエレメントは`update`メソッドを持っています。 このメソッドはエレメントの値や構成を変更したりするのに使用します。

テキストを黄色にしたい場合は、`update`メソッドに`text_color`パラメーターを追加して以下のように処理します。
```python
    window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます", text_color='yellow')
```

`text_color`パラメーターを追加した後、これが新しい結果ウィンドウとなります。

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/HelloWorldYellow.jpg">
</p>


各エレメントで使用できるパラメーターは[call referenceドキュメント](http://calls.PySimpleGUI.org)とdocstringsの両方に記載されています。PySimpleGUIには利用可能なすべてのオプションを理解するのに役立つ豊富なドキュメントが用意されています。`Text`エレメントの`update'`メソッドを検索すると、以下のような定義が見つかります:

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/TextUpdate.jpg">
</p>


ご覧のように、いくつかのものは、`Text`エレメントに変更できます。 call referenceドキュメントはPySimpleGUIでのプログラミングを簡単にする貴重なリソースです。

<hr>

## レイアウトはおもしろいです（笑）! :laughing:

ウィンドウのレイアウトは「リストのリスト」(LOL)です。 ウィンドウは「行」に分割されます。 ウィンドウの各行はレイアウトのリストになります。 すべてのリストを連結すると、レイアウトができあがります。リストのリストです。

行の定義を簡単に確認にするため、各行に追加で 'Text' エレメントを追加しました。レイアウトは自体は以前と同じです:

```python
layout = [  [sg.Text('ライン 1'), sg.Text("お名前は何ですか")],
            [sg.Text('ライン 2'), sg.Input()],
            [sg.Text('ライン 3'), sg.Button('はい')] ]
```

このレイアウトの各行は、ウィンドウ内の行に表示されるエレメントのリストです。


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/rows.jpg">
</p>



リストを使用してGUIを定義する場合、他のフレームワークを使用してGUIプログラミングを行う方法にくらべていくつかの大きな利点があります。 たとえば、Pythonのリスト内包表記を利用して、1行のコードでボタンのグリッドを作成できます。


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

「楽しむ」がプロジェクトの目的の1つであることを思い出してください。 Pythonの強力な基本機能をGUIの問題に直接適用するのは楽しいです。GUIを作成するコードのページの代わりに、数行（または多くの場合は1行）のコードを作成します。

## コードの折りたたみ

ウィンドウのコードを1行のコードに凝縮できます。 レイアウトの定義、ウィンドウ作成、表示、およびデータ収集はすべて、次の1行のコードで書けます。

```python
event, values = sg.Window('Window Title', [[sg.Text("お名前は何ですか？")],[sg.Input()],[sg.Button('はい')]]).read(close=True)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/WhatsYourName.jpg">
</p>


同じウィンドウが表示され、PySimpleGUIプログラムのセクションを示す例と同じ値が返されます。 非常に少ない量で多くのことを行うことができるため、Pythonコードにすばやく簡単にGUIを追加できます。 データを表示してユーザーからの選択を得たい場合は、1ページのコードではなく1行のコードで行うことができます。

短縮エイリアスを使用してより少ない文字数でコードのスペースをさらに短くできます。すべてのエレメントには、使用できる短い名前が1つ以上含まれています。 たとえば、`Text`エレメントは単に`T`として書けます。`Input`エレメントは `I`、`Button`は`B`と書けます。 したがって、ウィンドウの1行のコードは以下になります:

```python
event, values = sg.Window('Window Title', [[sg.T("あなたの名前は何ですか?")],[sg.I()],[sg.B('はい')]]).read(close=True)
```


### コードの移植性

PySimpleGUIは現在、4つのPythonのGUIフレームワークで実行できます。 使用するフレームワークは、importステートメントを使用して指定します。 インポートを変更すると、基本のGUIフレームワークが変更されます。プログラムによっては、別のGUIフレームワークで実行するためにはimport文以外の変更は必要ありません。 上記の例では、インポートを`PySimpleGUI`から`PySimpleGUIQt`、`PySimpleGUIWx`、`PySimpleGUIWeb`、`PySimpleGUIWeb`に変更すると、フレームワークが変更されます。

| ステートメントをインポート | 結果ウィンドウ |
|--|--|
| PySimpleGUI |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg) |
| PySimpleGUIQt |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Qt.jpg) |
| PySimpleGUIWx |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-WxPython.jpg) |
| PySimpleGUIWeb |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Remi.jpg) |



GUIのコードをあるフレームワークから別のフレームワークに移植する（たとえば、コードをtkinterからQtに変更する）には、通常はコードの書き換えが必要です。PySimpleGUIは、フレームワーク間の簡単な移動を可能にするように設計されています。 場合によってはいくつかの変更が必要ですが目的は最小限の変更で移植性の高いコードを作ることです。 

システムトレイアイコンなどの一部の機能は、すべてのポートで使用できないです。 システムトレイアイコン機能はQtおよびWxPythonポートで使用できます。シミュレートされたバージョンはtkinterで使用できます。システムトレイアイコンは、PySimpleGUIWebポートではサポートされません。

##  ランタイム環境

|環境 |サポートされる |
|--|--|
|パイソン| Python  3.4+ |
|オペレーティング システム |ウィンドウズ,Linux,マック |
|ハードウェア |デスクトップPC,ノートパソコン,ラズベリーパイ,PyDroid3 を実行しているアンドロイドデバイス |
|オンライン |repli.it,Trinket.com（どちらもブラウザ上でtkinterを実行する）|
|GUIフレームワーク |tkinter, pyside2, WxPython, Remi |


## 統合
200以上の「デモプログラム」の中には、多くの人気のPythonパッケージをGUIに統合する方法の例が見つかります。

ウィンドウにMatplotlibの描画を埋め込みたいですか？、問題ありません、 デモコードをコピーすると即座にあなたの夢のMatplotlibの描画をあなたのGUIに組み込めます。  

これらのパッケージやその他のパッケージは、デモプログラムやデモレポが用意されているので、GUIに入れる準備ができています。

|パッケージ |説明 |
|--|--|
 Matplotlib |グラフやプロットの多くの種類 |
 OpenCV |コンピュータビジョン（AIでよく使用さる） |
 VLC |ビデオ再生 |
 pymunk |物理エンジン|
 psutil |システム環境の統計 |
 prawn |Reddit  API |
json |PySimpleGUIは、「ユーザー設定」を格納する特別なAPIをラップします。 |
 weather |お天気アプリを作るためにいくつかの天気APIと統合 |
 mido |MIDIの再生 |
 beautiful soup |ウェブスクレイピング（GitHub issueウォッチャーでの例） |

<hr>

# インストール :floppy_disk:


PySimpleGUIをインストールする一般的に2つの方法があります。

1. PyPIからpipでインストールする
2. PySimpleGUI.pyファイルをダウンロードしてアプリケーションのフォルダーに配置します


### Pipインストールとアップグレード

現在提案されている`pip`コマンドを呼び出す方法は、Pythonを使ってモジュールとして実行することです。 以前は、`pip`または`pip3`コマンドはコマンドライン/シェル上で
直接実行されました。 提案された方法は以下となります。

Windowsの初期インストール

`python -m pip install PySimpleGUI`

LinuxおよびmacOSの初期インストール

`python3 -m pip install PySimpleGUI`

`pip`を使用してアップグレードするには、単に2つのパラメーター`--upgrade --no-cache-dir`を指定するだけです。

Windowsのアップグレード

`python -m pip install --upgrade --no-cache-dir PySimpleGUI`

LinuxおよびmacOSのアップグレード

`python3 -m pip install --upgrade --no-cache-dir PySimpleGUI`


### 単一ファイルのインストール

PySimpleGUIはRaspberry Piのようなインターネットに接続されていないシステムでも、簡単にインストールできるように単一の.py ファイルとして作成されました。 PySimpleGUI.pyファイルをインポートするアプリケーションと同じフォルダーに置くだけです。Pythonはインポート時にローカルのコピーを使用します。

.pyファイルを使用してインストールする場合は、PyPIから入手するか、最新の未リリースバージョンを実行したい場合はGitHubからダウンロードします。

PyPIからインストールするには、wheelまたは.gzファイルをダウンロードして解凍します。.whlファイルをzipにリネームすると、通常のzipファイルと同じように開くことができます。 フォルダーの中にはPySimpleGUI.pyファイルがあります。 このファイルをアプリケーションのフォルダーにコピーすると完了です。

tkinterバージョンのPySimpleGUIのPyPIリンクです
https://pypi.org/project/PySimpleGUI/#files

GitHubリポジトリの最新バージョンは、こちらで確認できます
https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/PySimpleGUI.py


「そうだけど、巨大なソースファイルを1つだけ持つのはなんてひどい考えだ」と今、考えている人もいるでしょう。 これは*時には*ひどい考えかもしれません。 今回は、メリットはデメリットを大幅に上回りました。 コンピュータサイエンスの概念の多くはトレードオフまたは主観的なものです。 一部の人が望むのと同じくらいすべてが白黒ではありません。 多くの場合、この質問に対する答えは「次第」です。



## ギャラリー :art:

ユーザーが投稿したGUIとGitHubにあるGUIのより正式なギャラリーの作成は進行中ですが、readmeを作成時点ではまだ完成していません。現在まとまってスクリーンショットを見れる場所は2か所あります。願わくは人々が作っている素晴らしい作品を正当化するためのWikiやその他の仕組みがすぐにリリースされることを願っています。

### ユーザーが提出したギャラリー

1つ目は、GitHubにある[ユーザーがスクリーンショットを提出したissue](https://github.com/PySimpleGUI/PySimpleGUI/issues/10)です。 これは、人々が作ったものを披露するための非公式な方法です。 理想的ではありませんがスタートでした。

### 大量にスクラップされたGitHubの画像

2つ目は、PySimpleGUIを使用していると伝えられているGitHubの1,000のプロジェクトか集めた[3,000以上の画像の大規模なギャラリー ](https://www.dropbox.com/sh/g67ms0darox0i2p/AAAMrkIM6C64nwHLDkboCWnaa?dl=0)です。 手作業でフィルタリングされており初期のドキュメントで使用されていた古いスクリーンショットがたくさんあります。 しかし、そこにあなたの想像力を引き起こす何かが見つかもしれません。

<hr>

# PySimpleGUIの用途について :hammer:

次のセクションでは、PySimpleGUIの用途の一部を紹介します。 GitHubだけでも1,000以上のプロジェクトでPySimpleGUIを使用しています。これだけの多くの人々の可能性が広がったことは本当に驚くべきことです。 多くのユーザーは以前にPythonでGUIを作成しようとして失敗したと話していましたが、彼らがPySimpleGUIを試してみて最終的に自分の夢を達成できたと話しています。

## 最初のGUI

もちろん、PySimpleGUIのもっとも優れた使い方の1つはPythonプロジェクト用のGUIを作ることです。 ファイル名をリクエストするだけの小さなプロジェクトから開始できます。 このためには、`popup`と呼ばれる「ハイレベル関数」の1つを1回呼び出すだけで済みます。 ポップアップにはあらゆる種類があり、一部は情報を収集します

`popup`自体で情報を表示するためのウィンドウを作成します。printと同じように複数のパラメーターを渡せます。情報を取得したい場合は、`popup_get_filename`のように`popup_get_`で始まる関数を呼び出すします。

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

ゲーム開発用のSDKとしては特に記述されていませんが、PySimpleGUIはゲームの開発を非常に簡単にします。

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


WEBカメラからビデオをキャプチャしてGUIで表示するのには、PySimpleGUIのコードでは4行でできます。 さらに印象的なのはこらの4行のコードがtkinter、Qt、および Webポートで動作します。  tkinterを使用して画像を表示するのと同じコードを使用して、ブラウザでWebカメラをリアルタイムが表示できます。

また、VLCプレーヤーを使って、オーディオやビデオなどのメディア再生も可能です。デモアプリケーションが提供されているので実際の作業例が用意されています。このreadmeに記載されている内容は全て、あなた自身の創作の出発点として利用できます。
<br><br><br><br><br>
<br><br><br><br><br>
<br><br>
## 人工知能

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"  alt="img" align="right" width="500px"></a>



AIとPythonは長い間、この2つが組み合わされたときのスーパーパワーとして認識されてきました。しかし、多くの場合、ユーザーがGUIを使用してこれらのAIアルゴリズムを身近に操作する方法が欠けています。

これらのYOLOのデモは、GUIがAIアルゴリズムとの対話においていかに大きな違いをもたらすかの素晴らしい例です。 これらのウィンドウの下部にある2つのスライダーに注目してください。 この2つのスライダーは、YOLOアルゴリズムが使用するパラメーターを変更します。 

コマンドラインのみを使用してYOLOデモをチューニングする場合は、アプリケーションを起動するときに、パラメーターを設定し、その実行方法を確認して、アプリケーションを停止し、パラメーターを変更して最後に新しいパラメーターでアプリケーションを再起動する必要があります。
<br><br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"  alt="img" align="right" width="500px"></a>

これらのステップと、GUIを使用して実行できる操作と比較してみます。 GUIを使用すると、これらのパラメーターをリアルタイムで変更できます。 アルゴリズムにどのような影響を与えているかについて、すぐにフィードバックを得られます。



<br><br><br><br><br>
<br><br>
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"  alt="img" align="right" width="500px"></a>


公開されているAIプログラムには、コマンドラインで動かすプログラムが非常に多く存在します。 これ自体は大きなハードルではありませんが、コマンドラインでカラーリングしたいファイル名を入力/貼り付け、プログラムを実行して、出力ファイルの結果をファイルビューアーで開くのは十分「面倒くさい」です。


GUIには、**ユーザーエクスペリエンスを変更する**を「GUIギャップ」に変化させる力があります。 このカラーライズの例では、ユーザーは画像が格納されてたフォルダーを指定して、画像をクリックするだけでカラーリングと結果表示の両方を行えます。  
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

前述の「GUIギャップ」は、PySimpleGUIを使用して簡単に解決できます。 GUIを追加するプログラムにソースコードを用意する必要もありません。「フロントエンド」GUI は、コマンドラインアプリケーションに渡す情報を収集するGUIです。
フロントエンドGUIは、プログラマにとってユーザーがコマンドライン・インターフェーイスを使い心地よく感じなかったために、以前は使いたがらなかったアプリケーションを配布するための素晴らしい方法です。これらのGUIは、ソースコードにアクセスできないコマンドラインプログラムのための唯一の選択肢です。
この例は、「Jump Cutter」というプログラムのフロントエンドです。 パラメーターはGUIをとおして収集されて、パラメーターを使用してコマンドラインが構築され、コマンドラインプログラムの出力がGUIインターフェイスにルーティングされてコマンドが実行されます。この例では、実行されたコマンドが黄色で表示されています。
<br><br>
<hr>

## Raspberry Pi

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"  alt="img" align="right" width="500px"></a>


PySimpleGUIはPython 3.4に対応しているため、Raspberry Piのプロジェクト用のGUIを作成できます。 タッチスクリーンと組み合わせるととくにうまく機能します。 モニターが接続されていない場合は、PySimpleGUIWebを使用してPiを制御することもできます。

<br><br>
<br><br>
<br><br>
<br><br><br>
<hr>


## 高度な機能への簡単なアクセス
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"  alt="img" align="right" width="500px"></a>


基礎となるGUIフレームワークの多くの機能に非常に簡単にアクセスできるため、GUIフレームワークを直接使っているようには見えないアプリケーションを作るための機能を組み合わせられます。

たとえば、tkinterやその他のGUIパッケージを使用してタイトルバーの色や外見を変更することはできませんが、PySimpleGUIを使用すると、カスタムタイトルバーを持っているかのように表示されるウィンドウを簡単に作成できます。
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


# 支援する	<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"  alt="img"  width="90px"></a>

プロジェクトの財政的支援は非常に高く評価されています。 正直に言うと、経済的な援助が必要です。 ライトをつけ続けるだけで高価です。 ドメイン名登録、トリンケット、コンサルティングヘルプなどのサブスクリプションの長いリストは、すぐにかなりの経常コストに加算されます。

PySimpleGUIの開発は安くありませんでした。愛情をこめて開発したとはいえ何年にもわたって非常に手間のかかる開発でした。こんにちの姿になるのにかなりの時間をついやしました。現在も続けています。

PySimpleGUIにはオープンソースライセンスがあり、そのまま残ることができれば素晴らしいことです。 お客様またはお客様の会社 (特に企業でPySimpleGUIを使用している場合) が、PySimpleGUIを使用して経済的に利益を得ている場合は、プロジェクトの寿命を延長する機会を持っています。

###　Buy Me a Coffee

「Buy Me a Coffee」は、開発者を公的にサポートするための素晴らしい方法です。 素早く、簡単に、貢献は記録されるので、あなたがPySimpleGUIのサポーターであることを他の人に見せられます。寄付を非公開にもできます。

<a href="https://www.buymeacoffee.com/PySimpleGUI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>




### GitHubスポンサー

<a href="https://github.com/sponsors/PySimpleGUI" target="_blank"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&link=%3Curl%3E&color=f88379"></a>

[GitHub定期的なスポンサーシップ](https://github.com/sponsorsー/PySimpleGUI)は、継続的にさまざまなレベルのサポートでプロジェクトをスポンサーする方法です。これにより、多くのオープンソース開発者が企業レベルのスポンサーシップを受けられます。

プロジェクトに金銭的に貢献していただけると、非常にありがたいです。オープンソースの開発者であることは、経済的に困難です。YouTube動画のクリエイターは、動画作成で生計を立てています。オープンソース開発者にとってはまだそれほど簡単ではありません。


# 感謝の気持ちをこめて

<!--
To everyone that's helped, in whatever fashion, I'm very very grateful.

Even taking a moment to say "thank you" helps, and a HUGE number of you have done that.  It's been an amazing number actually.  I value these thanks and find inspiration in the words alone.  Every message is a little push forward.  It adds a little bit of energy and keeps the whole project's momentum.  I'm so very grateful to everyone that's helped in whatever form it's been.
-->
どんな形でも協力してくれた皆さんにはとても感謝しています。

一瞬でも "ありがとう "と言ってくれるだけでも助かるし、とても多くの人たちががそうしてくれましたた。 実際、驚くべき人数です。 私はこの感謝の気持ちを大切にしてその言葉だけでインスピレーションを得ています。 すべてのメッセージは少しずつ前進しています。 メッセージはちょっとしたエネルギーとなってプロジェクト全体の勢いを保っています。 どのような形であれ協力してくれた皆さんには本当に感謝しています。

# Contributing  👷

# 貢献:construction_worker:

現在、PySimpleGUIはオープンソースライセンスでライセンスされていますが、プロジェクト自体は製品のように構成されています。プルリクエストは受け付けていません。

コードに貢献する最良の方法の1つは、アプリケーションを書いて公開することです。ユーザーは他のユーザーが作ったものを見て刺激を受けます。GitHubリポジトリを作成してコードを投稿しte
、スクリーンショットをreadmeファイルに入れましょう。

不足している機能があったり、機能強化を提案したい場合は、[issueを開いてください](https://github.com/PySimpleGUI/PySimpleGUI/issues/new?assignees=&labels=&template=issue-form---must-fill-in-this-form-with-every-new-issue-submitted.md&title=%5B+Enhancement%2FBug%2FQuestion%5D+My+problem+is.) 。


# 特別な感謝 :pray:

<!--
This version of the PySimpleGUI readme wouldn't have come together without the help from @M4cs. He's a fantastic developer and has been a PySimpleGUI supporter since the project's launch. @israel-dryer is another long-term supporter and has written several PySimpleGUI programs that pushed the envelope of the package's capabilities. The unique minesweeper that uses an image for the board was created by Israel. @jason990420 surprised many when he published the first card game using PySimpleGUI that you see pictured above as well as the first minesweeper game made with PySimpleGUI. @Chr0nicT is the youngest developer I've worked with, ever, on projects. This kid shocks me on a regular basis. Ask for a capability, such as the PySimpleGUI GitHub Issues form error checking bot, and it simply happens regardless of the technologies involved. I'm fortunate that we were introduced. Someday he's going to be whisked away, but until then we're all benefiting from his talent. The Japanese version of the readme was greatly improved with help from @okajun35. @nngogol has had a very large impact on the project, also getting involved with PySimpleGUI in the first year of initial release. He wrote a designer, came up with the familiar window[key] lookup syntax, wrote the tools that create the documentation, designed the first set of doc strings as well as tools that generate the online documenation using the PySimpleGUI code itself. PySimpleGUI would not be where it is today were it not for the help of these individuals.

The more than 2,200 GitHub repos that use PySimpleGUI are owed a "Thank You" as well, for it is you that has been the inspiration that fuels this project's engine.

The overseas users that post on Twitter overnight are the spark that starts the day's work on PySimpleGUI. They've been a source of positive energy that gets the development engine started and ready to run every day. As a token of appreciation, this readme file has been translated into Japanese.

You've all been the best user community an Open Source developer could hope for.
-->

このバージョンのPySimpleGUIreadmeは、[@M4cs](https://github.com/M4cs)の助けがなければ完成しませんでした。彼は素晴らしい開発者であり、プロジェクトの立ち上げ以来、PySimpleGUIのサポーターです。 [@israel-dryer](https://github.com/israel-dryer)は、もう1つの長期的なサポーターであり、パッケージの機能の限界を押し上げるいくつかのPySimpleGUIプログラムを作成しています。ボードの画像を使用するユニークな掃海艇は、israelによって作成されました。 [@jason990420](https://github.com/jason990420)は、上の写真にあるPySimpleGUIを使用した最初のカードゲームと、PySimpleGUIで作成された最初のマインスイーパゲームを公開したときに多くの人を驚かせました[@Chr0nicT](https://github.com/Chr0nicT)はこれまで一緒にプロジェクトを進めてきた中で最年少の開発者です。この子は定期的に私を驚かせてくれます。例えばPySimpleGUIのGitHub Issuesフォームのエラーチェックボットのような機能を求めると、関係する技術に関わらず簡単に実現してしまうのです。縁があって出会いました。いつの日か彼は去ってしまうかもしれませんが、それまでは私たちは彼の才能から恩恵を受けています。日本語版のreadmeは[@okajun35](https://github.com/okajun35)の助けを借りて大幅に改善されました。 [@nngogol](https://github.com/nngogol)はプロジェクトに非常に大きな影響を与え、初期リリースの最初の年には PySimpleGUIに関わってくれました。彼はデザイナーを書き、おなじみのwindow[key] ルックアップシンタックスを考案しました。またドキュメントを作成するツールを書きいて最初のdoc stringsを設定して、、PySimpleGUIコード自体を使ってオンライン・ドキュメントを生成するツールを作成しました。これらの人々の助けがなければPySimpleGUIは今日のようにはなりませんでした。

PySimpleGUIを使用する1,200を超えるGitHubリポジトリにも「ありがとう」があります。これは、。このプロジェクトのエンジンを動かしているのは、あなたのインスピレーションです。

一晩中Twitterに投稿してくれる海外のユーザーは、PySimpleGUIの一日の作業を始めるきっかけとなります。彼らはポジティブなエネルギーの源であり、開発エンジンを始動させ、毎日稼働させる準備をしてくれています。感謝の意を込めて、このreadmeファイルを[日本語](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md)に翻訳しました。

皆さんはオープンソース開発者が望む最高のユーザーコミュニティです。



&copy; Copyright 2021 PySimpleGUI 
