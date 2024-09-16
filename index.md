機械学習発展 (実践)
===

[![GitHub Pages](https://github.com/tatsy-classes/1284-sds-advml/actions/workflows/gh-pages.yaml/badge.svg)](https://github.com/tatsy-classes/1284-sds-advml/actions/workflows/gh-pages.yaml)
[![Python environment](https://github.com/tatsy-classes/1284-sds-advml/actions/workflows/python.yaml/badge.svg)](https://github.com/tatsy-classes/1284-sds-advml/actions/workflows/python.yaml)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

講義の概要
---

この講義ではPythonを用いて、画像認識と機械学習の実践的な利用法について学ぶ。資料の中では、ライブラリを使った実装を用いる場合も、その背景にある理論とライブラリに頼らない簡易実装を与える。これにより、**ライブラリのユーザから卒業**し、自分の必要とする機械学習のメソッドを実装する力を養う。

### 求める前提知識

- Pythonの**読み書きが不自由なく**できる (基本的な読み書きだけだと辛いかもしれない)
- WindowsのPowerShellやMac/Linuxの**ターミナルの基本操作**ができる
- 大学1, 2年生レベルの初等的な数学(**特に線形代数**)の知識

### 想定受講者

- Pythonを用いた画像認識・機械学習システムの実装方法について学びたい人
- 深層学習だけでなく、画像認識・機械学習技術の背景にある理論を学びたい人

### 資料中の表記について

- [こちら](sec:notation)をご覧ください

### 参考図書

- M. Beyeler 著、池田ほか訳、『OpenCVとPythonによる機械学習プログラミング』、マイナビ [[URL]](https://book.mynavi.jp/ec/products/detail/id=92292)
- A. Geron 著、下田 監修、長尾 訳、『scikit-learn、Keras、TensorFlowによる実践機械学習 (第2版)』、オライリー社 [[URL]](https://www.oreilly.co.jp/books/9784873119281/)
- 赤穂 著、『カーネル多変量解析』、岩波書店 [[URL]](https://www.iwanami.co.jp/book/b257891.html)
- R. S. Sutton, A. G. Barto 著、鈴木ほか訳、『強化学習 (第2版)』、森北出版 [[URL]](https://www.morikita.co.jp/books/mid/082662)

---

以下、一橋大生向け情報

講義について
---

- 実施時限: 秋冬学期 第2限
- 教室: 東2号館棟2206教室

### 講義形式

- 資料の内容を全て講義内で解説することはしないので、必要に応じて自習をお願いします。
- 資料を全て理解する必要はありませんが、演習については課題が解けるように取り組んでください。

### 講義日程

- **事前準備**
  - [Python環境の設定](https://tatsy-classes/1284-sds-prog2/contents/setup-python.html)
  - [Git環境の設定](https://tatsy-classes/1284-sds-prog2/contents/setup-git.html)

- **第1回**
  - [NumPyの基本](sec:numpy)
  - [Matplotlibの基本 (自習)](sec:matplotlib)
  - [Pandasの基本 (自習)](sec:pandas)

- **第2回**
  - [OpenCVの基本](sec:opencv)
  - [図形の検出](sec:figure-detection)

- **第3回**
  - [scikit-learnによる機械分類の基礎](sec:scikit-learn)

- **第4回**
  - [演習1 画像入力式数独ソルバーの作成](sec:exercise-sudoku)

- **第5回**
  - [演習1 画像入力式数独ソルバーの作成](sec:exercise-sudoku)

- **第6回**
  - [データ可視化と次元圧縮](sec:data-visualization)

- **第7回**
  - [画像からの特徴量抽出](sec:feature-extraction)
  - [深層学習による物体認識 (自習)](sec:deep-learning)

- **第8回**
  - [演習2 百人一首エージェントの作成](sec:exercise-ogura)

- **第9回**
  - [演習2 百人一首エージェントの作成](sec:exercise-ogura)

- **第10回**
  - [強化学習の基礎](sec:reinforcement-learning)
  - [Q学習の基礎](sec:q-learning)

- **第11回**
  - [オセロAIの基礎](sec:othello-agent)

- **第12回**
  - [演習3 オセロエージェントの作成](sec:exercise-othello)

- **第13回**
  - [演習3 オセロエージェントの作成](sec:exercise-othello)

課題の提出方法
---

- [こちら](sec:submit-assignment)を参照ください。

Build Status
---

```{nb-exec-table}
```
