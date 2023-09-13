機械学習発展 (実践)
===

[![Github Pages](https://github.com/tatsy/1284-sds-ml-advanced/actions/workflows/gh-pages.yaml/badge.svg)](https://github.com/tatsy/1284-sds-ml-advanced/actions/workflows/gh-pages.yaml)
[![Miniconda](https://github.com/tatsy/1284-sds-ml-advanced/actions/workflows/conda.yaml/badge.svg?branch=master)](https://github.com/tatsy/1284-sds-ml-advanced/actions/workflows/conda.yaml)

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## 講義の概要

この講義ではPythonを用いて、画像認識と機械学習の実践的な利用法について学ぶ。資料の中では、ライブラリを使った実装を用いる場合も、その背景にある理論とライブラリに頼らない簡易実装を与える。これにより、**ライブラリのユーザから卒業**し、自分の必要とする機械学習のメソッドを実装する力を養う。

### 求める前提知識

- Pythonの**読み書きが不自由なく**できる (基本的な読み書きだけだと辛いかもしれない)
- WindowsのPowerShellやMac/Linuxの**ターミナルの基本操作**ができる

### 想定受講者

- Pythonを用いた画像認識・機械学習システムの実装方法について学びたい人
- 深層学習だけでなく、画像認識・機械学習技術の背景にある理論を学びたい人

### 資料中の表記について

- [こちら](sec:notation)をご覧ください

### 参考図書

- M. Beyeler著、池田ほか訳『OpenCVとPythonによる機械学習プログラミング』、マイナビ [[URL]](https://book.mynavi.jp/ec/products/detail/id=92292)
- A. Geron著『scikit-learn、Keras、TensorFlowによる実践機械学習 (第2版)』、オライリー社 [[URL]](https://www.oreilly.co.jp/books/9784873119281/)
- 赤穂 著 『カーネル多変量解析』、岩波書店 [[URL]](https://www.iwanami.co.jp/book/b257891.html)
- R. S. Sutton, A. G. Barto著、鈴木ほか訳『強化学習 (第2版)』、森北出版 [[URL]](https://www.morikita.co.jp/books/mid/082662)

---

以下、一橋大生向け情報

## 講義について

- 実施時限: 秋冬学期 第2限
- 教室: 東2号館棟2206教室

### 講義日程

- **第1回**
  - [Python環境の設定](sec:setup-python)
  - [NumPyの基本](sec:numpy)
  - [Matplotlibの基本](sec:matplotlib)
  - [Pandasの基本](sec:pandas)

- **第2回**
  - [OpenCVの基本](sec:opencv)
  - [図形の検出](sec:figure-detection)

- **第3回**
  - [scikit-learnによる機械分類の基本](sec:scikit-learn)

- **第4回**
  - [演習1 画像入力式数独ソルバーを作る](sec:exercise-sudoku)

- **第5回**
  - [演習1 コンピュータ・数独大会](sec:exercise-sudoku)

- **第6回**
  - [データ可視化と次元圧縮](sec:data-visualization)
  - [特徴量抽出](sec:feature-extraction)

- **第7回**
  - [深層学習による物体認識](sec:deep-learning)

- **第8回**
  - [演習2 百人一首エージェントを作る](sec:exercise-ogura)

- **第9回**
  - [演習2 コンピュータ・百人一首大会](sec:exercise-ogura)

- **第10回**
  - [強化学習の基礎](sec:reinforcement-learning)
  - [Q学習](sec:q-learning)

- **第11回**
  - [基本のオセロAI](sec:othello-agent)
  - [深層強化学習](sec:deep-reinforcement-learning)

- **第12回**
  - [演習3 オセロエージェントを作る](sec:exercise-othello)

- **第13回**
  - [演習3 コンピュータ・オセロ大会](sec:exercise-othello)

## Build Status

```{nb-exec-table}
```
