const path = require('path');
const webpack = require('webpack');
module.exports = {
    entry: {
        main: path.resolve(__dirname, './index.ts')
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', 'js'],
    },
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, '../bff/static/js/')
    },
};

