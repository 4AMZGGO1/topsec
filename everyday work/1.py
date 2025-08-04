import os
import re
import shutil

def process_md_file(md_file_path, images_dir):
    # 读取md
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 匹配 Markdown 和 HTML
    md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    html_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']')

    md_matches = md_pattern.findall(md_content)
    html_matches = html_pattern.findall(md_content)

    all_matches = set(md_matches + html_matches)

    for match in all_matches:
        original_path = match
        normalized_path = match.replace('\\', '/')
        image_file_name = os.path.basename(normalized_path)

        # 源文件实际路径
        old_image_path = os.path.normpath(normalized_path)

        # 目标 images 文件夹中的新路径
        new_image_path = os.path.join(images_dir, image_file_name)

        # 确保 images 目录存在
        os.makedirs(images_dir, exist_ok=True)

        # 尝试复制
        if os.path.exists(old_image_path):
            try:
                if not os.path.exists(new_image_path):
                    shutil.copy2(old_image_path, new_image_path)
                    print(f"✅ 已复制 {image_file_name} 到 images/")
                else:
                    print(f"ℹ️ 已存在: images/{image_file_name}")
            except Exception as e:
                print(f"❌ 复制失败: {old_image_path} → {e}")
        else:
            print(f"⚠️ 未找到图片: {old_image_path}")

        # 替换路径为 images/xxx.png
        images_relative_path = os.path.join('images', image_file_name).replace('\\', '/')
        if original_path in md_content:
            md_content = md_content.replace(original_path, images_relative_path)
            print(f"🔁 修改路径: {original_path} → {images_relative_path}")
        else:
            print(f"❌ 路径在md中未找到: {original_path}")

    # 覆盖写回
    with open(md_file_path, 'w', encoding='utf-8') as out_file:
        out_file.write(md_content)
    print(f"🎉 处理完成：{md_file_path}\n")

def process_all_md_in_current_dir():
    current_dir = os.getcwd()
    images_dir = os.path.join(current_dir, 'images')

    md_files = [f for f in os.listdir(current_dir) if f.endswith('.md')]

    if not md_files:
        print("⚠️ 当前目录没有.md文件")
        return

    for md_file in md_files:
        process_md_file(md_file, images_dir)

if __name__ == "__main__":
    process_all_md_in_current_dir()
