NumPyの基本
===

NumPyの解説に入る前に、以下で用いるIPython環境について簡単に触れておく。IPythonとはInteractive Pythonの略でWindowsならコマンドプロンプトかPowerShell, Mac/Linuxならターミナルを開いて、

```shell
ipython
```

と打ち込むと、

```python
In [1]: 
```

のように表示されて、Pythonのコマンドを打ち込めるようになる。試しに電卓として以下のような計算を試してみよう。

```python
In [1]: 1 + 2  # Enterを押す(以下では省略する)
Out[1]: 3
```

上記の通り`1 + 2`の計算結果が正しく表示されることが分かる。また、変数に対する代入などといったPythonで普通に行える操作は使い勝手の善し悪しはあるももの、全て使用可能である。

```python
In [2]: a = 1

In [3]: b = 2

In [4]: a + b
Out[4]: 3
```

なお、以下では特別な理由がない限り`In [1]:`や`Out [1]`のような表記は省略するので注意すること。

## Pythonの配列とNumPyの配列

NumPyは一口に言えば、多次元の配列で表わされるデータ (例えば音声なら1次元の配列、画像なら2次元の配列)を様々な線形代数的な演算によって扱いやすくするためのライブラリといえる。まずは、Pythonの配列とNumPyの配列の違いについて見てみたい。

Pythonで配列を作成するには`[ ]`で数字をコンマ区切りにすれば良く、

```python
numbers = [1, 2, 3]
```

と書く。この時、aの各要素を2倍にしたいとすると、直感的には

```python
numbers * 2
```

とすれば良さそうだが、これは

```python
In [1]: numbers = [1, 2, 3]

In [2]: numbers * 2
Out[2]: [1, 2, 3, 1, 2, 3]
```

のように配列が2回繰り返されたものとなってしまう。Pythonの配列でこれを実現するには*リスト内包表記*と呼ばれる記法を使って

```python
In [2]: [x * 2 for x in numbers]
Out[2]: [2, 4, 6]
```

と書く必要がある。もちろん、これでも必要十分ではあるのだが、気持ちとしては、より直感的な記述で書きたいと思うのが人情という物だ。そこでNumPyの登場である。

NumPyはPythonの配列を引数にとる関数`numpy.array`を用いて、

```python
import numpy as np
numbers = np.array([1, 2, 3])
``` 

と書くことで作成できる。NumPyの配列であれば、下記のように要素を2倍にする計算を、より直感的に行うことができる。

```python
In [1]: import numpy as np

In [2]: numbers = np.array([1, 2, 3])

In [3]: numbers * 2
Out[3]: array([2, 4, 6])
```

### 多次元配列を作る

Pythonの配列で多次元配列を作るには、

```python
numbers = [[1, 2], [3, 4]]
```

のように`[ ]`を二重にすれば良かった。また、全ての要素が1の10x10の二次元配列を作りたい場合には、リスト内包表記を用いて

```python
ones = [[1] * 10 for _ in range(10)]
```

のように書く必要がある。NumPyで同様の配列を作る場合、先ほど紹介した方法で`numpy.array`の引数にPythonの多次元配列を代入すれば良い。

```python
numbers = [[1, 2], [3, 4]]
numbers_np = np.array(numbers)
```

また、NumPyにはいくつかの特殊な配列を作る関数が用意されていて、全ての要素が0や全ての要素が1、または特定の要素を持つ配列は次のように作成できる。

```python
zeros = np.zeros((10, 10))   # 全ての要素が0の10x10の二次元配列
ones = np.ones((10, 10))     # 全ての要素が1の10x10の二次元配列
twos = np.full((10, 10), 2)  # 全ての要素が2の10x10の二次元配列
```

上記の関数を使う場合、関数の引数がPythonの配列ではなく、多次元配列の大きさを表すタプルになるので注意すること。

### 配列の情報

上記のNumPyの配列をIPython上で表示すると

