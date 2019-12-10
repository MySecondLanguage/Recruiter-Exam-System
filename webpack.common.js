const path = require('path');
const CleanWebpackPlugin  = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: {
    app: './client/index.js'
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: "./client/index.html",

    })
  ],
  output: {
    // bundle js fs files
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
      rules: [
          {
            test: /\.js$/,
            exclude: /node_modules/, //ignore bundling node_moduels
            use: {
              loader: "babel-loader"
            }
          },
          {
            test: /\.(css|scss)$/, //
            use: [
              {
                loader: "style-loader",
              },
              {
                loader: "css-loader",
              },
              {
                loader: "sass-loader",
              }
            ]
          },
      ]
  }
};