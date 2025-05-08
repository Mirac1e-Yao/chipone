def bin_to_txt(input_bin_file, output_txt_file):
    try:
        # 读取二进制文件
        with open(input_bin_file, "rb") as bin_file:
            binary_data = bin_file.read()

        # 将二进制数据转换为十六进制字符串（每字节两个字符）
        hex_text = binary_data.hex()

        # 按每两个字符分割（例如 "0A1B2C" → "0A 1B 2C"）
        formatted_hex = [hex_text[i:i+2] for i in range(0, len(hex_text), 2)]

        # 按每 16 个十六进制数换行
        with open(output_txt_file, "w") as txt_file:
            for i in range(0, len(formatted_hex), 16):
                line = " ".join(formatted_hex[i:i+16])  # 每行 16 个，用空格隔开
                txt_file.write(line + "\n")

        print(f"转换完成！结果已保存到: {output_txt_file}")

    except FileNotFoundError:
        print(f"文件未找到: {input_bin_file}")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")


# 输入和输出文件路径
input_bin_file = "C:\\Users\\67064\\Desktop\\logo_2023_05_10.bin"  # 替换为你的输入文件路径
output_txt_file = "C:\\Users\\67064\\Desktop\\output.txt"  # 替换为你的输出文件路径

# 调用函数进行转换
bin_to_txt(input_bin_file, output_txt_file)