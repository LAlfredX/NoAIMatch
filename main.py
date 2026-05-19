
import os
import sys
import argparse
from datetime import datetime
from itertools import combinations
from image_processor import compare_images, get_similarity_label

# Language translations
TRANSLATIONS = {
    'en': {
        'title': 'NoAIMatch - Pure Hard-Coded Image Similarity Comparison',
        'select_lang': 'Please select your language:',
        'lang_options': '1. English\n2. 中文',
        'menu_title': 'Menu',
        'list_sets': '1. List available test sets',
        'run_compare': '2. Select test set to compare',
        'create_set': '3. Create new test set',
        'exit': '4. Exit',
        'select_operation': 'Please select operation (1-4): ',
        'available_sets': 'Available Test Sets',
        'no_sets': 'No test sets available!',
        'add_images': 'Please add images to test_images/ directory, or create a subdirectory.',
        'create_title': 'Create New Test Set',
        'enter_name': 'Enter test set name: ',
        'name_empty': 'Test set name cannot be empty!',
        'root_reserved': "'root' is a reserved name, cannot use!",
        'already_exists': 'Test set already exists!',
        'dir_created': 'Test set directory created: ',
        'copy_images': 'Copy images from test_images/ root directory? (y/n): ',
        'copied_count': 'Copied {} images to new test set!',
        'created_success': 'Test set created successfully!',
        'run_now': 'Run comparison now? (y/n): ',
        'select_set': 'Please select test set number: ',
        'invalid_number': 'Please enter a valid number!',
        'invalid_choice': 'Invalid choice! Please enter 1-4.',
        'bye': 'Goodbye!',
        'comparison_title': 'Batch Comparison Mode',
        'test_set': 'Test Set',
        'image_count': 'Image Count',
        'comparison_count': 'Comparison Count',
        'image_list': 'Image List',
        'img1': 'Image 1',
        'img2': 'Image 2',
        'similarity': 'Similarity',
        'rating': 'Rating',
        'set_not_exist': 'Error: Test set does not exist!',
        'path_expected': 'Expected path: ',
        'no_images': 'Error: No images found in test set!',
        'stats_title': 'Statistics',
        'avg_sim': 'Average Similarity: ',
        'max_sim': 'Highest Similarity: ',
        'min_sim': 'Lowest Similarity: ',
        'complete': 'Comparison Complete!',
        'saved_to': 'Results saved to: ',
        'factor_breakdown': 'Factor Breakdown'
    },
    'zh': {
        'title': 'NoAIMatch - 纯硬编码图像相似度比对系统',
        'select_lang': '请选择你的语言：',
        'lang_options': '1. English\n2. 中文',
        'menu_title': '菜单',
        'list_sets': '1. 列出可用测试集',
        'run_compare': '2. 选择测试集进行比较',
        'create_set': '3. 创建新测试集',
        'exit': '4. 退出',
        'select_operation': '请选择操作 (1-4)：',
        'available_sets': '可用的测试集',
        'no_sets': '没有找到可用的测试集！',
        'add_images': '请在 test_images/ 目录下添加图片，或创建子目录。',
        'create_title': '创建新测试集',
        'enter_name': '请输入测试集名称：',
        'name_empty': '测试集名称不能为空！',
        'root_reserved': "'root' 是保留名称，不能使用！",
        'already_exists': '测试集已存在！',
        'dir_created': '已创建测试集目录：',
        'copy_images': '是否从 test_images/ 根目录复制图片？ (y/n)：',
        'copied_count': '已复制 {} 张图片到新测试集！',
        'created_success': '测试集创建完成！',
        'run_now': '是否立即运行比较？ (y/n)：',
        'select_set': '请选择测试集编号：',
        'invalid_number': '请输入有效的数字！',
        'invalid_choice': '无效的选择！请输入 1-4。',
        'bye': '再见！',
        'comparison_title': '批量比较模式',
        'test_set': '测试集',
        'image_count': '图片数量',
        'comparison_count': '比较次数',
        'image_list': '图片列表',
        'img1': '图片1',
        'img2': '图片2',
        'similarity': '相似度',
        'rating': '评价',
        'set_not_exist': '错误：测试集不存在！',
        'path_expected': '期望路径：',
        'no_images': '错误：测试集中没有找到图片！',
        'stats_title': '统计信息',
        'avg_sim': '平均相似度：',
        'max_sim': '最高相似度：',
        'min_sim': '最低相似度：',
        'complete': '比较完成！',
        'saved_to': '结果已保存到：',
        'factor_breakdown': '因素分解'
    }
}

