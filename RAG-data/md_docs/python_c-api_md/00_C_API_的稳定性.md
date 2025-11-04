### 第1页

C API 的稳定性
除非另有文档说明，Python 的 C API 将遵循 PEP 387 所描述的向下兼容策略。 对它的大部分改变
都是源代码级兼容的（通常只会增加新的 new API）。 改变现有 API 或移除 API 只会在弃用期结束
之后或需修复严重问题时才会发生。
CPython 的应用程序二进制接口（ABI）可以跨微版本向上和向下兼容（在以相同方式编译的情况
下，参见下文 平台的考虑 一节）。 因此，针对 Python 3.10.0 编译的代码将适用于 3.10.8，反之亦
然，但对于 3.9.x 和 3.11.x 则需要单独编译。
存在具有不同稳定性预期的两个 C API 层次：
不稳定 API，可能在次要版本中发生改变而没有弃用期。 它的名称会以 PyUnstable 前缀来标
记。
受限 API，将会在多个次要版本间保持兼容。 当定义了 Py_LIMITED_API 时，将只有这个子集会
从 Python.h 对外公开。
这些将在下文中更详细地讨论。
带有一个下划线前缀的名称，如 _Py_InternalState，是可能不经通知就改变甚至是在补丁发布版
中改变的私有 API。 如果你需要使用这样的 API，请考虑联系 CPython 开发团队 来讨论为你的应用
场景添加公有 API。
不稳定 C API
任何名称带有 PyUnstable 前缀的 API 都将对外公开 CPython 的实现细节，并可能不加弃用警告即
在次要版本中发生改变（例如从 3.9 到 3.10）。 但是，它不会在问题修正发布版中改变（例如从
3.10.0 到 3.10.1）。
它通常是针对专门的，低层级的工具如调试器等。
使用此 API 的项目需要跟随 CPython 开发进程并花费额外的努力来适应改变。
应用程序二进制接口的稳定版
简单起见，本文档只讨论了 扩展，但受限 API 和稳定 ABI 对于 API 的所有用法都能发挥相同的作用
– 例如嵌入版的 Python 等。
受限 C API
Python 3.2 引入了 受限 API，它是 Python 的 C API 的子集。 只使用受限 API 的扩展可以一次编译即
可在多个 Python 版本上加载。 受限 API 内容 如下所示。
Py_LIMITED_API

### 第2页

请在包括 Python.h 之前定义这个宏以选择只使用受限 API，并选择受限 API 的版本。
将 Py_LIMITED_API 定义为对应于你的扩展所支持的最低 Python 版本的 PY_VERSION_HEX
值。 扩展将与从指定版本开始的所有 Python 3 发布版保持 ABI 兼容，并可使用到该版本为止
所引入的受限 API。
不直接使用 PY_VERSION_HEX 宏，而是碍编码一个最小的次要版本（例如 0x030A0000 表示
Python 3.10）以便在使用未来的 Python 版本进行编译时保持稳定。
你还可以将 Py_LIMITED_API 定义为 3。 其效果与 0x03020000 相同（即 Python 3.2，引入受
限 API 的版本）。
稳定 ABI
为启用此特性，Python 提供了一个 稳定 ABI:即一组将跨 Python 3.x 各个版本保持 ABI 兼容的符号集
合。
备注: 稳定 ABI 将防止多种 ABI 问题，如由于缺失符号导致的链接器错误或由于结构体布局或函
数签名中的变化导致的数据损坏。 不过，Python 中的其他修改可能改变扩展的 行为。 请参阅
Python 的向下兼容策略 (PEP 387) 了解详情。
稳定 ABI 包含在 受限 API 中对外公开的符号，但还包含其他符号 – 例如，为支持旧版本受限 API 所
需的函数。
在 Windows 上，使用稳定 ABI 的扩展应当被链接到 python3.dll 而不是版本专属的库如
python39.dll。
在某些平台上，Python 将查找并载入名称中带有 abi3 标签的共享库文件 (例如
mymodule.abi3.so)。 它不会检查这样的扩展是否兼容稳定 ABI。 使用方 (或其打包工具) 需要确保
这一些，例如，基于 3.10+ 受限 API 编译的扩展不可被安装于更低版本的 Python 中。
稳定 ABI 中的所有函数都会作为 Python 的共享库中的函数存在，而不仅是作为宏。 这使得它们可
以在不使用 C 预处理器的语言中使用。
受限 API 的作用域和性能
受限 API 的目标是允许使用在完整 C API 中可用的任何东西，但可能会有性能上的损失。
例如，虽然 PyList_GetItem() 是可用的，但其 “不安全的” 宏版本 PyList_GET_ITEM() 则是不可
用的。 这个宏的运行速度更快因为它可以利用版本专属的列表对象实现细节。
在未定义 Py_LIMITED_API 的情况下，某些 C API 函数将由宏来执行内联或替换。 定义
Py_LIMITED_API 会禁用这样的内联，允许提升 Python 的数据结构稳定性，但有可能降低性能。
通过省略 Py_LIMITED_API 定义，可以使基于版本专属的 ABI 来编译受限 API 扩展成为可能。 这能
提升其在相应 Python 版本上的性能，但也将限制其兼容性。 基于 Py_LIMITED_API 进行编译将产
生一个可在版本专属扩展不可用的场合分发的扩展 – 例如，针对即将发布的 Python 版本的预发布
包。

|  | 请在包括 Python.h 之前定义这个宏以选择只使用受限 API，并选择受限 API 的版本。
将 Py_LIMITED_API 定义为对应于你的扩展所支持的最低 Python 版本的 PY_VERSION_HEX
值。 扩展将与从指定版本开始的所有 Python 3 发布版保持 ABI 兼容，并可使用到该版本为止
所引入的受限 API。
不直接使用 PY_VERSION_HEX 宏，而是碍编码一个最小的次要版本（例如 0x030A0000 表示
Python 3.10）以便在使用未来的 Python 版本进行编译时保持稳定。
你还可以将 Py_LIMITED_API 定义为 3。 其效果与 0x03020000 相同（即 Python 3.2，引入受
限 API 的版本）。
稳定 ABI
为启用此特性，Python 提供了一个 稳定 ABI:即一组将跨 Python 3.x 各个版本保持 ABI 兼容的符号集
合。 |  |
| --- | --- | --- |
|  | 备注: 稳定 ABI 将防止多种 ABI 问题，如由于缺失符号导致的链接器错误或由于结构体布局或函
数签名中的变化导致的数据损坏。 不过，Python 中的其他修改可能改变扩展的 行为。 请参阅
Python 的向下兼容策略 (PEP 387) 了解详情。 |  |
|  | 稳定 ABI 包含在 受限 API 中对外公开的符号，但还包含其他符号 – 例如，为支持旧版本受限 API 所
需的函数。
在 Windows 上，使用稳定 ABI 的扩展应当被链接到 python3.dll 而不是版本专属的库如
python39.dll。
在某些平台上，Python 将查找并载入名称中带有 abi3 标签的共享库文件 (例如
mymodule.abi3.so)。 它不会检查这样的扩展是否兼容稳定 ABI。 使用方 (或其打包工具) 需要确保
这一些，例如，基于 3.10+ 受限 API 编译的扩展不可被安装于更低版本的 Python 中。
稳定 ABI 中的所有函数都会作为 Python 的共享库中的函数存在，而不仅是作为宏。 这使得它们可
以在不使用 C 预处理器的语言中使用。
受限 API 的作用域和性能
受限 API 的目标是允许使用在完整 C API 中可用的任何东西，但可能会有性能上的损失。
例如，虽然 PyList_GetItem() 是可用的，但其 “不安全的” 宏版本 PyList_GET_ITEM() 则是不可
用的。 这个宏的运行速度更快因为它可以利用版本专属的列表对象实现细节。
在未定义 Py_LIMITED_API 的情况下，某些 C API 函数将由宏来执行内联或替换。 定义
Py_LIMITED_API 会禁用这样的内联，允许提升 Python 的数据结构稳定性，但有可能降低性能。
通过省略 Py_LIMITED_API 定义，可以使基于版本专属的 ABI 来编译受限 API 扩展成为可能。 这能
提升其在相应 Python 版本上的性能，但也将限制其兼容性。 基于 Py_LIMITED_API 进行编译将产
生一个可在版本专属扩展不可用的场合分发的扩展 – 例如，针对即将发布的 Python 版本的预发布
包。 |  |

### 第3页