```python
In [1]: numbers = np.array([1, 2, 3])

In [2]: numbers
Out[2]: array([1, 2, 3])
```

のように表示されるが、この実態は`int32`型すなわち32bit符号付き整数となっている。これを調べるには，配列の`dtype`フィールドにアクセスすれば良く

```python
In [3]: numbers.dtype
Out[3]: dtype('int32')
```

のような出力が得られる。

また、配列の大きさは`shape`フィールドに、何次元の多次元配列なのかは`ndim`フィールドにアクセスすることで調べることができる。

```python
In [1]: ones = np.ones((4, 5, 6))

In [2]: ones.shape
Out[2]: (4, 5, 6)

In [3]: ones.ndim
Out[3]: 3
```

また、始めから配列要素の型を指定して、

```python
numbers = np.array([1, 2, 3], dtype='float32')
```

のようにすることもできる。上記の例では、配列内の各要素が`float32`型、すなわち32bitの単精度浮動小数で表わされる。NumPyで使える配列の型には、この他にも`int8` / `uint8` (それぞれ8bit符号あり、符号なし整数)以下、`int16`、`int32`、`int64`が符号付き整数 (それぞれに符号なし整数である`uint..`が存在)の他、64bit倍精度浮動小数として`double`、また複素数を表わす`complex64` (実部と虚部がそれぞれ32bit単精度浮動小数)や`complex128` (実部と虚部がそれぞれ64bit浮動小数)などがある。

最初に異なる型で宣言した配列を途中から別の型に変更したい場合には`astype`メソッドを使って、

```python
numbers = np.array([1, 2, 3])  # int32型
numbers = numbers.astype('float32')  # 型をfloat32に変更
```

のようにすることで実現できる。

---

#### 閑話休題: オブジェクト指向型言語の用語

Pythonはプログラミング言語の中ではオブジェクト指向型の言語に分類される (他には手続き型や関数型などがある)。オブジェクト指向型言語では、実世界のモノをプログラムにより表現するための仕組みとしてモノ(= オブジェクト)を「クラス」という概念で表わす。ここでは、詳しい明言を避けるが、Pythonのクラスとは以下のようなものだ。

```python
class Human(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def intro(self):
    print('Hi, my name is %s. I\'m %d years old.' % (self.name, self.age))
```

このようなクラスにおいて、クラスが保持する変数 (= `self.name`や`self.age`)のことを**パラメータ**や**フィールド**と呼び、クラスが備える関数(= `intro`)のことを**メソッド**と呼ぶ。

また、上記のクラスを用いて、実際の`Human`を作ること、すなわち

```python
taro = Human('Taro', 22)
```

という処理を**インスタンス化**と呼ぶ。これらの用語はPythonに限らず、オブジェクト指向型言語の基本用語なので覚えておくこと。

---

## NumPyを用いた線形代数

### スカラに対する演算

ベクトルや行列に対して、スカラを四則演算すると、要素ごとに同じ計算が行われる。例えば、

```python
a = np.array([1, 2])
print(a + 1)  # array([2, 3])
```

の例では、aの各要素に1が足し算されていることが分かる。これは、他の四則演算に対しても同様である。

### 要素ごとの四則演算

同じ要素数を持つベクトル同士や行列同士を四則演算すると、要素ごとの演算が行われる。例えば、

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)  # array([4, 6])
```

の例では、aとbの各要素に対して、和が取られていることが分かる。これは、他の四則演算に対しても同様である。

### 各要素への関数適用

NumPyには`numpy.exp`などのように、ベクトル・行列の各要素に対して、特定のスカラに対する演算を行う関数が用意されている。一例として、`numpy.sin`、`numpy.cos`、`numpy.exp`、`numpy.log`などがあり、高校レベルで思いつくものであれば大抵は用意されている。

### ベクトルの内積

内積の計算には二つのベクトルに対して`numpy.dot`を用いれば良い。

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.dot(a, b))  # 11
```

また、`numpy.dot`と同じ効果を現す演算子として`@`が用意されており、上と同様のコードは`@`を使って以下のように書ける。

