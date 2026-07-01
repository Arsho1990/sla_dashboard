import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract script content
match = re.search(r'<script>([\s\S]*?)</script>', content)
if match:
    script = match.group(1)
    
    # Count braces and parens
    open_braces = script.count('{')
    close_braces = script.count('}')
    open_parens = script.count('(')
    close_parens = script.count(')')
    
    print(f'Script length: {len(script)} chars')
    print(f'Braces: {open_braces} open, {close_braces} close - {"OK" if open_braces == close_braces else "MISMATCH"}')
    print(f'Parens: {open_parens} open, {close_parens} close - {"OK" if open_parens == close_parens else "MISMATCH"}')
    
    # Check for function definitions
    funcs = re.findall(r'function (\w+)', script)
    print(f'\nFunctions found ({len(funcs)}): {funcs}')