受限 API 警示
请注意使用 Py_LIMITED_API 进行编译 无法 完全保证代码能够兼容 受限 API 或 稳定 ABI。
Py_LIMITED_API 仅仅涵盖定义部分，但一个 API 还包括其他因素，如预期的语义等。
Py_LIMITED_API 不能处理的一个问题是附带在较低 Python 版本中无效的参数调用某个函数。 例
如，考虑一个接受 NULL 作为参数的函数。 在 Python 3.9 中，NULL 现在会选择一个默认行为，但在
Python 3.8 中，该参数将被直接使用，导致一个 NULL 引用被崩溃。 类似的参数也适用于结构体的
字段。
另一个问题是当定义了 Py_LIMITED_API 时某些结构体字段目前不会被隐藏，即使它们是受限 API
的一部分。
出于这些原因，我们建议用要支持的 所有 Python 小版本号来测试一个扩展，并最好是用其中 最低
的版本来编译它。
我们还建议查看所使用 API 的全部文档以检查其是否显式指明为受限 API 的一部分。 即使定义了
Py_LIMITED_API，少数私有声明还是会出于技术原因（或者甚至是作为程序缺陷在无意中）被暴露
出来。
还要注意受限 API 并不必然是稳定的：在 Python 3.8 上用 Py_LIMITED_API 编译扩展意味着该扩展
能在 Python 3.12 上运行，但它将不一定能用 Python 3.12 编译。 特别地，在稳定 ABI 保持稳定的情
况下，部分受限 API 可能会被弃用并被移除。
平台的考虑
ABI 的稳定性不仅取决于 Python，取决于所使用的编译器、低层级库和编译器选项等。 对于 稳定
ABI 的目标来说，这些细节定义了一个 “平台”。 它们通常会依赖于 OS 类型和处理器架构等。
确保在特定平台上的所有 Python 版本都以不破坏稳定 ABI 的方式构建是每个特定 Python 分发方的
责任。 来自 python.org 以及许多第三方分发商的 Windows 和 macOS 发布版都必于这种情况。
受限 API 的内容
目前 受限 API 包括下面这些项:
PY_VECTORCALL_ARGUMENTS_OFFSET
PyAIter_Check()
PyArg_Parse()
PyArg_ParseTuple()
PyArg_ParseTupleAndKeywords()
PyArg_UnpackTuple()
PyArg_VaParse()
PyArg_VaParseTupleAndKeywords()
PyArg_ValidateKeywordArguments()
PyBaseObject_Type

|  | 受限 API 警示
请注意使用 Py_LIMITED_API 进行编译 无法 完全保证代码能够兼容 受限 API 或 稳定 ABI。
Py_LIMITED_API 仅仅涵盖定义部分，但一个 API 还包括其他因素，如预期的语义等。
Py_LIMITED_API 不能处理的一个问题是附带在较低 Python 版本中无效的参数调用某个函数。 例
如，考虑一个接受 NULL 作为参数的函数。 在 Python 3.9 中，NULL 现在会选择一个默认行为，但在
Python 3.8 中，该参数将被直接使用，导致一个 NULL 引用被崩溃。 类似的参数也适用于结构体的
字段。
另一个问题是当定义了 Py_LIMITED_API 时某些结构体字段目前不会被隐藏，即使它们是受限 API
的一部分。
出于这些原因，我们建议用要支持的 所有 Python 小版本号来测试一个扩展，并最好是用其中 最低
的版本来编译它。
我们还建议查看所使用 API 的全部文档以检查其是否显式指明为受限 API 的一部分。 即使定义了
Py_LIMITED_API，少数私有声明还是会出于技术原因（或者甚至是作为程序缺陷在无意中）被暴露
出来。
还要注意受限 API 并不必然是稳定的：在 Python 3.8 上用 Py_LIMITED_API 编译扩展意味着该扩展
能在 Python 3.12 上运行，但它将不一定能用 Python 3.12 编译。 特别地，在稳定 ABI 保持稳定的情
况下，部分受限 API 可能会被弃用并被移除。
平台的考虑
ABI 的稳定性不仅取决于 Python，取决于所使用的编译器、低层级库和编译器选项等。 对于 稳定
ABI 的目标来说，这些细节定义了一个 “平台”。 它们通常会依赖于 OS 类型和处理器架构等。
确保在特定平台上的所有 Python 版本都以不破坏稳定 ABI 的方式构建是每个特定 Python 分发方的
责任。 来自 python.org 以及许多第三方分发商的 Windows 和 macOS 发布版都必于这种情况。
受限 API 的内容
目前 受限 API 包括下面这些项:
PY_VECTORCALL_ARGUMENTS_OFFSET
PyAIter_Check()
PyArg_Parse()
PyArg_ParseTuple()
PyArg_ParseTupleAndKeywords()
PyArg_UnpackTuple()
PyArg_VaParse()
PyArg_VaParseTupleAndKeywords()
PyArg_ValidateKeywordArguments()
PyBaseObject_Type |  |
| --- | --- | --- |

### 第4页

PyBool_FromLong()
PyBool_Type
PyBuffer_FillContiguousStrides()
PyBuffer_FillInfo()
PyBuffer_FromContiguous()
PyBuffer_GetPointer()
PyBuffer_IsContiguous()
PyBuffer_Release()
PyBuffer_SizeFromFormat()
PyBuffer_ToContiguous()
PyByteArrayIter_Type
PyByteArray_AsString()
PyByteArray_Concat()
PyByteArray_FromObject()
PyByteArray_FromStringAndSize()
PyByteArray_Resize()
PyByteArray_Size()
PyByteArray_Type
PyBytesIter_Type
PyBytes_AsString()
PyBytes_AsStringAndSize()
PyBytes_Concat()
PyBytes_ConcatAndDel()
PyBytes_DecodeEscape()
PyBytes_FromFormat()
PyBytes_FromFormatV()
PyBytes_FromObject()
PyBytes_FromString()
PyBytes_FromStringAndSize()
PyBytes_Repr()
PyBytes_Size()
PyBytes_Type
PyCFunction
PyCFunctionFast
PyCFunctionFastWithKeywords
PyCFunctionWithKeywords
PyCFunction_GetFlags()
PyCFunction_GetFunction()
PyCFunction_GetSelf()
PyCFunction_New()
PyCFunction_NewEx()
PyCFunction_Type
PyCMethod_New()

|  | PyBool_FromLong()
PyBool_Type
PyBuffer_FillContiguousStrides()
PyBuffer_FillInfo()
PyBuffer_FromContiguous()
PyBuffer_GetPointer()
PyBuffer_IsContiguous()
PyBuffer_Release()
PyBuffer_SizeFromFormat()
PyBuffer_ToContiguous()
PyByteArrayIter_Type
PyByteArray_AsString()
PyByteArray_Concat()
PyByteArray_FromObject()
PyByteArray_FromStringAndSize()
PyByteArray_Resize()
PyByteArray_Size()
PyByteArray_Type
PyBytesIter_Type
PyBytes_AsString()
PyBytes_AsStringAndSize()
PyBytes_Concat()
PyBytes_ConcatAndDel()
PyBytes_DecodeEscape()
PyBytes_FromFormat()
PyBytes_FromFormatV()
PyBytes_FromObject()
PyBytes_FromString()
PyBytes_FromStringAndSize()
PyBytes_Repr()
PyBytes_Size()
PyBytes_Type
PyCFunction
PyCFunctionFast
PyCFunctionFastWithKeywords
PyCFunctionWithKeywords
PyCFunction_GetFlags()
PyCFunction_GetFunction()
PyCFunction_GetSelf()
PyCFunction_New()
PyCFunction_NewEx()
PyCFunction_Type
PyCMethod_New() |  |
| --- | --- | --- |

### 第5页

PyCallIter_New()
PyCallIter_Type
PyCallable_Check()
PyCapsule_Destructor
PyCapsule_GetContext()
PyCapsule_GetDestructor()
PyCapsule_GetName()
PyCapsule_GetPointer()
PyCapsule_Import()
PyCapsule_IsValid()
PyCapsule_New()
PyCapsule_SetContext()
PyCapsule_SetDestructor()
PyCapsule_SetName()
PyCapsule_SetPointer()
PyCapsule_Type
PyClassMethodDescr_Type
PyCodec_BackslashReplaceErrors()
PyCodec_Decode()
PyCodec_Decoder()
PyCodec_Encode()
PyCodec_Encoder()
PyCodec_IgnoreErrors()
PyCodec_IncrementalDecoder()
PyCodec_IncrementalEncoder()
PyCodec_KnownEncoding()
PyCodec_LookupError()
PyCodec_NameReplaceErrors()
PyCodec_Register()
PyCodec_RegisterError()
PyCodec_ReplaceErrors()
PyCodec_StreamReader()
PyCodec_StreamWriter()
PyCodec_StrictErrors()
PyCodec_Unregister()
PyCodec_XMLCharRefReplaceErrors()
PyComplex_FromDoubles()
PyComplex_ImagAsDouble()
PyComplex_RealAsDouble()
PyComplex_Type
PyDescr_NewClassMethod()
PyDescr_NewGetSet()
PyDescr_NewMember()

