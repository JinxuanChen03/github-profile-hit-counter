import os
from PIL import Image
import io

# 读取当前计数
if os.path.exists('counter.txt'):
    with open('counter.txt', 'r') as f:
        count = int(f.read().strip())
else:
    count = 0

# 更新计数
count += 1

# 保存新的计数
with open('counter.txt', 'w') as f:
    f.write(str(count))

# 生成计数图片
count_str = str(count)
digit_images = [Image.open(f'assets/themes/test/{digit}.png') for digit in count_str]

width = sum(img.width for img in digit_images)
height = max(img.height for img in digit_images)

combined_image = Image.new('RGBA', (width, height))

x_offset = 0
for img in digit_images:
    combined_image.paste(img, (x_offset, 0))
    x_offset += img.width

combined_image.save('hit_counter.png')
