const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// 提供静态文件
app.use(express.static('public'));

app.get('/api/get-directory-structure', (req, res) => {
    const directoryPath = path.join(__dirname, 'public');
    const directoryStructure = getDirectoryStructure(directoryPath);
    res.json(directoryStructure);
});

function getDirectoryStructure(dir, level = 0) {
    if (level > 1) return [];
    const structure = [];
    const items = fs.readdirSync(dir);
    items.forEach(item => {
        const itemPath = path.join(dir, item);
        const stats = fs.statSync(itemPath);
        if (stats.isDirectory()) {
            structure.push({
                name: item,
                type: 'directory',
                path: itemPath.replace(__dirname, ''), // 相对路径
                children: getDirectoryStructure(itemPath, level + 1)
            });
        } else {
            structure.push({
                name: item,
                type: 'file',
                path: itemPath.replace(__dirname, '') // 相对路径
            });
        }
    });
    return structure;
}

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});