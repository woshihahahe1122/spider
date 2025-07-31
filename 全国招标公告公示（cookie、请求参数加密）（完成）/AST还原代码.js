const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const types = require("@babel/types");
const generator = require("@babel/generator").default;

// 混淆的js代码文件
const encode_file = "./params参数解密.js";
// 反混淆的js代码文件
const decode_file = "./decode.js";
console.log(encode_file);

// 读取混淆的js文件
let jsCode = fs.readFileSync(encode_file, { encoding: "utf-8" });
// 将javascript代码转换为ast树(json结构)
let ast = parser.parse(jsCode);

// todo: 编写ast插件
const visitor = {
    ExpressionStatement(path) {
        console.log('hello');
    },

};

// 调用插件,处理混淆的代码
traverse(ast, visitor);

// 将处理后的ast转换为js代码(反混淆后的代码)
console.log(traverse(ast, visitor))