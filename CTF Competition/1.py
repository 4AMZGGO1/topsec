import re
import os
import shutil

def replace_all_image_paths(md_file_path, output_file_path=None):
    current_directory = os.path.dirname(os.path.abspath(md_file_path))

    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 匹配 Markdown 图片 ![xxx](path)
    md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    md_matches = md_pattern.findall(md_content)

    # 匹配 HTML 图片 <img src="path">
    html_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']')
    html_matches = html_pattern.findall(md_content)

    all_matches = set(md_matches + html_matches)  # 去重

    if not all_matches:
        print("⚠️ 没有找到图片路径")
        return

    for match in all_matches:
        normalized_path = match.replace('\\', '/')
        image_file_name = os.path.basename(normalized_path)
        old_image_path = os.path.normpath(normalized_path)
        new_image_path = os.path.join(current_directory, image_file_name)

        # 尝试复制图片
        if os.path.exists(old_image_path):
            try:
                if not os.path.exists(new_image_path):
                    shutil.copy2(old_image_path, new_image_path)
                    print(f"✅ 复制: {old_image_path} → {image_file_name}")
            except Exception as e:
                print(f"❌ 复制失败: {old_image_path} → {e}")
        else:
            print(f"⚠️ 图片文件不存在: {old_image_path}")

        # 替换 Markdown 和 HTML 中的路径为仅文件名
        md_content = re.sub(
            rf'(!\[.*?\]\(){re.escape(match)}(\))',
            rf'\1{image_file_name}\2',
            md_content
        )
        md_content = re.sub(
            rf'(<img\s+[^>]*src=["\']){re.escape(match)}(["\'])',
            rf'\1{image_file_name}\2',
            md_content
        )

    # 保存
    if output_file_path is None:
        output_file_path = md_file_path

    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        out_file.write(md_content)

    print(f"\n🎉 路径替换完成，输出文件：{output_file_path}")

# 执行
replace_all_image_paths('第一次ctf的wp.md')
