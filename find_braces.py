import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract script content
match = re.search(r'<script>([\s\S]*?)</script>', content)
if match:
    script = match.group(1)
    lines = script.split('\n')
    
    # Track braces per line
    brace_count = 0
    last_line_with_neg = None
    
    for i, line in enumerate(lines, 1):
        # Count { and }
        open_count = line.count('{')
        close_count = line.count('}')
        
        brace_count += open_count - close_count
        
        if brace_count < 0 and last_line_with_neg is None:
            last_line_with_neg = (i, line.strip()[:100], brace_count)
            
    print(f"Total braces: {script.count('{')} open, {script.count('}')} close")
    print(f"Final balance: {brace_count}")
    
    if last_line_with_neg:
        print(f"\n❌ First line with negative brace count:")
        print(f"   Line {last_line_with_neg[0]}: {last_line_with_neg[1]}")
        print(f"   Brace count: {last_line_with_neg[2]}")