```python
print(a @ b)  # 11
```

### ベクトルの外積

外積の計算には二つのベクトルに対して`numpy.cross`を用いれば良い。

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.cross(a, b))  # array([-3, 6, -3])
```

なお、この`numpy.cross`は二次元ベクトルに対しても計算が可能で、その場合は二次元ベクトルを並べて作られる2x2行列の行列式が計算される。

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.cross(a, b))  # -2
```

この計算は二次元平面においてa → bというベクトルの移動が時計回りの回転(負の値になる)なのか、反時計回りの回転(正の値になる)なのかを調べる時などに役に立つ。

### 逆行列・疑似逆行列

とある行列が正則行列 (逆行列を持つ = 行列式が0でない)ときには`numpy.linalg.inv`を用いて逆行列が計算できる。

```python
A = np.array([[1, 2], [3, 4]], dtype='double')
invA = np.linalg.inv(A)
print(invA)
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])
```

なお、その行列が正則行列かどうかを調べるには、行列のランクや行列式が0でないかを調べれば良いだろう。

```python
# 行列のランク
np.linalg.matrix_rank(A)  # 2
# 行列式
np.linalg.det(A)  # -2.0000
```

では、次に、正則でない行列 (= 特異行列という)の場合に逆行列を求めようとするとどうなるかを見てみる。

```python
A = np.array([[1, 2], [2, 4]], dtype='double')
np.linalg.inv(A)
```

上記の例では、おそらくエラーメッセージが数行表示されて、最後の行に"**LinAlgError: Singular matrix**"と表示されるはずだ。実際、上記の行列のランクは1で行列式は0.0になるので、各自で調べて見てほしい。

さて、このようは特異行列に対して、逆行列を求めるにはどうすれば良いのだろうか？特異行列に対して、逆行列を求めたい場面というのは実用上はそれなりに多く、その一番身近な例が、以下のような最小二乗問題を解きたい場合だろう。

$$
\min_{\mathbf{x}} \frac{1}{2} \| \mathbf{Ax} - \mathbf{b} \|^2
$$

この場合、 $\mathbf{x}$ について被最小化関数を微分したものがゼロベクトルになる箇所を探せば、それが求める $\mathbf{x}$ だが、この際、被最小化関数の $\mathbf{x}$ についての微分によって得られる

$$
\mathbf{A}^\top \mathbf{Ax} = \mathbf{A}^\top \mathbf{b}
$$

という方程式において $\mathbf{A}^\top \mathbf{A}$ が特異行列になることは実問題においては頻繁に起こる問題である。

このような場合、上記の最小化問題の解は、特異行列に対して逆行列と似た性質を持つ疑似逆行列 (正しくはMoore-Penroseの疑似逆行列と呼ぶ)を右辺に乗ずることで求められる。

すなわち、疑似逆行列を$(\mathbf{A}^\top \mathbf{A})^\dagger$のように表わす時、最小化を実現する$\mathbf{x}$は次の式のように定まる。

$$
\mathbf{x} = (\mathbf{A}^\top \mathbf{A})^\dagger (\mathbf{A}^\top \mathbf{b})
$$

では、疑似逆行列とは、一体どういう性質を持った行列なのだろうか？これを説明するには特異値分解について説明をする必要があるため、詳しくは触れないが、ぜひNumPyで疑似逆行列を求める`numpy.linalg.pinv`を用いて、以下の計算を試してみてほしい。

```python
A = np.array([[1, 2], [2, 4]], dtype='double')
pinvA = np.linalg.pinv(A)
print(pinvA @ A)
print(A @ pinvA @ A)
```
---

#### 閑話休題: 数値誤差

上記の例ではNumPyの関数を用いて行列式や逆行列を求める方法について紹介してきた。前述の通り、行列が正則であれば、`numpy.linalg.inv`で逆行列が求められ、そうでなければ特異行列である旨のエラーメッセージが表示されることを確認したが、実際の数値計算で、入力された行列が正則か特異かを判断するのには若干の問題がある。

