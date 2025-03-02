const fs = require('fs');
const path = require('path');

const directoryPath = path.join(__dirname, 'public');
const outputFilePath = path.join(__dirname, 'public', 'directoryStructure.json');

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

const directoryStructure = getDirectoryStructure(directoryPath);
fs.writeFileSync(outputFilePath, JSON.stringify(directoryStructure, null, 2));

console.log('Directory structure has been generated.');