|  | PyCallIter_New()
PyCallIter_Type
PyCallable_Check()
PyCapsule_Destructor
PyCapsule_GetContext()
PyCapsule_GetDestructor()
PyCapsule_GetName()
PyCapsule_GetPointer()
PyCapsule_Import()
PyCapsule_IsValid()
PyCapsule_New()
PyCapsule_SetContext()
PyCapsule_SetDestructor()
PyCapsule_SetName()
PyCapsule_SetPointer()
PyCapsule_Type
PyClassMethodDescr_Type
PyCodec_BackslashReplaceErrors()
PyCodec_Decode()
PyCodec_Decoder()
PyCodec_Encode()
PyCodec_Encoder()
PyCodec_IgnoreErrors()
PyCodec_IncrementalDecoder()
PyCodec_IncrementalEncoder()
PyCodec_KnownEncoding()
PyCodec_LookupError()
PyCodec_NameReplaceErrors()
PyCodec_Register()
PyCodec_RegisterError()
PyCodec_ReplaceErrors()
PyCodec_StreamReader()
PyCodec_StreamWriter()
PyCodec_StrictErrors()
PyCodec_Unregister()
PyCodec_XMLCharRefReplaceErrors()
PyComplex_FromDoubles()
PyComplex_ImagAsDouble()
PyComplex_RealAsDouble()
PyComplex_Type
PyDescr_NewClassMethod()
PyDescr_NewGetSet()
PyDescr_NewMember() |  |
| --- | --- | --- |

### 第6页

PyDescr_NewMethod()
PyDictItems_Type
PyDictIterItem_Type
PyDictIterKey_Type
PyDictIterValue_Type
PyDictKeys_Type
PyDictProxy_New()
PyDictProxy_Type
PyDictRevIterItem_Type
PyDictRevIterKey_Type
PyDictRevIterValue_Type
PyDictValues_Type
PyDict_Clear()
PyDict_Contains()
PyDict_Copy()
PyDict_DelItem()
PyDict_DelItemString()
PyDict_GetItem()
PyDict_GetItemRef()
PyDict_GetItemString()
PyDict_GetItemStringRef()
PyDict_GetItemWithError()
PyDict_Items()
PyDict_Keys()
PyDict_Merge()
PyDict_MergeFromSeq2()
PyDict_New()
PyDict_Next()
PyDict_SetItem()
PyDict_SetItemString()
PyDict_Size()
PyDict_Type
PyDict_Update()
PyDict_Values()
PyEllipsis_Type
PyEnum_Type
PyErr_BadArgument()
PyErr_BadInternalCall()
PyErr_CheckSignals()
PyErr_Clear()
PyErr_Display()
PyErr_DisplayException()
PyErr_ExceptionMatches()

|  | PyDescr_NewMethod()
PyDictItems_Type
PyDictIterItem_Type
PyDictIterKey_Type
PyDictIterValue_Type
PyDictKeys_Type
PyDictProxy_New()
PyDictProxy_Type
PyDictRevIterItem_Type
PyDictRevIterKey_Type
PyDictRevIterValue_Type
PyDictValues_Type
PyDict_Clear()
PyDict_Contains()
PyDict_Copy()
PyDict_DelItem()
PyDict_DelItemString()
PyDict_GetItem()
PyDict_GetItemRef()
PyDict_GetItemString()
PyDict_GetItemStringRef()
PyDict_GetItemWithError()
PyDict_Items()
PyDict_Keys()
PyDict_Merge()
PyDict_MergeFromSeq2()
PyDict_New()
PyDict_Next()
PyDict_SetItem()
PyDict_SetItemString()
PyDict_Size()
PyDict_Type
PyDict_Update()
PyDict_Values()
PyEllipsis_Type
PyEnum_Type
PyErr_BadArgument()
PyErr_BadInternalCall()
PyErr_CheckSignals()
PyErr_Clear()
PyErr_Display()
PyErr_DisplayException()
PyErr_ExceptionMatches() |  |
| --- | --- | --- |

### 第7页

PyErr_Fetch()
PyErr_Format()
PyErr_FormatV()
PyErr_GetExcInfo()
PyErr_GetHandledException()
PyErr_GetRaisedException()
PyErr_GivenExceptionMatches()
PyErr_NewException()
PyErr_NewExceptionWithDoc()
PyErr_NoMemory()
PyErr_NormalizeException()
PyErr_Occurred()
PyErr_Print()
PyErr_PrintEx()
PyErr_ProgramText()
PyErr_ResourceWarning()
PyErr_Restore()
PyErr_SetExcFromWindowsErr()
PyErr_SetExcFromWindowsErrWithFilename()
PyErr_SetExcFromWindowsErrWithFilenameObject()
PyErr_SetExcFromWindowsErrWithFilenameObjects()
PyErr_SetExcInfo()
PyErr_SetFromErrno()
PyErr_SetFromErrnoWithFilename()
PyErr_SetFromErrnoWithFilenameObject()
PyErr_SetFromErrnoWithFilenameObjects()
PyErr_SetFromWindowsErr()
PyErr_SetFromWindowsErrWithFilename()
PyErr_SetHandledException()
PyErr_SetImportError()
PyErr_SetImportErrorSubclass()
PyErr_SetInterrupt()
PyErr_SetInterruptEx()
PyErr_SetNone()
PyErr_SetObject()
PyErr_SetRaisedException()
PyErr_SetString()
PyErr_SyntaxLocation()
PyErr_SyntaxLocationEx()
PyErr_WarnEx()
PyErr_WarnExplicit()
PyErr_WarnFormat()
PyErr_WriteUnraisable()

|  | PyErr_Fetch()
PyErr_Format()
PyErr_FormatV()
PyErr_GetExcInfo()
PyErr_GetHandledException()
PyErr_GetRaisedException()
PyErr_GivenExceptionMatches()
PyErr_NewException()
PyErr_NewExceptionWithDoc()
PyErr_NoMemory()
PyErr_NormalizeException()
PyErr_Occurred()
PyErr_Print()
PyErr_PrintEx()
PyErr_ProgramText()
PyErr_ResourceWarning()
PyErr_Restore()
PyErr_SetExcFromWindowsErr()
PyErr_SetExcFromWindowsErrWithFilename()
PyErr_SetExcFromWindowsErrWithFilenameObject()
PyErr_SetExcFromWindowsErrWithFilenameObjects()
PyErr_SetExcInfo()
PyErr_SetFromErrno()
PyErr_SetFromErrnoWithFilename()
PyErr_SetFromErrnoWithFilenameObject()
PyErr_SetFromErrnoWithFilenameObjects()
PyErr_SetFromWindowsErr()
PyErr_SetFromWindowsErrWithFilename()
PyErr_SetHandledException()
PyErr_SetImportError()
PyErr_SetImportErrorSubclass()
PyErr_SetInterrupt()
PyErr_SetInterruptEx()
PyErr_SetNone()
PyErr_SetObject()
PyErr_SetRaisedException()
PyErr_SetString()
PyErr_SyntaxLocation()
PyErr_SyntaxLocationEx()
PyErr_WarnEx()
PyErr_WarnExplicit()
PyErr_WarnFormat()
PyErr_WriteUnraisable() |  |
| --- | --- | --- |

### 第8页

PyEval_AcquireThread()
PyEval_EvalCode()
PyEval_EvalCodeEx()
PyEval_EvalFrame()
PyEval_EvalFrameEx()
PyEval_GetBuiltins()
PyEval_GetFrame()
PyEval_GetFrameBuiltins()
PyEval_GetFrameGlobals()
PyEval_GetFrameLocals()
PyEval_GetFuncDesc()
PyEval_GetFuncName()
PyEval_GetGlobals()
PyEval_GetLocals()
PyEval_InitThreads()
PyEval_ReleaseThread()
PyEval_RestoreThread()
PyEval_SaveThread()
PyExc_ArithmeticError
PyExc_AssertionError
PyExc_AttributeError
PyExc_BaseException
PyExc_BaseExceptionGroup
PyExc_BlockingIOError
PyExc_BrokenPipeError
PyExc_BufferError
PyExc_BytesWarning
PyExc_ChildProcessError
PyExc_ConnectionAbortedError
PyExc_ConnectionError
PyExc_ConnectionRefusedError
PyExc_ConnectionResetError
PyExc_DeprecationWarning
PyExc_EOFError
PyExc_EncodingWarning
PyExc_EnvironmentError
PyExc_Exception
PyExc_FileExistsError
PyExc_FileNotFoundError
PyExc_FloatingPointError
PyExc_FutureWarning
PyExc_GeneratorExit
PyExc_IOError

|  | PyEval_AcquireThread()
PyEval_EvalCode()
PyEval_EvalCodeEx()
PyEval_EvalFrame()
PyEval_EvalFrameEx()
PyEval_GetBuiltins()
PyEval_GetFrame()
PyEval_GetFrameBuiltins()
PyEval_GetFrameGlobals()
PyEval_GetFrameLocals()
PyEval_GetFuncDesc()
PyEval_GetFuncName()
PyEval_GetGlobals()
PyEval_GetLocals()
PyEval_InitThreads()
PyEval_ReleaseThread()
PyEval_RestoreThread()
PyEval_SaveThread()
PyExc_ArithmeticError
PyExc_AssertionError
PyExc_AttributeError
PyExc_BaseException
PyExc_BaseExceptionGroup
PyExc_BlockingIOError
PyExc_BrokenPipeError
PyExc_BufferError
PyExc_BytesWarning
PyExc_ChildProcessError
PyExc_ConnectionAbortedError
PyExc_ConnectionError
PyExc_ConnectionRefusedError
PyExc_ConnectionResetError
PyExc_DeprecationWarning
PyExc_EOFError
PyExc_EncodingWarning
PyExc_EnvironmentError
PyExc_Exception
PyExc_FileExistsError
PyExc_FileNotFoundError
PyExc_FloatingPointError
PyExc_FutureWarning
PyExc_GeneratorExit
PyExc_IOError |  |
| --- | --- | --- |