例えば、以下の行列の行列式を計算してみてほしい。

$$
\begin{pmatrix}
  1 & 2 & 3 \\
  100 & 200 & 300 \\
  10000 & 20000 & 30000
\end{pmatrix}
$$

説明するまでもなく、上記の行列のランクは1だから、行列式は0になるはずだが...各自で結果を確認してみてほしい。

このように実際の数値計算では数学的には特異であるような行列が正則と判断されてしまうことなどがあり、実際の問題で逆行列を計算するときには、注意が必要である。多くの場合は、逆行列の代わりに疑似逆行列を用いることで上記の問題を回避できるが、その場合には疑似逆行列を用いて得られる解が、どのような性質を持つかに留意する必要がある。

疑似逆行列を用いる、ということは行列が特異、すなわちランク落ちしている場合であるから、実際の線形方程式を満たす解は無数に存在することになる。疑似逆行列を用いて得られる解は、そのうち、ノルムの大きさ (より正確にはl2ノルムの大きさ)が最小になるものになるので、自身が求めたい解がその解で良いのかは、実際の問題を扱う上では重要だろう。

---

### 線形方程式を解く

先ほどの説明では、 $\mathbf{Ax} = \mathbf{b}$ という線形方程式に対して、逆行列を計算して解 $\mathbf{x}$ を求める方法について述べた。

