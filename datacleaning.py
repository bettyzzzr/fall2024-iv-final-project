import pandas as pd

# 1. 加载 CSV 文件
file_path = "./15国碳排放.csv"  # 替换为实际的文件路径
data = pd.read_csv(file_path)

# 2. 检查空缺值
# 检查每列的空缺值总数
missing_values = data.isnull().sum()
print("每列空缺值总数：")
print(missing_values)

# 查找包含空缺值的行
rows_with_missing = data[data.isnull().any(axis=1)]
print("包含空缺值的行：")
print(rows_with_missing)

# 3. 处理空缺值
# (a) 删除包含空缺值的行
data_without_missing = data.dropna()
print("删除缺失值后的数据：")
print(data_without_missing)

# (b) 删除包含空缺值的列
data_without_missing_columns = data.dropna(axis=1)
print("删除缺失值列后的数据：")
print(data_without_missing_columns)

# (c) 用特定值填充空缺值（例如，填充为 0）
data_filled_with_zero = data.fillna(0)
print("用 0 填充后的数据：")
print(data_filled_with_zero)

# (d) 用列的平均值填充空缺值
data_filled_with_mean = data.fillna(data.mean())
print("用列平均值填充后的数据：")
print(data_filled_with_mean)

# 4. 保存处理后的数据（可选）
output_path = "./cleaned_data.csv"  # 替换为保存路径
data_without_missing.to_csv(output_path, index=False)
print(f"清理后的数据已保存至 {output_path}")
