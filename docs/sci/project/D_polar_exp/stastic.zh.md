---
title: 统计
tag:
    - 统计
---


## 误差传递

假设有 $n$ 个随机变量 $\vec{x}$，服从某联合概率分布。若定义一个函数 $y = f(\vec{x})$，则 $y$ 的误差可以通过以下公式传递：

$$
\sigma_y^2 = \sum_{i=1}^n \left( \frac{\partial f}{\partial x_i} \right)^2 \sigma_{x_i}^2 + 2 \sum_{i=1}^n \sum_{j=i+1}^n \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} \text{Cov}(x_i, x_j)
$$

其中：

- $\sigma_y^2$ 是 $y$ 的方差；
- $\sigma_{x_i}^2$ 是 $x_i$ 的方差；
- $\text{Cov}(x_i, x_j)$ 是 $x_i$ 和 $x_j$ 的协方差；
- $\frac{\partial f}{\partial x_i}$ 是函数 $f$ 对 $x_i$ 的偏导数。

泰勒展开近似



假设 $f$ 是输入变量的平滑函数，可以对 $f$ 进行一阶泰勒展开近似：

 $$ f \approx f_0 + \sum_{i=1}^n \frac{\partial f}{\partial x_i} (x_i - x_{i,0}) $$ 
 
 其中：

$f_0$ 是 $f$ 在点 $(x_{1,0}, x_{2,0}, ..., x_{n,0})$ 的值；
$\frac{\partial f}{\partial x_i}$ 是 $f$ 对 $x_i$ 的偏导数。

1. 方差的定义

方差的定义为：
 $$ \text{Var}(f) = \mathbb{E}[(f - \mathbb{E}[f])^2] $$ 
 将 $f$ 的泰勒展开代入，忽略高阶项，得到： 
 
 $$ f - \mathbb{E}[f] \approx \sum_{i=1}^n \frac{\partial f}{\partial x_i} (x_i - \mathbb{E}[x_i]) $$

因此，$f$ 的方差可以近似为： 
$$ \text{Var}(f) \approx \text{Var}\left(\sum_{i=1}^n \frac{\partial f}{\partial x_i} (x_i - \mathbb{E}[x_i])\right) $$

2. 方差的性质

根据方差的性质，对于随机变量的线性组合：
 $$ \text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \text{Var}(X_i) + 2 \sum_{i=1}^n \sum_{j=i+1}^n a_i a_j \text{Cov}(X_i, X_j) $$ 
 其中 $a_i$ 是常数，$X_i$ 是随机变量。

在这里，令 $a_i = \frac{\partial f}{\partial x_i}$，$X_i = x_i - \mathbb{E}[x_i]$，代入后得到： 

$$ \text{Var}(f) \approx \sum_{i=1}^n \left( \frac{\partial f}{\partial x_i} \right)^2 \text{Var}(x_i) + 2 \sum_{i=1}^n \sum_{j=i+1}^n \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} \text{Cov}(x_i, x_j) $$


## 多项式分布的方差与协方差

对于多项式分布，假设有 $n$ 个类别，每个类别的概率为 $p_i$，其中 $i = 1, 2, ..., n$，且 $\sum_{i=1}^n p_i = 1$。若进行 $N$ 次独立试验，记每个类别的计数为 $X_i$，则随机向量 $\vec{X} = (X_1, X_2, ..., X_n)$ 服从多项式分布。

### 方差

多项式分布中，每个类别的计数 $X_i$ 的方差为：
$$
\text{Var}(X_i) = N p_i (1 - p_i)
$$

### 协方差

对于不同类别 $i$ 和 $j$，计数 $X_i$ 和 $X_j$ 的协方差为：
$$
\text{Cov}(X_i, X_j) = -N p_i p_j \quad (i \neq j)
$$



## 多项式分布近似为泊松分布或高斯分布

### 泊松分布近似

当试验次数 $N$ 很大且每个类别的概率 $p_i$ 很小（满足 $N p_i$ 为有限值）时，多项式分布中的每个类别计数 $X_i$ 可以近似为泊松分布，其参数为 $\lambda_i = N p_i$。即：
$$
X_i \sim \text{Poisson}(\lambda_i)
$$

#### 方差与标准差

在泊松分布中，每个类别计数 $X_i$ 的方差等于其均值 $\lambda_i$，即：
$$
\text{Var}(X_i) = \lambda_i
$$

标准差是方差的平方根，因此：
$$
\text{Std}(X_i) = \sqrt{\lambda_i}
$$

其中：
- $\lambda_i = N p_i$ 是泊松分布的参数；
- $N$ 是试验次数；
- $p_i$ 是类别 $i$ 的概率。


### 高斯分布近似

当试验次数 $N$ 很大且每个类别的概率 $p_i$ 不太小（满足 $N p_i (1 - p_i)$ 较大）时，多项式分布可以近似为高斯分布。随机向量 $\vec{X} = (X_1, X_2, ..., X_n)$ 的分布近似为多元高斯分布，其均值和协方差矩阵分别为：

- 均值向量：
$$
\mathbb{E}[\vec{X}] = (N p_1, N p_2, ..., N p_n)
$$

- 协方差矩阵：
$$
\text{Cov}(\vec{X}) = 
\begin{bmatrix}
N p_1 (1 - p_1) & -N p_1 p_2 & \cdots & -N p_1 p_n \\
-N p_2 p_1 & N p_2 (1 - p_2) & \cdots & -N p_2 p_n \\
\vdots & \vdots & \ddots & \vdots \\
-N p_n p_1 & -N p_n p_2 & \cdots & N p_n (1 - p_n)
\end{bmatrix}
$$

这种高斯分布近似在类别数较多且每个类别的概率 $p_i$ 不极端的情况下表现较好。






