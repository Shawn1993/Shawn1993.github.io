---
layout: post
title:  "Emergent Logical Structure in Vector Representations of Neural Readers"
date:   2016-11-29 13:31:01 +0800
categories: 论文阅读
tag: QA
---

* content
{:toc}

## 一、文章信息

### 作者
Hai Wang, Takeshi Onishi, Kevin Gimpel, David McAllester

### 单位
Toyota Technological Institute at Chicago

### 文章来源
[ICLR 2017 Submission](https://arxiv.org/abs/1611.07954)

## 二、文章内容

### 1 解决问题
本文中作者认为最近提出的各种attention based readers 可以分为两类，进行了全面的总结，并且作者从数学层面分析了两类Reader的相关性。

### 2 Aggregation Readers模型
这种Readers是最先出现的，包括Memory Networks，Attentive Reader，Stanford Reader等

#### 2.1 Stanford Reader

$$
\begin{align}
h&=\text{biLSTM}(e(p))\tag{1}\\
q&=[\text{fLSTM}(e(q))_{|q|},bLSTM(e(q))_1]\tag{2}\\
\end{align}
$$

$e(p)$表示paragraph的词向量$e(w_i)$序列，$w_i \in p$。
$e(q)$表示question的词向量序列。
biLSTM(s)表示双向LSTM的hidden state序列。
fLSTM(s)，bLSTM(s)分别表示前向LSTM和后向LSTM的hidden stae序列。
$[\cdot,\cdot]$表示concatenation。

接下来的可以看作是Attention机制：
$$
\begin{align}
\alpha_t &=\mathop{softmax}\limits_t\ h_t^TW_{\alpha}q\tag{3}\\
o &= \sum_t \alpha_t h_t\tag{4}\\
\end{align}
$$

a表示答案，q表示问题，p表示段落线索，$\mathcal{A}$表示问题候选集。

$$
\begin{align}
P(a\mid p,q,\mathcal{A}) &= \mathop{softmax}\limits_{a\in\mathcal{A}}\ e_o(a)^To\tag{5}\\
\hat{a} &=\mathop{argmax}\limits_{a\in\mathcal{A}}\ e_o(a)^To\tag{6}
\end{align}
$$

$e_o(a)$表示问题的output embedding，$e$和$e_o$属于不同的向量空间。

#### 2.2 Memory Network

$$
\begin{align}
h&=\text{biLSTM}(e(p))\tag{1}\\
q&=[\text{fLSTM}(e(q))_{|q|},bLSTM(e(q))_1]\tag{2}\\
\alpha_t &=\mathop{softmax}\limits_t\ h_t^TW_{\alpha}q\tag{3}\\
o &= \sum_t \alpha_t h_t\tag{4}\\
P(w\mid p,q,\mathcal{A}) &=P(w\mid p,q)= \mathop{softmax}\limits_{w\in\mathcal{V}}\ e_o(w)^To\tag{5}\\
\hat{a} &=\mathop{argmax}\limits_{w\in\mathcal{V}}\ e_o(w)^To\tag{6}
\end{align}
$$

跟Stanford Reader的区别就是最后求概率时，是求词表大小的概率分布，所以它将训练整个词表的output embedding。

#### 2.3 Attentive Reader 
Stanford Reader就是从Attentive Reader得来的。

$$
\begin{align}
h&=\text{biLSTM}(e(p)) \tag{1}\\
q&=[\text{fLSTM}(e(q))_{|q|},bLSTM(e(q))_1]\tag{2}\\
\alpha_t &=\mathop{softmax}\limits_t \text{MLP}([h_t,q])\tag{3}\\
o &= \sum_t \alpha_t h_t\tag{4}\\
P(w\mid p,q,\mathcal{A}) &=P(w\mid p,q)= \mathop{softmax}\limits_{w\in\mathcal{V}}\ e_o(w)^T\text{MLP}([o,q])\tag{5}\\
\hat{a} &=\mathop{argmax}\limits_{w\in\mathcal{V}}\ e_o(w)^To\tag{6}
\end{align}
$$

MLP是指多层感知器(multi layer perceptron)。在词表上预测结果，会使得在非匿名的数据集上的表现提高。

### 3 Explicit Reference Readers模型

#### 3.1 Attention-Sum Reader

$$
\begin{align}
h&=\text{biGRU}(e(p))\tag{1}\\
q&=[\text{fGRU}(e(q))_{|q|},bGRU(e(q))_1]\tag{2}\\
\alpha_t &=\mathop{softmax}\limits_t h_t^Tq\tag{3}\\
P(a\mid p,q,\mathcal{A}) &= \sum_{t\in R(a,p)}\alpha_t\tag{4}\\
\hat{a} &=\mathop{argmax}\limits_{a}\sum_{t\in R(a,p)} \alpha_t\tag{5}
\end{align}
$$

#### 3.2 Gated-Attention Reader
它有多层双向GRU。

$$
\begin{align}
q^\ell&=[\text{fGRU}(e(q))_{|q|},bGRU(e(q))_1]\ 1\leq\ell\leq K \tag{1}\\
h^1&=\text{biGRU}(e(p))\tag{2}\\
h^\ell&= \text{biGRU}(h^{\ell-1}\odot q^{\ell-1})2\leq\ell\leq K\tag{3}\\
\alpha_t &=\mathop{softmax}\limits_t (h_t^K)^Tq^K\tag{4}\\
P(a\mid p,q,\mathcal{A}) &= \sum_{t\in R(a,p)}\alpha_t\tag{5}\\
\hat{a} &=\mathop{argmax}\limits_{a}\sum_{t\in R(a,p)} \alpha_t\tag{6}
\end{align}
$$

#### 3.3 Attenion-over-Attention Reader

$$
\begin{align*}
h & = \text{biGRU}(e(p)) &q&=\text{biGRU}(e(q))\\
\alpha_{t,j} &= softmax_t\ h_t^Tq_j &\beta_{t,j}  &= softmax_j h_t^Tq^j\\
\beta_j&=\frac{1}{|p|}\sum_t\beta_{t,j} &\alpha_t&=\sum_j\beta_j\alpha_{t,j}\\
P(a\mid p,q,\mathcal{A}) &= \sum_{t\in R(a,p)}\alpha_t &\hat{a} &=\mathop{argmax}\limits_{a}\sum_{t\in R(a,p)} \alpha_t
\end{align*}
$$

使用更精密的方法计算attention，$q_j$表示双向GRU的hiddent state序列中的第$j$个向量。

### 4 两种readers的相似性
aggregation readers在匿名化的数据中表现的也不错，所以我们猜想aggregation readers中的$o$包含了一定的pointer信息，作者认为$h_t$和$e_o(a)$有以下关系：

$$
e_o(a)^Th_t = \left\{\begin{array}{l}
\ c\ \ \text{if}\ t\in R(a,p)\\
\ 0\ \ \text{otherwise}
\end{array}\right.
$$

如果满足上述关系就会推出两种readers是等价的：

$$
\begin{align*}
\mathop{\text{argmax}}_a e_0(a)^To &= \mathop{\text{argmax}}_a e_o(a)^T\sum_t \alpha_th_t\\
&=\mathop{\text{argmax}}_a\sum_t\alpha_te_o(a)^Th_t = \mathop{\text{argmax}}_a \sum_{t\in R(a,p)}\alpha_t
\end{align*}
$$

同时作者也用数据来证明了这种猜想：
![](http://oddpnmpll.bkt.clouddn.com/2016-11-29-085545.jpg)

作者还认为attention $\alpha_t$和匿名化后的ID顺序无关，两个具有不同ID顺序的相同文档，应该具有相同的attention，$q^Th_t=q^Th_t^{'}$。因此认为$h_t$包含与ID相关的内容，也包含与ID无关的内容：

$$
q^T(h_i+e_o(a))=q^Th_{i\cdot}
$$

也就是等价于$q^Te_o(a)=0$，同时作者也用数据来证明了：
![](http://oddpnmpll.bkt.clouddn.com/2016-11-29-091617.jpg)

### 5 数据集
1. [CNN & DailyMail](http://cs.nyu.edu/~kcho/DMQA/)  
论文：[Teaching Machines to Read and Comprehend](https://arxiv.org/abs/1506.03340)  
数据来自CNN和Daily Mail新闻，文章中高亮显示而且挖空的就是问题。为了防止使用外界知识，将命名实体都用ID替换，给出答案候选集。

2. [Who-did-What(WDW)](https://tticnlp.github.io/who_did_what/)  
论文：[Who did What: A Large-Scale Person-Centered Cloze Dataset](http://aclweb.org/anthology/D/D16/D16-1241.pdf)  
数据来自LDC English Gigaword newswire corpus。该数据集为了防止文章摘要被使用，每一个问题都从两个独立的文章中生成，一篇用来做Context，一篇用来挖空作为问题。该数据集为了不像CNN&DailyMail那样将实体匿名，所有的问题都是人名实体。而且使用了一些简单的baselines来筛选掉那些容易解决的问题。

3. Children's Book Test(CBT)  
论文：[The goldilocks principle: Reading childrens books with explicit memory representations](https://arxiv.org/abs/1511.02301)  
数据来自一个儿童读物，每个问题都是从中挑选出21条连续的句子，将前20条作为Context，将第21条挖空作为问题。

4. [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)  
论文：[SQuAD: 100,000+ Questions for Machine Comprehension of Text](https://arxiv.org/abs/1606.05250)

5. [bAbI](http://fb.ai/babi)  
论文：[Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks](https://arxiv.org/abs/1502.05698)

### 6 相关论文
1. Stanford Reader  
[A Thorough Examination of the CNN/Daily Mail Reading Comprehension Task](https://arxiv.org/abs/1606.02858)
2. Memory Networks  
[End-To-End Memory Networks](https://arxiv.org/abs/1503.08895)
3. Attentive Networks  
[Teaching Machines to Read and Comprehend](https://arxiv.org/abs/1506.03340)
4. Attention-Sum Reader  
[Text Understanding with the Attention Sum Reader Network](https://arxiv.org/abs/1603.01547)
5. Gated-Attention Reader  
[Gated-Attention Readers for Text Comprehension](https://arxiv.org/abs/1606.01549)
6. Attention-over-Attention Reader  
[Attention-over-Attention Neural Networks for Reading Comprehension](https://arxiv.org/abs/1607.04423)

## 三、简评
在我看来这是一篇很全面的综述，作者全面总结了最近出现的各种Readers，对开展机器阅读方面的研究有一个很好的参考。但是我很好奇为什么这里没有提到Dynamic Memory Networks，但是我觉得不好归类吧，毕竟Dynamic Memory Networks的Answers是通过RNN来decode而得来的。