### 第9页

PyExc_ImportError
PyExc_ImportWarning
PyExc_IndentationError
PyExc_IndexError
PyExc_InterruptedError
PyExc_IsADirectoryError
PyExc_KeyError
PyExc_KeyboardInterrupt
PyExc_LookupError
PyExc_MemoryError
PyExc_ModuleNotFoundError
PyExc_NameError
PyExc_NotADirectoryError
PyExc_NotImplementedError
PyExc_OSError
PyExc_OverflowError
PyExc_PendingDeprecationWarning
PyExc_PermissionError
PyExc_ProcessLookupError
PyExc_RecursionError
PyExc_ReferenceError
PyExc_ResourceWarning
PyExc_RuntimeError
PyExc_RuntimeWarning
PyExc_StopAsyncIteration
PyExc_StopIteration
PyExc_SyntaxError
PyExc_SyntaxWarning
PyExc_SystemError
PyExc_SystemExit
PyExc_TabError
PyExc_TimeoutError
PyExc_TypeError
PyExc_UnboundLocalError
PyExc_UnicodeDecodeError
PyExc_UnicodeEncodeError
PyExc_UnicodeError
PyExc_UnicodeTranslateError
PyExc_UnicodeWarning
PyExc_UserWarning
PyExc_ValueError
PyExc_Warning
PyExc_WindowsError

|  | PyExc_ImportError
PyExc_ImportWarning
PyExc_IndentationError
PyExc_IndexError
PyExc_InterruptedError
PyExc_IsADirectoryError
PyExc_KeyError
PyExc_KeyboardInterrupt
PyExc_LookupError
PyExc_MemoryError
PyExc_ModuleNotFoundError
PyExc_NameError
PyExc_NotADirectoryError
PyExc_NotImplementedError
PyExc_OSError
PyExc_OverflowError
PyExc_PendingDeprecationWarning
PyExc_PermissionError
PyExc_ProcessLookupError
PyExc_RecursionError
PyExc_ReferenceError
PyExc_ResourceWarning
PyExc_RuntimeError
PyExc_RuntimeWarning
PyExc_StopAsyncIteration
PyExc_StopIteration
PyExc_SyntaxError
PyExc_SyntaxWarning
PyExc_SystemError
PyExc_SystemExit
PyExc_TabError
PyExc_TimeoutError
PyExc_TypeError
PyExc_UnboundLocalError
PyExc_UnicodeDecodeError
PyExc_UnicodeEncodeError
PyExc_UnicodeError
PyExc_UnicodeTranslateError
PyExc_UnicodeWarning
PyExc_UserWarning
PyExc_ValueError
PyExc_Warning
PyExc_WindowsError |  |
| --- | --- | --- |

### 第10页

PyExc_ZeroDivisionError
PyExceptionClass_Name()
PyException_GetArgs()
PyException_GetCause()
PyException_GetContext()
PyException_GetTraceback()
PyException_SetArgs()
PyException_SetCause()
PyException_SetContext()
PyException_SetTraceback()
PyFile_FromFd()
PyFile_GetLine()
PyFile_WriteObject()
PyFile_WriteString()
PyFilter_Type
PyFloat_AsDouble()
PyFloat_FromDouble()
PyFloat_FromString()
PyFloat_GetInfo()
PyFloat_GetMax()
PyFloat_GetMin()
PyFloat_Type
PyFrameObject
PyFrame_GetCode()
PyFrame_GetLineNumber()
PyFrozenSet_New()
PyFrozenSet_Type
PyGC_Collect()
PyGC_Disable()
PyGC_Enable()
PyGC_IsEnabled()
PyGILState_Ensure()
PyGILState_GetThisThreadState()
PyGILState_Release()
PyGILState_STATE
PyGetSetDef
PyGetSetDescr_Type
PyImport_AddModule()
PyImport_AddModuleObject()
PyImport_AddModuleRef()
PyImport_AppendInittab()
PyImport_ExecCodeModule()
PyImport_ExecCodeModuleEx()

|  | PyExc_ZeroDivisionError
PyExceptionClass_Name()
PyException_GetArgs()
PyException_GetCause()
PyException_GetContext()
PyException_GetTraceback()
PyException_SetArgs()
PyException_SetCause()
PyException_SetContext()
PyException_SetTraceback()
PyFile_FromFd()
PyFile_GetLine()
PyFile_WriteObject()
PyFile_WriteString()
PyFilter_Type
PyFloat_AsDouble()
PyFloat_FromDouble()
PyFloat_FromString()
PyFloat_GetInfo()
PyFloat_GetMax()
PyFloat_GetMin()
PyFloat_Type
PyFrameObject
PyFrame_GetCode()
PyFrame_GetLineNumber()
PyFrozenSet_New()
PyFrozenSet_Type
PyGC_Collect()
PyGC_Disable()
PyGC_Enable()
PyGC_IsEnabled()
PyGILState_Ensure()
PyGILState_GetThisThreadState()
PyGILState_Release()
PyGILState_STATE
PyGetSetDef
PyGetSetDescr_Type
PyImport_AddModule()
PyImport_AddModuleObject()
PyImport_AddModuleRef()
PyImport_AppendInittab()
PyImport_ExecCodeModule()
PyImport_ExecCodeModuleEx() |  |
| --- | --- | --- |

### 第11页

PyImport_ExecCodeModuleObject()
PyImport_ExecCodeModuleWithPathnames()
PyImport_GetImporter()
PyImport_GetMagicNumber()
PyImport_GetMagicTag()
PyImport_GetModule()
PyImport_GetModuleDict()
PyImport_Import()
PyImport_ImportFrozenModule()
PyImport_ImportFrozenModuleObject()
PyImport_ImportModule()
PyImport_ImportModuleLevel()
PyImport_ImportModuleLevelObject()
PyImport_ImportModuleNoBlock()
PyImport_ReloadModule()
PyIndex_Check()
PyInterpreterState
PyInterpreterState_Clear()
PyInterpreterState_Delete()
PyInterpreterState_Get()
PyInterpreterState_GetDict()
PyInterpreterState_GetID()
PyInterpreterState_New()
PyIter_Check()
PyIter_Next()
PyIter_NextItem()
PyIter_Send()
PyListIter_Type
PyListRevIter_Type
PyList_Append()
PyList_AsTuple()
PyList_GetItem()
PyList_GetItemRef()
PyList_GetSlice()
PyList_Insert()
PyList_New()
PyList_Reverse()
PyList_SetItem()
PyList_SetSlice()
PyList_Size()
PyList_Sort()
PyList_Type
PyLongObject

|  | PyImport_ExecCodeModuleObject()
PyImport_ExecCodeModuleWithPathnames()
PyImport_GetImporter()
PyImport_GetMagicNumber()
PyImport_GetMagicTag()
PyImport_GetModule()
PyImport_GetModuleDict()
PyImport_Import()
PyImport_ImportFrozenModule()
PyImport_ImportFrozenModuleObject()
PyImport_ImportModule()
PyImport_ImportModuleLevel()
PyImport_ImportModuleLevelObject()
PyImport_ImportModuleNoBlock()
PyImport_ReloadModule()
PyIndex_Check()
PyInterpreterState
PyInterpreterState_Clear()
PyInterpreterState_Delete()
PyInterpreterState_Get()
PyInterpreterState_GetDict()
PyInterpreterState_GetID()
PyInterpreterState_New()
PyIter_Check()
PyIter_Next()
PyIter_NextItem()
PyIter_Send()
PyListIter_Type
PyListRevIter_Type
PyList_Append()
PyList_AsTuple()
PyList_GetItem()
PyList_GetItemRef()
PyList_GetSlice()
PyList_Insert()
PyList_New()
PyList_Reverse()
PyList_SetItem()
PyList_SetSlice()
PyList_Size()
PyList_Sort()
PyList_Type
PyLongObject |  |
| --- | --- | --- |

### 第12页

