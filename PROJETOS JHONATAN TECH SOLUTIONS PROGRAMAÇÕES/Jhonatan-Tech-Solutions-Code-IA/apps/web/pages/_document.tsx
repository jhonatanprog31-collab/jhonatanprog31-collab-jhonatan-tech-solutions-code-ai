import Document, { Html, Head, Main, NextScript } from 'next/document'

export default class MyDocument extends Document {
  render() {
    return (
      <Html lang="pt-BR">
        <Head>
          <meta charSet="utf-8" />
          <meta name="description" content="JHONATAN TECH SOLUTIONS CODE AI - Sistema IA Especializado em Engenharia de Software" />
          <meta name="theme-color" content="#0066cc" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}
