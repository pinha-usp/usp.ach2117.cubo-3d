# USP - ACH2117 - Cubo 3D

> Implementação de um cubo 3D em movimentação utilizando OpenGL

O cubo foi implementado utilizando as bibliotecas [moderngl](https://github.com/moderngl/moderngl) e [moderngl_window](https://github.com/moderngl/moderngl_window)

A partir da posição inicial com centro no vértice `(0,0,0)` e tamanho de aresta `1`, foram aplicadas rotações e translações para a movimentação e posição do
cubo. Também foi utilizada uma textura no formato de uma caixa em cada face do cubo

Para fazer os cálculos de rotação, translação e projeção perspectiva, a biblioteca [PyGLM](https://github.com/Zuzu-Typ/PyGLM) foi utilizada

<div align="center">
  <img src="https://github.com/willpinha/usp.ach2117.cubo-3d/assets/86596621/fc785551-679e-4c6d-a165-9a6e6bccbe19">
</div>

## Como executar?

Instale as dependências do projeto:

```
python install -r requirements.txt
```

Após, é só rodar o script principal:

```
python main.py
```

> **Warning**
> A versão Python 3.10 foi utilizada

> **Note**
> A tela ficará em fullscreen. Para sair do programa, basta apertar <kbd>ESC</kbd>
