---
title: python 定义类
subtitle: 以lorentz vector为例
---

# LorentzVector 类的定义与用法

本例演示如何用 Python 定义一个四维动量（洛伦兹矢量）类，并实现常用的物理操作，如 boost（洛伦兹变换）、矢量加法、极角设置等。

## 1. 导入依赖

```python
import numpy as np
```

## 2. 定义 LorentzVector 类

```python
class LorentzVector:
    def __init__(self, px=0, py=0, pz=0, E=0):
        """
        初始化四维动量
        px, py, pz: 三维动量分量
        E: 能量
        """
        self.px = px
        self.py = py
        self.pz = pz
        self.E = E

    def __add__(self, other):
        """
        四维动量加法
        """
        return LorentzVector(
            self.px + other.px,
            self.py + other.py,
            self.pz + other.pz,
            self.E + other.E
        )

    def boost(self, beta_vec):
        """
        对四维动量进行洛伦兹变换（boost）
        beta_vec: 三维速度向量（单位c）
        """
        bx, by, bz = beta_vec
        b2 = bx**2 + by**2 + bz**2
        gamma = 1.0 / np.sqrt(1 - b2)
        bp = bx*self.px + by*self.py + bz*self.pz
        gamma2 = (gamma - 1.0)/b2 if b2 > 0 else 0.0

        # 变换后的分量
        px_ = self.px + gamma2*bp*bx + gamma*bx*self.E
        py_ = self.py + gamma2*bp*by + gamma*by*self.E
        pz_ = self.pz + gamma2*bp*bz + gamma*bz*self.E
        E_  = gamma*(self.E + bp)
        self.px, self.py, self.pz, self.E = px_, py_, pz_, E_

    def set_theta_phi(self, theta, phi):
        """
        设置极角（theta, phi），保持动量大小不变
        """
        p = np.sqrt(self.px**2 + self.py**2 + self.pz**2)
        self.px = p * np.sin(theta) * np.cos(phi)
        self.py = p * np.sin(theta) * np.sin(phi)
        self.pz = p * np.cos(theta)

    def p(self):
        """
        返回三维动量大小
        """
        return np.sqrt(self.px**2 + self.py**2 + self.pz**2)

    def __repr__(self):
        """
        打印四维动量信息
        """
        return f"LorentzVector(px={self.px}, py={self.py}, pz={self.pz}, E={self.E})"
```

## 3. 物理过程示例函数

下面以质心系与实验室系的四动量变换为例，演示如何使用 LorentzVector 类。

```python
def P_lab(theta_D_c, phi_D_c):
    """
    输入：D在质心系下的极角
    输出：D和质子在实验室系下的四动量
    """
    # 假设已知常量 mP, pD, ED
    # mP: 质子质量
    # pD: D三动量大小
    # ED: D能量

    # 初始四动量
    P_pro_lab_before = LorentzVector(0, 0, 0, mP)
    P_D_lab_before = LorentzVector(0, 0, pD, ED)
    P_total_lab = P_pro_lab_before + P_D_lab_before

    # boost到质心系
    beta_z = P_total_lab.pz / P_total_lab.E
    boost_vec = np.array([0, 0, beta_z])

    # 质心系下四动量
    P_pro_c = LorentzVector(P_pro_lab_before.px, P_pro_lab_before.py, P_pro_lab_before.pz, P_pro_lab_before.E)
    P_D_c = LorentzVector(P_D_lab_before.px, P_D_lab_before.py, P_D_lab_before.pz, P_D_lab_before.E)
    P_pro_c.boost(-boost_vec)
    P_D_c.boost(-boost_vec)

    # 旋转到指定极角
    P_pro_c.set_theta_phi(np.pi - theta_D_c, np.pi + phi_D_c)
    P_D_c.set_theta_phi(theta_D_c, phi_D_c)

    # boost回实验室系
    P_pro_c.boost(boost_vec)
    P_D_c.boost(boost_vec)

    return P_D_c, P_pro_c
```

## 4. 总结

本例展示了如何用 Python 类封装四维动量的常用操作，并结合物理过程进行实际应用。通过合理封装，可以极大提升代码的可读性和复用性。