PyLongRangeIter_Type
PyLong_AsDouble()
PyLong_AsInt()
PyLong_AsInt32()
PyLong_AsInt64()
PyLong_AsLong()
PyLong_AsLongAndOverflow()
PyLong_AsLongLong()
PyLong_AsLongLongAndOverflow()
PyLong_AsNativeBytes()
PyLong_AsSize_t()
PyLong_AsSsize_t()
PyLong_AsUInt32()
PyLong_AsUInt64()
PyLong_AsUnsignedLong()
PyLong_AsUnsignedLongLong()
PyLong_AsUnsignedLongLongMask()
PyLong_AsUnsignedLongMask()
PyLong_AsVoidPtr()
PyLong_FromDouble()
PyLong_FromInt32()
PyLong_FromInt64()
PyLong_FromLong()
PyLong_FromLongLong()
PyLong_FromNativeBytes()
PyLong_FromSize_t()
PyLong_FromSsize_t()
PyLong_FromString()
PyLong_FromUInt32()
PyLong_FromUInt64()
PyLong_FromUnsignedLong()
PyLong_FromUnsignedLongLong()
PyLong_FromUnsignedNativeBytes()
PyLong_FromVoidPtr()
PyLong_GetInfo()
PyLong_Type
PyMap_Type
PyMapping_Check()
PyMapping_GetItemString()
PyMapping_GetOptionalItem()
PyMapping_GetOptionalItemString()
PyMapping_HasKey()
PyMapping_HasKeyString()

|  | PyLongRangeIter_Type
PyLong_AsDouble()
PyLong_AsInt()
PyLong_AsInt32()
PyLong_AsInt64()
PyLong_AsLong()
PyLong_AsLongAndOverflow()
PyLong_AsLongLong()
PyLong_AsLongLongAndOverflow()
PyLong_AsNativeBytes()
PyLong_AsSize_t()
PyLong_AsSsize_t()
PyLong_AsUInt32()
PyLong_AsUInt64()
PyLong_AsUnsignedLong()
PyLong_AsUnsignedLongLong()
PyLong_AsUnsignedLongLongMask()
PyLong_AsUnsignedLongMask()
PyLong_AsVoidPtr()
PyLong_FromDouble()
PyLong_FromInt32()
PyLong_FromInt64()
PyLong_FromLong()
PyLong_FromLongLong()
PyLong_FromNativeBytes()
PyLong_FromSize_t()
PyLong_FromSsize_t()
PyLong_FromString()
PyLong_FromUInt32()
PyLong_FromUInt64()
PyLong_FromUnsignedLong()
PyLong_FromUnsignedLongLong()
PyLong_FromUnsignedNativeBytes()
PyLong_FromVoidPtr()
PyLong_GetInfo()
PyLong_Type
PyMap_Type
PyMapping_Check()
PyMapping_GetItemString()
PyMapping_GetOptionalItem()
PyMapping_GetOptionalItemString()
PyMapping_HasKey()
PyMapping_HasKeyString() |  |
| --- | --- | --- |

### 第13页

PyMapping_HasKeyStringWithError()
PyMapping_HasKeyWithError()
PyMapping_Items()
PyMapping_Keys()
PyMapping_Length()
PyMapping_SetItemString()
PyMapping_Size()
PyMapping_Values()
PyMem_Calloc()
PyMem_Free()
PyMem_Malloc()
PyMem_RawCalloc()
PyMem_RawFree()
PyMem_RawMalloc()
PyMem_RawRealloc()
PyMem_Realloc()
PyMemberDef
PyMemberDescr_Type
PyMember_GetOne()
PyMember_SetOne()
PyMemoryView_FromBuffer()
PyMemoryView_FromMemory()
PyMemoryView_FromObject()
PyMemoryView_GetContiguous()
PyMemoryView_Type
PyMethodDef
PyMethodDescr_Type
PyModuleDef
PyModuleDef_Base
PyModuleDef_Init()
PyModuleDef_Type
PyModule_Add()
PyModule_AddFunctions()
PyModule_AddIntConstant()
PyModule_AddObject()
PyModule_AddObjectRef()
PyModule_AddStringConstant()
PyModule_AddType()
PyModule_Create2()
PyModule_ExecDef()
PyModule_FromDefAndSpec2()
PyModule_GetDef()
PyModule_GetDict()

|  | PyMapping_HasKeyStringWithError()
PyMapping_HasKeyWithError()
PyMapping_Items()
PyMapping_Keys()
PyMapping_Length()
PyMapping_SetItemString()
PyMapping_Size()
PyMapping_Values()
PyMem_Calloc()
PyMem_Free()
PyMem_Malloc()
PyMem_RawCalloc()
PyMem_RawFree()
PyMem_RawMalloc()
PyMem_RawRealloc()
PyMem_Realloc()
PyMemberDef
PyMemberDescr_Type
PyMember_GetOne()
PyMember_SetOne()
PyMemoryView_FromBuffer()
PyMemoryView_FromMemory()
PyMemoryView_FromObject()
PyMemoryView_GetContiguous()
PyMemoryView_Type
PyMethodDef
PyMethodDescr_Type
PyModuleDef
PyModuleDef_Base
PyModuleDef_Init()
PyModuleDef_Type
PyModule_Add()
PyModule_AddFunctions()
PyModule_AddIntConstant()
PyModule_AddObject()
PyModule_AddObjectRef()
PyModule_AddStringConstant()
PyModule_AddType()
PyModule_Create2()
PyModule_ExecDef()
PyModule_FromDefAndSpec2()
PyModule_GetDef()
PyModule_GetDict() |  |
| --- | --- | --- |

### 第14页

PyModule_GetFilename()
PyModule_GetFilenameObject()
PyModule_GetName()
PyModule_GetNameObject()
PyModule_GetState()
PyModule_New()
PyModule_NewObject()
PyModule_SetDocString()
PyModule_Type
PyNumber_Absolute()
PyNumber_Add()
PyNumber_And()
PyNumber_AsSsize_t()
PyNumber_Check()
PyNumber_Divmod()
PyNumber_Float()
PyNumber_FloorDivide()
PyNumber_InPlaceAdd()
PyNumber_InPlaceAnd()
PyNumber_InPlaceFloorDivide()
PyNumber_InPlaceLshift()
PyNumber_InPlaceMatrixMultiply()
PyNumber_InPlaceMultiply()
PyNumber_InPlaceOr()
PyNumber_InPlacePower()
PyNumber_InPlaceRemainder()
PyNumber_InPlaceRshift()
PyNumber_InPlaceSubtract()
PyNumber_InPlaceTrueDivide()
PyNumber_InPlaceXor()
PyNumber_Index()
PyNumber_Invert()
PyNumber_Long()
PyNumber_Lshift()
PyNumber_MatrixMultiply()
PyNumber_Multiply()
PyNumber_Negative()
PyNumber_Or()
PyNumber_Positive()
PyNumber_Power()
PyNumber_Remainder()
PyNumber_Rshift()
PyNumber_Subtract()

|  | PyModule_GetFilename()
PyModule_GetFilenameObject()
PyModule_GetName()
PyModule_GetNameObject()
PyModule_GetState()
PyModule_New()
PyModule_NewObject()
PyModule_SetDocString()
PyModule_Type
PyNumber_Absolute()
PyNumber_Add()
PyNumber_And()
PyNumber_AsSsize_t()
PyNumber_Check()
PyNumber_Divmod()
PyNumber_Float()
PyNumber_FloorDivide()
PyNumber_InPlaceAdd()
PyNumber_InPlaceAnd()
PyNumber_InPlaceFloorDivide()
PyNumber_InPlaceLshift()
PyNumber_InPlaceMatrixMultiply()
PyNumber_InPlaceMultiply()
PyNumber_InPlaceOr()
PyNumber_InPlacePower()
PyNumber_InPlaceRemainder()
PyNumber_InPlaceRshift()
PyNumber_InPlaceSubtract()
PyNumber_InPlaceTrueDivide()
PyNumber_InPlaceXor()
PyNumber_Index()
PyNumber_Invert()
PyNumber_Long()
PyNumber_Lshift()
PyNumber_MatrixMultiply()
PyNumber_Multiply()
PyNumber_Negative()
PyNumber_Or()
PyNumber_Positive()
PyNumber_Power()
PyNumber_Remainder()
PyNumber_Rshift()
PyNumber_Subtract() |  |
| --- | --- | --- |

### 第15页

PyNumber_ToBase()
PyNumber_TrueDivide()
PyNumber_Xor()
PyOS_AfterFork()
PyOS_AfterFork_Child()
PyOS_AfterFork_Parent()
PyOS_BeforeFork()
PyOS_CheckStack()
PyOS_FSPath()
PyOS_InputHook
PyOS_InterruptOccurred()
PyOS_double_to_string()
PyOS_getsig()
PyOS_mystricmp()
PyOS_mystrnicmp()
PyOS_setsig()
PyOS_sighandler_t
PyOS_snprintf()
PyOS_string_to_double()
PyOS_strtol()
PyOS_strtoul()
PyOS_vsnprintf()
PyObject
PyObject.ob_refcnt
PyObject.ob_type
PyObject_ASCII()
PyObject_AsFileDescriptor()
PyObject_Bytes()
PyObject_Call()
PyObject_CallFunction()
PyObject_CallFunctionObjArgs()
PyObject_CallMethod()
PyObject_CallMethodObjArgs()
PyObject_CallNoArgs()
PyObject_CallObject()
PyObject_Calloc()
PyObject_CheckBuffer()
PyObject_ClearWeakRefs()
PyObject_CopyData()
PyObject_DelAttr()
PyObject_DelAttrString()
PyObject_DelItem()
PyObject_DelItemString()

