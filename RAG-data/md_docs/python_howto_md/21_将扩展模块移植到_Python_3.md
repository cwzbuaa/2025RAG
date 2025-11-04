### 第1页

将扩展模块移植到 Python 3
对于将扩展模块移植到 Python 3，我们推荐下列资源：
Supporting Python 3: An in-depth guide 中的 Migrating C extensions 这一章，这本书介绍了如何
从 Python 2 迁移到 Python 3，包括指导读者如何移植扩展模块。
py3c 项目中的 Porting guide 提供了有关支持代码的指导性建议。
推荐的第三方工具 提供了对于 Python 的 C API 的进一步抽象。 扩展通常需要被重写以使用它们
中的某一个，而在此之后就可通过库来处理各种 Python 版本和实现之间的差异。

