def process_txt_file(input_file, output_file, remove_strings):
    """
    处理文本文件，移除指定字符串，并将剩余数据按一行一个十六进制数排布。

    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :param remove_strings: 要移除的字符串列表
    """
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        buffer = ""  # 用于存储处理后的数据
        for line in infile:
            # 移除指定字符串
            for string in remove_strings:
                line = line.replace(string, "")
            buffer += line.strip()  # 去除行首尾空格并累积数据

        # 将数据按一行一个十六进制数排布
        for i in range(0, len(buffer), 2):  # 假设每个十六进制数占两位
            hex_number = buffer[i:i+2]
            if hex_number:  # 确保不为空
                outfile.write(hex_number + "\n")

# 输入文件路径
input_file = "C:\\Users\\67064\\Desktop\\1read-all-flash-ng.txt"
# 输出文件路径
output_file = "C:\\Users\\67064\\Desktop\\output.txt"
# 要移除的字符串
remove_strings = ["RFD #64","RFD = "," "]  # 替换为实际需要移除的字符串列表

# 调用函数处理文件
process_txt_file(input_file, output_file, remove_strings)

print(f"处理完成，结果已保存到 {output_file}")