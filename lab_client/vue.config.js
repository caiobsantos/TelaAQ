const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? '/Painel/Comunicacao' : '/',
    configureWebpack: {
      optimization: {
        splitChunks: false,
        minimizer: [
          new TerserPlugin({
            terserOptions: {
              output: {
                comments: false,
              }
            }
          })
        ]
      },
      output: {
        filename: 'js/frontAQ.js'
      }
    },
    css: {
      extract: {
        filename: 'css/frontAQ.css',
      }
    },
    filenameHashing: false
  }