T = None

def get_test_set_path(test_set_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "test_images", test_set_name)

def list_image_files(directory):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    image_files = []
    
    if not os.path.exists(directory):
        return image_files
    
    for filename in sorted(os.listdir(directory)):
        if filename.lower().endswith(image_extensions):
            image_files.append(filename)
    
    return image_files

def log_message(log_file, message, also_print=True):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[{timestamp}] {message}"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')
    
    if also_print:
        print(log_line)

def list_available_test_sets():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_images_dir = os.path.join(base_dir, "test_images")
    
    if not os.path.exists(test_images_dir):
        return []
    
    test_sets = []
    
    root_images = list_image_files(test_images_dir)
    if root_images:
        test_sets.append(("root", len(root_images)))
    
    for item in sorted(os.listdir(test_images_dir)):
        item_path = os.path.join(test_images_dir, item)
        if os.path.isdir(item_path):
            image_files = list_image_files(item_path)
            test_sets.append((item, len(image_files)))
    
    return test_sets

def print_available_test_sets():
    test_sets = list_available_test_sets()
    
    print("\n" + "=" * 60)
    print(f"📁 {T['available_sets']}:")
    print("=" * 60)
    
    if not test_sets:
        print(f"  {T['no_sets']}")
        print(f"  {T['add_images']}")
    else:
        for i, (name, count) in enumerate(test_sets, 1):
            print(f"  {i}. {name} ({count} 张图片)")
    
    print("=" * 60 + "\n")

def create_test_set_interactive():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("\n" + "=" * 60)
    print(f"🆕 {T['create_title']}")
    print("=" * 60)
    
    test_set_name = input(f"\n{T['enter_name']}").strip()
    
    if not test_set_name:
        print(f"❌ {T['name_empty']}")
        return None
    
    if test_set_name == "root":
        print(f"❌ {T['root_reserved']}")
        return None
    
    test_set_dir = get_test_set_path(test_set_name)
    
    if os.path.exists(test_set_dir):
        print(f"❌ {T['already_exists']}")
        return None
    
    os.makedirs(test_set_dir, exist_ok=True)
    print(f"✅ {T['dir_created']}{test_set_dir}")
    
    copy_choice = input(f"\n{T['copy_images']}").strip().lower()
    
    if copy_choice == 'y':
        root_test_dir = os.path.join(base_dir, "test_images")
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
        copied = 0
        
        for filename in os.listdir(root_test_dir):
            if filename.lower().endswith(image_extensions):
                src = os.path.join(root_test_dir, filename)
                dst = os.path.join(test_set_dir, filename)
                if os.path.isfile(src):
                    import shutil
                    shutil.copy2(src, dst)
                    copied += 1
        
        print(f"✅ {T['copied_count'].format(copied)}")
    
    print(f"\n✅ {T['created_success']}")
    print(f"📂 {T['dir_created']}{test_set_dir}")
    
    return test_set_name

def get_similarity_label_translated(similarity, lang):
    if lang == 'en':
        if similarity >= 0.8:
            return "Highly Similar"
        elif similarity >= 0.6:
            return "Similar"
        elif similarity >= 0.4:
            return "Moderately Similar"
        elif similarity >= 0.3:
            return "Less Similar"
        else:
            return "Not Similar"
    else:
        return get_similarity_label(similarity)