|  | PyNumber_ToBase()
PyNumber_TrueDivide()
PyNumber_Xor()
PyOS_AfterFork()
PyOS_AfterFork_Child()
PyOS_AfterFork_Parent()
PyOS_BeforeFork()
PyOS_CheckStack()
PyOS_FSPath()
PyOS_InputHook
PyOS_InterruptOccurred()
PyOS_double_to_string()
PyOS_getsig()
PyOS_mystricmp()
PyOS_mystrnicmp()
PyOS_setsig()
PyOS_sighandler_t
PyOS_snprintf()
PyOS_string_to_double()
PyOS_strtol()
PyOS_strtoul()
PyOS_vsnprintf()
PyObject
PyObject.ob_refcnt
PyObject.ob_type
PyObject_ASCII()
PyObject_AsFileDescriptor()
PyObject_Bytes()
PyObject_Call()
PyObject_CallFunction()
PyObject_CallFunctionObjArgs()
PyObject_CallMethod()
PyObject_CallMethodObjArgs()
PyObject_CallNoArgs()
PyObject_CallObject()
PyObject_Calloc()
PyObject_CheckBuffer()
PyObject_ClearWeakRefs()
PyObject_CopyData()
PyObject_DelAttr()
PyObject_DelAttrString()
PyObject_DelItem()
PyObject_DelItemString() |  |
| --- | --- | --- |

### 第16页

PyObject_Dir()
PyObject_Format()
PyObject_Free()
PyObject_GC_Del()
PyObject_GC_IsFinalized()
PyObject_GC_IsTracked()
PyObject_GC_Track()
PyObject_GC_UnTrack()
PyObject_GenericGetAttr()
PyObject_GenericGetDict()
PyObject_GenericSetAttr()
PyObject_GenericSetDict()
PyObject_GetAIter()
PyObject_GetAttr()
PyObject_GetAttrString()
PyObject_GetBuffer()
PyObject_GetItem()
PyObject_GetIter()
PyObject_GetOptionalAttr()
PyObject_GetOptionalAttrString()
PyObject_GetTypeData()
PyObject_HasAttr()
PyObject_HasAttrString()
PyObject_HasAttrStringWithError()
PyObject_HasAttrWithError()
PyObject_Hash()
PyObject_HashNotImplemented()
PyObject_Init()
PyObject_InitVar()
PyObject_IsInstance()
PyObject_IsSubclass()
PyObject_IsTrue()
PyObject_Length()
PyObject_Malloc()
PyObject_Not()
PyObject_Realloc()
PyObject_Repr()
PyObject_RichCompare()
PyObject_RichCompareBool()
PyObject_SelfIter()
PyObject_SetAttr()
PyObject_SetAttrString()
PyObject_SetItem()

|  | PyObject_Dir()
PyObject_Format()
PyObject_Free()
PyObject_GC_Del()
PyObject_GC_IsFinalized()
PyObject_GC_IsTracked()
PyObject_GC_Track()
PyObject_GC_UnTrack()
PyObject_GenericGetAttr()
PyObject_GenericGetDict()
PyObject_GenericSetAttr()
PyObject_GenericSetDict()
PyObject_GetAIter()
PyObject_GetAttr()
PyObject_GetAttrString()
PyObject_GetBuffer()
PyObject_GetItem()
PyObject_GetIter()
PyObject_GetOptionalAttr()
PyObject_GetOptionalAttrString()
PyObject_GetTypeData()
PyObject_HasAttr()
PyObject_HasAttrString()
PyObject_HasAttrStringWithError()
PyObject_HasAttrWithError()
PyObject_Hash()
PyObject_HashNotImplemented()
PyObject_Init()
PyObject_InitVar()
PyObject_IsInstance()
PyObject_IsSubclass()
PyObject_IsTrue()
PyObject_Length()
PyObject_Malloc()
PyObject_Not()
PyObject_Realloc()
PyObject_Repr()
PyObject_RichCompare()
PyObject_RichCompareBool()
PyObject_SelfIter()
PyObject_SetAttr()
PyObject_SetAttrString()
PyObject_SetItem() |  |
| --- | --- | --- |

### 第17页

PyObject_Size()
PyObject_Str()
PyObject_Type()
PyObject_Vectorcall()
PyObject_VectorcallMethod()
PyProperty_Type
PyRangeIter_Type
PyRange_Type
PyReversed_Type
PySeqIter_New()
PySeqIter_Type
PySequence_Check()
PySequence_Concat()
PySequence_Contains()
PySequence_Count()
PySequence_DelItem()
PySequence_DelSlice()
PySequence_Fast()
PySequence_GetItem()
PySequence_GetSlice()
PySequence_In()
PySequence_InPlaceConcat()
PySequence_InPlaceRepeat()
PySequence_Index()
PySequence_Length()
PySequence_List()
PySequence_Repeat()
PySequence_SetItem()
PySequence_SetSlice()
PySequence_Size()
PySequence_Tuple()
PySetIter_Type
PySet_Add()
PySet_Clear()
PySet_Contains()
PySet_Discard()
PySet_New()
PySet_Pop()
PySet_Size()
PySet_Type
PySlice_AdjustIndices()
PySlice_GetIndices()
PySlice_GetIndicesEx()

|  | PyObject_Size()
PyObject_Str()
PyObject_Type()
PyObject_Vectorcall()
PyObject_VectorcallMethod()
PyProperty_Type
PyRangeIter_Type
PyRange_Type
PyReversed_Type
PySeqIter_New()
PySeqIter_Type
PySequence_Check()
PySequence_Concat()
PySequence_Contains()
PySequence_Count()
PySequence_DelItem()
PySequence_DelSlice()
PySequence_Fast()
PySequence_GetItem()
PySequence_GetSlice()
PySequence_In()
PySequence_InPlaceConcat()
PySequence_InPlaceRepeat()
PySequence_Index()
PySequence_Length()
PySequence_List()
PySequence_Repeat()
PySequence_SetItem()
PySequence_SetSlice()
PySequence_Size()
PySequence_Tuple()
PySetIter_Type
PySet_Add()
PySet_Clear()
PySet_Contains()
PySet_Discard()
PySet_New()
PySet_Pop()
PySet_Size()
PySet_Type
PySlice_AdjustIndices()
PySlice_GetIndices()
PySlice_GetIndicesEx() |  |
| --- | --- | --- |

### 第18页

PySlice_New()
PySlice_Type
PySlice_Unpack()
PyState_AddModule()
PyState_FindModule()
PyState_RemoveModule()
PyStructSequence_Desc
PyStructSequence_Field
PyStructSequence_GetItem()
PyStructSequence_New()
PyStructSequence_NewType()
PyStructSequence_SetItem()
PyStructSequence_UnnamedField
PySuper_Type
PySys_Audit()
PySys_AuditTuple()
PySys_FormatStderr()
PySys_FormatStdout()
PySys_GetObject()
PySys_GetXOptions()
PySys_ResetWarnOptions()
PySys_SetArgv()
PySys_SetArgvEx()
PySys_SetObject()
PySys_WriteStderr()
PySys_WriteStdout()
PyThreadState
PyThreadState_Clear()
PyThreadState_Delete()
PyThreadState_Get()
PyThreadState_GetDict()
PyThreadState_GetFrame()
PyThreadState_GetID()
PyThreadState_GetInterpreter()
PyThreadState_New()
PyThreadState_SetAsyncExc()
PyThreadState_Swap()
PyThread_GetInfo()
PyThread_ReInitTLS()
PyThread_acquire_lock()
PyThread_acquire_lock_timed()
PyThread_allocate_lock()
PyThread_create_key()

|  | PySlice_New()
PySlice_Type
PySlice_Unpack()
PyState_AddModule()
PyState_FindModule()
PyState_RemoveModule()
PyStructSequence_Desc
PyStructSequence_Field
PyStructSequence_GetItem()
PyStructSequence_New()
PyStructSequence_NewType()
PyStructSequence_SetItem()
PyStructSequence_UnnamedField
PySuper_Type
PySys_Audit()
PySys_AuditTuple()
PySys_FormatStderr()
PySys_FormatStdout()
PySys_GetObject()
PySys_GetXOptions()
PySys_ResetWarnOptions()
PySys_SetArgv()
PySys_SetArgvEx()
PySys_SetObject()
PySys_WriteStderr()
PySys_WriteStdout()
PyThreadState
PyThreadState_Clear()
PyThreadState_Delete()
PyThreadState_Get()
PyThreadState_GetDict()
PyThreadState_GetFrame()
PyThreadState_GetID()
PyThreadState_GetInterpreter()
PyThreadState_New()
PyThreadState_SetAsyncExc()
PyThreadState_Swap()
PyThread_GetInfo()
PyThread_ReInitTLS()
PyThread_acquire_lock()
PyThread_acquire_lock_timed()
PyThread_allocate_lock()
PyThread_create_key() |  |
| --- | --- | --- |

### 第19页