一方で、この方法は数値計算の側面からは、常に最良のやり方であるとは言い難い。通常、行列のサイズが $N \times N$ の時に、逆行列を求めるために必要な計算量は $O(N^3)$ になるが、[ガウスの消去法](https://ja.wikipedia.org/wiki/%E3%82%AC%E3%82%A6%E3%82%B9%E3%81%AE%E6%B6%88%E5%8E%BB%E6%B3%95)のような線形方程式を解くための初等的なアルゴリズムであっても、その計算量は高々 $O(N^2)$ である。

従って、逆行列それ自体が必要でなく、単に線形方程式を解くことが目的であるならば、逆行列を求めることは得策ではない。このような場合には、行列分解を用いて効率的に線形問題を解く`numpy.linalg.solve`を使うと良い。より厳密には、この関数は行列を[LU分解](https://ja.wikipedia.org/wiki/LU%E5%88%86%E8%A7%A3)して、分解によって得られた下三角行列と上三角行列に対して線形問題を解く。この際、LU分解にかかる計算量は $O(N^2)$ であり、三角行列を係数に持つ線形方程式を解くための計算量も同様に $O(N^2)$ であることから、計算量が $O(N^3)$ である逆行列を計算する方法より、効率的であることが分かる。

```python
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 1])
x = np.linalg.solve(A, b)  # array([-1, 1])
```

また、実用的には $\mathbf{Ax} = \mathbf{b}$ という線形方程式で、 $\mathbf{A}$ は変わらないけれども $\mathbf{b}$ が異なるような問題を繰り返し解きたい場合というのが多くある。このような場合`numpy.linalg.solve`の計算量が $O(N^2)$ であるとはいえ、内部でLU分解の計算を行っていることを考えると、繰り返し同じLU分解を解くことは無駄が多いことが分かるだろう。

このような場合、一度LU分解を計算してしまって、三角行列に対する線形問題を解く、という方法が考えられる。残念ながら、この方法はNumPyには実装されていないが類似ライブラリであるSciPyを用いると、以下の形で実現できる。

```python
import scipy as sp
import scipy.linalg

A = np.array([[1, 2], [3, 4]])
lu, piv = sp.linalg.lu_factor(A)
b1 = np.array([1, 1])
x1 = sp.linalg.lu_solve((lu, piv), b1)  # array([-1, 1])
b2 = np.array([2, 2])
x2 = sp.linalg.lu_solve((lu, piv), b2)  # array([-2, 2])
```

なお、上記のコードで`scipy.linalg.lu_factor`には2つの戻り値`lu`と、`piv`が帰ってくるが、通常、LU分解を上手く計算すると、上三角行列と下三角行列のうちのどちらかは対角成分が全て1になるようにできるので、その1となる対角成分を省略して1つの行列にまとめたものが`lu`である。

一方、`piv`はガウスの消去法などを用いて行列分解を行う際に、数値計算の誤差を減らすために行列の行や列の順序を入れ替える操作をすることがあるのだが、入れ替え前後の行、列の対応を表わす行列が`piv`である。このあたりの説明は数値計算のより専門的な教科書を読むなどして各自勉強してみてほしい。

---

#### 閑話休題: 線形方程式の解法における直接法と反復法

先ほど紹介した`numpy.linalg.solve`はLU分解を用いて線形問題を解いていると説明した。このように行列分解などを用いて、線形問題の解を行列のサイズのみに依存する計算量で得るような解法を**直接法**と呼ぶ。直接法にはLU分解を用いる方法の他、[QR分解](https://ja.wikipedia.org/wiki/QR%E5%88%86%E8%A7%A3)など、別の行列分解を用いる方法がある。

一方、ここでは紹介しなかったが、線形問題の両辺に特定の線形代数的操作を施すことで、適当な $\mathbf{x}$ の初期値を徐々に線形問題の解に反復計算によって近づける方法を**反復法**と呼ぶ。反復法の中で最も単純なものはJacobi法がある (Jacobi法には固有値を求める手法などもありややこしい...)。Jacobi法は係数行列 $\mathbf{A}$ の対角成分だけを取りだした対角行列 $\mathbf{D}$を用いて、 $k$ 回反復時に得られている $\mathbf{x}^k$ を次の式で $\mathbf{x}^{k+1}$ に更新する。

$$
\mathbf{x}^{k+1} = \mathbf{D}^{-1} \left( \mathbf{b} - (\mathbf{A} - \mathbf{D}) \mathbf{x}^k \right)
$$

これ以外にも、Jacobi法を改良したGauss-Seidel法やSOR法がある他、実用的には[共役勾配法](https://ja.wikipedia.org/wiki/%E5%85%B1%E5%BD%B9%E5%8B%BE%E9%85%8D%E6%B3%95)と呼ばれる、より収束の早いアルゴリズムが用いられる。最も一般的な共役勾配法は対称正定値行列 (正定値 = 全ての固有値が0より大きい)にしか用いることができないが、これを非対称行列に拡張した双共役勾配法 (BiCG法)など、多くの発展的な手法が存在する。

---

### 行列の固有値・固有ベクトル


## 練習課題

1. 今回の講義で紹介したサンプルコードを踏まえて、正則行列に対する逆行列と、特異行列に対する疑似逆行列の違いと共通点について述べよ。
1. 逆行列を`numpy.linalg.inv`によって求めることで線形問題を解く方法と、`numpy.linalg.solve`を用いてLU分解により解を求める方法で計算時間がそれぞれ行列サイズの3乗、2乗に比例することを`numpy.random.random`を用いて作成したランダムな $\mathbf{A}$, $\mathbf{b}$ について調べよ。
1. 前述のヤコビ法により、正しく線形問題が解ける(= `numpy.linalg.solve`と解が一致)ことを調べよ。なお、ヤコビ法は優対角行列と呼ばれる対角成分が、各列の対角成分以外の成分の総和より大きい行列にしか用いることができないので、そのような行列を各自適当に設定すること。
1. NumPyには多項方程式を解くための関数として`numpy.roots`という関数が用意されている ([参考](https://numpy.org/doc/stable/reference/generated/numpy.roots.html)、特性方程式の係数は手計算で求めること)。この関数を用いて、以下の行列について、特性方程式を解くことで得られる固有値と、`numpy.linalg.eig`を解くことで得られる固有値が一致することを調べよ。
$$
\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 2 & 3 \\ 3 & 3 & 3 \end{pmatrix}
$$

