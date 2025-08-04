import re
import os
import shutil

def replace_all_image_paths(md_file_path, output_file_path=None):
    current_directory = os.path.dirname(os.path.abspath(md_file_path))

    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 匹配 Markdown 和 HTML 图片路径
    md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    html_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']')

    md_matches = md_pattern.findall(md_content)
    html_matches = html_pattern.findall(md_content)

    all_matches = set(md_matches + html_matches)

    if not all_matches:
        print("⚠️ 没有找到图片路径")
        return

    for match in all_matches:
        original_path_in_md = match
        normalized_path = match.replace('\\', '/')
        image_file_name = os.path.basename(normalized_path)
        old_image_path = os.path.normpath(normalized_path)
        new_image_path = os.path.join(current_directory, image_file_name)

        # 复制图片到当前目录
        if os.path.exists(old_image_path):
            try:
                if not os.path.exists(new_image_path):
                    shutil.copy2(old_image_path, new_image_path)
                    print(f"✅ 已复制图片: {image_file_name}")
            except Exception as e:
                print(f"❌ 复制失败: {old_image_path} → {e}")
        else:
            print(f"⚠️ 图片文件不存在: {old_image_path}")

        # 强行替换原路径字符串（无论 \ 还是 /）
        if original_path_in_md in md_content:
            md_content = md_content.replace(original_path_in_md, image_file_name)
            print(f"🔁 替换路径: {original_path_in_md} → {image_file_name}")
        else:
            print(f"❌ 没找到要替换的路径: {original_path_in_md}")

    # 保存结果
    if output_file_path is None:
        output_file_path = md_file_path

    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        out_file.write(md_content)

    print(f"\n🎉 路径替换完成，输出文件：{output_file_path}")

# 执行
replace_all_image_paths('第一次ctf的wp.md')