def run_comparison(test_set_name, log_to_file=True):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    if test_set_name == "root":
        test_set_dir = os.path.join(base_dir, "test_images")
    else:
        test_set_dir = get_test_set_path(test_set_name)
    
    if not os.path.exists(test_set_dir):
        print(f"❌ {T['set_not_exist']}")
        print(f"   {T['path_expected']}{test_set_dir}")
        return False
    
    image_files = list_image_files(test_set_dir)
    
    if not image_files:
        print(f"❌ {T['no_images']}")
        return False
    
    log_file = None
    if log_to_file:
        timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"comparison_result_{test_set_name}_{timestamp_str}.log"
        log_file = os.path.join(base_dir, log_filename)
        if os.path.exists(log_file):
            os.remove(log_file)
    
    print("\n" + "=" * 120)
    print(f"📊 {T['title']} - {T['comparison_title']}")
    print("=" * 120)
    print(f"🎯 {T['test_set']}: {test_set_name}")
    print(f"📝 {T['image_count']}: {len(image_files)}")
    print(f"🔢 {T['comparison_count']}: {len(list(combinations(image_files, 2)))}")
    print("=" * 120)
    
    if log_file:
        log_message(log_file, "=" * 120, also_print=False)
        log_message(log_file, f"{T['title']} - {T['comparison_title']}", also_print=False)
        log_message(log_file, "=" * 120, also_print=False)
        log_message(log_file, f"{T['test_set']}: {test_set_name}", also_print=False)
        log_message(log_file, f"{T['image_count']}: {len(image_files)}", also_print=False)
        log_message(log_file, "=" * 120, also_print=False)
        log_message(log_file, "", also_print=False)
    
    print(f"\n📝 {T['image_list']}:")
    for i, img in enumerate(image_files, 1):
        print(f"  {i}. {img}")
        if log_file:
            log_message(log_file, f"Image {i}: {img}", also_print=False)
    
    results = []
    for img1_name, img2_name in combinations(image_files, 2):
        img1_path = os.path.join(test_set_dir, img1_name)
        img2_path = os.path.join(test_set_dir, img2_name)
        
        try:
            result = compare_images(img1_path, img2_path)
            similarity = result['similarity']
            label = get_similarity_label_translated(similarity, T['_lang'])
            
            factor_scores = result.get('factor_scores', {})
            
            # Print comparison with factor scores
            print("\n" + "-" * 120)
            print(f"{T['img1']}: {img1_name}")
            print(f"{T['img2']}: {img2_name}")
            print("-" * 120)
            print(f"  {T['similarity']}: {similarity * 100:>6.1f}% ({label})")
            print(f"\n  {T['factor_breakdown']}:")
            
            for factor_name, factor_score in factor_scores.items():
                print(f"    {factor_name:<45}: {factor_score * 100:>6.1f}%")
            
            if log_file:
                log_message(log_file, "-" * 120, also_print=False)
                log_message(log_file, f"{T['img1']}: {img1_name}", also_print=False)
                log_message(log_file, f"{T['img2']}: {img2_name}", also_print=False)
                log_message(log_file, "-" * 120, also_print=False)
                log_message(log_file, f"  {T['similarity']}: {similarity * 100:>6.1f}% ({label})", also_print=False)
                log_message(log_file, f"\n  {T['factor_breakdown']}:", also_print=False)
                for factor_name, factor_score in factor_scores.items():
                    log_message(log_file, f"    {factor_name:<45}: {factor_score * 100:>6.1f}%", also_print=False)
            
            results.append({
                'img1': img1_name,
                'img2': img2_name,
                'similarity': similarity,
                'label': label,
                'factor_scores': factor_scores
            })
            
        except Exception as e:
            error_text = "Error" if T['_lang'] == 'en' else "错误"
            print("\n" + "-" * 120)
            print(f"{T['img1']}: {img1_name}")
            print(f"{T['img2']}: {img2_name}")
            print(f"  {error_text}: {str(e)}")
            if log_file:
                log_message(log_file, "-" * 120, also_print=False)
                log_message(log_file, f"{T['img1']}: {img1_name}", also_print=False)
                log_message(log_file, f"{T['img2']}: {img2_name}", also_print=False)
                log_message(log_file, f"  {error_text}: {str(e)}", also_print=False)
    
    print("\n" + "-" * 120)
    
    if log_file:
        log_message(log_file, "", also_print=False)
        log_message(log_file, "-" * 120, also_print=False)
        
        log_message(log_file, f"\n📈 {T['stats_title']}:", also_print=False)
        avg_similarity = sum(r['similarity'] for r in results) / len(results) if results else 0
        log_message(log_file, f"{T['avg_sim']}{avg_similarity * 100:.1f}%", also_print=False)
        max_sim = max(results, key=lambda x: x['similarity']) if results else None
        min_sim = min(results, key=lambda x: x['similarity']) if results else None
        
        if max_sim:
            log_message(log_file, f"{T['max_sim']}{max_sim['similarity'] * 100:.1f}% ({max_sim['img1']} vs {max_sim['img2']})", also_print=False)
        if min_sim:
            log_message(log_file, f"{T['min_sim']}{min_sim['similarity'] * 100:.1f}% ({min_sim['img1']} vs {min_sim['img2']})", also_print=False)
        
        log_message(log_file, "", also_print=False)
        log_message(log_file, "=" * 120, also_print=False)
        log_message(log_file, f"{T['complete']}", also_print=False)
        log_message(log_file, "=" * 120, also_print=False)
        
        print(f"\n✅ {T['saved_to']}{log_file}")
    
    print("=" * 120)
    return True

