import os
import shutil

# 1. Cleanup: Remove legacy dist directory if it exists
if os.path.exists('dist'):
    shutil.rmtree('dist')

# 2. Define standard directory architecture
folders = ['assets/lineart', 'data/medium', 'docs', 'src']

# 3. Define files and their content (English standard)
files = {
    'src/printRenderer.js': '// CMS-004R-B1.5 - Vanilla Rendering Engine\n' +
                             'export function drawCombinedPlanPng() { console.log("Rendering engine active..."); return document.createElement("canvas"); }',
    'src/index.js': 'export { drawCombinedPlanPng } from "./printRenderer.js";',
    'src/interfaces.js': 'export class PaletteRenderContext { constructor(palette = []) { this.palette = palette; } }',
    'index.html': '''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Coloring Studio (CS)</title></head>
<body>
    <h1>CS Production Engine</h1>
    <button id="run">Execute RC1</button>
    <script type="module">
        import { drawCombinedPlanPng } from './src/printRenderer.js';
        document.getElementById('run').addEventListener('click', async () => {
            const res = await fetch('./data/medium/Ohuhu_Master.xlsx');
            if(!res.ok) throw new Error("Failed to load Excel data");
            console.log("Data stream initialized.");
            const canvas = drawCombinedPlanPng();
            alert("RC1 Rendering Triggered");
        });
    </script>
</body>
</html>''',
    '.gitignore': '''# System files
.DS_Store
Thumbs.db

# Build artifacts and dependencies
dist/
__pycache__/
*.pyc

# Local environment
.env
.vscode/
'''
}

# 4. Establish file system structure
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 5. Generate files
for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)

print("Coloring Studio (CS) environment successfully established with .gitignore.")