PyThread_delete_key()
PyThread_delete_key_value()
PyThread_exit_thread()
PyThread_free_lock()
PyThread_get_key_value()
PyThread_get_stacksize()
PyThread_get_thread_ident()
PyThread_get_thread_native_id()
PyThread_init_thread()
PyThread_release_lock()
PyThread_set_key_value()
PyThread_set_stacksize()
PyThread_start_new_thread()
PyThread_tss_alloc()
PyThread_tss_create()
PyThread_tss_delete()
PyThread_tss_free()
PyThread_tss_get()
PyThread_tss_is_created()
PyThread_tss_set()
PyTraceBack_Here()
PyTraceBack_Print()
PyTraceBack_Type
PyTupleIter_Type
PyTuple_GetItem()
PyTuple_GetSlice()
PyTuple_New()
PyTuple_Pack()
PyTuple_SetItem()
PyTuple_Size()
PyTuple_Type
PyTypeObject
PyType_ClearCache()
PyType_Freeze()
PyType_FromMetaclass()
PyType_FromModuleAndSpec()
PyType_FromSpec()
PyType_FromSpecWithBases()
PyType_GenericAlloc()
PyType_GenericNew()
PyType_GetBaseByToken()
PyType_GetFlags()
PyType_GetFullyQualifiedName()

|  | PyThread_delete_key()
PyThread_delete_key_value()
PyThread_exit_thread()
PyThread_free_lock()
PyThread_get_key_value()
PyThread_get_stacksize()
PyThread_get_thread_ident()
PyThread_get_thread_native_id()
PyThread_init_thread()
PyThread_release_lock()
PyThread_set_key_value()
PyThread_set_stacksize()
PyThread_start_new_thread()
PyThread_tss_alloc()
PyThread_tss_create()
PyThread_tss_delete()
PyThread_tss_free()
PyThread_tss_get()
PyThread_tss_is_created()
PyThread_tss_set()
PyTraceBack_Here()
PyTraceBack_Print()
PyTraceBack_Type
PyTupleIter_Type
PyTuple_GetItem()
PyTuple_GetSlice()
PyTuple_New()
PyTuple_Pack()
PyTuple_SetItem()
PyTuple_Size()
PyTuple_Type
PyTypeObject
PyType_ClearCache()
PyType_Freeze()
PyType_FromMetaclass()
PyType_FromModuleAndSpec()
PyType_FromSpec()
PyType_FromSpecWithBases()
PyType_GenericAlloc()
PyType_GenericNew()
PyType_GetBaseByToken()
PyType_GetFlags()
PyType_GetFullyQualifiedName() |  |
| --- | --- | --- |

### 第20页

PyType_GetModule()
PyType_GetModuleByDef()
PyType_GetModuleName()
PyType_GetModuleState()
PyType_GetName()
PyType_GetQualName()
PyType_GetSlot()
PyType_GetTypeDataSize()
PyType_IsSubtype()
PyType_Modified()
PyType_Ready()
PyType_Slot
PyType_Spec
PyType_Type
PyUnicodeDecodeError_Create()
PyUnicodeDecodeError_GetEncoding()
PyUnicodeDecodeError_GetEnd()
PyUnicodeDecodeError_GetObject()
PyUnicodeDecodeError_GetReason()
PyUnicodeDecodeError_GetStart()
PyUnicodeDecodeError_SetEnd()
PyUnicodeDecodeError_SetReason()
PyUnicodeDecodeError_SetStart()
PyUnicodeEncodeError_GetEncoding()
PyUnicodeEncodeError_GetEnd()
PyUnicodeEncodeError_GetObject()
PyUnicodeEncodeError_GetReason()
PyUnicodeEncodeError_GetStart()
PyUnicodeEncodeError_SetEnd()
PyUnicodeEncodeError_SetReason()
PyUnicodeEncodeError_SetStart()
PyUnicodeIter_Type
PyUnicodeTranslateError_GetEnd()
PyUnicodeTranslateError_GetObject()
PyUnicodeTranslateError_GetReason()
PyUnicodeTranslateError_GetStart()
PyUnicodeTranslateError_SetEnd()
PyUnicodeTranslateError_SetReason()
PyUnicodeTranslateError_SetStart()
PyUnicode_Append()
PyUnicode_AppendAndDel()
PyUnicode_AsASCIIString()
PyUnicode_AsCharmapString()

|  | PyType_GetModule()
PyType_GetModuleByDef()
PyType_GetModuleName()
PyType_GetModuleState()
PyType_GetName()
PyType_GetQualName()
PyType_GetSlot()
PyType_GetTypeDataSize()
PyType_IsSubtype()
PyType_Modified()
PyType_Ready()
PyType_Slot
PyType_Spec
PyType_Type
PyUnicodeDecodeError_Create()
PyUnicodeDecodeError_GetEncoding()
PyUnicodeDecodeError_GetEnd()
PyUnicodeDecodeError_GetObject()
PyUnicodeDecodeError_GetReason()
PyUnicodeDecodeError_GetStart()
PyUnicodeDecodeError_SetEnd()
PyUnicodeDecodeError_SetReason()
PyUnicodeDecodeError_SetStart()
PyUnicodeEncodeError_GetEncoding()
PyUnicodeEncodeError_GetEnd()
PyUnicodeEncodeError_GetObject()
PyUnicodeEncodeError_GetReason()
PyUnicodeEncodeError_GetStart()
PyUnicodeEncodeError_SetEnd()
PyUnicodeEncodeError_SetReason()
PyUnicodeEncodeError_SetStart()
PyUnicodeIter_Type
PyUnicodeTranslateError_GetEnd()
PyUnicodeTranslateError_GetObject()
PyUnicodeTranslateError_GetReason()
PyUnicodeTranslateError_GetStart()
PyUnicodeTranslateError_SetEnd()
PyUnicodeTranslateError_SetReason()
PyUnicodeTranslateError_SetStart()
PyUnicode_Append()
PyUnicode_AppendAndDel()
PyUnicode_AsASCIIString()
PyUnicode_AsCharmapString() |  |
| --- | --- | --- |

### 第21页

PyUnicode_AsDecodedObject()
PyUnicode_AsDecodedUnicode()
PyUnicode_AsEncodedObject()
PyUnicode_AsEncodedString()
PyUnicode_AsEncodedUnicode()
PyUnicode_AsLatin1String()
PyUnicode_AsMBCSString()
PyUnicode_AsRawUnicodeEscapeString()
PyUnicode_AsUCS4()
PyUnicode_AsUCS4Copy()
PyUnicode_AsUTF16String()
PyUnicode_AsUTF32String()
PyUnicode_AsUTF8AndSize()
PyUnicode_AsUTF8String()
PyUnicode_AsUnicodeEscapeString()
PyUnicode_AsWideChar()
PyUnicode_AsWideCharString()
PyUnicode_BuildEncodingMap()
PyUnicode_Compare()
PyUnicode_CompareWithASCIIString()
PyUnicode_Concat()
PyUnicode_Contains()
PyUnicode_Count()
PyUnicode_Decode()
PyUnicode_DecodeASCII()
PyUnicode_DecodeCharmap()
PyUnicode_DecodeCodePageStateful()
PyUnicode_DecodeFSDefault()
PyUnicode_DecodeFSDefaultAndSize()
PyUnicode_DecodeLatin1()
PyUnicode_DecodeLocale()
PyUnicode_DecodeLocaleAndSize()
PyUnicode_DecodeMBCS()
PyUnicode_DecodeMBCSStateful()
PyUnicode_DecodeRawUnicodeEscape()
PyUnicode_DecodeUTF16()
PyUnicode_DecodeUTF16Stateful()
PyUnicode_DecodeUTF32()
PyUnicode_DecodeUTF32Stateful()
PyUnicode_DecodeUTF7()
PyUnicode_DecodeUTF7Stateful()
PyUnicode_DecodeUTF8()
PyUnicode_DecodeUTF8Stateful()

|  | PyUnicode_AsDecodedObject()
PyUnicode_AsDecodedUnicode()
PyUnicode_AsEncodedObject()
PyUnicode_AsEncodedString()
PyUnicode_AsEncodedUnicode()
PyUnicode_AsLatin1String()
PyUnicode_AsMBCSString()
PyUnicode_AsRawUnicodeEscapeString()
PyUnicode_AsUCS4()
PyUnicode_AsUCS4Copy()
PyUnicode_AsUTF16String()
PyUnicode_AsUTF32String()
PyUnicode_AsUTF8AndSize()
PyUnicode_AsUTF8String()
PyUnicode_AsUnicodeEscapeString()
PyUnicode_AsWideChar()
PyUnicode_AsWideCharString()
PyUnicode_BuildEncodingMap()
PyUnicode_Compare()
PyUnicode_CompareWithASCIIString()
PyUnicode_Concat()
PyUnicode_Contains()
PyUnicode_Count()
PyUnicode_Decode()
PyUnicode_DecodeASCII()
PyUnicode_DecodeCharmap()
PyUnicode_DecodeCodePageStateful()
PyUnicode_DecodeFSDefault()
PyUnicode_DecodeFSDefaultAndSize()
PyUnicode_DecodeLatin1()
PyUnicode_DecodeLocale()
PyUnicode_DecodeLocaleAndSize()
PyUnicode_DecodeMBCS()
PyUnicode_DecodeMBCSStateful()
PyUnicode_DecodeRawUnicodeEscape()
PyUnicode_DecodeUTF16()
PyUnicode_DecodeUTF16Stateful()
PyUnicode_DecodeUTF32()
PyUnicode_DecodeUTF32Stateful()
PyUnicode_DecodeUTF7()
PyUnicode_DecodeUTF7Stateful()
PyUnicode_DecodeUTF8()
PyUnicode_DecodeUTF8Stateful() |  |
| --- | --- | --- |

