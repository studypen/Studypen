/* eslint-disable*/
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack')
module.exports = {
  devtool: 'inline-source-map',
  entry: ['react-hot-loader/patch', "./src/index.tsx"],
  target: "web",
  mode: "development",
  optimization: {
    splitChunks: { chunks: "all" }
  },
  output: {
    publicPath: 'http://localhost:9000/static/',
    // publicPath: 'static/',
    path: path.resolve(__dirname, "build", "static"),
    filename: "js/[name].js", //"js/[name].[chunkhash:8].js",
    chunkFilename: "js/[name].chunk.js",//"js/[name].[chunkhash:8].chunk.js",
  },
  resolve: {
    alias: {
      "react-dom": "@hot-loader/react-dom",
    },
  },
  devServer: {
    historyApiFallback: true,
    // for assets not handled by webpack
    // port should be different from the one you use to run Django
    port: 9000,

    hot:true,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },

  },
  resolve: {
    extensions: [".js", ".jsx", ".json", ".ts", ".tsx"],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: "babel-loader",
        exclude: /node_modules/,
        options: {
          cacheDirectory: true,
        }
      },
      {
        enforce: "pre",
        test: /\.js$/,
        loader: "source-map-loader",
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          'style-loader',
          "css-loader",
          "sass-loader",
        ],
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
            },
          },]
      },
    ],
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
};