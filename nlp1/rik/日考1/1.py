# 1.完成以下操作（每小题10分）
# (1)矩阵创建
import tensorflow as tf
# ①创建一个维度为3*3的全1矩阵
ones=tf.ones(shape=(3,3))
print(ones)
# ②使用range，创建一个1-9的1阶张量
# ③打印上题的维度
range1_9=tf.range(1,10)
print(range1_9)
print(range1_9.shape)
# ④将上题维度修改为3,1,3
reshape_range1_9=tf.reshape(range1_9,(3,1,3))
print(reshape_range1_9)
# ⑤使用函数，去除维度中函数1的维度
range1_9=tf.squeeze(range1_9)
print(range1_9.shape)
# (2)切片及其他
# ①使用1-9的向量，使用切片，打印3,4,5,6
num_3456=range1_9[2:6]
print(num_3456)
# ②打印上题向量的均值
num_mean=tf.reduce_mean(num_3456)
print(num_mean)
# ③创见一个2行2列的标准正态分布矩阵
mean_2_2=tf.random.normal((2,2))
print(mean_2_2)
# ④创建一个2行2列的全0矩阵
zero_2_2=tf.zeros((2,2))
print(zero_2_2)
# ⑤将3,4问的结果拼接成一个4行2列的结果
cat_3_4=tf.concat((mean_2_2,zero_2_2),axis=0)
print(cat_3_4)