def interactive_menu():
    while True:
        print("\n" + "=" * 60)
        print(f"🎯 {T['title']}")
        print("=" * 60)
        print(f"  {T['list_sets']}")
        print(f"  {T['run_compare']}")
        print(f"  {T['create_set']}")
        print(f"  {T['exit']}")
        print("=" * 60)
        
        choice = input(f"\n{T['select_operation']}").strip()
        
        if choice == "1":
            print_available_test_sets()
        
        elif choice == "2":
            test_sets = list_available_test_sets()
            
            if not test_sets:
                print(f"❌ {T['no_sets']}")
                continue
            
            print_available_test_sets()
            
            try:
                selection = int(input(f"{T['select_set']}")) - 1
                if 0 <= selection < len(test_sets):
                    test_set_name = test_sets[selection][0]
                    run_comparison(test_set_name, log_to_file=True)
                else:
                    print(f"❌ {T['invalid_choice']}")
            except ValueError:
                print(f"❌ {T['invalid_number']}")
        
        elif choice == "3":
            new_test_set = create_test_set_interactive()
            if new_test_set:
                run_choice = input(f"\n{T['run_now']}").strip().lower()
                if run_choice == 'y':
                    run_comparison(new_test_set, log_to_file=True)
        
        elif choice == "4":
            print(f"\n👋 {T['bye']}")
            break
        
        else:
            print(f"❌ {T['invalid_choice']}")

def main():
    global T
    
    parser = argparse.ArgumentParser(
        description="Pure Hard-Coded Image Similarity Comparison",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  python main.py                          # Interactive mode
  python main.py -l                       # List test sets
  python main.py -t small_test            # Run comparison
        """
    )
    
    parser.add_argument(
        "-t", "--testset",
        help="Specify test set name"
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all available test sets"
    )
    parser.add_argument(
        "-n", "--no-log",
        action="store_true",
        help="Don't save results to log file"
    )
    parser.add_argument(
        "-c", "--create",
        help="Create new test set"
    )
    
    args = parser.parse_args()
    
    if len(sys.argv) > 1:
        lang = 'en'
        T = TRANSLATIONS[lang]
        T['_lang'] = lang
    else:
        print("=" * 60)
        print("🌍 Language Selection")
        print("=" * 60)
        print("1. English")
        print("2. 中文")
        print("=" * 60)
        
        while True:
            lang_choice = input("\nPlease select language / 请选择语言 (1-2): ").strip()
            if lang_choice == "1":
                lang = 'en'
                break
            elif lang_choice == "2":
                lang = 'zh'
                break
            else:
                print("Invalid choice, please try again.")
        
        T = TRANSLATIONS[lang]
        T['_lang'] = lang
    
    if args.list:
        print_available_test_sets()
        return
    
    if args.create:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        test_set_name = args.create
        
        if test_set_name == "root":
            print(f"❌ {T['root_reserved']}")
            return
        
        test_set_dir = get_test_set_path(test_set_name)
        
        if os.path.exists(test_set_dir):
            print(f"❌ {T['already_exists']}")
            return
        
        os.makedirs(test_set_dir, exist_ok=True)
        print(f"✅ {T['dir_created']}{test_set_name}")
        print(f"📂 {T['dir_created']}{test_set_dir}")
        return
    
    if args.testset:
        success = run_comparison(args.testset, log_to_file=not args.no_log)
        return
    
    interactive_menu()

if __name__ == "__main__":
    main()

