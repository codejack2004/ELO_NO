


def split_image(image, split_rows, split_cols):
        # 获取图片尺寸
        width, height = image.size
        # 计算每块的宽度和高度
        block_width = width // split_rows
        block_height = height // split_cols
        # 列表存储每块图片
        blocks = []
        # 切割图片
        for row in range(split_rows):
            for col in range(split_cols):
                left = col * block_width
                top = row * block_height
                right = left + block_width
                bottom = top + block_height

                # 根据计算好的坐标位置切割图片
                block = image.crop((left, top, right, bottom))
                blocks.append(block)
        return blocks