## Layer Normalization

normalization的目的是将输入转化为均值为0方差为1的数据，缓解Internal Covariate Shift问题，可以**将数据分布拉到激活函数的非饱和区，具有权重/数据伸缩不变性的特点。起到缓解梯度消失/爆炸、加速训练、正则化的效果。**

LN与BN不同，Layer Normalization在每一个样本（单一样本）上计算均值和方差，然后做归一化，多用于RNN这种输入序列是变长的模型中，每一个时间步都有自己的分布。同一层的所有神经元具有相同的均值和方差。对于使用LN的RNNs，**每个时刻加权后的输入通过标准化被重新调整在合适的范围**，很大程度避免了梯度消失、梯度爆炸问题，隐藏状态的传递更加稳定。

**LN计算公式：**其中$\alpha$和$\beta$是可训练的模型参数，需要参与反向传播。
$$
LN(x_i)=\alpha*\frac{x_i-\mu_L}{\sqrt{(\sigma_L^2+\epsilon)}}+\beta
$$
**LN代码：**在x向量的隐层维度(hidden state)的方向上进行计算，得到$\mu$和$\sigma^2$。

```python
class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."

    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2

```

LN：适合用于RNN（**考虑句子长度信息**）以及单条训练样本，不关心batch_size。

## Batch Normalization

在CNN训练时，绝大多数都采用mini-batch使用随机梯度下降算法进行训练，那么随着输入数据的不断变化，以及网络中参数不断调整，**网络的各层输入数据的分布则会不断变化**。 机器学习领域有个很重要的假设：IID独立同分布假设，就是假设**训练数据和测试数据是满足相同分布**的，这是通过训练数据获得的模型能够在测试集获得好的效果的一个基本保障。**Internal Covariate Shift 问题就是说，在训练过程中，因为各层参数老在变，所以每个隐层都会面临covariate shift的问题，也就是在训练过程中，隐层的输入分布老是变来变去。**导致激活函数的输入绝对值大，使用sigmoid或tanh中模型中反向传播时低层网络梯度消失。**BN可以将输入强制拉回标准正态分布。**
*作者：阮恒链接：https://www.jianshu.com/p/d984b257a4b2来源：简书著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*

和LN的归一化方向不同，BN是在batch的方向上，对同一层的每一个神经元进行归一化，同一层的每个神经元具有不同的均值和方差，分别由一个batch上的样本数据在该位置上的值对应计算得到。（一层是指隐层向量维度）

BN中：如果batch_size过小，则缺少统计意义（难以反映全局信息），在batch_size较大时表现较好。