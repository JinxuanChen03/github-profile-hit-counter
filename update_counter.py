import sqlite3
from PIL import Image

# 连接到 SQLite 数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('hit_counter.db')
cursor = conn.cursor()

# 创建计数器表（如果表不存在）
cursor.execute('''
CREATE TABLE IF NOT EXISTS counter (
    id INTEGER PRIMARY KEY,
    count INTEGER
)
''')

# 读取当前计数
cursor.execute('SELECT count FROM counter WHERE id = 1')
row = cursor.fetchone()
if row:
    count = row[0]
else:
    count = 0
    cursor.execute('INSERT INTO counter (id, count) VALUES (1, ?)', (count,))

# 更新计数
count += 1
cursor.execute('UPDATE counter SET count = ? WHERE id = 1', (count,))
conn.commit()

# 生成计数图片
count_str = str(count).zfill(8)  # 将计数转换为8位字符串，左侧补0
digit_images = [Image.open(f'assets/themes/test/{digit}.png') for digit in count_str]

width = sum(img.width for img in digit_images)
height = max(img.height for img in digit_images)

combined_image = Image.new('RGBA', (width, height))

x_offset = 0
for img in digit_images:
    combined_image.paste(img, (x_offset, 0))
    x_offset += img.width

combined_image.save('hit_counter.png')

# 关闭数据库连接
conn.close()