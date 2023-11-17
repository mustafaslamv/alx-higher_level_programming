#!/usr/bin/node
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];
const fs = require('fs');

const file1Content = fs.readFileSync(file1Path, 'utf8');
const file2Content = fs.readFileSync(file2Path, 'utf8');
const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destinationPath, concatenatedContent);