### 第22页

PyUnicode_DecodeUnicodeEscape()
PyUnicode_EncodeCodePage()
PyUnicode_EncodeFSDefault()
PyUnicode_EncodeLocale()
PyUnicode_Equal()
PyUnicode_EqualToUTF8()
PyUnicode_EqualToUTF8AndSize()
PyUnicode_FSConverter()
PyUnicode_FSDecoder()
PyUnicode_Find()
PyUnicode_FindChar()
PyUnicode_Format()
PyUnicode_FromEncodedObject()
PyUnicode_FromFormat()
PyUnicode_FromFormatV()
PyUnicode_FromObject()
PyUnicode_FromOrdinal()
PyUnicode_FromString()
PyUnicode_FromStringAndSize()
PyUnicode_FromWideChar()
PyUnicode_GetDefaultEncoding()
PyUnicode_GetLength()
PyUnicode_InternFromString()
PyUnicode_InternInPlace()
PyUnicode_IsIdentifier()
PyUnicode_Join()
PyUnicode_Partition()
PyUnicode_RPartition()
PyUnicode_RSplit()
PyUnicode_ReadChar()
PyUnicode_Replace()
PyUnicode_Resize()
PyUnicode_RichCompare()
PyUnicode_Split()
PyUnicode_Splitlines()
PyUnicode_Substring()
PyUnicode_Tailmatch()
PyUnicode_Translate()
PyUnicode_Type
PyUnicode_WriteChar()
PyVarObject
PyVarObject.ob_base
PyVarObject.ob_size

|  | PyUnicode_DecodeUnicodeEscape()
PyUnicode_EncodeCodePage()
PyUnicode_EncodeFSDefault()
PyUnicode_EncodeLocale()
PyUnicode_Equal()
PyUnicode_EqualToUTF8()
PyUnicode_EqualToUTF8AndSize()
PyUnicode_FSConverter()
PyUnicode_FSDecoder()
PyUnicode_Find()
PyUnicode_FindChar()
PyUnicode_Format()
PyUnicode_FromEncodedObject()
PyUnicode_FromFormat()
PyUnicode_FromFormatV()
PyUnicode_FromObject()
PyUnicode_FromOrdinal()
PyUnicode_FromString()
PyUnicode_FromStringAndSize()
PyUnicode_FromWideChar()
PyUnicode_GetDefaultEncoding()
PyUnicode_GetLength()
PyUnicode_InternFromString()
PyUnicode_InternInPlace()
PyUnicode_IsIdentifier()
PyUnicode_Join()
PyUnicode_Partition()
PyUnicode_RPartition()
PyUnicode_RSplit()
PyUnicode_ReadChar()
PyUnicode_Replace()
PyUnicode_Resize()
PyUnicode_RichCompare()
PyUnicode_Split()
PyUnicode_Splitlines()
PyUnicode_Substring()
PyUnicode_Tailmatch()
PyUnicode_Translate()
PyUnicode_Type
PyUnicode_WriteChar()
PyVarObject
PyVarObject.ob_base
PyVarObject.ob_size |  |
| --- | --- | --- |

### 第23页

PyVectorcall_Call()
PyVectorcall_NARGS()
PyWeakReference
PyWeakref_GetObject()
PyWeakref_GetRef()
PyWeakref_NewProxy()
PyWeakref_NewRef()
PyWrapperDescr_Type
PyWrapper_New()
PyZip_Type
Py_AddPendingCall()
Py_AtExit()
Py_BEGIN_ALLOW_THREADS
Py_BLOCK_THREADS
Py_BuildValue()
Py_BytesMain()
Py_CompileString()
Py_DecRef()
Py_DecodeLocale()
Py_END_ALLOW_THREADS
Py_EncodeLocale()
Py_EndInterpreter()
Py_EnterRecursiveCall()
Py_Exit()
Py_FatalError()
Py_FileSystemDefaultEncodeErrors
Py_FileSystemDefaultEncoding
Py_Finalize()
Py_FinalizeEx()
Py_GenericAlias()
Py_GenericAliasType
Py_GetBuildInfo()
Py_GetCompiler()
Py_GetConstant()
Py_GetConstantBorrowed()
Py_GetCopyright()
Py_GetExecPrefix()
Py_GetPath()
Py_GetPlatform()
Py_GetPrefix()
Py_GetProgramFullPath()
Py_GetProgramName()
Py_GetPythonHome()

|  | PyVectorcall_Call()
PyVectorcall_NARGS()
PyWeakReference
PyWeakref_GetObject()
PyWeakref_GetRef()
PyWeakref_NewProxy()
PyWeakref_NewRef()
PyWrapperDescr_Type
PyWrapper_New()
PyZip_Type
Py_AddPendingCall()
Py_AtExit()
Py_BEGIN_ALLOW_THREADS
Py_BLOCK_THREADS
Py_BuildValue()
Py_BytesMain()
Py_CompileString()
Py_DecRef()
Py_DecodeLocale()
Py_END_ALLOW_THREADS
Py_EncodeLocale()
Py_EndInterpreter()
Py_EnterRecursiveCall()
Py_Exit()
Py_FatalError()
Py_FileSystemDefaultEncodeErrors
Py_FileSystemDefaultEncoding
Py_Finalize()
Py_FinalizeEx()
Py_GenericAlias()
Py_GenericAliasType
Py_GetBuildInfo()
Py_GetCompiler()
Py_GetConstant()
Py_GetConstantBorrowed()
Py_GetCopyright()
Py_GetExecPrefix()
Py_GetPath()
Py_GetPlatform()
Py_GetPrefix()
Py_GetProgramFullPath()
Py_GetProgramName()
Py_GetPythonHome() |  |
| --- | --- | --- |

### 第24页

Py_GetRecursionLimit()
Py_GetVersion()
Py_HasFileSystemDefaultEncoding
Py_IncRef()
Py_Initialize()
Py_InitializeEx()
Py_Is()
Py_IsFalse()
Py_IsFinalizing()
Py_IsInitialized()
Py_IsNone()
Py_IsTrue()
Py_LeaveRecursiveCall()
Py_Main()
Py_MakePendingCalls()
Py_NewInterpreter()
Py_NewRef()
Py_PACK_FULL_VERSION()
Py_PACK_VERSION()
Py_REFCNT()
Py_ReprEnter()
Py_ReprLeave()
Py_SetProgramName()
Py_SetPythonHome()
Py_SetRecursionLimit()
Py_TYPE()
Py_UCS4
Py_UNBLOCK_THREADS
Py_UTF8Mode
Py_VaBuildValue()
Py_Version
Py_XNewRef()
Py_buffer
Py_intptr_t
Py_ssize_t
Py_uintptr_t
allocfunc
binaryfunc
descrgetfunc
descrsetfunc
destructor
getattrfunc
getattrofunc

|  | Py_GetRecursionLimit()
Py_GetVersion()
Py_HasFileSystemDefaultEncoding
Py_IncRef()
Py_Initialize()
Py_InitializeEx()
Py_Is()
Py_IsFalse()
Py_IsFinalizing()
Py_IsInitialized()
Py_IsNone()
Py_IsTrue()
Py_LeaveRecursiveCall()
Py_Main()
Py_MakePendingCalls()
Py_NewInterpreter()
Py_NewRef()
Py_PACK_FULL_VERSION()
Py_PACK_VERSION()
Py_REFCNT()
Py_ReprEnter()
Py_ReprLeave()
Py_SetProgramName()
Py_SetPythonHome()
Py_SetRecursionLimit()
Py_TYPE()
Py_UCS4
Py_UNBLOCK_THREADS
Py_UTF8Mode
Py_VaBuildValue()
Py_Version
Py_XNewRef()
Py_buffer
Py_intptr_t
Py_ssize_t
Py_uintptr_t
allocfunc
binaryfunc
descrgetfunc
descrsetfunc
destructor
getattrfunc
getattrofunc |  |
| --- | --- | --- |

### 第25页

getbufferproc
getiterfunc
getter
hashfunc
initproc
inquiry
iternextfunc
lenfunc
newfunc
objobjargproc
objobjproc
releasebufferproc
reprfunc
richcmpfunc
setattrfunc
setattrofunc
setter
ssizeargfunc
ssizeobjargproc
ssizessizeargfunc
ssizessizeobjargproc
symtable
ternaryfunc
traverseproc
unaryfunc
vectorcallfunc
visitproc

