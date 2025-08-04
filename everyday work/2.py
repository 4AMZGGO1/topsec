import os
import re
import shutil
import urllib.parse

def fix_md_image_paths_in_dir():
    current_dir = os.getcwd()
    image_output_dir = os.path.join(current_dir, 'images')

    # 确保 images 文件夹存在
    os.makedirs(image_output_dir, exist_ok=True)

    # 遍历所有 .md 文件
    md_files = [f for f in os.listdir(current_dir) if f.endswith('.md')]

    if not md_files:
        print("⚠️ 当前目录没有 Markdown 文件")
        return

    for md_file in md_files:
        md_path = os.path.join(current_dir, md_file)
        print(f"\n📝 处理文件: {md_file}")

        with open(md_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 匹配 Markdown 和 HTML 图片路径
        md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
        html_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']')
        paths = set(md_pattern.findall(content) + html_pattern.findall(content))

        for original_path in paths:
            # 解码 URL 编码，例如 %5C → \
            decoded_path = urllib.parse.unquote(original_path)
            normalized_path = decoded_path.replace('\\', '/')
            image_file_name = os.path.basename(normalized_path)

            # 绝对路径推导
            if os.path.isabs(normalized_path):
                source_path = normalized_path
            else:
                source_path = os.path.join(current_dir, normalized_path)

            # 目标路径：images/文件名
            target_path = os.path.join(image_output_dir, image_file_name)

            # 复制图片
            if os.path.exists(source_path):
                try:
                    shutil.copy2(source_path, target_path)
                    print(f"✅ 复制图片: {source_path} → images/{image_file_name}")
                except Exception as e:
                    print(f"❌ 复制失败: {e}")
            else:
                print(f"⚠️ 图片文件不存在: {source_path}")

            # 替换 Markdown 中路径为 images/xxx.png
            new_rel_path = f'images/{image_file_name}'
            content = content.replace(original_path, new_rel_path)
            print(f"🔁 替换路径: {original_path} → {new_rel_path}")

        # 保存结果
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"🎉 完成更新: {md_file}")

# 执行函数
if __name__ == "__main__":
    fix_md_image_paths_in_dir()
