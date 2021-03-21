/* eslint-disable*/
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: "./src/index.tsx",
  target: "web",
  mode: "development",
  output: {
    publicPath: 'http://localhost:9000/static/',
    // publicPath: 'static/',
    path: path.resolve(__dirname, "build", "static"),
    filename: "js/[name].[chunkhash:8].js",
    chunkFilename: "js/[name].[chunkhash:8].chunk.js",
  },
  devServer: {
    // for assets not handled by webpack
    // port should be different from the one you use to run Django
    port: 9000,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    // gzip everything served by dev server, could speed things up a bit
    // compress: true,
    // HMR
    // writeToDisk: true,
    injectHot: true,
    hot: true
  },
  resolve: {
    extensions: [".js", ".jsx", ".json", ".ts", ".tsx"],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: "awesome-typescript-loader",
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
    // new HtmlWebpackPlugin({
    //   inject: true,
    //   filename: path.resolve(__dirname, "build", "index.html"),
    //   template: path.resolve(__dirname, "public", "index.html"),
    // }),

    new CopyWebpackPlugin({
      patterns: [
        { from: path.resolve(__dirname, 'public'), to: path.resolve(__dirname, 'build/static') },
      ]
    }),
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
};